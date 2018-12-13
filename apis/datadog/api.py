#!/usr/bin/python

print '*** from datadog.api'

import json
import sys
import pandas as pd
from pandas                import DataFrame
from time                  import time
from datetime              import datetime
from datadog               import initialize, api
from datadog.api.constants import CheckStatus

# private library
from apis.base import Api

class Datadog(Api):

    def __init__(self):
        self.api_key = None
        self.app_key = None
        self.config  = self._readConfigFile('conf/datadog.cfg')
        self.ddogKeys = self._readApiKeys()
        self.hosts    = eval(self.config.get('CPU_INFO','hostname'), {}, {})

    def hello(self):
        return 'hello from datadog.api.Datadog'

    def _getApiKey(self):
        return self.ddogKeys.get('DATADOG', 'api_key')

    def _getAppKey(self):
        return self.ddogKeys.get('DATADOG', 'app_key')

    def authorization(self):
        options = {}
        options['api_key'] = self._getApiKey()
        options['app_key'] = self._getAppKey()
        return initialize(**options)

    def printRes(self, results):
        for item in results:
            if item != 'series':
                #print '%s: %s' % (item, results[item])
                pass
            else:
                series = results['series']
                for i in range(len(series)):
                    print 'i = %s' % i
                    for serie in series[i]:
                        if serie != 'pointlist':
                            pass
                        else:
                            pointlist = []
                            for col1, col2 in series[i][serie]:
                                pointlist.append([datetime.fromtimestamp(col1/1000.).strftime('%Y-%m-%d %H:%M:%S'), col2])
                            print pointlist

    def _getPointList(self, results):
        pointlists = results['series'][0]['pointlist']
        return pointlists[:5]

    def formatData(self, data):
        """
        This function is to change data format from Dictionary to pandas.DataFrame
        FROM - {'hostname1' : [[k1,v1], [k2,v2], ... ],
                'hostname2' : [[k1,v1], [k2,v2], ... ], ... }
        TO   -      key  hostname1   hostname2   ...
                0    k1      v1          v1
                1    k2      v2          v2
                2    ...     ...         ...
        """

        df_res = DataFrame()
        for hostname, datalist in data.items():
            df = DataFrame(datalist, columns=['key',hostname])
            # change datetime format
            def changedateformat(x):
                return datetime.fromtimestamp(x/1000.).strftime('%Y-%m-%d %H:%M:%S')
            df['key'] = df['key'].apply(changedateformat)

            if df_res.empty:
                df_res = df
            else:
                df_res = pd.merge(df_res, df, left_on='key', right_on='key', how='outer')
        return df_res

    def query(self):
        # read config
        endTime   = int(time())
        startTime = endTime - int(self.config.get('DEFAULT','time_inteval'))
        query     = self.config.get('CPU_INFO','query')

        data = {}
        for hostname in self.hosts:
            q       = '%s{name: %s}' % (query, hostname)
            results = api.Metric.query(
                        start = startTime ,
                        end   = endTime   ,
                        query = q)

            data[hostname] = self._getPointList(results)

        return self.formatData(data)

