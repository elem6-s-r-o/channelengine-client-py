# channelengine_client.ReturnsApi

All URIs are relative to *https://demo.channelengine.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**return_acknowledge**](ReturnsApi.md#return_acknowledge) | **POST** /v2.1/returns/merchant/acknowledge | [CLOSED BETA] Acknowledge a return
[**return_acknowledge_0**](ReturnsApi.md#return_acknowledge_0) | **POST** /v2/returns/merchant/acknowledge | Acknowledges a return
[**return_create**](ReturnsApi.md#return_create) | **POST** /v2.1/returns/merchant | [CLOSED BETA] Create a return
[**return_declare_for_merchant**](ReturnsApi.md#return_declare_for_merchant) | **POST** /v2/returns/merchant | Creates merchant return
[**return_get**](ReturnsApi.md#return_get) | **GET** /v2.1/returns/merchant/{identifier} | [CLOSED BETA] Get return by identifier
[**return_get_by_filter**](ReturnsApi.md#return_get_by_filter) | **GET** /v2.1/returns/merchant | [CLOSED BETA] Get returns by filter
[**return_get_by_merchant_order_no**](ReturnsApi.md#return_get_by_merchant_order_no) | **GET** /v2/returns/merchant/{merchantOrderNo} | Gets a return
[**return_get_declared_by_channel**](ReturnsApi.md#return_get_declared_by_channel) | **GET** /v2/returns/merchant | Gets marketplace returns
[**return_get_returns**](ReturnsApi.md#return_get_returns) | **GET** /v2/returns | Gets returns by filter
[**return_get_unhandled**](ReturnsApi.md#return_get_unhandled) | **GET** /v2/returns/merchant/new | Gets unhandled returns
[**return_handle**](ReturnsApi.md#return_handle) | **POST** /v2.1/returns/merchant/handle | [CLOSED BETA] Handle a return
[**return_update_for_merchant**](ReturnsApi.md#return_update_for_merchant) | **PUT** /v2/returns | Marks returns as received

# **return_acknowledge**
> ApiResponse return_acknowledge(body=body)

[CLOSED BETA] Acknowledge a return

Acknowledges a return<br /> <br />Beware, this endpoint is part of a closed beta and is only available for closed beta participants.

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
api_instance = channelengine_client.ReturnsApi(channelengine_client.ApiClient(configuration))
body = channelengine_client.SingleMerchantAcknowledgeReturnRequest() # SingleMerchantAcknowledgeReturnRequest | The return to acknowledge (optional)

try:
    # [CLOSED BETA] Acknowledge a return
    api_response = api_instance.return_acknowledge(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReturnsApi->return_acknowledge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SingleMerchantAcknowledgeReturnRequest**](SingleMerchantAcknowledgeReturnRequest.md)| The return to acknowledge | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **return_acknowledge_0**
> ApiResponse return_acknowledge_0(body=body)

Acknowledges a return

Acknowledges a return based on the **Return ID** provided.<br /><br />**NB:** by acknowledging a return, you signal that it was registered in your system.<br />You can later filter your returns on the **Is acknowledged** parameter.

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
api_instance = channelengine_client.ReturnsApi(channelengine_client.ApiClient(configuration))
body = channelengine_client.MerchantReturnAcknowledgeRequest() # MerchantReturnAcknowledgeRequest |  (optional)

try:
    # Acknowledges a return
    api_response = api_instance.return_acknowledge_0(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReturnsApi->return_acknowledge_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MerchantReturnAcknowledgeRequest**](MerchantReturnAcknowledgeRequest.md)|  | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **return_create**
> ApiResponse return_create(body=body)

[CLOSED BETA] Create a return

Creates a new return<br /> <br />Beware, this endpoint is part of a closed beta and is only available for closed beta participants.

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
api_instance = channelengine_client.ReturnsApi(channelengine_client.ApiClient(configuration))
body = channelengine_client.SingleMerchantCreateReturnRequest() # SingleMerchantCreateReturnRequest | The return (optional)

try:
    # [CLOSED BETA] Create a return
    api_response = api_instance.return_create(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReturnsApi->return_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SingleMerchantCreateReturnRequest**](SingleMerchantCreateReturnRequest.md)| The return | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **return_declare_for_merchant**
> ApiResponse return_declare_for_merchant(body=body)

Creates merchant return

Marks an order as either fully or partially returned.<br /><br />**NB:** this endpoint is used for merchant returns (i.e.: returns dealt with by the merchant).

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
api_instance = channelengine_client.ReturnsApi(channelengine_client.ApiClient(configuration))
body = channelengine_client.MerchantReturnRequest() # MerchantReturnRequest |  (optional)

try:
    # Creates merchant return
    api_response = api_instance.return_declare_for_merchant(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReturnsApi->return_declare_for_merchant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MerchantReturnRequest**](MerchantReturnRequest.md)|  | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **return_get**
> SingleOfIReturn return_get(identifier, type=type)

[CLOSED BETA] Get return by identifier

Gets a single return by the given identifier<br /> <br />Beware, this endpoint is part of a closed beta and is only available for closed beta participants.

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
api_instance = channelengine_client.ReturnsApi(channelengine_client.ApiClient(configuration))
identifier = 'identifier_example' # str | The identifier to search for
type = channelengine_client.ReturnIdentifier() # ReturnIdentifier | Specify whether to search by ID, Merchant Return No or Channel Return No (optional)

try:
    # [CLOSED BETA] Get return by identifier
    api_response = api_instance.return_get(identifier, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReturnsApi->return_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| The identifier to search for | 
 **type** | [**ReturnIdentifier**](.md)| Specify whether to search by ID, Merchant Return No or Channel Return No | [optional] 

### Return type

[**SingleOfIReturn**](SingleOfIReturn.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **return_get_by_filter**
> SingleOfIReturn return_get_by_filter(identifiers_identifier_type=identifiers_identifier_type, identifiers_models=identifiers_models, channel_export_status_statuses=channel_export_status_statuses, channel_export_status_max_number_of_export_attempts=channel_export_status_max_number_of_export_attempts, reasons=reasons, created_date_range_from_date=created_date_range_from_date, created_date_range_to_date=created_date_range_to_date, statuses=statuses, channel_ids=channel_ids, search=search, is_acknowledged_by_merchant=is_acknowledged_by_merchant, is_acknowledged_by_channel=is_acknowledged_by_channel, fulfillment_type=fulfillment_type, creator_type=creator_type, external_batch_nos=external_batch_nos, page_index=page_index, page_size=page_size)

[CLOSED BETA] Get returns by filter

Gets multiple returns by the given filter<br /> <br />Beware, this endpoint is part of a closed beta and is only available for closed beta participants.

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
api_instance = channelengine_client.ReturnsApi(channelengine_client.ApiClient(configuration))
identifiers_identifier_type = channelengine_client.ReturnByFilterIdentifier() # ReturnByFilterIdentifier | The type of identifier: which identifier to filter on (optional)
identifiers_models = ['identifiers_models_example'] # list[str] | The value (of the selected type) to filter on (optional)
channel_export_status_statuses = [channelengine_client.ChannelExportStatus()] # list[ChannelExportStatus] |  (optional)
channel_export_status_max_number_of_export_attempts = 56 # int |  (optional)
reasons = [channelengine_client.ModuleReturnReason()] # list[ModuleReturnReason] |  (optional)
created_date_range_from_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
created_date_range_to_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
statuses = [channelengine_client.ModuleReturnStatus()] # list[ModuleReturnStatus] |  (optional)
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
    # [CLOSED BETA] Get returns by filter
    api_response = api_instance.return_get_by_filter(identifiers_identifier_type=identifiers_identifier_type, identifiers_models=identifiers_models, channel_export_status_statuses=channel_export_status_statuses, channel_export_status_max_number_of_export_attempts=channel_export_status_max_number_of_export_attempts, reasons=reasons, created_date_range_from_date=created_date_range_from_date, created_date_range_to_date=created_date_range_to_date, statuses=statuses, channel_ids=channel_ids, search=search, is_acknowledged_by_merchant=is_acknowledged_by_merchant, is_acknowledged_by_channel=is_acknowledged_by_channel, fulfillment_type=fulfillment_type, creator_type=creator_type, external_batch_nos=external_batch_nos, page_index=page_index, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReturnsApi->return_get_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifiers_identifier_type** | [**ReturnByFilterIdentifier**](.md)| The type of identifier: which identifier to filter on | [optional] 
 **identifiers_models** | [**list[str]**](str.md)| The value (of the selected type) to filter on | [optional] 
 **channel_export_status_statuses** | [**list[ChannelExportStatus]**](ChannelExportStatus.md)|  | [optional] 
 **channel_export_status_max_number_of_export_attempts** | **int**|  | [optional] 
 **reasons** | [**list[ModuleReturnReason]**](ModuleReturnReason.md)|  | [optional] 
 **created_date_range_from_date** | **datetime**|  | [optional] 
 **created_date_range_to_date** | **datetime**|  | [optional] 
 **statuses** | [**list[ModuleReturnStatus]**](ModuleReturnStatus.md)|  | [optional] 
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

[**SingleOfIReturn**](SingleOfIReturn.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **return_get_by_merchant_order_no**
> CollectionOfMerchantSingleOrderReturnResponse return_get_by_merchant_order_no(merchant_order_no)

Gets a return

Gets the returns based on the **Merchant order number** provided.<br /><br />**NB:** this endpoint is meant for merchants. Marketplaces should use the **GET /v2/returns/channel** call instead.

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
api_instance = channelengine_client.ReturnsApi(channelengine_client.ApiClient(configuration))
merchant_order_no = 'merchant_order_no_example' # str | 

try:
    # Gets a return
    api_response = api_instance.return_get_by_merchant_order_no(merchant_order_no)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReturnsApi->return_get_by_merchant_order_no: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_order_no** | **str**|  | 

### Return type

[**CollectionOfMerchantSingleOrderReturnResponse**](CollectionOfMerchantSingleOrderReturnResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **return_get_declared_by_channel**
> CollectionOfMerchantReturnResponse return_get_declared_by_channel(channel_ids=channel_ids, merchant_order_nos=merchant_order_nos, channel_order_nos=channel_order_nos, fulfillment_type=fulfillment_type, statuses=statuses, reasons=reasons, from_date=from_date, to_date=to_date, is_acknowledged=is_acknowledged, page=page)

Gets marketplace returns

Gets all returns created by the marketplace.<br /><br />**NB:** this endpoint is used for both marketplace and marketplace-fulfilled returns.

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
api_instance = channelengine_client.ReturnsApi(channelengine_client.ApiClient(configuration))
channel_ids = [56] # list[int] | Filter on Channel IDs (optional)
merchant_order_nos = ['merchant_order_nos_example'] # list[str] | Filter on unique order reference used by the merchant. (optional)
channel_order_nos = ['channel_order_nos_example'] # list[str] | Filter on unique order reference used by the channel. (optional)
fulfillment_type = channelengine_client.FulfillmentType() # FulfillmentType | Filter on the fulfillment type of the order. (optional)
statuses = [channelengine_client.ReturnStatus()] # list[ReturnStatus] | Return status(es) to filter on. (optional)
reasons = [channelengine_client.ReturnReason()] # list[ReturnReason] | Return reason(s) to filter on. (optional)
from_date = '2013-10-20T19:20:30+01:00' # datetime | Filter on the creation date, starting from this date. This date is inclusive. (optional)
to_date = '2013-10-20T19:20:30+01:00' # datetime | Filter on the creation date, until this date. This date is exclusive. (optional)
is_acknowledged = true # bool | Filters based on acknowledgements (optional)
page = 56 # int | The page to filter on. Starts at 1. (optional)

try:
    # Gets marketplace returns
    api_response = api_instance.return_get_declared_by_channel(channel_ids=channel_ids, merchant_order_nos=merchant_order_nos, channel_order_nos=channel_order_nos, fulfillment_type=fulfillment_type, statuses=statuses, reasons=reasons, from_date=from_date, to_date=to_date, is_acknowledged=is_acknowledged, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReturnsApi->return_get_declared_by_channel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_ids** | [**list[int]**](int.md)| Filter on Channel IDs | [optional] 
 **merchant_order_nos** | [**list[str]**](str.md)| Filter on unique order reference used by the merchant. | [optional] 
 **channel_order_nos** | [**list[str]**](str.md)| Filter on unique order reference used by the channel. | [optional] 
 **fulfillment_type** | [**FulfillmentType**](.md)| Filter on the fulfillment type of the order. | [optional] 
 **statuses** | [**list[ReturnStatus]**](ReturnStatus.md)| Return status(es) to filter on. | [optional] 
 **reasons** | [**list[ReturnReason]**](ReturnReason.md)| Return reason(s) to filter on. | [optional] 
 **from_date** | **datetime**| Filter on the creation date, starting from this date. This date is inclusive. | [optional] 
 **to_date** | **datetime**| Filter on the creation date, until this date. This date is exclusive. | [optional] 
 **is_acknowledged** | **bool**| Filters based on acknowledgements | [optional] 
 **page** | **int**| The page to filter on. Starts at 1. | [optional] 

### Return type

[**CollectionOfMerchantReturnResponse**](CollectionOfMerchantReturnResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **return_get_returns**
> CollectionOfMerchantReturnResponse return_get_returns(creator_type=creator_type, channel_ids=channel_ids, merchant_order_nos=merchant_order_nos, channel_order_nos=channel_order_nos, fulfillment_type=fulfillment_type, statuses=statuses, reasons=reasons, from_date=from_date, to_date=to_date, is_acknowledged=is_acknowledged, page=page)

Gets returns by filter

Gets the returns based on the filter provided.<br /><br />**NB:** this endpoint is used to retrieve all types of returns: merchant, marketplace, mixed, and marketplace-fulfilled.

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
api_instance = channelengine_client.ReturnsApi(channelengine_client.ApiClient(configuration))
creator_type = channelengine_client.CreatorFilter() # CreatorFilter | Filter on the return's creator. Default is MIXED. (optional)
channel_ids = [56] # list[int] | Filter on Channel IDs (optional)
merchant_order_nos = ['merchant_order_nos_example'] # list[str] | Filter on unique order reference used by the merchant. (optional)
channel_order_nos = ['channel_order_nos_example'] # list[str] | Filter on unique order reference used by the channel. (optional)
fulfillment_type = channelengine_client.FulfillmentType() # FulfillmentType | Filter on the fulfillment type of the order. (optional)
statuses = [channelengine_client.ReturnStatus()] # list[ReturnStatus] | Return status(es) to filter on. (optional)
reasons = [channelengine_client.ReturnReason()] # list[ReturnReason] | Return reason(s) to filter on. (optional)
from_date = '2013-10-20T19:20:30+01:00' # datetime | Filter on the creation date, starting from this date. This date is inclusive. (optional)
to_date = '2013-10-20T19:20:30+01:00' # datetime | Filter on the creation date, until this date. This date is exclusive. (optional)
is_acknowledged = true # bool | Filters based on acknowledgements (optional)
page = 56 # int | The page to filter on. Starts at 1. (optional)

try:
    # Gets returns by filter
    api_response = api_instance.return_get_returns(creator_type=creator_type, channel_ids=channel_ids, merchant_order_nos=merchant_order_nos, channel_order_nos=channel_order_nos, fulfillment_type=fulfillment_type, statuses=statuses, reasons=reasons, from_date=from_date, to_date=to_date, is_acknowledged=is_acknowledged, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReturnsApi->return_get_returns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **creator_type** | [**CreatorFilter**](.md)| Filter on the return&#x27;s creator. Default is MIXED. | [optional] 
 **channel_ids** | [**list[int]**](int.md)| Filter on Channel IDs | [optional] 
 **merchant_order_nos** | [**list[str]**](str.md)| Filter on unique order reference used by the merchant. | [optional] 
 **channel_order_nos** | [**list[str]**](str.md)| Filter on unique order reference used by the channel. | [optional] 
 **fulfillment_type** | [**FulfillmentType**](.md)| Filter on the fulfillment type of the order. | [optional] 
 **statuses** | [**list[ReturnStatus]**](ReturnStatus.md)| Return status(es) to filter on. | [optional] 
 **reasons** | [**list[ReturnReason]**](ReturnReason.md)| Return reason(s) to filter on. | [optional] 
 **from_date** | **datetime**| Filter on the creation date, starting from this date. This date is inclusive. | [optional] 
 **to_date** | **datetime**| Filter on the creation date, until this date. This date is exclusive. | [optional] 
 **is_acknowledged** | **bool**| Filters based on acknowledgements | [optional] 
 **page** | **int**| The page to filter on. Starts at 1. | [optional] 

### Return type

[**CollectionOfMerchantReturnResponse**](CollectionOfMerchantReturnResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **return_get_unhandled**
> CollectionOfMerchantReturnResponse return_get_unhandled(channel_ids=channel_ids, page=page)

Gets unhandled returns

Gets all marketplace returns with the status **In progress**.

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
api_instance = channelengine_client.ReturnsApi(channelengine_client.ApiClient(configuration))
channel_ids = [56] # list[int] | Filter on Channel IDs (optional)
page = 56 # int | The page to filter on. Starts at 1. (optional)

try:
    # Gets unhandled returns
    api_response = api_instance.return_get_unhandled(channel_ids=channel_ids, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReturnsApi->return_get_unhandled: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_ids** | [**list[int]**](int.md)| Filter on Channel IDs | [optional] 
 **page** | **int**| The page to filter on. Starts at 1. | [optional] 

### Return type

[**CollectionOfMerchantReturnResponse**](CollectionOfMerchantReturnResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **return_handle**
> ApiResponse return_handle(body=body)

[CLOSED BETA] Handle a return

Handles a return<br /> <br />Beware, this endpoint is part of a closed beta and is only available for closed beta participants.

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
api_instance = channelengine_client.ReturnsApi(channelengine_client.ApiClient(configuration))
body = channelengine_client.SingleMerchantHandleReturnRequest() # SingleMerchantHandleReturnRequest | The return to handle (optional)

try:
    # [CLOSED BETA] Handle a return
    api_response = api_instance.return_handle(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReturnsApi->return_handle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SingleMerchantHandleReturnRequest**](SingleMerchantHandleReturnRequest.md)| The return to handle | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **return_update_for_merchant**
> ApiResponse return_update_for_merchant(body=body)

Marks returns as received

Marks a return as either fully or partially received.<br /> <br />**NB:** this endpoint is used for marketplace returns, and you can only accept or reject a return once.

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
api_instance = channelengine_client.ReturnsApi(channelengine_client.ApiClient(configuration))
body = channelengine_client.MerchantReturnUpdateRequest() # MerchantReturnUpdateRequest |  (optional)

try:
    # Marks returns as received
    api_response = api_instance.return_update_for_merchant(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReturnsApi->return_update_for_merchant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MerchantReturnUpdateRequest**](MerchantReturnUpdateRequest.md)|  | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

