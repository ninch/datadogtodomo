#!/usr/bin/python

import sys
from apis.base import Api
from apis.datadog.api import Datadog
from apis.domo.api import Domo

class main():

    def __init__(self):
        self.domo = Domo()
        self.ddog = Datadog()

    def callHello(self, api):
        if api == 'domo':
            return self.domo.hello()
        elif api == 'datadog':
            return self.ddog.hello()

    def getData(self):
        self.ddog.authorization()
        result = self.ddog.query()
        print result

m = main()
print m.callHello('datadog')
print m.callHello('domo')

m.getData()

