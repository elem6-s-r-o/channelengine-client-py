# channelengine_client.CancellationsApi

All URIs are relative to *https://demo.channelengine.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancellation_create**](CancellationsApi.md#cancellation_create) | **POST** /v2/cancellations | Creates a cancelation
[**cancellation_get_for_merchant**](CancellationsApi.md#cancellation_get_for_merchant) | **GET** /v2/cancellations/merchant | Gets cancelations

# **cancellation_create**
> ApiResponse cancellation_create(body=body)

Creates a cancelation

Marks an order as fully or partially canceled based on order line and quantity input.

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
api_instance = channelengine_client.CancellationsApi(channelengine_client.ApiClient(configuration))
body = channelengine_client.MerchantCancellationRequest() # MerchantCancellationRequest |  (optional)

try:
    # Creates a cancelation
    api_response = api_instance.cancellation_create(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CancellationsApi->cancellation_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MerchantCancellationRequest**](MerchantCancellationRequest.md)|  | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancellation_get_for_merchant**
> CollectionOfMerchantCancellationResponse cancellation_get_for_merchant(created_since=created_since, page=page)

Gets cancelations

Gets cancelations based on their creation date.

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
api_instance = channelengine_client.CancellationsApi(channelengine_client.ApiClient(configuration))
created_since = '2013-10-20T19:20:30+01:00' # datetime | Filter on the create date of the cancellation in ChannelEngine, starting from this date. This date is inclusive. (optional)
page = 56 # int | The page to filter on. Starts at 1. (optional)

try:
    # Gets cancelations
    api_response = api_instance.cancellation_get_for_merchant(created_since=created_since, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CancellationsApi->cancellation_get_for_merchant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **created_since** | **datetime**| Filter on the create date of the cancellation in ChannelEngine, starting from this date. This date is inclusive. | [optional] 
 **page** | **int**| The page to filter on. Starts at 1. | [optional] 

### Return type

[**CollectionOfMerchantCancellationResponse**](CollectionOfMerchantCancellationResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

