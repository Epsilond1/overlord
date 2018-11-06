# coding: utf-8

"""
FIXME
"""

import json

class Cacher:
    CONFFILE = '/home/epsilond1/a.json'
    _confdata = {}

    def reload_file(self):
        with open(self.CONFFILE) as fileconf:
            self._confdata = json.load(fileconf)
        return self._confdata

    def get_cached_data(self):
        return self._confdata