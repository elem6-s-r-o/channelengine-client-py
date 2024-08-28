# channelengine_client.CustomFieldsApi

All URIs are relative to *https://demo.channelengine.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**custom_fields_get_custom_fields**](CustomFieldsApi.md#custom_fields_get_custom_fields) | **GET** /v2/custom-fields | Gets custom fields

# **custom_fields_get_custom_fields**
> CollectionOfCustomFieldResponse custom_fields_get_custom_fields(page_index=page_index, page_size=page_size)

Gets custom fields

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
api_instance = channelengine_client.CustomFieldsApi(channelengine_client.ApiClient(configuration))
page_index = 56 # int | A page index to get the items (starts from 0) (optional)
page_size = 56 # int | Number of items to return (default 100) (optional)

try:
    # Gets custom fields
    api_response = api_instance.custom_fields_get_custom_fields(page_index=page_index, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomFieldsApi->custom_fields_get_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_index** | **int**| A page index to get the items (starts from 0) | [optional] 
 **page_size** | **int**| Number of items to return (default 100) | [optional] 

### Return type

[**CollectionOfCustomFieldResponse**](CollectionOfCustomFieldResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

