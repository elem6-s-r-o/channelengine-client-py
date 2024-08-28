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
from channelengine_client.api.competition_prices_api import CompetitionPricesApi  # noqa: E501
from channelengine_client.rest import ApiException


class TestCompetitionPricesApi(unittest.TestCase):
    """CompetitionPricesApi unit test stubs"""

    def setUp(self):
        self.api = CompetitionPricesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_competition_prices_get_buy_box_prices(self):
        """Test case for competition_prices_get_buy_box_prices

        Gets the price from the buy box winner  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()