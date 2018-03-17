#
#  ZermApi-python-client : A Python client library for ZermApi (https://api.zermthings.fr)
#  Copyright (c) 2018 SCION Gael (https://www.gael67350.eu)
#

from zermapi.ZermApi import ZermApi
# -*- coding: utf-8 -*-
from zermapi.objects.Response import Response


class DeviceMapper(object):

    @staticmethod
    def find_all():
        req = ZermApi().get(endpoint='/devices')
        data = req.json()
        return Response(status=data["status"], message=data["message"], url=data["uri"], data=data["results"])

    @staticmethod
    def find_by_uuid(uuid):
        req = ZermApi().get(endpoint='/devices/' + uuid)
        data = req.json()
        return Response(status=data["status"], message=data["message"], url=data["uri"], data=data["results"])

    @staticmethod
    def get_device_features(uuid, sensor=None):
        url = '/devices/' + uuid + '/features'

        if isinstance(sensor, bool):
            req = ZermApi().get(endpoint=url, params={'sensor': sensor})
        else:
            req = ZermApi().get(endpoint=url)

        data = req.json()
        return Response(status=data["status"], message=data["message"], url=data["uri"], data=data["results"])

    @staticmethod
    def get_device_feature(uuid, feature_id, logical=None):
        url = '/devices/' + uuid + '/features/' + str(feature_id)

        if isinstance(logical, int):
            req = ZermApi().get(endpoint=url, params={'logical': logical})
        else:
            req = ZermApi().get(endpoint=url)

        data = req.json()
        return Response(status=data["status"], message=data["message"], url=data["uri"], data=data["results"])

    @staticmethod
    def get_device_feature_states(uuid, feature_id, limit=10):
        url = '/devices/' + uuid + '/features/' + str(feature_id) + '/states'

        req = ZermApi().get(endpoint=url, params={'limit': limit})
        data = req.json()
        return Response(status=data["status"], message=data["message"], url=data["uri"], data=data["results"])

    @staticmethod
    def get_device_feature_state(uuid, feature_id, state_id, logical=None):
        url = '/devices/' + uuid + '/features/' + str(feature_id) + '/states/' + str(state_id)

        if isinstance(logical, int):
            req = ZermApi().get(endpoint=url, params={'logical': logical})
        else:
            req = ZermApi().get(endpoint=url)

        data = req.json()
        return Response(status=data["status"], message=data["message"], url=data["uri"], data=data["results"])

    @staticmethod
    def set_device_feature_state(uuid, feature_id, value=0, logical=None):
        url = '/devices/' + uuid + '/features/' + str(feature_id) + '/states'

        if isinstance(logical, int):
            req = ZermApi().put(endpoint=url, params={'value': value, 'logical': logical})
        else:
            req = ZermApi().put(endpoint=url, params={'value': value})

        data = req.json()
        return Response(status=data["status"], message=data["message"], url=data["uri"], data=data["results"])

    @staticmethod
    def reset_device_states(uuid):
        url = '/devices/' + uuid + '/states/reset'

        req = ZermApi().put(endpoint=url)
        data = req.json()
        return Response(status=data["status"], message=data["message"], url=data["uri"], data=data["results"])
