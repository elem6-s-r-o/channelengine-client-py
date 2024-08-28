# channelengine_client.NotificationsApi

All URIs are relative to *https://demo.channelengine.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**notification_index**](NotificationsApi.md#notification_index) | **GET** /v2/notifications | Gets notifications

# **notification_index**
> CollectionOfMerchantNotificationResponse notification_index(from_date=from_date, to_date=to_date, types=types, merchant_order_nos=merchant_order_nos, channel_order_nos=channel_order_nos, merchant_return_nos=merchant_return_nos, channel_return_nos=channel_return_nos, merchant_shipment_nos=merchant_shipment_nos, page=page)

Gets notifications

Gets ChannelEngine notifications based on the available filters.

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
api_instance = channelengine_client.NotificationsApi(channelengine_client.ApiClient(configuration))
from_date = '2013-10-20T19:20:30+01:00' # datetime | Filter on the notification date, starting from this date. This date is inclusive. (optional)
to_date = '2013-10-20T19:20:30+01:00' # datetime | Filter on the notification date, until this date. This date is exclusive. (optional)
types = [channelengine_client.NotificationType()] # list[NotificationType] | Notification type(s) to filter on. (optional)
merchant_order_nos = ['merchant_order_nos_example'] # list[str] | Filter on unique order reference used by the merchant. (optional)
channel_order_nos = ['channel_order_nos_example'] # list[str] | Filter on unique order reference used by the channel. (optional)
merchant_return_nos = ['merchant_return_nos_example'] # list[str] | Filter on unique return reference used by the merchant. (optional)
channel_return_nos = ['channel_return_nos_example'] # list[str] | Filter on unique return reference used by the channel. (optional)
merchant_shipment_nos = ['merchant_shipment_nos_example'] # list[str] | Filter on unique shipment reference used by the merchant. (optional)
page = 56 # int | The page to filter on. Starts at 1. (optional)

try:
    # Gets notifications
    api_response = api_instance.notification_index(from_date=from_date, to_date=to_date, types=types, merchant_order_nos=merchant_order_nos, channel_order_nos=channel_order_nos, merchant_return_nos=merchant_return_nos, channel_return_nos=channel_return_nos, merchant_shipment_nos=merchant_shipment_nos, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationsApi->notification_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **from_date** | **datetime**| Filter on the notification date, starting from this date. This date is inclusive. | [optional] 
 **to_date** | **datetime**| Filter on the notification date, until this date. This date is exclusive. | [optional] 
 **types** | [**list[NotificationType]**](NotificationType.md)| Notification type(s) to filter on. | [optional] 
 **merchant_order_nos** | [**list[str]**](str.md)| Filter on unique order reference used by the merchant. | [optional] 
 **channel_order_nos** | [**list[str]**](str.md)| Filter on unique order reference used by the channel. | [optional] 
 **merchant_return_nos** | [**list[str]**](str.md)| Filter on unique return reference used by the merchant. | [optional] 
 **channel_return_nos** | [**list[str]**](str.md)| Filter on unique return reference used by the channel. | [optional] 
 **merchant_shipment_nos** | [**list[str]**](str.md)| Filter on unique shipment reference used by the merchant. | [optional] 
 **page** | **int**| The page to filter on. Starts at 1. | [optional] 

### Return type

[**CollectionOfMerchantNotificationResponse**](CollectionOfMerchantNotificationResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

