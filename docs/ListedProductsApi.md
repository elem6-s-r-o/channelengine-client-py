# channelengine_client.ListedProductsApi

All URIs are relative to *https://demo.channelengine.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**listed_product_get_by_filter**](ListedProductsApi.md#listed_product_get_by_filter) | **GET** /v2/channels/{channelId}/products | Gets products listed by channel

# **listed_product_get_by_filter**
> CollectionOfChannelListedProductResponse listed_product_get_by_filter(channel_id, merchant_product_nos=merchant_product_nos, page=page)

Gets products listed by channel

Gets the products listed per channel based on the **Channel ID**.<br /> <br />**NB:** not all marketplaces provide adequate options to retrieve the status of a product as seen on the marketplace.

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
api_instance = channelengine_client.ListedProductsApi(channelengine_client.ApiClient(configuration))
channel_id = 56 # int | The id of a channel
merchant_product_nos = ['merchant_product_nos_example'] # list[str] | The unique product references used by the Merchant (SKUs) (optional)
page = 56 # int | The page to filter on. Starts at 1. (optional)

try:
    # Gets products listed by channel
    api_response = api_instance.listed_product_get_by_filter(channel_id, merchant_product_nos=merchant_product_nos, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ListedProductsApi->listed_product_get_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **int**| The id of a channel | 
 **merchant_product_nos** | [**list[str]**](str.md)| The unique product references used by the Merchant (SKUs) | [optional] 
 **page** | **int**| The page to filter on. Starts at 1. | [optional] 

### Return type

[**CollectionOfChannelListedProductResponse**](CollectionOfChannelListedProductResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

