# channelengine_client.SettlementsApi

All URIs are relative to *https://demo.channelengine.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**settlement_get_by_filter**](SettlementsApi.md#settlement_get_by_filter) | **GET** /v2/settlements | Gets settlements
[**settlement_upload_settlement**](SettlementsApi.md#settlement_upload_settlement) | **POST** /v2/settlements/upload | Uploads a settlement file to ChannelEngine.

# **settlement_get_by_filter**
> CollectionOfMerchantSettlementReportsResponse settlement_get_by_filter(un_exported_only=un_exported_only, settlement_ids=settlement_ids, channel_settlement_nos=channel_settlement_nos, channel_ids=channel_ids, from_start_date=from_start_date, to_start_date=to_start_date, from_end_date=from_end_date, to_end_date=to_end_date, from_create_date=from_create_date, to_create_date=to_create_date, from_update_date=from_update_date, to_update_date=to_update_date, page=page)

Gets settlements

Gets the settlements based on the available filters.

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
api_instance = channelengine_client.SettlementsApi(channelengine_client.ApiClient(configuration))
un_exported_only = true # bool | Filter on settlements that have not been exported before. (optional)
settlement_ids = [56] # list[int] | Filter on settlement IDs. (optional)
channel_settlement_nos = ['channel_settlement_nos_example'] # list[str] | Filter on channel settlement nos. (optional)
channel_ids = [56] # list[int] | Filter on channel id list. (optional)
from_start_date = '2013-10-20T19:20:30+01:00' # datetime | Filter on the start date of the settlement in ChannelEngine, until this date. This date is exclusive. (optional)
to_start_date = '2013-10-20T19:20:30+01:00' # datetime | Filter on the start date of the settlement in ChannelEngine, until this date. This date is exclusive. (optional)
from_end_date = '2013-10-20T19:20:30+01:00' # datetime | Filter on the end date of the settlement in ChannelEngine, starting from this date. This date is inclusive. (optional)
to_end_date = '2013-10-20T19:20:30+01:00' # datetime | Filter on the end date of the settlement in ChannelEngine, until this date. This date is exclusive. (optional)
from_create_date = '2013-10-20T19:20:30+01:00' # datetime | Filter on the create date of the settlement in ChannelEngine, until this date. This date is exclusive. (optional)
to_create_date = '2013-10-20T19:20:30+01:00' # datetime | Filter on the create date of the settlement in ChannelEngine, until this date. This date is exclusive. (optional)
from_update_date = '2013-10-20T19:20:30+01:00' # datetime | Filter on the update date of the settlement in ChannelEngine, starting from this date. This date is inclusive. (optional)
to_update_date = '2013-10-20T19:20:30+01:00' # datetime | Filter on the update date of the settlement in ChannelEngine, until this date. This date is exclusive. (optional)
page = 56 # int | The page to filter on. Starts at 1. (optional)

try:
    # Gets settlements
    api_response = api_instance.settlement_get_by_filter(un_exported_only=un_exported_only, settlement_ids=settlement_ids, channel_settlement_nos=channel_settlement_nos, channel_ids=channel_ids, from_start_date=from_start_date, to_start_date=to_start_date, from_end_date=from_end_date, to_end_date=to_end_date, from_create_date=from_create_date, to_create_date=to_create_date, from_update_date=from_update_date, to_update_date=to_update_date, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettlementsApi->settlement_get_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **un_exported_only** | **bool**| Filter on settlements that have not been exported before. | [optional] 
 **settlement_ids** | [**list[int]**](int.md)| Filter on settlement IDs. | [optional] 
 **channel_settlement_nos** | [**list[str]**](str.md)| Filter on channel settlement nos. | [optional] 
 **channel_ids** | [**list[int]**](int.md)| Filter on channel id list. | [optional] 
 **from_start_date** | **datetime**| Filter on the start date of the settlement in ChannelEngine, until this date. This date is exclusive. | [optional] 
 **to_start_date** | **datetime**| Filter on the start date of the settlement in ChannelEngine, until this date. This date is exclusive. | [optional] 
 **from_end_date** | **datetime**| Filter on the end date of the settlement in ChannelEngine, starting from this date. This date is inclusive. | [optional] 
 **to_end_date** | **datetime**| Filter on the end date of the settlement in ChannelEngine, until this date. This date is exclusive. | [optional] 
 **from_create_date** | **datetime**| Filter on the create date of the settlement in ChannelEngine, until this date. This date is exclusive. | [optional] 
 **to_create_date** | **datetime**| Filter on the create date of the settlement in ChannelEngine, until this date. This date is exclusive. | [optional] 
 **from_update_date** | **datetime**| Filter on the update date of the settlement in ChannelEngine, starting from this date. This date is inclusive. | [optional] 
 **to_update_date** | **datetime**| Filter on the update date of the settlement in ChannelEngine, until this date. This date is exclusive. | [optional] 
 **page** | **int**| The page to filter on. Starts at 1. | [optional] 

### Return type

[**CollectionOfMerchantSettlementReportsResponse**](CollectionOfMerchantSettlementReportsResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settlement_upload_settlement**
> ApiResponse settlement_upload_settlement(settlement=settlement, channel_id=channel_id)

Uploads a settlement file to ChannelEngine.

Uploads a settlement file to ChannelEngine.

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
api_instance = channelengine_client.SettlementsApi(channelengine_client.ApiClient(configuration))
settlement = 'settlement_example' # str |  (optional)
channel_id = 56 # int | The channel ID of the channel which the settlement is for. (optional)

try:
    # Uploads a settlement file to ChannelEngine.
    api_response = api_instance.settlement_upload_settlement(settlement=settlement, channel_id=channel_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettlementsApi->settlement_upload_settlement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settlement** | **str**|  | [optional] 
 **channel_id** | **int**| The channel ID of the channel which the settlement is for. | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

