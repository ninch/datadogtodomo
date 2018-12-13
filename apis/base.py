#!/usr/bin/python

import os
import sys
import logging

from ConfigParser import SafeConfigParser

class Api():

    def __init__(self):
        self.executableDirectoryPath = os.path.dirname(os.path.abspath(sys.argv[0]))

    def hello(self):
        return 'hello from api class'

    def _readConfigFile(self, configFile):
        configParser = SafeConfigParser()
        configParser.read(configFile)
        return configParser

    def _readApiKeys(self):
        # TODO : put this in global config file
        apiPassFile = '/home/thongkhamrap01/poc/datadog_app/conf/.passwords/.apikeys.cfg'
        return self._readConfigFile(apiPassFile)

