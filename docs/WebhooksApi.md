# channelengine_client.WebhooksApi

All URIs are relative to *https://demo.channelengine.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**webhooks_create**](WebhooksApi.md#webhooks_create) | **POST** /v2/webhooks | Creates a webhook
[**webhooks_delete**](WebhooksApi.md#webhooks_delete) | **DELETE** /v2/webhooks/{webhookName} | Deletes a webhook
[**webhooks_get_all**](WebhooksApi.md#webhooks_get_all) | **GET** /v2/webhooks | Gets webhooks
[**webhooks_update**](WebhooksApi.md#webhooks_update) | **PUT** /v2/webhooks | Updates a webhook

# **webhooks_create**
> ApiResponse webhooks_create(body=body)

Creates a webhook

Creates a webhook on ChannelEngine.

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
api_instance = channelengine_client.WebhooksApi(channelengine_client.ApiClient(configuration))
body = channelengine_client.MerchantWebhookRequest() # MerchantWebhookRequest |  (optional)

try:
    # Creates a webhook
    api_response = api_instance.webhooks_create(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->webhooks_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MerchantWebhookRequest**](MerchantWebhookRequest.md)|  | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhooks_delete**
> ApiResponse webhooks_delete(webhook_name)

Deletes a webhook

Deletes a webhook from ChannelEngine.

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
api_instance = channelengine_client.WebhooksApi(channelengine_client.ApiClient(configuration))
webhook_name = 'webhook_name_example' # str | The unique name of a webhook you want to delete.

try:
    # Deletes a webhook
    api_response = api_instance.webhooks_delete(webhook_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->webhooks_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_name** | **str**| The unique name of a webhook you want to delete. | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhooks_get_all**
> CollectionOfMerchantWebhookResponse webhooks_get_all()

Gets webhooks

Gets all webhooks created on ChannelEngine.

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
api_instance = channelengine_client.WebhooksApi(channelengine_client.ApiClient(configuration))

try:
    # Gets webhooks
    api_response = api_instance.webhooks_get_all()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->webhooks_get_all: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CollectionOfMerchantWebhookResponse**](CollectionOfMerchantWebhookResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhooks_update**
> ApiResponse webhooks_update(body=body)

Updates a webhook

Updates a webhook on ChannelEngine.

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
api_instance = channelengine_client.WebhooksApi(channelengine_client.ApiClient(configuration))
body = channelengine_client.MerchantWebhookRequest() # MerchantWebhookRequest |  (optional)

try:
    # Updates a webhook
    api_response = api_instance.webhooks_update(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->webhooks_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MerchantWebhookRequest**](MerchantWebhookRequest.md)|  | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

