# channelengine_client.StockLocationsApi

All URIs are relative to *https://demo.channelengine.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**stock_location_create**](StockLocationsApi.md#stock_location_create) | **POST** /v2/stocklocations | Creates a stock location
[**stock_location_index**](StockLocationsApi.md#stock_location_index) | **GET** /v2/stocklocations | Gets stock locations

# **stock_location_create**
> ApiResponse stock_location_create(body=body)

Creates a stock location

Creates a stock location on ChannelEngine.

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
api_instance = channelengine_client.StockLocationsApi(channelengine_client.ApiClient(configuration))
body = channelengine_client.MerchantStockLocationCreateRequest() # MerchantStockLocationCreateRequest |  (optional)

try:
    # Creates a stock location
    api_response = api_instance.stock_location_create(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StockLocationsApi->stock_location_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MerchantStockLocationCreateRequest**](MerchantStockLocationCreateRequest.md)|  | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stock_location_index**
> CollectionOfMerchantStockLocationWithCountryIsoResponse stock_location_index()

Gets stock locations

Gets the different stock locations in use. <br />**NB:** the response may include stock locations for 'marketplace fulfilment' solutions (e.g.: FBA, LVB, ZFS, etc.).<br />Use the retrieved IDs to get the stock of products in specific stock locations, such as the FBA stock.

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
api_instance = channelengine_client.StockLocationsApi(channelengine_client.ApiClient(configuration))

try:
    # Gets stock locations
    api_response = api_instance.stock_location_index()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StockLocationsApi->stock_location_index: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CollectionOfMerchantStockLocationWithCountryIsoResponse**](CollectionOfMerchantStockLocationWithCountryIsoResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

