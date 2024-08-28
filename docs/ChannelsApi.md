# channelengine_client.ChannelsApi

All URIs are relative to *https://demo.channelengine.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**channel_plugins_get**](ChannelsApi.md#channel_plugins_get) | **GET** /v2/channels | Gets channels

# **channel_plugins_get**
> CollectionOfChannelGlobalChannelResponse channel_plugins_get()

Gets channels

Gets the complete list of channels available on ChannelEngine including their **Global channel ID**.

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
api_instance = channelengine_client.ChannelsApi(channelengine_client.ApiClient(configuration))

try:
    # Gets channels
    api_response = api_instance.channel_plugins_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChannelsApi->channel_plugins_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CollectionOfChannelGlobalChannelResponse**](CollectionOfChannelGlobalChannelResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

