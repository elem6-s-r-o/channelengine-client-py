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


class RefundsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def refund_acknowledge(self, **kwargs):  # noqa: E501
        """[CLOSED BETA] Acknowledge a refund  # noqa: E501

        Acknowledges a refund<br /> <br />Beware, this endpoint is part of a closed beta and is only available for closed beta participants.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.refund_acknowledge(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SingleMerchantAcknowledgeRefundRequest body: The refund to acknowledge
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.refund_acknowledge_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.refund_acknowledge_with_http_info(**kwargs)  # noqa: E501
            return data

    def refund_acknowledge_with_http_info(self, **kwargs):  # noqa: E501
        """[CLOSED BETA] Acknowledge a refund  # noqa: E501

        Acknowledges a refund<br /> <br />Beware, this endpoint is part of a closed beta and is only available for closed beta participants.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.refund_acknowledge_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SingleMerchantAcknowledgeRefundRequest body: The refund to acknowledge
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method refund_acknowledge" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/v2.1/refunds/merchant/acknowledge', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def refund_create(self, **kwargs):  # noqa: E501
        """[CLOSED BETA] Create a refund  # noqa: E501

        Creates a new refund<br /> <br />Beware, this endpoint is part of a closed beta and is only available for closed beta participants.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.refund_create(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SingleMerchantCreateRefundRequest body: The refund
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.refund_create_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.refund_create_with_http_info(**kwargs)  # noqa: E501
            return data

    def refund_create_with_http_info(self, **kwargs):  # noqa: E501
        """[CLOSED BETA] Create a refund  # noqa: E501

        Creates a new refund<br /> <br />Beware, this endpoint is part of a closed beta and is only available for closed beta participants.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.refund_create_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SingleMerchantCreateRefundRequest body: The refund
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method refund_create" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/v2.1/refunds/merchant', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def refund_get(self, identifier, **kwargs):  # noqa: E501
        """[CLOSED BETA] Get refund by identifier  # noqa: E501

        Gets a single refund by the given identifier<br /> <br />Beware, this endpoint is part of a closed beta and is only available for closed beta participants.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.refund_get(identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str identifier: The identifier to search for (required)
        :param RefundIdentifier type: Specify whether to search by ID, Merchant Refund No or Channel Refund No
        :return: SingleOfIRefund
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.refund_get_with_http_info(identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.refund_get_with_http_info(identifier, **kwargs)  # noqa: E501
            return data

    def refund_get_with_http_info(self, identifier, **kwargs):  # noqa: E501
        """[CLOSED BETA] Get refund by identifier  # noqa: E501

        Gets a single refund by the given identifier<br /> <br />Beware, this endpoint is part of a closed beta and is only available for closed beta participants.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.refund_get_with_http_info(identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str identifier: The identifier to search for (required)
        :param RefundIdentifier type: Specify whether to search by ID, Merchant Refund No or Channel Refund No
        :return: SingleOfIRefund
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['identifier', 'type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method refund_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `refund_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'identifier' in params:
            path_params['identifier'] = params['identifier']  # noqa: E501

        query_params = []
        if 'type' in params:
            query_params.append(('type', params['type']))  # noqa: E501

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
            '/v2.1/refunds/merchant/{identifier}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SingleOfIRefund',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def refund_get_by_filter(self, **kwargs):  # noqa: E501
        """[CLOSED BETA] Get refunds by filter  # noqa: E501

        Gets multiple refunds by the given filter<br /> <br />Beware, this endpoint is part of a closed beta and is only available for closed beta participants.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.refund_get_by_filter(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RefundByFilterIdentifier identifiers_identifier_type: The type of identifier: which identifier to filter on
        :param list[str] identifiers_models: The value (of the selected type) to filter on
        :param list[ChannelExportStatus] channel_export_status_statuses:
        :param int channel_export_status_max_number_of_export_attempts:
        :param list[RefundReason] reasons:
        :param datetime created_date_range_from_date:
        :param datetime created_date_range_to_date:
        :param list[int] channel_ids:
        :param str search:
        :param bool is_acknowledged_by_merchant:
        :param bool is_acknowledged_by_channel:
        :param ModuleFulfillmentType fulfillment_type:
        :param CreatorType creator_type:
        :param list[str] external_batch_nos:
        :param int page_index:
        :param int page_size:
        :return: SingleOfIRefund
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.refund_get_by_filter_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.refund_get_by_filter_with_http_info(**kwargs)  # noqa: E501
            return data

    def refund_get_by_filter_with_http_info(self, **kwargs):  # noqa: E501
        """[CLOSED BETA] Get refunds by filter  # noqa: E501

        Gets multiple refunds by the given filter<br /> <br />Beware, this endpoint is part of a closed beta and is only available for closed beta participants.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.refund_get_by_filter_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RefundByFilterIdentifier identifiers_identifier_type: The type of identifier: which identifier to filter on
        :param list[str] identifiers_models: The value (of the selected type) to filter on
        :param list[ChannelExportStatus] channel_export_status_statuses:
        :param int channel_export_status_max_number_of_export_attempts:
        :param list[RefundReason] reasons:
        :param datetime created_date_range_from_date:
        :param datetime created_date_range_to_date:
        :param list[int] channel_ids:
        :param str search:
        :param bool is_acknowledged_by_merchant:
        :param bool is_acknowledged_by_channel:
        :param ModuleFulfillmentType fulfillment_type:
        :param CreatorType creator_type:
        :param list[str] external_batch_nos:
        :param int page_index:
        :param int page_size:
        :return: SingleOfIRefund
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['identifiers_identifier_type', 'identifiers_models', 'channel_export_status_statuses', 'channel_export_status_max_number_of_export_attempts', 'reasons', 'created_date_range_from_date', 'created_date_range_to_date', 'channel_ids', 'search', 'is_acknowledged_by_merchant', 'is_acknowledged_by_channel', 'fulfillment_type', 'creator_type', 'external_batch_nos', 'page_index', 'page_size']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method refund_get_by_filter" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'identifiers_identifier_type' in params:
            query_params.append(('identifiers.identifierType', params['identifiers_identifier_type']))  # noqa: E501
        if 'identifiers_models' in params:
            query_params.append(('identifiers.models', params['identifiers_models']))  # noqa: E501
            collection_formats['identifiers.models'] = 'multi'  # noqa: E501
        if 'channel_export_status_statuses' in params:
            query_params.append(('channelExportStatus.statuses', params['channel_export_status_statuses']))  # noqa: E501
            collection_formats['channelExportStatus.statuses'] = 'multi'  # noqa: E501
        if 'channel_export_status_max_number_of_export_attempts' in params:
            query_params.append(('channelExportStatus.maxNumberOfExportAttempts', params['channel_export_status_max_number_of_export_attempts']))  # noqa: E501
        if 'reasons' in params:
            query_params.append(('reasons', params['reasons']))  # noqa: E501
            collection_formats['reasons'] = 'multi'  # noqa: E501
        if 'created_date_range_from_date' in params:
            query_params.append(('createdDateRange.fromDate', params['created_date_range_from_date']))  # noqa: E501
        if 'created_date_range_to_date' in params:
            query_params.append(('createdDateRange.toDate', params['created_date_range_to_date']))  # noqa: E501
        if 'channel_ids' in params:
            query_params.append(('channelIds', params['channel_ids']))  # noqa: E501
            collection_formats['channelIds'] = 'multi'  # noqa: E501
        if 'search' in params:
            query_params.append(('search', params['search']))  # noqa: E501
        if 'is_acknowledged_by_merchant' in params:
            query_params.append(('isAcknowledgedByMerchant', params['is_acknowledged_by_merchant']))  # noqa: E501
        if 'is_acknowledged_by_channel' in params:
            query_params.append(('isAcknowledgedByChannel', params['is_acknowledged_by_channel']))  # noqa: E501
        if 'fulfillment_type' in params:
            query_params.append(('fulfillmentType', params['fulfillment_type']))  # noqa: E501
        if 'creator_type' in params:
            query_params.append(('creatorType', params['creator_type']))  # noqa: E501
        if 'external_batch_nos' in params:
            query_params.append(('externalBatchNos', params['external_batch_nos']))  # noqa: E501
            collection_formats['externalBatchNos'] = 'multi'  # noqa: E501
        if 'page_index' in params:
            query_params.append(('pageIndex', params['page_index']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))  # noqa: E501

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
            '/v2.1/refunds/merchant', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SingleOfIRefund',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
