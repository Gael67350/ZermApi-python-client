#
#  ZermApi-python-client : A Python client library for ZermApi (https://api.zermthings.fr)
#  Copyright (c) 2018 SCION Gael (https://www.gael67350.eu)
#

# -*- coding: utf-8 -*-
from zermapi.ZermApi import ZermApi

UUID = "3e6f2591-dd00-4f35-92ca-ea2336811444"
SECRET = "a336ff50f88c7df768ab4e05be0e3963"

# Instantiation of the main class
api = ZermApi(UUID, SECRET)

# List all homes
r = api.homes().find_all()
print(r.data)

# Get the room with id=1
r = api.rooms().find_by_id(1)
print(r.data)

# List all devices
r = api.devices().find_all()
print(r.data)

# Get the device with uuid=bf26791d-ff9b-4755-935f-166fd82f33f0
r = api.devices().find_by_uuid("bf26791d-ff9b-4755-935f-166fd82f33f0")
print(r.data)

# Reset device state with uuid=bf26791d-ff9b-4755-935f-166fd82f33f0
r = api.devices().reset_device_states("bf26791d-ff9b-4755-935f-166fd82f33f0")
print(r.data)
