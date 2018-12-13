#!/usr/bin/python

print '*** from datadog.api'

# private library
from apis.base import Api

class Domo(Api):

    def __init__(self):
        Api.__init__(self)
        self.client_id = None
        self.secret    = None
        self.domoConfig = self._readApiKeys()

    def _getClient(self):
        return self.domoConfig.get('DOMO', 'client_id')

    def _getSecret(self):
        return self.domoConfig.get('DOMO', 'secret')

    def hello(self):
        return 'hello from domo.api.Domo'


