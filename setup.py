#!/usr/bin/python

from setuptools import setup

setup(name='swift_tempurl',
    version='1.0.0',
    description='Tempurl with cname and domainremap support',
    author='Koert van der Veer, CloudVPS',
    author_email='koert@cloudvps.com',
    url='https://github.com/CloudVPS/swift-tempurl',
    py_modules=['tempurl', 'formpost'],
    requires=['swift(>=1.7)'],
    entry_points = {
        'paste.filter_factory': [
            'tempurl_cloudvps=tempurl:filter_factory',
            'formpost_cloudvps=formpost:filter_factory',
        ]
    }
)