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
from channelengine_client.api.refunds_api import RefundsApi  # noqa: E501
from channelengine_client.rest import ApiException


class TestRefundsApi(unittest.TestCase):
    """RefundsApi unit test stubs"""

    def setUp(self):
        self.api = RefundsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_refund_acknowledge(self):
        """Test case for refund_acknowledge

        [CLOSED BETA] Acknowledge a refund  # noqa: E501
        """
        pass

    def test_refund_create(self):
        """Test case for refund_create

        [CLOSED BETA] Create a refund  # noqa: E501
        """
        pass

    def test_refund_get(self):
        """Test case for refund_get

        [CLOSED BETA] Get refund by identifier  # noqa: E501
        """
        pass

    def test_refund_get_by_filter(self):
        """Test case for refund_get_by_filter

        [CLOSED BETA] Get refunds by filter  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()