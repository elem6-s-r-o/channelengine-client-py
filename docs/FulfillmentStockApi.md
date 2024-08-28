# channelengine_client.FulfillmentStockApi

All URIs are relative to *https://demo.channelengine.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fulfillment_stock_get_fulfillement_stock_with_stock_locations**](FulfillmentStockApi.md#fulfillment_stock_get_fulfillement_stock_with_stock_locations) | **GET** /v2/fulfillmentstock | Gets product stock across all warehouses with stock locations

# **fulfillment_stock_get_fulfillement_stock_with_stock_locations**
> CollectionOfMerchantFulfillmentStockStockLocationsResponse fulfillment_stock_get_fulfillement_stock_with_stock_locations(merchant_product_nos=merchant_product_nos, page_index=page_index, page_size=page_size)

Gets product stock across all warehouses with stock locations

Gets the stocks. The warehouses must be set up as stock locations on ChannelEngine.

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
api_instance = channelengine_client.FulfillmentStockApi(channelengine_client.ApiClient(configuration))
merchant_product_nos = ['merchant_product_nos_example'] # list[str] | List of your products' MerchantProductNo's. (optional)
page_index = 56 # int | A page index to get the items (starts from 0) (optional)
page_size = 56 # int | Number of items to return (default 100) (optional)

try:
    # Gets product stock across all warehouses with stock locations
    api_response = api_instance.fulfillment_stock_get_fulfillement_stock_with_stock_locations(merchant_product_nos=merchant_product_nos, page_index=page_index, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FulfillmentStockApi->fulfillment_stock_get_fulfillement_stock_with_stock_locations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_product_nos** | [**list[str]**](str.md)| List of your products&#x27; MerchantProductNo&#x27;s. | [optional] 
 **page_index** | **int**| A page index to get the items (starts from 0) | [optional] 
 **page_size** | **int**| Number of items to return (default 100) | [optional] 

### Return type

[**CollectionOfMerchantFulfillmentStockStockLocationsResponse**](CollectionOfMerchantFulfillmentStockStockLocationsResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

