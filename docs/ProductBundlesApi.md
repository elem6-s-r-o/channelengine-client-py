# channelengine_client.ProductBundlesApi

All URIs are relative to *https://demo.channelengine.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**product_bundle_get_by_filter**](ProductBundlesApi.md#product_bundle_get_by_filter) | **GET** /v2/productbundles | Gets product bundles

# **product_bundle_get_by_filter**
> CollectionOfMerchantProductBundleResponse product_bundle_get_by_filter(search=search, ean_list=ean_list, merchant_product_no_list=merchant_product_no_list, page=page)

Gets product bundles

Gets the product bundle details.

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
api_instance = channelengine_client.ProductBundlesApi(channelengine_client.ApiClient(configuration))
search = 'search_example' # str | Search product(s) by Name, MerchantProductNo, Ean or Brand<br />This search is applied to the result after applying the other filters. (optional)
ean_list = ['ean_list_example'] # list[str] | Search products by submitting a list of EAN's. (optional)
merchant_product_no_list = ['merchant_product_no_list_example'] # list[str] | Search products by submitting a list of MerchantProductNo's. (optional)
page = 56 # int | The page to filter on. Starts at 1. (optional)

try:
    # Gets product bundles
    api_response = api_instance.product_bundle_get_by_filter(search=search, ean_list=ean_list, merchant_product_no_list=merchant_product_no_list, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductBundlesApi->product_bundle_get_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Search product(s) by Name, MerchantProductNo, Ean or Brand&lt;br /&gt;This search is applied to the result after applying the other filters. | [optional] 
 **ean_list** | [**list[str]**](str.md)| Search products by submitting a list of EAN&#x27;s. | [optional] 
 **merchant_product_no_list** | [**list[str]**](str.md)| Search products by submitting a list of MerchantProductNo&#x27;s. | [optional] 
 **page** | **int**| The page to filter on. Starts at 1. | [optional] 

### Return type

[**CollectionOfMerchantProductBundleResponse**](CollectionOfMerchantProductBundleResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

