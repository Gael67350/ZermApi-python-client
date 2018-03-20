#
#  ZermApi-python-client : A Python client library for ZermApi (https://api.zermthings.fr)
#  Copyright (c) 2018 SCION Gael (https://www.gael67350.eu)
#

# -*- coding: utf-8 -*-
import json
import os


class Response(object):

    def __init__(self, status, message, url, data=None):
        self._status = status
        self._message = message
        self._url = url
        self._data = data

    @property
    def status(self):
        return self._status

    @property
    def message(self):
        return self._message

    @property
    def url(self):
        return self._url

    @property
    def data(self):
        return self._data

    def dictionary(self):
        return {'status': self._status, 'message': self._message, 'data': self._data, 'url': self._url}

    def json(self):
        json_obj = json.dumps(self.dictionary(), encoding="utf-8")
        return json_obj

    def __str__(self):
        string = "Response: " + os.linesep
        string += "status: " + str(self.status) + os.linesep
        string += "message: " + self._message + os.linesep
        string += "url: " + self._url + os.linesep
        string += "data: " + str(self._data)
        return string
