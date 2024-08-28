# channelengine_client.ProductAttributesApi

All URIs are relative to *https://demo.channelengine.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**product_attribute_group_add_product_extra_data**](ProductAttributesApi.md#product_attribute_group_add_product_extra_data) | **PUT** /v2/product-attribute-group/{groupName}/add | Adds custom attributes to a group
[**product_attribute_group_create**](ProductAttributesApi.md#product_attribute_group_create) | **POST** /v2/product-attribute-group | Creates a custom attribute group
[**product_attribute_group_delete**](ProductAttributesApi.md#product_attribute_group_delete) | **DELETE** /v2/product-attribute-group/{groupName} | Deletes a custom attribute group
[**product_attribute_group_get_by_filter**](ProductAttributesApi.md#product_attribute_group_get_by_filter) | **GET** /v2/product-attribute-group | Gets custom attribute groups
[**product_attribute_group_get_with_channels_by_filter**](ProductAttributesApi.md#product_attribute_group_get_with_channels_by_filter) | **GET** /v2/product-attribute-group/linked-channels | Gets custom attribute groups and linked marketplaces
[**product_attribute_group_remove_product_extra_data**](ProductAttributesApi.md#product_attribute_group_remove_product_extra_data) | **PUT** /v2/product-attribute-group/{groupName}/remove | Deletes custom attributes from a group
[**product_attribute_group_rename_product_attribute_group**](ProductAttributesApi.md#product_attribute_group_rename_product_attribute_group) | **POST** /v2/product-attribute-group/rename | Renames custom attribute groups

# **product_attribute_group_add_product_extra_data**
> ApiResponse product_attribute_group_add_product_extra_data(group_name, body=body)

Adds custom attributes to a group

Adds the provided custom attributes (a.k.a. extra data keys) to the custom attribute group.<br />**NB:** you can only add existing custom attributes to a group.

### Example
```python
from __future__ import print_function
import time
import channelengine_client
from channelengine_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = channelengine_client.Configuration()
configuration.api_key['apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# create an instance of the API class
api_instance = channelengine_client.ProductAttributesApi(channelengine_client.ApiClient(configuration))
group_name = 'group_name_example' # str | The group name of the product attribute group you wish to add product extra data.
body = channelengine_client.AddProductExtraDataRequests() # AddProductExtraDataRequests | Product extra data keys to be added. (optional)

try:
    # Adds custom attributes to a group
    api_response = api_instance.product_attribute_group_add_product_extra_data(group_name, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductAttributesApi->product_attribute_group_add_product_extra_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | **str**| The group name of the product attribute group you wish to add product extra data. | 
 **body** | [**AddProductExtraDataRequests**](AddProductExtraDataRequests.md)| Product extra data keys to be added. | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_attribute_group_create**
> ApiResponse product_attribute_group_create(body)

Creates a custom attribute group

Creates a custom attribute group based on the set of custom attributes (a.k.a. extra data keys).

### Example
```python
from __future__ import print_function
import time
import channelengine_client
from channelengine_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = channelengine_client.Configuration()
configuration.api_key['apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# create an instance of the API class
api_instance = channelengine_client.ProductAttributesApi(channelengine_client.ApiClient(configuration))
body = [channelengine_client.ProductAttributeGroupRequest()] # list[ProductAttributeGroupRequest] | Collection of product attribute groups with linked product extra data keys.

try:
    # Creates a custom attribute group
    api_response = api_instance.product_attribute_group_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductAttributesApi->product_attribute_group_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[ProductAttributeGroupRequest]**](ProductAttributeGroupRequest.md)| Collection of product attribute groups with linked product extra data keys. | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_attribute_group_delete**
> ApiResponse product_attribute_group_delete(group_name)

Deletes a custom attribute group

Deletes the custom attribute group based on the **Group name** provided.<br />**NB:** you can only delete a custom attribute group that does not have any markeplaces (a.k.a. channels) linked to it.

### Example
```python
from __future__ import print_function
import time
import channelengine_client
from channelengine_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = channelengine_client.Configuration()
configuration.api_key['apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# create an instance of the API class
api_instance = channelengine_client.ProductAttributesApi(channelengine_client.ApiClient(configuration))
group_name = 'group_name_example' # str | The group name of the product attribute group you wish to delete.

try:
    # Deletes a custom attribute group
    api_response = api_instance.product_attribute_group_delete(group_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductAttributesApi->product_attribute_group_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | **str**| The group name of the product attribute group you wish to delete. | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_attribute_group_get_by_filter**
> CollectionOfMerchantProductAttributeGroupWithProductExtraDataResponse product_attribute_group_get_by_filter(group_names=group_names, page=page)

Gets custom attribute groups

Gets the custom attribute groups based on the **Group name** provided.

### Example
```python
from __future__ import print_function
import time
import channelengine_client
from channelengine_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = channelengine_client.Configuration()
configuration.api_key['apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# create an instance of the API class
api_instance = channelengine_client.ProductAttributesApi(channelengine_client.ApiClient(configuration))
group_names = ['group_names_example'] # list[str] |  (optional)
page = 56 # int | The page to filter on. Starts at 1. (optional)

try:
    # Gets custom attribute groups
    api_response = api_instance.product_attribute_group_get_by_filter(group_names=group_names, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductAttributesApi->product_attribute_group_get_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_names** | [**list[str]**](str.md)|  | [optional] 
 **page** | **int**| The page to filter on. Starts at 1. | [optional] 

### Return type

[**CollectionOfMerchantProductAttributeGroupWithProductExtraDataResponse**](CollectionOfMerchantProductAttributeGroupWithProductExtraDataResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_attribute_group_get_with_channels_by_filter**
> CollectionOfMerchantProductAttributeGroupWithLinkedChannelsResponse product_attribute_group_get_with_channels_by_filter(group_names=group_names, page=page)

Gets custom attribute groups and linked marketplaces

Gets all custom attribute groups and marketplaces (a.k.a. channels) linked to them.

### Example
```python
from __future__ import print_function
import time
import channelengine_client
from channelengine_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = channelengine_client.Configuration()
configuration.api_key['apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# create an instance of the API class
api_instance = channelengine_client.ProductAttributesApi(channelengine_client.ApiClient(configuration))
group_names = ['group_names_example'] # list[str] |  (optional)
page = 56 # int | The page to filter on. Starts at 1. (optional)

try:
    # Gets custom attribute groups and linked marketplaces
    api_response = api_instance.product_attribute_group_get_with_channels_by_filter(group_names=group_names, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductAttributesApi->product_attribute_group_get_with_channels_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_names** | [**list[str]**](str.md)|  | [optional] 
 **page** | **int**| The page to filter on. Starts at 1. | [optional] 

### Return type

[**CollectionOfMerchantProductAttributeGroupWithLinkedChannelsResponse**](CollectionOfMerchantProductAttributeGroupWithLinkedChannelsResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_attribute_group_remove_product_extra_data**
> ApiResponse product_attribute_group_remove_product_extra_data(group_name, body=body)

Deletes custom attributes from a group

Removes the custom attributes (a.k.a. extra data keys) from the custom attribute group.<br />**NB:** you can only remove existing custom attributes from a group.

### Example
```python
from __future__ import print_function
import time
import channelengine_client
from channelengine_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = channelengine_client.Configuration()
configuration.api_key['apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# create an instance of the API class
api_instance = channelengine_client.ProductAttributesApi(channelengine_client.ApiClient(configuration))
group_name = 'group_name_example' # str | The group name of the product attribute group you wish to remove product extra data.
body = channelengine_client.RemoveProductExtraDataRequests() # RemoveProductExtraDataRequests | Product extra data keys to be removed. (optional)

try:
    # Deletes custom attributes from a group
    api_response = api_instance.product_attribute_group_remove_product_extra_data(group_name, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductAttributesApi->product_attribute_group_remove_product_extra_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | **str**| The group name of the product attribute group you wish to remove product extra data. | 
 **body** | [**RemoveProductExtraDataRequests**](RemoveProductExtraDataRequests.md)| Product extra data keys to be removed. | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_attribute_group_rename_product_attribute_group**
> ApiResponse product_attribute_group_rename_product_attribute_group(body=body)

Renames custom attribute groups

Renames the custom attribute groups.

### Example
```python
from __future__ import print_function
import time
import channelengine_client
from channelengine_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = channelengine_client.Configuration()
configuration.api_key['apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# create an instance of the API class
api_instance = channelengine_client.ProductAttributesApi(channelengine_client.ApiClient(configuration))
body = [channelengine_client.RenameProductAttributeGroupRequests()] # list[RenameProductAttributeGroupRequests] | List of old and new product attribute group names. (optional)

try:
    # Renames custom attribute groups
    api_response = api_instance.product_attribute_group_rename_product_attribute_group(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductAttributesApi->product_attribute_group_rename_product_attribute_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[RenameProductAttributeGroupRequests]**](RenameProductAttributeGroupRequests.md)| List of old and new product attribute group names. | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

