# channelengine_client.PurchaseOrdersApi

All URIs are relative to *https://demo.channelengine.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**acknowledge**](PurchaseOrdersApi.md#acknowledge) | **POST** /v2/purchase-orders/lines/acknowledge | Acknowledges lines of a purchase order
[**create**](PurchaseOrdersApi.md#create) | **POST** /v2/purchase-orders/shipments | Create a purchase order shipment.
[**get_by_filter**](PurchaseOrdersApi.md#get_by_filter) | **GET** /v2/purchase-orders/shipments/merchant | Gets purchase order shipments by filter
[**get_by_filter_0**](PurchaseOrdersApi.md#get_by_filter_0) | **GET** /v2/purchase-orders | Gets purchase orders by filter
[**purchase_orders_create_invoice**](PurchaseOrdersApi.md#purchase_orders_create_invoice) | **POST** /v2/purchase-orders/invoice | Creates a purchase order invoice
[**purchase_orders_create_invoices**](PurchaseOrdersApi.md#purchase_orders_create_invoices) | **POST** /v2/purchase-orders/invoice/bulk | Creates a purchase order invoices in a bulk
[**update**](PurchaseOrdersApi.md#update) | **PUT** /v2/purchase-orders/shipments | Update a purchase order shipment.

# **acknowledge**
> ApiResponse acknowledge(body=body)

Acknowledges lines of a purchase order

Creates line acknowledgements (i.e., accepted, backordered, rejected) for a purchase order.<br />Request will be accepted and data persisted only if all validations passed.<br />Any validation messages and errors will be returned in a HTTP 4xx response.

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
api_instance = channelengine_client.PurchaseOrdersApi(channelengine_client.ApiClient(configuration))
body = channelengine_client.SingleMerchantAcknowledgePurchaseOrderLinesRequest() # SingleMerchantAcknowledgePurchaseOrderLinesRequest | Model for purchase order and lines data to be acknowledged with the channel. (optional)

try:
    # Acknowledges lines of a purchase order
    api_response = api_instance.acknowledge(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PurchaseOrdersApi->acknowledge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SingleMerchantAcknowledgePurchaseOrderLinesRequest**](SingleMerchantAcknowledgePurchaseOrderLinesRequest.md)| Model for purchase order and lines data to be acknowledged with the channel. | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create**
> ApiResponse create(body=body)

Create a purchase order shipment.

One shipments can ship (parts of) multiple orders

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
api_instance = channelengine_client.PurchaseOrdersApi(channelengine_client.ApiClient(configuration))
body = channelengine_client.SingleMerchantCreatePurchaseOrderShipmentRequest() # SingleMerchantCreatePurchaseOrderShipmentRequest |  (optional)

try:
    # Create a purchase order shipment.
    api_response = api_instance.create(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PurchaseOrdersApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SingleMerchantCreatePurchaseOrderShipmentRequest**](SingleMerchantCreatePurchaseOrderShipmentRequest.md)|  | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_by_filter**
> CollectionOfIPurchaseOrderShipmentByFilter get_by_filter(channel_id=channel_id, identifiers_identifier_type=identifiers_identifier_type, identifiers_models=identifiers_models, shipped_date_range_from_date=shipped_date_range_from_date, shipped_date_range_to_date=shipped_date_range_to_date, create_date_range_from_date=create_date_range_from_date, create_date_range_to_date=create_date_range_to_date, update_date_range_from_date=update_date_range_from_date, update_date_range_to_date=update_date_range_to_date, bill_of_lading_number=bill_of_lading_number, carrier_name=carrier_name, page_index=page_index, page_size=page_size)

Gets purchase order shipments by filter

Gets purchase order shipments based on the available filters.

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
api_instance = channelengine_client.PurchaseOrdersApi(channelengine_client.ApiClient(configuration))
channel_id = 56 # int | The identifier of the channel (optional)
identifiers_identifier_type = channelengine_client.PurchaseOrderShipmentIdentifierTypeValue() # PurchaseOrderShipmentIdentifierTypeValue | The type of identifier: which identifier to filter on (optional)
identifiers_models = ['identifiers_models_example'] # list[str] | The value (of the selected type) to filter on (optional)
shipped_date_range_from_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
shipped_date_range_to_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
create_date_range_from_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
create_date_range_to_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
update_date_range_from_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
update_date_range_to_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
bill_of_lading_number = 'bill_of_lading_number_example' # str | The Bill of Lading number. Multiple shipments can have the same Bill of Lading number (optional)
carrier_name = 'carrier_name_example' # str | The name of the carrier (optional)
page_index = 56 # int |  (optional)
page_size = 56 # int |  (optional)

try:
    # Gets purchase order shipments by filter
    api_response = api_instance.get_by_filter(channel_id=channel_id, identifiers_identifier_type=identifiers_identifier_type, identifiers_models=identifiers_models, shipped_date_range_from_date=shipped_date_range_from_date, shipped_date_range_to_date=shipped_date_range_to_date, create_date_range_from_date=create_date_range_from_date, create_date_range_to_date=create_date_range_to_date, update_date_range_from_date=update_date_range_from_date, update_date_range_to_date=update_date_range_to_date, bill_of_lading_number=bill_of_lading_number, carrier_name=carrier_name, page_index=page_index, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PurchaseOrdersApi->get_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **int**| The identifier of the channel | [optional] 
 **identifiers_identifier_type** | [**PurchaseOrderShipmentIdentifierTypeValue**](.md)| The type of identifier: which identifier to filter on | [optional] 
 **identifiers_models** | [**list[str]**](str.md)| The value (of the selected type) to filter on | [optional] 
 **shipped_date_range_from_date** | **datetime**|  | [optional] 
 **shipped_date_range_to_date** | **datetime**|  | [optional] 
 **create_date_range_from_date** | **datetime**|  | [optional] 
 **create_date_range_to_date** | **datetime**|  | [optional] 
 **update_date_range_from_date** | **datetime**|  | [optional] 
 **update_date_range_to_date** | **datetime**|  | [optional] 
 **bill_of_lading_number** | **str**| The Bill of Lading number. Multiple shipments can have the same Bill of Lading number | [optional] 
 **carrier_name** | **str**| The name of the carrier | [optional] 
 **page_index** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 

### Return type

[**CollectionOfIPurchaseOrderShipmentByFilter**](CollectionOfIPurchaseOrderShipmentByFilter.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_by_filter_0**
> CollectionOfIPurchaseOrderByFilter get_by_filter_0(identifiers_identifier_type=identifiers_identifier_type, identifiers_models=identifiers_models, statuses=statuses, order_date_range_from_date=order_date_range_from_date, order_date_range_to_date=order_date_range_to_date, create_date_range_from_date=create_date_range_from_date, create_date_range_to_date=create_date_range_to_date, update_date_range_from_date=update_date_range_from_date, update_date_range_to_date=update_date_range_to_date, channel_ids=channel_ids, type=type, page_index=page_index, page_size=page_size)

Gets purchase orders by filter

Gets purchase orders based on the available filters.

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
api_instance = channelengine_client.PurchaseOrdersApi(channelengine_client.ApiClient(configuration))
identifiers_identifier_type = channelengine_client.PurchaseOrderIdentifierType() # PurchaseOrderIdentifierType | The type of identifier: which identifier to filter on (optional)
identifiers_models = ['identifiers_models_example'] # list[str] | The value (of the selected type) to filter on (optional)
statuses = [channelengine_client.ModulesPurchaseOrderStatus()] # list[ModulesPurchaseOrderStatus] |  (optional)
order_date_range_from_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
order_date_range_to_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
create_date_range_from_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
create_date_range_to_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
update_date_range_from_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
update_date_range_to_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
channel_ids = [56] # list[int] |  (optional)
type = channelengine_client.ModulesPurchaseOrderType() # ModulesPurchaseOrderType |  (optional)
page_index = 56 # int |  (optional)
page_size = 56 # int |  (optional)

try:
    # Gets purchase orders by filter
    api_response = api_instance.get_by_filter_0(identifiers_identifier_type=identifiers_identifier_type, identifiers_models=identifiers_models, statuses=statuses, order_date_range_from_date=order_date_range_from_date, order_date_range_to_date=order_date_range_to_date, create_date_range_from_date=create_date_range_from_date, create_date_range_to_date=create_date_range_to_date, update_date_range_from_date=update_date_range_from_date, update_date_range_to_date=update_date_range_to_date, channel_ids=channel_ids, type=type, page_index=page_index, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PurchaseOrdersApi->get_by_filter_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifiers_identifier_type** | [**PurchaseOrderIdentifierType**](.md)| The type of identifier: which identifier to filter on | [optional] 
 **identifiers_models** | [**list[str]**](str.md)| The value (of the selected type) to filter on | [optional] 
 **statuses** | [**list[ModulesPurchaseOrderStatus]**](ModulesPurchaseOrderStatus.md)|  | [optional] 
 **order_date_range_from_date** | **datetime**|  | [optional] 
 **order_date_range_to_date** | **datetime**|  | [optional] 
 **create_date_range_from_date** | **datetime**|  | [optional] 
 **create_date_range_to_date** | **datetime**|  | [optional] 
 **update_date_range_from_date** | **datetime**|  | [optional] 
 **update_date_range_to_date** | **datetime**|  | [optional] 
 **channel_ids** | [**list[int]**](int.md)|  | [optional] 
 **type** | [**ModulesPurchaseOrderType**](.md)|  | [optional] 
 **page_index** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 

### Return type

[**CollectionOfIPurchaseOrderByFilter**](CollectionOfIPurchaseOrderByFilter.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purchase_orders_create_invoice**
> ApiResponse purchase_orders_create_invoice(body=body)

Creates a purchase order invoice

Creates invoice for a purchase order.<br />Request will be accepted and data persisted only if all validations passed.<br />Any validation messages and errors will be returned in a HTTP 4xx response.

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
api_instance = channelengine_client.PurchaseOrdersApi(channelengine_client.ApiClient(configuration))
body = channelengine_client.SingleMerchantCreatePurchaseOrderInvoiceRequest() # SingleMerchantCreatePurchaseOrderInvoiceRequest | Model for purchase order invoice. (optional)

try:
    # Creates a purchase order invoice
    api_response = api_instance.purchase_orders_create_invoice(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PurchaseOrdersApi->purchase_orders_create_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SingleMerchantCreatePurchaseOrderInvoiceRequest**](SingleMerchantCreatePurchaseOrderInvoiceRequest.md)| Model for purchase order invoice. | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purchase_orders_create_invoices**
> ApiResponse purchase_orders_create_invoices(body=body)

Creates a purchase order invoices in a bulk

Creates invoices for a purchase orders in a bulk.<br />Request will be accepted and data persisted only if all validations passed.<br />Any validation messages and errors will be returned in a HTTP 4xx response.

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
api_instance = channelengine_client.PurchaseOrdersApi(channelengine_client.ApiClient(configuration))
body = channelengine_client.BulkMerchantCreatePurchaseOrderInvoicesRequest() # BulkMerchantCreatePurchaseOrderInvoicesRequest | Model for purchase order invoices. (optional)

try:
    # Creates a purchase order invoices in a bulk
    api_response = api_instance.purchase_orders_create_invoices(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PurchaseOrdersApi->purchase_orders_create_invoices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BulkMerchantCreatePurchaseOrderInvoicesRequest**](BulkMerchantCreatePurchaseOrderInvoicesRequest.md)| Model for purchase order invoices. | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> ApiResponse update(body=body)

Update a purchase order shipment.

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
api_instance = channelengine_client.PurchaseOrdersApi(channelengine_client.ApiClient(configuration))
body = channelengine_client.SingleMerchantUpdatePurchaseOrderShipmentRequest() # SingleMerchantUpdatePurchaseOrderShipmentRequest |  (optional)

try:
    # Update a purchase order shipment.
    api_response = api_instance.update(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PurchaseOrdersApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SingleMerchantUpdatePurchaseOrderShipmentRequest**](SingleMerchantUpdatePurchaseOrderShipmentRequest.md)|  | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

