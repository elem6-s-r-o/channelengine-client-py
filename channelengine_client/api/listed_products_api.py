# coding: utf-8

"""
    ChannelEngine Merchant API

    ChannelEngine API for merchants  # noqa: E501

    OpenAPI spec version: 2.17.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from channelengine_client.api_client import ApiClient


class ListedProductsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def listed_product_get_by_filter(self, channel_id, **kwargs):  # noqa: E501
        """Gets products listed by channel  # noqa: E501

        Gets the products listed per channel based on the **Channel ID**.<br /> <br />**NB:** not all marketplaces provide adequate options to retrieve the status of a product as seen on the marketplace.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.listed_product_get_by_filter(channel_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int channel_id: The id of a channel (required)
        :param list[str] merchant_product_nos: The unique product references used by the Merchant (SKUs)
        :param int page: The page to filter on. Starts at 1.
        :return: CollectionOfChannelListedProductResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.listed_product_get_by_filter_with_http_info(channel_id, **kwargs)  # noqa: E501
        else:
            (data) = self.listed_product_get_by_filter_with_http_info(channel_id, **kwargs)  # noqa: E501
            return data

    def listed_product_get_by_filter_with_http_info(self, channel_id, **kwargs):  # noqa: E501
        """Gets products listed by channel  # noqa: E501

        Gets the products listed per channel based on the **Channel ID**.<br /> <br />**NB:** not all marketplaces provide adequate options to retrieve the status of a product as seen on the marketplace.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.listed_product_get_by_filter_with_http_info(channel_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int channel_id: The id of a channel (required)
        :param list[str] merchant_product_nos: The unique product references used by the Merchant (SKUs)
        :param int page: The page to filter on. Starts at 1.
        :return: CollectionOfChannelListedProductResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['channel_id', 'merchant_product_nos', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method listed_product_get_by_filter" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'channel_id' is set
        if ('channel_id' not in params or
                params['channel_id'] is None):
            raise ValueError("Missing the required parameter `channel_id` when calling `listed_product_get_by_filter`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'channel_id' in params:
            path_params['channelId'] = params['channel_id']  # noqa: E501

        query_params = []
        if 'merchant_product_nos' in params:
            query_params.append(('merchantProductNos', params['merchant_product_nos']))  # noqa: E501
            collection_formats['merchantProductNos'] = 'multi'  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/v2/channels/{channelId}/products', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CollectionOfChannelListedProductResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
