# channelengine_client.CompetitionPricesApi

All URIs are relative to *https://demo.channelengine.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**competition_prices_get_buy_box_prices**](CompetitionPricesApi.md#competition_prices_get_buy_box_prices) | **GET** /v2/competitionprices/buyboxprices | Gets the price from the buy box winner

# **competition_prices_get_buy_box_prices**
> CollectionOfMerchantProductWithBuyBoxPrice competition_prices_get_buy_box_prices(channel_id=channel_id, gtin_list=gtin_list, sku_list=sku_list, page=page)

Gets the price from the buy box winner

Gets the current price of the buy box winner per product for a marketplace.

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
api_instance = channelengine_client.CompetitionPricesApi(channelengine_client.ApiClient(configuration))
channel_id = 56 # int | The id of the channel (optional)
gtin_list = ['gtin_list_example'] # list[str] | Search products by submitting a list of GTIN's. (optional)<br />Max. 2000. (optional)
sku_list = ['sku_list_example'] # list[str] | Search products by submitting a list of Sku's. (optional)<br />Max. 2000. If GtinList is already set, this one is ignored. (optional)
page = 56 # int | The page to filter on. Starts at 1. (optional)

try:
    # Gets the price from the buy box winner
    api_response = api_instance.competition_prices_get_buy_box_prices(channel_id=channel_id, gtin_list=gtin_list, sku_list=sku_list, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompetitionPricesApi->competition_prices_get_buy_box_prices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **int**| The id of the channel | [optional] 
 **gtin_list** | [**list[str]**](str.md)| Search products by submitting a list of GTIN&#x27;s. (optional)&lt;br /&gt;Max. 2000. | [optional] 
 **sku_list** | [**list[str]**](str.md)| Search products by submitting a list of Sku&#x27;s. (optional)&lt;br /&gt;Max. 2000. If GtinList is already set, this one is ignored. | [optional] 
 **page** | **int**| The page to filter on. Starts at 1. | [optional] 

### Return type

[**CollectionOfMerchantProductWithBuyBoxPrice**](CollectionOfMerchantProductWithBuyBoxPrice.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

