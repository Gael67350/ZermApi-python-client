#
#  ZermApi-python-client : A Python client library for ZermApi (https://api.zermthings.fr)
#  Copyright (c) 2018 SCION Gael (https://www.gael67350.eu)
#

# -*- coding: utf-8 -*-
from zermapi.ZermApi import ZermApi
from zermapi.objects.Response import Response


class UnitMapper(object):

    @staticmethod
    def find_all():
        req = ZermApi().get(endpoint='/units')
        data = req.json()
        return Response(status=data["status"], message=data["message"], url=data["uri"], data=data["results"])

    @staticmethod
    def find_by_id(id):
        req = ZermApi().get(endpoint='/units/' + str(id))
        data = req.json()
        return Response(status=data["status"], message=data["message"], url=data["uri"], data=data["results"])
