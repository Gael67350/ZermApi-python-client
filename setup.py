#
#  ZermApi-python-client : A Python client library for ZermApi (https://api.zermthings.fr)
#  Copyright (c) 2018 SCION Gael (https://www.gael67350.eu)
#

from setuptools import setup

setup(
    name='ZermApi-python-client',
    version='1.0',
    packages=['src', 'src.mappers', 'src.objects'],
    url='https://api.zermthings.fr',
    license='MIT License',
    author='Gael SCION',
    author_email='gael67350@gmail.com',
    description='A Python client library for ZermApi',
    install_requires=['requests']
)
