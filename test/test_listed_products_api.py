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
from channelengine_client.api.listed_products_api import ListedProductsApi  # noqa: E501
from channelengine_client.rest import ApiException


class TestListedProductsApi(unittest.TestCase):
    """ListedProductsApi unit test stubs"""

    def setUp(self):
        self.api = ListedProductsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_listed_product_get_by_filter(self):
        """Test case for listed_product_get_by_filter

        Gets products listed by channel  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
