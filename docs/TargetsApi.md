# channelengine_client.TargetsApi

All URIs are relative to *https://demo.channelengine.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**targets_create_targets**](TargetsApi.md#targets_create_targets) | **POST** /v2/targets | Creates multiple targets
[**targets_delete_targets**](TargetsApi.md#targets_delete_targets) | **DELETE** /v2/targets | Deletes multiple targets
[**targets_edit_targets**](TargetsApi.md#targets_edit_targets) | **PUT** /v2/targets | Edits multiple targets

# **targets_create_targets**
> SingleOfListOfTargetResponseVm targets_create_targets(body=body)

Creates multiple targets

Creates multiple targets on ChannelEngine.

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
api_instance = channelengine_client.TargetsApi(channelengine_client.ApiClient(configuration))
body = [channelengine_client.CreateEditTargetRequest()] # list[CreateEditTargetRequest] |  (optional)

try:
    # Creates multiple targets
    api_response = api_instance.targets_create_targets(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TargetsApi->targets_create_targets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[CreateEditTargetRequest]**](CreateEditTargetRequest.md)|  | [optional] 

### Return type

[**SingleOfListOfTargetResponseVm**](SingleOfListOfTargetResponseVm.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **targets_delete_targets**
> SingleOfDeleteTargetsResponse targets_delete_targets(body=body)

Deletes multiple targets

Deletes multiple targets on ChannelEngine.

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
api_instance = channelengine_client.TargetsApi(channelengine_client.ApiClient(configuration))
body = [channelengine_client.DeleteTargetRequest()] # list[DeleteTargetRequest] |  (optional)

try:
    # Deletes multiple targets
    api_response = api_instance.targets_delete_targets(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TargetsApi->targets_delete_targets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[DeleteTargetRequest]**](DeleteTargetRequest.md)|  | [optional] 

### Return type

[**SingleOfDeleteTargetsResponse**](SingleOfDeleteTargetsResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **targets_edit_targets**
> SingleOfListOfTargetResponseVm targets_edit_targets(body=body)

Edits multiple targets

Edits multiple targets on ChannelEngine.

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
api_instance = channelengine_client.TargetsApi(channelengine_client.ApiClient(configuration))
body = [channelengine_client.CreateEditTargetRequest()] # list[CreateEditTargetRequest] |  (optional)

try:
    # Edits multiple targets
    api_response = api_instance.targets_edit_targets(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TargetsApi->targets_edit_targets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[CreateEditTargetRequest]**](CreateEditTargetRequest.md)|  | [optional] 

### Return type

[**SingleOfListOfTargetResponseVm**](SingleOfListOfTargetResponseVm.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

