# coding: utf-8

"""
    ChannelEngine Merchant API

    ChannelEngine API for merchants  # noqa: E501

    OpenAPI spec version: 2.17.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import channelengine_client
from channelengine_client.api.notifications_api import NotificationsApi  # noqa: E501
from channelengine_client.rest import ApiException


class TestNotificationsApi(unittest.TestCase):
    """NotificationsApi unit test stubs"""

    def setUp(self):
        self.api = NotificationsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_notification_index(self):
        """Test case for notification_index

        Gets notifications  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
