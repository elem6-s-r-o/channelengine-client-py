# channelengine_client.OffersApi

All URIs are relative to *https://demo.channelengine.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**offer_get_stock**](OffersApi.md#offer_get_stock) | **GET** /v2/offer/stock | Gets product stock across all warehouses
[**offer_stock_price_update**](OffersApi.md#offer_stock_price_update) | **PUT** /v2/offer | Updates stock and price
[**offer_stock_update**](OffersApi.md#offer_stock_update) | **PUT** /v2/offer/stock | Updates stock

# **offer_get_stock**
> CollectionOfMerchantOfferGetStockResponse offer_get_stock(stock_location_ids, skus=skus, page_index=page_index, page_size=page_size)

Gets product stock across all warehouses

Gets the stock available in the warehouses. The warehouses must be set up as stock locations on ChannelEngine.

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
api_instance = channelengine_client.OffersApi(channelengine_client.ApiClient(configuration))
stock_location_ids = [56] # list[int] | The ChannelEngine id of the stock location(s).
skus = ['skus_example'] # list[str] | List of your products' sku's. (optional)
page_index = 56 # int | A page index to get the items (starts from 0) (optional)
page_size = 56 # int | Number of items to return (default 100) (optional)

try:
    # Gets product stock across all warehouses
    api_response = api_instance.offer_get_stock(stock_location_ids, skus=skus, page_index=page_index, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OffersApi->offer_get_stock: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stock_location_ids** | [**list[int]**](int.md)| The ChannelEngine id of the stock location(s). | 
 **skus** | [**list[str]**](str.md)| List of your products&#x27; sku&#x27;s. | [optional] 
 **page_index** | **int**| A page index to get the items (starts from 0) | [optional] 
 **page_size** | **int**| Number of items to return (default 100) | [optional] 

### Return type

[**CollectionOfMerchantOfferGetStockResponse**](CollectionOfMerchantOfferGetStockResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **offer_stock_price_update**
> SingleOfDictionaryOfStringAndListOfString offer_stock_price_update(body)

Updates stock and price

Updates product stock and price.

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
api_instance = channelengine_client.OffersApi(channelengine_client.ApiClient(configuration))
body = [channelengine_client.MerchantStockPriceUpdateRequest()] # list[MerchantStockPriceUpdateRequest] | References to the products that should be updated, and the new values<br />for the stock or price fields. It is possible to supply only one of the two fields<br />or both.

try:
    # Updates stock and price
    api_response = api_instance.offer_stock_price_update(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OffersApi->offer_stock_price_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[MerchantStockPriceUpdateRequest]**](MerchantStockPriceUpdateRequest.md)| References to the products that should be updated, and the new values&lt;br /&gt;for the stock or price fields. It is possible to supply only one of the two fields&lt;br /&gt;or both. | 

### Return type

[**SingleOfDictionaryOfStringAndListOfString**](SingleOfDictionaryOfStringAndListOfString.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **offer_stock_update**
> SingleOfDictionaryOfStringAndListOfString offer_stock_update(body)

Updates stock

Updates product stock.

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
api_instance = channelengine_client.OffersApi(channelengine_client.ApiClient(configuration))
body = [channelengine_client.MerchantOfferStockUpdateRequest()] # list[MerchantOfferStockUpdateRequest] | References to the new values for the stock fields.

try:
    # Updates stock
    api_response = api_instance.offer_stock_update(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OffersApi->offer_stock_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[MerchantOfferStockUpdateRequest]**](MerchantOfferStockUpdateRequest.md)| References to the new values for the stock fields. | 

### Return type

[**SingleOfDictionaryOfStringAndListOfString**](SingleOfDictionaryOfStringAndListOfString.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

