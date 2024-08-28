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


class ProductAttributesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def product_attribute_group_add_product_extra_data(self, group_name, **kwargs):  # noqa: E501
        """Adds custom attributes to a group  # noqa: E501

        Adds the provided custom attributes (a.k.a. extra data keys) to the custom attribute group.<br />**NB:** you can only add existing custom attributes to a group.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.product_attribute_group_add_product_extra_data(group_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_name: The group name of the product attribute group you wish to add product extra data. (required)
        :param AddProductExtraDataRequests body: Product extra data keys to be added.
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.product_attribute_group_add_product_extra_data_with_http_info(group_name, **kwargs)  # noqa: E501
        else:
            (data) = self.product_attribute_group_add_product_extra_data_with_http_info(group_name, **kwargs)  # noqa: E501
            return data

    def product_attribute_group_add_product_extra_data_with_http_info(self, group_name, **kwargs):  # noqa: E501
        """Adds custom attributes to a group  # noqa: E501

        Adds the provided custom attributes (a.k.a. extra data keys) to the custom attribute group.<br />**NB:** you can only add existing custom attributes to a group.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.product_attribute_group_add_product_extra_data_with_http_info(group_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_name: The group name of the product attribute group you wish to add product extra data. (required)
        :param AddProductExtraDataRequests body: Product extra data keys to be added.
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group_name', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method product_attribute_group_add_product_extra_data" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group_name' is set
        if ('group_name' not in params or
                params['group_name'] is None):
            raise ValueError("Missing the required parameter `group_name` when calling `product_attribute_group_add_product_extra_data`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_name' in params:
            path_params['groupName'] = params['group_name']  # noqa: E501

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
            '/v2/product-attribute-group/{groupName}/add', 'PUT',
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

    def product_attribute_group_create(self, body, **kwargs):  # noqa: E501
        """Creates a custom attribute group  # noqa: E501

        Creates a custom attribute group based on the set of custom attributes (a.k.a. extra data keys).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.product_attribute_group_create(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[ProductAttributeGroupRequest] body: Collection of product attribute groups with linked product extra data keys. (required)
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.product_attribute_group_create_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.product_attribute_group_create_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def product_attribute_group_create_with_http_info(self, body, **kwargs):  # noqa: E501
        """Creates a custom attribute group  # noqa: E501

        Creates a custom attribute group based on the set of custom attributes (a.k.a. extra data keys).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.product_attribute_group_create_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[ProductAttributeGroupRequest] body: Collection of product attribute groups with linked product extra data keys. (required)
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
                    " to method product_attribute_group_create" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `product_attribute_group_create`")  # noqa: E501

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
            '/v2/product-attribute-group', 'POST',
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

    def product_attribute_group_delete(self, group_name, **kwargs):  # noqa: E501
        """Deletes a custom attribute group  # noqa: E501

        Deletes the custom attribute group based on the **Group name** provided.<br />**NB:** you can only delete a custom attribute group that does not have any markeplaces (a.k.a. channels) linked to it.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.product_attribute_group_delete(group_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_name: The group name of the product attribute group you wish to delete. (required)
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.product_attribute_group_delete_with_http_info(group_name, **kwargs)  # noqa: E501
        else:
            (data) = self.product_attribute_group_delete_with_http_info(group_name, **kwargs)  # noqa: E501
            return data

    def product_attribute_group_delete_with_http_info(self, group_name, **kwargs):  # noqa: E501
        """Deletes a custom attribute group  # noqa: E501

        Deletes the custom attribute group based on the **Group name** provided.<br />**NB:** you can only delete a custom attribute group that does not have any markeplaces (a.k.a. channels) linked to it.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.product_attribute_group_delete_with_http_info(group_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_name: The group name of the product attribute group you wish to delete. (required)
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method product_attribute_group_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group_name' is set
        if ('group_name' not in params or
                params['group_name'] is None):
            raise ValueError("Missing the required parameter `group_name` when calling `product_attribute_group_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_name' in params:
            path_params['groupName'] = params['group_name']  # noqa: E501

        query_params = []

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
            '/v2/product-attribute-group/{groupName}', 'DELETE',
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

    def product_attribute_group_get_by_filter(self, **kwargs):  # noqa: E501
        """Gets custom attribute groups  # noqa: E501

        Gets the custom attribute groups based on the **Group name** provided.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.product_attribute_group_get_by_filter(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] group_names:
        :param int page: The page to filter on. Starts at 1.
        :return: CollectionOfMerchantProductAttributeGroupWithProductExtraDataResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.product_attribute_group_get_by_filter_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.product_attribute_group_get_by_filter_with_http_info(**kwargs)  # noqa: E501
            return data

    def product_attribute_group_get_by_filter_with_http_info(self, **kwargs):  # noqa: E501
        """Gets custom attribute groups  # noqa: E501

        Gets the custom attribute groups based on the **Group name** provided.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.product_attribute_group_get_by_filter_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] group_names:
        :param int page: The page to filter on. Starts at 1.
        :return: CollectionOfMerchantProductAttributeGroupWithProductExtraDataResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group_names', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method product_attribute_group_get_by_filter" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'group_names' in params:
            query_params.append(('groupNames', params['group_names']))  # noqa: E501
            collection_formats['groupNames'] = 'multi'  # noqa: E501
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
            '/v2/product-attribute-group', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CollectionOfMerchantProductAttributeGroupWithProductExtraDataResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def product_attribute_group_get_with_channels_by_filter(self, **kwargs):  # noqa: E501
        """Gets custom attribute groups and linked marketplaces  # noqa: E501

        Gets all custom attribute groups and marketplaces (a.k.a. channels) linked to them.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.product_attribute_group_get_with_channels_by_filter(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] group_names:
        :param int page: The page to filter on. Starts at 1.
        :return: CollectionOfMerchantProductAttributeGroupWithLinkedChannelsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.product_attribute_group_get_with_channels_by_filter_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.product_attribute_group_get_with_channels_by_filter_with_http_info(**kwargs)  # noqa: E501
            return data

    def product_attribute_group_get_with_channels_by_filter_with_http_info(self, **kwargs):  # noqa: E501
        """Gets custom attribute groups and linked marketplaces  # noqa: E501

        Gets all custom attribute groups and marketplaces (a.k.a. channels) linked to them.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.product_attribute_group_get_with_channels_by_filter_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] group_names:
        :param int page: The page to filter on. Starts at 1.
        :return: CollectionOfMerchantProductAttributeGroupWithLinkedChannelsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group_names', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method product_attribute_group_get_with_channels_by_filter" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'group_names' in params:
            query_params.append(('groupNames', params['group_names']))  # noqa: E501
            collection_formats['groupNames'] = 'multi'  # noqa: E501
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
            '/v2/product-attribute-group/linked-channels', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CollectionOfMerchantProductAttributeGroupWithLinkedChannelsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def product_attribute_group_remove_product_extra_data(self, group_name, **kwargs):  # noqa: E501
        """Deletes custom attributes from a group  # noqa: E501

        Removes the custom attributes (a.k.a. extra data keys) from the custom attribute group.<br />**NB:** you can only remove existing custom attributes from a group.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.product_attribute_group_remove_product_extra_data(group_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_name: The group name of the product attribute group you wish to remove product extra data. (required)
        :param RemoveProductExtraDataRequests body: Product extra data keys to be removed.
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.product_attribute_group_remove_product_extra_data_with_http_info(group_name, **kwargs)  # noqa: E501
        else:
            (data) = self.product_attribute_group_remove_product_extra_data_with_http_info(group_name, **kwargs)  # noqa: E501
            return data

    def product_attribute_group_remove_product_extra_data_with_http_info(self, group_name, **kwargs):  # noqa: E501
        """Deletes custom attributes from a group  # noqa: E501

        Removes the custom attributes (a.k.a. extra data keys) from the custom attribute group.<br />**NB:** you can only remove existing custom attributes from a group.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.product_attribute_group_remove_product_extra_data_with_http_info(group_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_name: The group name of the product attribute group you wish to remove product extra data. (required)
        :param RemoveProductExtraDataRequests body: Product extra data keys to be removed.
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group_name', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method product_attribute_group_remove_product_extra_data" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group_name' is set
        if ('group_name' not in params or
                params['group_name'] is None):
            raise ValueError("Missing the required parameter `group_name` when calling `product_attribute_group_remove_product_extra_data`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_name' in params:
            path_params['groupName'] = params['group_name']  # noqa: E501

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
            '/v2/product-attribute-group/{groupName}/remove', 'PUT',
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

    def product_attribute_group_rename_product_attribute_group(self, **kwargs):  # noqa: E501
        """Renames custom attribute groups  # noqa: E501

        Renames the custom attribute groups.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.product_attribute_group_rename_product_attribute_group(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[RenameProductAttributeGroupRequests] body: List of old and new product attribute group names.
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.product_attribute_group_rename_product_attribute_group_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.product_attribute_group_rename_product_attribute_group_with_http_info(**kwargs)  # noqa: E501
            return data

    def product_attribute_group_rename_product_attribute_group_with_http_info(self, **kwargs):  # noqa: E501
        """Renames custom attribute groups  # noqa: E501

        Renames the custom attribute groups.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.product_attribute_group_rename_product_attribute_group_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[RenameProductAttributeGroupRequests] body: List of old and new product attribute group names.
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
                    " to method product_attribute_group_rename_product_attribute_group" % key
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
            '/v2/product-attribute-group/rename', 'POST',
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
