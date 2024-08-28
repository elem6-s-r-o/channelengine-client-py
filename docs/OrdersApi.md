# channelengine_client.OrdersApi

All URIs are relative to *https://demo.channelengine.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**order_acknowledge**](OrdersApi.md#order_acknowledge) | **POST** /v2/orders/acknowledge | Acknowledges orders
[**order_get_by_filter**](OrdersApi.md#order_get_by_filter) | **GET** /v2/orders | Gets orders by filter
[**order_get_new**](OrdersApi.md#order_get_new) | **GET** /v2/orders/new | Gets new orders
[**order_invoice**](OrdersApi.md#order_invoice) | **GET** /v2/orders/{merchantOrderNo}/invoice | Generates an order invoice
[**order_packing_slip**](OrdersApi.md#order_packing_slip) | **GET** /v2/orders/{merchantOrderNo}/packingslip | Generates a packing slip
[**order_update**](OrdersApi.md#order_update) | **PUT** /v2/orders/comment | Updates an order comment
[**order_upload_invoice**](OrdersApi.md#order_upload_invoice) | **POST** /v2/orders/{merchantOrderNo}/invoice | Uploads an order invoice
[**order_upload_invoice_as_string**](OrdersApi.md#order_upload_invoice_as_string) | **POST** /v2/orders/{merchantOrderNo}/invoice-base64 | Uploads an order invoice PDF from Base64 string.

# **order_acknowledge**
> ApiResponse order_acknowledge(body=body)

Acknowledges orders

Acknowledges an order to confirm order import.

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
api_instance = channelengine_client.OrdersApi(channelengine_client.ApiClient(configuration))
body = channelengine_client.MerchantOrderAcknowledgementRequest() # MerchantOrderAcknowledgementRequest | Relations between the id's returned by ChannelEngine and the references which the merchant uses. (optional)

try:
    # Acknowledges orders
    api_response = api_instance.order_acknowledge(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->order_acknowledge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MerchantOrderAcknowledgementRequest**](MerchantOrderAcknowledgementRequest.md)| Relations between the id&#x27;s returned by ChannelEngine and the references which the merchant uses. | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_get_by_filter**
> CollectionOfMerchantOrderResponse order_get_by_filter(statuses=statuses, email_addresses=email_addresses, merchant_order_nos=merchant_order_nos, channel_order_nos=channel_order_nos, commercial_order_nos=commercial_order_nos, from_date=from_date, to_date=to_date, from_created_at_date=from_created_at_date, to_created_at_date=to_created_at_date, exclude_marketplace_fulfilled_orders_and_lines=exclude_marketplace_fulfilled_orders_and_lines, fulfillment_type=fulfillment_type, only_with_cancellation_requests=only_with_cancellation_requests, channel_ids=channel_ids, stock_location_ids=stock_location_ids, is_acknowledged=is_acknowledged, from_updated_at_date=from_updated_at_date, to_updated_at_date=to_updated_at_date, from_acknowledged_date=from_acknowledged_date, to_acknowledged_date=to_acknowledged_date, from_closed_at_date=from_closed_at_date, to_closed_at_date=to_closed_at_date, page=page)

Gets orders by filter

Gets orders based on the available filters.

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
api_instance = channelengine_client.OrdersApi(channelengine_client.ApiClient(configuration))
statuses = [channelengine_client.OrderStatusView()] # list[OrderStatusView] | Order status(es) to filter on. AWAITING_PAYMENT orders will be excluded if it is not included in this Statuses filter. (optional)
email_addresses = ['email_addresses_example'] # list[str] | Client emailaddresses to filter on. (optional)
merchant_order_nos = ['merchant_order_nos_example'] # list[str] | Filter on unique order reference used by the merchant. (optional)
channel_order_nos = ['channel_order_nos_example'] # list[str] | Filter on unique order reference used by the channel. (optional)
commercial_order_nos = ['commercial_order_nos_example'] # list[str] | Filter on commercial order numbers. (optional)
from_date = '2013-10-20T19:20:30+01:00' # datetime | Filter on the order date, starting from this date. This date is inclusive.<br />The order date is based on the data we got from a channel. (optional)
to_date = '2013-10-20T19:20:30+01:00' # datetime | Filter on the order date, until this date. This date is exclusive.<br />The order date is based on the data we got from a channel. (optional)
from_created_at_date = '2013-10-20T19:20:30+01:00' # datetime | Filter on the created at date in ChannelEngine, starting from this date. This date is inclusive.<br />The created date is set on the date and time when the order is created. (optional)
to_created_at_date = '2013-10-20T19:20:30+01:00' # datetime | Filter on the created at date in ChannelEngine, until this date. This date is exclusive.<br />The created date is set on the date and time when the order is created. (optional)
exclude_marketplace_fulfilled_orders_and_lines = true # bool | Exclude order (lines) fulfilled by the marketplace (amazon:FBA, bol:LVB, etc.) (optional)
fulfillment_type = channelengine_client.FulfillmentType() # FulfillmentType | Filter orders on fulfillment type. This will include all orders lines, even if they are partially fulfilled by the marketplace.<br />To exclude orders and lines that are fulfilled by the marketplace from the response, set ExcludeMarketplaceFulfilledOrdersAndLines to true. (optional)
only_with_cancellation_requests = true # bool | Filter on orders containing cancellation requests.<br />Some channels allow a customer to cancel an order until it has been shipped.<br />When an order has already been acknowledged in ChannelEngine, it can only be cancelled by creating a cancellation. (optional)
channel_ids = [56] # list[int] | Filter orders on channel(s). (optional)
stock_location_ids = [56] # list[int] | Filter on stock locations (optional)
is_acknowledged = true # bool | Filter on acknowledged value (optional)
from_updated_at_date = '2013-10-20T19:20:30+01:00' # datetime | Filter on the order update date, starting from this date. This date is inclusive. (optional)
to_updated_at_date = '2013-10-20T19:20:30+01:00' # datetime | Filter on the order update date, unitl this date. This date is exclusive. (optional)
from_acknowledged_date = '2013-10-20T19:20:30+01:00' # datetime | Filter on the order acknowledged date, starting from this date. This date is inclusive. (optional)
to_acknowledged_date = '2013-10-20T19:20:30+01:00' # datetime | Filter on the order acknowledged date, until this date. This date is exclusive. (optional)
from_closed_at_date = '2013-10-20T19:20:30+01:00' # datetime | Filter on the order ClosedAt date, starting from this date. This date is inclusive. (optional)
to_closed_at_date = '2013-10-20T19:20:30+01:00' # datetime | Filter on the order ClosedAt date, until this date. This date is exclusive. (optional)
page = 56 # int | The page to filter on. Starts at 1. (optional)

try:
    # Gets orders by filter
    api_response = api_instance.order_get_by_filter(statuses=statuses, email_addresses=email_addresses, merchant_order_nos=merchant_order_nos, channel_order_nos=channel_order_nos, commercial_order_nos=commercial_order_nos, from_date=from_date, to_date=to_date, from_created_at_date=from_created_at_date, to_created_at_date=to_created_at_date, exclude_marketplace_fulfilled_orders_and_lines=exclude_marketplace_fulfilled_orders_and_lines, fulfillment_type=fulfillment_type, only_with_cancellation_requests=only_with_cancellation_requests, channel_ids=channel_ids, stock_location_ids=stock_location_ids, is_acknowledged=is_acknowledged, from_updated_at_date=from_updated_at_date, to_updated_at_date=to_updated_at_date, from_acknowledged_date=from_acknowledged_date, to_acknowledged_date=to_acknowledged_date, from_closed_at_date=from_closed_at_date, to_closed_at_date=to_closed_at_date, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->order_get_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **statuses** | [**list[OrderStatusView]**](OrderStatusView.md)| Order status(es) to filter on. AWAITING_PAYMENT orders will be excluded if it is not included in this Statuses filter. | [optional] 
 **email_addresses** | [**list[str]**](str.md)| Client emailaddresses to filter on. | [optional] 
 **merchant_order_nos** | [**list[str]**](str.md)| Filter on unique order reference used by the merchant. | [optional] 
 **channel_order_nos** | [**list[str]**](str.md)| Filter on unique order reference used by the channel. | [optional] 
 **commercial_order_nos** | [**list[str]**](str.md)| Filter on commercial order numbers. | [optional] 
 **from_date** | **datetime**| Filter on the order date, starting from this date. This date is inclusive.&lt;br /&gt;The order date is based on the data we got from a channel. | [optional] 
 **to_date** | **datetime**| Filter on the order date, until this date. This date is exclusive.&lt;br /&gt;The order date is based on the data we got from a channel. | [optional] 
 **from_created_at_date** | **datetime**| Filter on the created at date in ChannelEngine, starting from this date. This date is inclusive.&lt;br /&gt;The created date is set on the date and time when the order is created. | [optional] 
 **to_created_at_date** | **datetime**| Filter on the created at date in ChannelEngine, until this date. This date is exclusive.&lt;br /&gt;The created date is set on the date and time when the order is created. | [optional] 
 **exclude_marketplace_fulfilled_orders_and_lines** | **bool**| Exclude order (lines) fulfilled by the marketplace (amazon:FBA, bol:LVB, etc.) | [optional] 
 **fulfillment_type** | [**FulfillmentType**](.md)| Filter orders on fulfillment type. This will include all orders lines, even if they are partially fulfilled by the marketplace.&lt;br /&gt;To exclude orders and lines that are fulfilled by the marketplace from the response, set ExcludeMarketplaceFulfilledOrdersAndLines to true. | [optional] 
 **only_with_cancellation_requests** | **bool**| Filter on orders containing cancellation requests.&lt;br /&gt;Some channels allow a customer to cancel an order until it has been shipped.&lt;br /&gt;When an order has already been acknowledged in ChannelEngine, it can only be cancelled by creating a cancellation. | [optional] 
 **channel_ids** | [**list[int]**](int.md)| Filter orders on channel(s). | [optional] 
 **stock_location_ids** | [**list[int]**](int.md)| Filter on stock locations | [optional] 
 **is_acknowledged** | **bool**| Filter on acknowledged value | [optional] 
 **from_updated_at_date** | **datetime**| Filter on the order update date, starting from this date. This date is inclusive. | [optional] 
 **to_updated_at_date** | **datetime**| Filter on the order update date, unitl this date. This date is exclusive. | [optional] 
 **from_acknowledged_date** | **datetime**| Filter on the order acknowledged date, starting from this date. This date is inclusive. | [optional] 
 **to_acknowledged_date** | **datetime**| Filter on the order acknowledged date, until this date. This date is exclusive. | [optional] 
 **from_closed_at_date** | **datetime**| Filter on the order ClosedAt date, starting from this date. This date is inclusive. | [optional] 
 **to_closed_at_date** | **datetime**| Filter on the order ClosedAt date, until this date. This date is exclusive. | [optional] 
 **page** | **int**| The page to filter on. Starts at 1. | [optional] 

### Return type

[**CollectionOfMerchantOrderResponse**](CollectionOfMerchantOrderResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_get_new**
> CollectionOfMerchantOrderResponse order_get_new(stock_location_id=stock_location_id)

Gets new orders

Gets orders with the status **New**.

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
api_instance = channelengine_client.OrdersApi(channelengine_client.ApiClient(configuration))
stock_location_id = 56 # int | The ChannelEngine id of the stock location. (optional)

try:
    # Gets new orders
    api_response = api_instance.order_get_new(stock_location_id=stock_location_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->order_get_new: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stock_location_id** | **int**| The ChannelEngine id of the stock location. | [optional] 

### Return type

[**CollectionOfMerchantOrderResponse**](CollectionOfMerchantOrderResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_invoice**
> file order_invoice(merchant_order_no, use_customer_culture=use_customer_culture)

Generates an order invoice

Generates the ChannelEngine sales tax invoice for an order in PDF.

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
api_instance = channelengine_client.OrdersApi(channelengine_client.ApiClient(configuration))
merchant_order_no = 'merchant_order_no_example' # str | The unique order reference as used by the merchant.
use_customer_culture = false # bool | Generate the invoice in the billing address' country's language. (optional) (default to false)

try:
    # Generates an order invoice
    api_response = api_instance.order_invoice(merchant_order_no, use_customer_culture=use_customer_culture)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->order_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_order_no** | **str**| The unique order reference as used by the merchant. | 
 **use_customer_culture** | **bool**| Generate the invoice in the billing address&#x27; country&#x27;s language. | [optional] [default to false]

### Return type

[**file**](file.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_packing_slip**
> file order_packing_slip(merchant_order_no, use_customer_culture=use_customer_culture)

Generates a packing slip

Generates the ChannelEngine packing slip for an order in PDF.

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
api_instance = channelengine_client.OrdersApi(channelengine_client.ApiClient(configuration))
merchant_order_no = 'merchant_order_no_example' # str | The unique order reference as used by the merchant.
use_customer_culture = false # bool | Generate the invoice in the billing address' country's language. (optional) (default to false)

try:
    # Generates a packing slip
    api_response = api_instance.order_packing_slip(merchant_order_no, use_customer_culture=use_customer_culture)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->order_packing_slip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_order_no** | **str**| The unique order reference as used by the merchant. | 
 **use_customer_culture** | **bool**| Generate the invoice in the billing address&#x27; country&#x27;s language. | [optional] [default to false]

### Return type

[**file**](file.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_update**
> ApiResponse order_update(body=body)

Updates an order comment

Updates the merchant comment for an order based on the ChannelEngine **Order ID** or the **Merchant order number**.

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
api_instance = channelengine_client.OrdersApi(channelengine_client.ApiClient(configuration))
body = channelengine_client.MerchantOrderCommentUpdateRequest() # MerchantOrderCommentUpdateRequest |  (optional)

try:
    # Updates an order comment
    api_response = api_instance.order_update(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->order_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MerchantOrderCommentUpdateRequest**](MerchantOrderCommentUpdateRequest.md)|  | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_upload_invoice**
> ApiResponse order_upload_invoice(merchant_order_no, invoice=invoice, invoice_number=invoice_number)

Uploads an order invoice

Uploads the invoice for an order in PDF.

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
api_instance = channelengine_client.OrdersApi(channelengine_client.ApiClient(configuration))
merchant_order_no = 'merchant_order_no_example' # str | The unique order reference as used by the merchant.
invoice = 'invoice_example' # str |  (optional)
invoice_number = 'invoice_number_example' # str |  (optional)

try:
    # Uploads an order invoice
    api_response = api_instance.order_upload_invoice(merchant_order_no, invoice=invoice, invoice_number=invoice_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->order_upload_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_order_no** | **str**| The unique order reference as used by the merchant. | 
 **invoice** | **str**|  | [optional] 
 **invoice_number** | **str**|  | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_upload_invoice_as_string**
> ApiResponse order_upload_invoice_as_string(merchant_order_no, body=body)

Uploads an order invoice PDF from Base64 string.

Uploads an order invoice PDF from Base64 string.<br />Invoice size must be less than 1 mb.

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
api_instance = channelengine_client.OrdersApi(channelengine_client.ApiClient(configuration))
merchant_order_no = 'merchant_order_no_example' # str | 
body = channelengine_client.MerchantInvoiceUploadRequest() # MerchantInvoiceUploadRequest |  (optional)

try:
    # Uploads an order invoice PDF from Base64 string.
    api_response = api_instance.order_upload_invoice_as_string(merchant_order_no, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->order_upload_invoice_as_string: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_order_no** | **str**|  | 
 **body** | [**MerchantInvoiceUploadRequest**](MerchantInvoiceUploadRequest.md)|  | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

