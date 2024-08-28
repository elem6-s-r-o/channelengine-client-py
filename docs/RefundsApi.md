# channelengine_client.RefundsApi

All URIs are relative to *https://demo.channelengine.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**refund_acknowledge**](RefundsApi.md#refund_acknowledge) | **POST** /v2.1/refunds/merchant/acknowledge | [CLOSED BETA] Acknowledge a refund
[**refund_create**](RefundsApi.md#refund_create) | **POST** /v2.1/refunds/merchant | [CLOSED BETA] Create a refund
[**refund_get**](RefundsApi.md#refund_get) | **GET** /v2.1/refunds/merchant/{identifier} | [CLOSED BETA] Get refund by identifier
[**refund_get_by_filter**](RefundsApi.md#refund_get_by_filter) | **GET** /v2.1/refunds/merchant | [CLOSED BETA] Get refunds by filter

# **refund_acknowledge**
> ApiResponse refund_acknowledge(body=body)

[CLOSED BETA] Acknowledge a refund

Acknowledges a refund<br /> <br />Beware, this endpoint is part of a closed beta and is only available for closed beta participants.

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
api_instance = channelengine_client.RefundsApi(channelengine_client.ApiClient(configuration))
body = channelengine_client.SingleMerchantAcknowledgeRefundRequest() # SingleMerchantAcknowledgeRefundRequest | The refund to acknowledge (optional)

try:
    # [CLOSED BETA] Acknowledge a refund
    api_response = api_instance.refund_acknowledge(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RefundsApi->refund_acknowledge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SingleMerchantAcknowledgeRefundRequest**](SingleMerchantAcknowledgeRefundRequest.md)| The refund to acknowledge | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refund_create**
> ApiResponse refund_create(body=body)

[CLOSED BETA] Create a refund

Creates a new refund<br /> <br />Beware, this endpoint is part of a closed beta and is only available for closed beta participants.

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
api_instance = channelengine_client.RefundsApi(channelengine_client.ApiClient(configuration))
body = channelengine_client.SingleMerchantCreateRefundRequest() # SingleMerchantCreateRefundRequest | The refund (optional)

try:
    # [CLOSED BETA] Create a refund
    api_response = api_instance.refund_create(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RefundsApi->refund_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SingleMerchantCreateRefundRequest**](SingleMerchantCreateRefundRequest.md)| The refund | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refund_get**
> SingleOfIRefund refund_get(identifier, type=type)

[CLOSED BETA] Get refund by identifier

Gets a single refund by the given identifier<br /> <br />Beware, this endpoint is part of a closed beta and is only available for closed beta participants.

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
api_instance = channelengine_client.RefundsApi(channelengine_client.ApiClient(configuration))
identifier = 'identifier_example' # str | The identifier to search for
type = channelengine_client.RefundIdentifier() # RefundIdentifier | Specify whether to search by ID, Merchant Refund No or Channel Refund No (optional)

try:
    # [CLOSED BETA] Get refund by identifier
    api_response = api_instance.refund_get(identifier, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RefundsApi->refund_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| The identifier to search for | 
 **type** | [**RefundIdentifier**](.md)| Specify whether to search by ID, Merchant Refund No or Channel Refund No | [optional] 

### Return type

[**SingleOfIRefund**](SingleOfIRefund.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refund_get_by_filter**
> SingleOfIRefund refund_get_by_filter(identifiers_identifier_type=identifiers_identifier_type, identifiers_models=identifiers_models, channel_export_status_statuses=channel_export_status_statuses, channel_export_status_max_number_of_export_attempts=channel_export_status_max_number_of_export_attempts, reasons=reasons, created_date_range_from_date=created_date_range_from_date, created_date_range_to_date=created_date_range_to_date, channel_ids=channel_ids, search=search, is_acknowledged_by_merchant=is_acknowledged_by_merchant, is_acknowledged_by_channel=is_acknowledged_by_channel, fulfillment_type=fulfillment_type, creator_type=creator_type, external_batch_nos=external_batch_nos, page_index=page_index, page_size=page_size)

[CLOSED BETA] Get refunds by filter

Gets multiple refunds by the given filter<br /> <br />Beware, this endpoint is part of a closed beta and is only available for closed beta participants.

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
api_instance = channelengine_client.RefundsApi(channelengine_client.ApiClient(configuration))
identifiers_identifier_type = channelengine_client.RefundByFilterIdentifier() # RefundByFilterIdentifier | The type of identifier: which identifier to filter on (optional)
identifiers_models = ['identifiers_models_example'] # list[str] | The value (of the selected type) to filter on (optional)
channel_export_status_statuses = [channelengine_client.ChannelExportStatus()] # list[ChannelExportStatus] |  (optional)
channel_export_status_max_number_of_export_attempts = 56 # int |  (optional)
reasons = [channelengine_client.RefundReason()] # list[RefundReason] |  (optional)
created_date_range_from_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
created_date_range_to_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
channel_ids = [56] # list[int] |  (optional)
search = 'search_example' # str |  (optional)
is_acknowledged_by_merchant = true # bool |  (optional)
is_acknowledged_by_channel = true # bool |  (optional)
fulfillment_type = channelengine_client.ModuleFulfillmentType() # ModuleFulfillmentType |  (optional)
creator_type = channelengine_client.CreatorType() # CreatorType |  (optional)
external_batch_nos = ['external_batch_nos_example'] # list[str] |  (optional)
page_index = 56 # int |  (optional)
page_size = 56 # int |  (optional)

try:
    # [CLOSED BETA] Get refunds by filter
    api_response = api_instance.refund_get_by_filter(identifiers_identifier_type=identifiers_identifier_type, identifiers_models=identifiers_models, channel_export_status_statuses=channel_export_status_statuses, channel_export_status_max_number_of_export_attempts=channel_export_status_max_number_of_export_attempts, reasons=reasons, created_date_range_from_date=created_date_range_from_date, created_date_range_to_date=created_date_range_to_date, channel_ids=channel_ids, search=search, is_acknowledged_by_merchant=is_acknowledged_by_merchant, is_acknowledged_by_channel=is_acknowledged_by_channel, fulfillment_type=fulfillment_type, creator_type=creator_type, external_batch_nos=external_batch_nos, page_index=page_index, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RefundsApi->refund_get_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifiers_identifier_type** | [**RefundByFilterIdentifier**](.md)| The type of identifier: which identifier to filter on | [optional] 
 **identifiers_models** | [**list[str]**](str.md)| The value (of the selected type) to filter on | [optional] 
 **channel_export_status_statuses** | [**list[ChannelExportStatus]**](ChannelExportStatus.md)|  | [optional] 
 **channel_export_status_max_number_of_export_attempts** | **int**|  | [optional] 
 **reasons** | [**list[RefundReason]**](RefundReason.md)|  | [optional] 
 **created_date_range_from_date** | **datetime**|  | [optional] 
 **created_date_range_to_date** | **datetime**|  | [optional] 
 **channel_ids** | [**list[int]**](int.md)|  | [optional] 
 **search** | **str**|  | [optional] 
 **is_acknowledged_by_merchant** | **bool**|  | [optional] 
 **is_acknowledged_by_channel** | **bool**|  | [optional] 
 **fulfillment_type** | [**ModuleFulfillmentType**](.md)|  | [optional] 
 **creator_type** | [**CreatorType**](.md)|  | [optional] 
 **external_batch_nos** | [**list[str]**](str.md)|  | [optional] 
 **page_index** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 

### Return type

[**SingleOfIRefund**](SingleOfIRefund.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

