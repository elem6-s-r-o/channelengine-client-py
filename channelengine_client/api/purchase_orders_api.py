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


class PurchaseOrdersApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def acknowledge(self, **kwargs):  # noqa: E501
        """Acknowledges lines of a purchase order  # noqa: E501

        Creates line acknowledgements (i.e., accepted, backordered, rejected) for a purchase order.<br />Request will be accepted and data persisted only if all validations passed.<br />Any validation messages and errors will be returned in a HTTP 4xx response.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.acknowledge(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SingleMerchantAcknowledgePurchaseOrderLinesRequest body: Model for purchase order and lines data to be acknowledged with the channel.
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.acknowledge_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.acknowledge_with_http_info(**kwargs)  # noqa: E501
            return data

    def acknowledge_with_http_info(self, **kwargs):  # noqa: E501
        """Acknowledges lines of a purchase order  # noqa: E501

        Creates line acknowledgements (i.e., accepted, backordered, rejected) for a purchase order.<br />Request will be accepted and data persisted only if all validations passed.<br />Any validation messages and errors will be returned in a HTTP 4xx response.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.acknowledge_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SingleMerchantAcknowledgePurchaseOrderLinesRequest body: Model for purchase order and lines data to be acknowledged with the channel.
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
                    " to method acknowledge" % key
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
            '/v2/purchase-orders/lines/acknowledge', 'POST',
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

    def create(self, **kwargs):  # noqa: E501
        """Create a purchase order shipment.  # noqa: E501

        One shipments can ship (parts of) multiple orders  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SingleMerchantCreatePurchaseOrderShipmentRequest body:
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.create_with_http_info(**kwargs)  # noqa: E501
            return data

    def create_with_http_info(self, **kwargs):  # noqa: E501
        """Create a purchase order shipment.  # noqa: E501

        One shipments can ship (parts of) multiple orders  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SingleMerchantCreatePurchaseOrderShipmentRequest body:
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
                    " to method create" % key
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
            '/v2/purchase-orders/shipments', 'POST',
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

    def get_by_filter(self, **kwargs):  # noqa: E501
        """Gets purchase order shipments by filter  # noqa: E501

        Gets purchase order shipments based on the available filters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_by_filter(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int channel_id: The identifier of the channel
        :param PurchaseOrderShipmentIdentifierTypeValue identifiers_identifier_type: The type of identifier: which identifier to filter on
        :param list[str] identifiers_models: The value (of the selected type) to filter on
        :param datetime shipped_date_range_from_date:
        :param datetime shipped_date_range_to_date:
        :param datetime create_date_range_from_date:
        :param datetime create_date_range_to_date:
        :param datetime update_date_range_from_date:
        :param datetime update_date_range_to_date:
        :param str bill_of_lading_number: The Bill of Lading number. Multiple shipments can have the same Bill of Lading number
        :param str carrier_name: The name of the carrier
        :param int page_index:
        :param int page_size:
        :return: CollectionOfIPurchaseOrderShipmentByFilter
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_by_filter_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_by_filter_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_by_filter_with_http_info(self, **kwargs):  # noqa: E501
        """Gets purchase order shipments by filter  # noqa: E501

        Gets purchase order shipments based on the available filters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_by_filter_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int channel_id: The identifier of the channel
        :param PurchaseOrderShipmentIdentifierTypeValue identifiers_identifier_type: The type of identifier: which identifier to filter on
        :param list[str] identifiers_models: The value (of the selected type) to filter on
        :param datetime shipped_date_range_from_date:
        :param datetime shipped_date_range_to_date:
        :param datetime create_date_range_from_date:
        :param datetime create_date_range_to_date:
        :param datetime update_date_range_from_date:
        :param datetime update_date_range_to_date:
        :param str bill_of_lading_number: The Bill of Lading number. Multiple shipments can have the same Bill of Lading number
        :param str carrier_name: The name of the carrier
        :param int page_index:
        :param int page_size:
        :return: CollectionOfIPurchaseOrderShipmentByFilter
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['channel_id', 'identifiers_identifier_type', 'identifiers_models', 'shipped_date_range_from_date', 'shipped_date_range_to_date', 'create_date_range_from_date', 'create_date_range_to_date', 'update_date_range_from_date', 'update_date_range_to_date', 'bill_of_lading_number', 'carrier_name', 'page_index', 'page_size']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_by_filter" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'channel_id' in params:
            query_params.append(('channelId', params['channel_id']))  # noqa: E501
        if 'identifiers_identifier_type' in params:
            query_params.append(('identifiers.identifierType', params['identifiers_identifier_type']))  # noqa: E501
        if 'identifiers_models' in params:
            query_params.append(('identifiers.models', params['identifiers_models']))  # noqa: E501
            collection_formats['identifiers.models'] = 'multi'  # noqa: E501
        if 'shipped_date_range_from_date' in params:
            query_params.append(('shippedDateRange.fromDate', params['shipped_date_range_from_date']))  # noqa: E501
        if 'shipped_date_range_to_date' in params:
            query_params.append(('shippedDateRange.toDate', params['shipped_date_range_to_date']))  # noqa: E501
        if 'create_date_range_from_date' in params:
            query_params.append(('createDateRange.fromDate', params['create_date_range_from_date']))  # noqa: E501
        if 'create_date_range_to_date' in params:
            query_params.append(('createDateRange.toDate', params['create_date_range_to_date']))  # noqa: E501
        if 'update_date_range_from_date' in params:
            query_params.append(('updateDateRange.fromDate', params['update_date_range_from_date']))  # noqa: E501
        if 'update_date_range_to_date' in params:
            query_params.append(('updateDateRange.toDate', params['update_date_range_to_date']))  # noqa: E501
        if 'bill_of_lading_number' in params:
            query_params.append(('billOfLadingNumber', params['bill_of_lading_number']))  # noqa: E501
        if 'carrier_name' in params:
            query_params.append(('carrierName', params['carrier_name']))  # noqa: E501
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
            '/v2/purchase-orders/shipments/merchant', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CollectionOfIPurchaseOrderShipmentByFilter',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_by_filter_0(self, **kwargs):  # noqa: E501
        """Gets purchase orders by filter  # noqa: E501

        Gets purchase orders based on the available filters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_by_filter_0(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PurchaseOrderIdentifierType identifiers_identifier_type: The type of identifier: which identifier to filter on
        :param list[str] identifiers_models: The value (of the selected type) to filter on
        :param list[ModulesPurchaseOrderStatus] statuses:
        :param datetime order_date_range_from_date:
        :param datetime order_date_range_to_date:
        :param datetime create_date_range_from_date:
        :param datetime create_date_range_to_date:
        :param datetime update_date_range_from_date:
        :param datetime update_date_range_to_date:
        :param list[int] channel_ids:
        :param ModulesPurchaseOrderType type:
        :param int page_index:
        :param int page_size:
        :return: CollectionOfIPurchaseOrderByFilter
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_by_filter_0_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_by_filter_0_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_by_filter_0_with_http_info(self, **kwargs):  # noqa: E501
        """Gets purchase orders by filter  # noqa: E501

        Gets purchase orders based on the available filters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_by_filter_0_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PurchaseOrderIdentifierType identifiers_identifier_type: The type of identifier: which identifier to filter on
        :param list[str] identifiers_models: The value (of the selected type) to filter on
        :param list[ModulesPurchaseOrderStatus] statuses:
        :param datetime order_date_range_from_date:
        :param datetime order_date_range_to_date:
        :param datetime create_date_range_from_date:
        :param datetime create_date_range_to_date:
        :param datetime update_date_range_from_date:
        :param datetime update_date_range_to_date:
        :param list[int] channel_ids:
        :param ModulesPurchaseOrderType type:
        :param int page_index:
        :param int page_size:
        :return: CollectionOfIPurchaseOrderByFilter
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['identifiers_identifier_type', 'identifiers_models', 'statuses', 'order_date_range_from_date', 'order_date_range_to_date', 'create_date_range_from_date', 'create_date_range_to_date', 'update_date_range_from_date', 'update_date_range_to_date', 'channel_ids', 'type', 'page_index', 'page_size']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_by_filter_0" % key
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
        if 'statuses' in params:
            query_params.append(('statuses', params['statuses']))  # noqa: E501
            collection_formats['statuses'] = 'multi'  # noqa: E501
        if 'order_date_range_from_date' in params:
            query_params.append(('orderDateRange.fromDate', params['order_date_range_from_date']))  # noqa: E501
        if 'order_date_range_to_date' in params:
            query_params.append(('orderDateRange.toDate', params['order_date_range_to_date']))  # noqa: E501
        if 'create_date_range_from_date' in params:
            query_params.append(('createDateRange.fromDate', params['create_date_range_from_date']))  # noqa: E501
        if 'create_date_range_to_date' in params:
            query_params.append(('createDateRange.toDate', params['create_date_range_to_date']))  # noqa: E501
        if 'update_date_range_from_date' in params:
            query_params.append(('updateDateRange.fromDate', params['update_date_range_from_date']))  # noqa: E501
        if 'update_date_range_to_date' in params:
            query_params.append(('updateDateRange.toDate', params['update_date_range_to_date']))  # noqa: E501
        if 'channel_ids' in params:
            query_params.append(('channelIds', params['channel_ids']))  # noqa: E501
            collection_formats['channelIds'] = 'multi'  # noqa: E501
        if 'type' in params:
            query_params.append(('type', params['type']))  # noqa: E501
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
            '/v2/purchase-orders', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CollectionOfIPurchaseOrderByFilter',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def purchase_orders_create_invoice(self, **kwargs):  # noqa: E501
        """Creates a purchase order invoice  # noqa: E501

        Creates invoice for a purchase order.<br />Request will be accepted and data persisted only if all validations passed.<br />Any validation messages and errors will be returned in a HTTP 4xx response.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.purchase_orders_create_invoice(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SingleMerchantCreatePurchaseOrderInvoiceRequest body: Model for purchase order invoice.
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.purchase_orders_create_invoice_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.purchase_orders_create_invoice_with_http_info(**kwargs)  # noqa: E501
            return data

    def purchase_orders_create_invoice_with_http_info(self, **kwargs):  # noqa: E501
        """Creates a purchase order invoice  # noqa: E501

        Creates invoice for a purchase order.<br />Request will be accepted and data persisted only if all validations passed.<br />Any validation messages and errors will be returned in a HTTP 4xx response.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.purchase_orders_create_invoice_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SingleMerchantCreatePurchaseOrderInvoiceRequest body: Model for purchase order invoice.
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
                    " to method purchase_orders_create_invoice" % key
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
            '/v2/purchase-orders/invoice', 'POST',
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

    def purchase_orders_create_invoices(self, **kwargs):  # noqa: E501
        """Creates a purchase order invoices in a bulk  # noqa: E501

        Creates invoices for a purchase orders in a bulk.<br />Request will be accepted and data persisted only if all validations passed.<br />Any validation messages and errors will be returned in a HTTP 4xx response.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.purchase_orders_create_invoices(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param BulkMerchantCreatePurchaseOrderInvoicesRequest body: Model for purchase order invoices.
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.purchase_orders_create_invoices_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.purchase_orders_create_invoices_with_http_info(**kwargs)  # noqa: E501
            return data

    def purchase_orders_create_invoices_with_http_info(self, **kwargs):  # noqa: E501
        """Creates a purchase order invoices in a bulk  # noqa: E501

        Creates invoices for a purchase orders in a bulk.<br />Request will be accepted and data persisted only if all validations passed.<br />Any validation messages and errors will be returned in a HTTP 4xx response.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.purchase_orders_create_invoices_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param BulkMerchantCreatePurchaseOrderInvoicesRequest body: Model for purchase order invoices.
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
                    " to method purchase_orders_create_invoices" % key
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
            '/v2/purchase-orders/invoice/bulk', 'POST',
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

    def update(self, **kwargs):  # noqa: E501
        """Update a purchase order shipment.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SingleMerchantUpdatePurchaseOrderShipmentRequest body:
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.update_with_http_info(**kwargs)  # noqa: E501
            return data

    def update_with_http_info(self, **kwargs):  # noqa: E501
        """Update a purchase order shipment.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SingleMerchantUpdatePurchaseOrderShipmentRequest body:
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
                    " to method update" % key
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
            '/v2/purchase-orders/shipments', 'PUT',
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
