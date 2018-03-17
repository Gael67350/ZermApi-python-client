#
#  ZermApi-python-client : A Python client library for ZermApi (https://api.zermthings.fr)
#  Copyright (c) 2018 SCION Gael (https://www.gael67350.eu)
#

# -*- coding: utf-8 -*-
import requests

from .Singleton import Singleton


class ZermApi(object):
    __metaclass__ = Singleton

    def __init__(self, uuid=None, secret=None):
        self._base_url = "https://api.zermthings.fr"
        self._uuid = uuid
        self._secret = secret
        self._token = None
        self._last_status = None

    def _get_token(self):
        print("Auth required. Proceed...")
        url = self._base_url + '/token'

        req = requests.get(url=url, params={'uuid': self._uuid, 'secret': self._secret}, verify=True)
        self._last_status = req.status_code

        if req.status_code == 200:
            data = req.json()
            self._token = data["results"]["token"]
            print("Authentication OK")
        elif req.status_code == 400:
            raise ValueError("Bad request : check your auth credentials")
        else:
            raise ValueError("Unexpected error")

    @staticmethod
    def homes():
        from zermapi.mappers.HomeMapper import HomeMapper
        return HomeMapper

    @staticmethod
    def rooms():
        from zermapi.mappers.RoomMapper import RoomMapper
        return RoomMapper

    @staticmethod
    def devices():
        from zermapi.mappers.DeviceMapper import DeviceMapper
        return DeviceMapper

    @staticmethod
    def units():
        from zermapi.mappers.UnitMapper import UnitMapper
        return UnitMapper

    def get(self, endpoint, params=None):
        if not self._token or self._last_status == 401:
            self._get_token()

        headers = {"Authorization": "Bearer " + self._token}
        req = requests.get(url=self._base_url + endpoint, params=params, headers=headers, verify=True)
        self._last_status = req.status_code
        return req

    def put(self, endpoint, params=None):
        if not self._token or self._last_status == 401:
            self._get_token()

        headers = {"Authorization": "Bearer " + self._token}
        req = requests.put(url=self._base_url + endpoint, params=params, headers=headers, verify=True)
        self._last_status = req.status_code
        return req
