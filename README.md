# channelengine-client-py
ChannelEngine API for merchants

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 2.17.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import channelengine_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import channelengine_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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

## Documentation for API Endpoints

All URIs are relative to *https://demo.channelengine.net/api*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CancellationsApi* | [**cancellation_create**](docs/CancellationsApi.md#cancellation_create) | **POST** /v2/cancellations | Creates a cancelation
*CancellationsApi* | [**cancellation_get_for_merchant**](docs/CancellationsApi.md#cancellation_get_for_merchant) | **GET** /v2/cancellations/merchant | Gets cancelations
*ChannelsApi* | [**channel_plugins_get**](docs/ChannelsApi.md#channel_plugins_get) | **GET** /v2/channels | Gets channels
*CompetitionPricesApi* | [**competition_prices_get_buy_box_prices**](docs/CompetitionPricesApi.md#competition_prices_get_buy_box_prices) | **GET** /v2/competitionprices/buyboxprices | Gets the price from the buy box winner
*CustomFieldsApi* | [**custom_fields_get_custom_fields**](docs/CustomFieldsApi.md#custom_fields_get_custom_fields) | **GET** /v2/custom-fields | Gets custom fields
*FulfillmentStockApi* | [**fulfillment_stock_get_fulfillement_stock_with_stock_locations**](docs/FulfillmentStockApi.md#fulfillment_stock_get_fulfillement_stock_with_stock_locations) | **GET** /v2/fulfillmentstock | Gets product stock across all warehouses with stock locations
*ListedProductsApi* | [**listed_product_get_by_filter**](docs/ListedProductsApi.md#listed_product_get_by_filter) | **GET** /v2/channels/{channelId}/products | Gets products listed by channel
*NotificationsApi* | [**notification_index**](docs/NotificationsApi.md#notification_index) | **GET** /v2/notifications | Gets notifications
*OffersApi* | [**offer_get_stock**](docs/OffersApi.md#offer_get_stock) | **GET** /v2/offer/stock | Gets product stock across all warehouses
*OffersApi* | [**offer_stock_price_update**](docs/OffersApi.md#offer_stock_price_update) | **PUT** /v2/offer | Updates stock and price
*OffersApi* | [**offer_stock_update**](docs/OffersApi.md#offer_stock_update) | **PUT** /v2/offer/stock | Updates stock
*OrdersApi* | [**order_acknowledge**](docs/OrdersApi.md#order_acknowledge) | **POST** /v2/orders/acknowledge | Acknowledges orders
*OrdersApi* | [**order_get_by_filter**](docs/OrdersApi.md#order_get_by_filter) | **GET** /v2/orders | Gets orders by filter
*OrdersApi* | [**order_get_new**](docs/OrdersApi.md#order_get_new) | **GET** /v2/orders/new | Gets new orders
*OrdersApi* | [**order_invoice**](docs/OrdersApi.md#order_invoice) | **GET** /v2/orders/{merchantOrderNo}/invoice | Generates an order invoice
*OrdersApi* | [**order_packing_slip**](docs/OrdersApi.md#order_packing_slip) | **GET** /v2/orders/{merchantOrderNo}/packingslip | Generates a packing slip
*OrdersApi* | [**order_update**](docs/OrdersApi.md#order_update) | **PUT** /v2/orders/comment | Updates an order comment
*OrdersApi* | [**order_upload_invoice**](docs/OrdersApi.md#order_upload_invoice) | **POST** /v2/orders/{merchantOrderNo}/invoice | Uploads an order invoice
*OrdersApi* | [**order_upload_invoice_as_string**](docs/OrdersApi.md#order_upload_invoice_as_string) | **POST** /v2/orders/{merchantOrderNo}/invoice-base64 | Uploads an order invoice PDF from Base64 string.
*ProductAttributesApi* | [**product_attribute_group_add_product_extra_data**](docs/ProductAttributesApi.md#product_attribute_group_add_product_extra_data) | **PUT** /v2/product-attribute-group/{groupName}/add | Adds custom attributes to a group
*ProductAttributesApi* | [**product_attribute_group_create**](docs/ProductAttributesApi.md#product_attribute_group_create) | **POST** /v2/product-attribute-group | Creates a custom attribute group
*ProductAttributesApi* | [**product_attribute_group_delete**](docs/ProductAttributesApi.md#product_attribute_group_delete) | **DELETE** /v2/product-attribute-group/{groupName} | Deletes a custom attribute group
*ProductAttributesApi* | [**product_attribute_group_get_by_filter**](docs/ProductAttributesApi.md#product_attribute_group_get_by_filter) | **GET** /v2/product-attribute-group | Gets custom attribute groups
*ProductAttributesApi* | [**product_attribute_group_get_with_channels_by_filter**](docs/ProductAttributesApi.md#product_attribute_group_get_with_channels_by_filter) | **GET** /v2/product-attribute-group/linked-channels | Gets custom attribute groups and linked marketplaces
*ProductAttributesApi* | [**product_attribute_group_remove_product_extra_data**](docs/ProductAttributesApi.md#product_attribute_group_remove_product_extra_data) | **PUT** /v2/product-attribute-group/{groupName}/remove | Deletes custom attributes from a group
*ProductAttributesApi* | [**product_attribute_group_rename_product_attribute_group**](docs/ProductAttributesApi.md#product_attribute_group_rename_product_attribute_group) | **POST** /v2/product-attribute-group/rename | Renames custom attribute groups
*ProductBundlesApi* | [**product_bundle_get_by_filter**](docs/ProductBundlesApi.md#product_bundle_get_by_filter) | **GET** /v2/productbundles | Gets product bundles
*ProductsApi* | [**product_bulk_delete**](docs/ProductsApi.md#product_bulk_delete) | **POST** /v2/products/bulkdelete | Deletes products
*ProductsApi* | [**product_bulk_patch**](docs/ProductsApi.md#product_bulk_patch) | **PATCH** /v2/products | Updates products attributes
*ProductsApi* | [**product_bulk_patch_extra_data_items**](docs/ProductsApi.md#product_bulk_patch_extra_data_items) | **PATCH** /v2/products/extra-data/bulk | Adds, updates, or deletes custom attributes
*ProductsApi* | [**product_create**](docs/ProductsApi.md#product_create) | **POST** /v2/products | Updates or creates products
*ProductsApi* | [**product_delete**](docs/ProductsApi.md#product_delete) | **DELETE** /v2/products/{merchantProductNo} | Deletes a product
*ProductsApi* | [**product_freeze**](docs/ProductsApi.md#product_freeze) | **POST** /v2/products/freeze | Updates selected products and sets them either to frozen or not-frozen status.
*ProductsApi* | [**product_get_by_filter**](docs/ProductsApi.md#product_get_by_filter) | **GET** /v2/products | Gets products
*ProductsApi* | [**product_get_by_merchant_product_no**](docs/ProductsApi.md#product_get_by_merchant_product_no) | **GET** /v2/products/{merchantProductNo} | Gets a product
*ProductsApi* | [**product_patch**](docs/ProductsApi.md#product_patch) | **PATCH** /v2/products/{merchantProductNo} | Updates product attributes
*ProductsApi* | [**product_patch_extra_data_items**](docs/ProductsApi.md#product_patch_extra_data_items) | **PATCH** /v2/products/extra-data | Adds, updates, or deletes a custom attribute
*PurchaseOrdersApi* | [**acknowledge**](docs/PurchaseOrdersApi.md#acknowledge) | **POST** /v2/purchase-orders/lines/acknowledge | Acknowledges lines of a purchase order
*PurchaseOrdersApi* | [**create**](docs/PurchaseOrdersApi.md#create) | **POST** /v2/purchase-orders/shipments | Create a purchase order shipment.
*PurchaseOrdersApi* | [**get_by_filter**](docs/PurchaseOrdersApi.md#get_by_filter) | **GET** /v2/purchase-orders/shipments/merchant | Gets purchase order shipments by filter
*PurchaseOrdersApi* | [**get_by_filter_0**](docs/PurchaseOrdersApi.md#get_by_filter_0) | **GET** /v2/purchase-orders | Gets purchase orders by filter
*PurchaseOrdersApi* | [**purchase_orders_create_invoice**](docs/PurchaseOrdersApi.md#purchase_orders_create_invoice) | **POST** /v2/purchase-orders/invoice | Creates a purchase order invoice
*PurchaseOrdersApi* | [**purchase_orders_create_invoices**](docs/PurchaseOrdersApi.md#purchase_orders_create_invoices) | **POST** /v2/purchase-orders/invoice/bulk | Creates a purchase order invoices in a bulk
*PurchaseOrdersApi* | [**update**](docs/PurchaseOrdersApi.md#update) | **PUT** /v2/purchase-orders/shipments | Update a purchase order shipment.
*RefundsApi* | [**refund_acknowledge**](docs/RefundsApi.md#refund_acknowledge) | **POST** /v2.1/refunds/merchant/acknowledge | [CLOSED BETA] Acknowledge a refund
*RefundsApi* | [**refund_create**](docs/RefundsApi.md#refund_create) | **POST** /v2.1/refunds/merchant | [CLOSED BETA] Create a refund
*RefundsApi* | [**refund_get**](docs/RefundsApi.md#refund_get) | **GET** /v2.1/refunds/merchant/{identifier} | [CLOSED BETA] Get refund by identifier
*RefundsApi* | [**refund_get_by_filter**](docs/RefundsApi.md#refund_get_by_filter) | **GET** /v2.1/refunds/merchant | [CLOSED BETA] Get refunds by filter
*ReportsApi* | [**report_create_settlements_report**](docs/ReportsApi.md#report_create_settlements_report) | **POST** /v2/reports/settlements | Creates a settlement report
*ReportsApi* | [**report_get_report**](docs/ReportsApi.md#report_get_report) | **GET** /v2/reports/{reportId} | Gets a settlement report
*ReportsApi* | [**report_get_status**](docs/ReportsApi.md#report_get_status) | **GET** /v2/reports/{reportId}/status | Gets the status of a settlement report
*ReturnsApi* | [**return_acknowledge**](docs/ReturnsApi.md#return_acknowledge) | **POST** /v2.1/returns/merchant/acknowledge | [CLOSED BETA] Acknowledge a return
*ReturnsApi* | [**return_acknowledge_0**](docs/ReturnsApi.md#return_acknowledge_0) | **POST** /v2/returns/merchant/acknowledge | Acknowledges a return
*ReturnsApi* | [**return_create**](docs/ReturnsApi.md#return_create) | **POST** /v2.1/returns/merchant | [CLOSED BETA] Create a return
*ReturnsApi* | [**return_declare_for_merchant**](docs/ReturnsApi.md#return_declare_for_merchant) | **POST** /v2/returns/merchant | Creates merchant return
*ReturnsApi* | [**return_get**](docs/ReturnsApi.md#return_get) | **GET** /v2.1/returns/merchant/{identifier} | [CLOSED BETA] Get return by identifier
*ReturnsApi* | [**return_get_by_filter**](docs/ReturnsApi.md#return_get_by_filter) | **GET** /v2.1/returns/merchant | [CLOSED BETA] Get returns by filter
*ReturnsApi* | [**return_get_by_merchant_order_no**](docs/ReturnsApi.md#return_get_by_merchant_order_no) | **GET** /v2/returns/merchant/{merchantOrderNo} | Gets a return
*ReturnsApi* | [**return_get_declared_by_channel**](docs/ReturnsApi.md#return_get_declared_by_channel) | **GET** /v2/returns/merchant | Gets marketplace returns
*ReturnsApi* | [**return_get_returns**](docs/ReturnsApi.md#return_get_returns) | **GET** /v2/returns | Gets returns by filter
*ReturnsApi* | [**return_get_unhandled**](docs/ReturnsApi.md#return_get_unhandled) | **GET** /v2/returns/merchant/new | Gets unhandled returns
*ReturnsApi* | [**return_handle**](docs/ReturnsApi.md#return_handle) | **POST** /v2.1/returns/merchant/handle | [CLOSED BETA] Handle a return
*ReturnsApi* | [**return_update_for_merchant**](docs/ReturnsApi.md#return_update_for_merchant) | **PUT** /v2/returns | Marks returns as received
*SettingsApi* | [**settings_get**](docs/SettingsApi.md#settings_get) | **GET** /v2/settings | Gets settings
*SettlementsApi* | [**settlement_get_by_filter**](docs/SettlementsApi.md#settlement_get_by_filter) | **GET** /v2/settlements | Gets settlements
*SettlementsApi* | [**settlement_upload_settlement**](docs/SettlementsApi.md#settlement_upload_settlement) | **POST** /v2/settlements/upload | Uploads a settlement file to ChannelEngine.
*ShipmentsApi* | [**shipment_create**](docs/ShipmentsApi.md#shipment_create) | **POST** /v2/shipments | Creates shipments
*ShipmentsApi* | [**shipment_create_for_channel_method**](docs/ShipmentsApi.md#shipment_create_for_channel_method) | **POST** /v2/shipments/channelmethod | Creates a shipment and initiates shipping label generation
*ShipmentsApi* | [**shipment_get_shipment_label_carriers**](docs/ShipmentsApi.md#shipment_get_shipment_label_carriers) | **POST** /v2/carriers/{merchantOrderNo} | Gets carriers providing shipping labels
*ShipmentsApi* | [**shipment_index**](docs/ShipmentsApi.md#shipment_index) | **GET** /v2/shipments/merchant | Gets shipments by filter
*ShipmentsApi* | [**shipment_shipping_label**](docs/ShipmentsApi.md#shipment_shipping_label) | **GET** /v2/orders/{merchantShipmentNo}/shippinglabel | Gets a shipping label
*ShipmentsApi* | [**shipment_update**](docs/ShipmentsApi.md#shipment_update) | **PUT** /v2/shipments/{merchantShipmentNo} | Updates a shipment
*StockLocationsApi* | [**stock_location_create**](docs/StockLocationsApi.md#stock_location_create) | **POST** /v2/stocklocations | Creates a stock location
*StockLocationsApi* | [**stock_location_index**](docs/StockLocationsApi.md#stock_location_index) | **GET** /v2/stocklocations | Gets stock locations
*TargetsApi* | [**targets_create_targets**](docs/TargetsApi.md#targets_create_targets) | **POST** /v2/targets | Creates multiple targets
*TargetsApi* | [**targets_delete_targets**](docs/TargetsApi.md#targets_delete_targets) | **DELETE** /v2/targets | Deletes multiple targets
*TargetsApi* | [**targets_edit_targets**](docs/TargetsApi.md#targets_edit_targets) | **PUT** /v2/targets | Edits multiple targets
*WebhooksApi* | [**webhooks_create**](docs/WebhooksApi.md#webhooks_create) | **POST** /v2/webhooks | Creates a webhook
*WebhooksApi* | [**webhooks_delete**](docs/WebhooksApi.md#webhooks_delete) | **DELETE** /v2/webhooks/{webhookName} | Deletes a webhook
*WebhooksApi* | [**webhooks_get_all**](docs/WebhooksApi.md#webhooks_get_all) | **GET** /v2/webhooks | Gets webhooks
*WebhooksApi* | [**webhooks_update**](docs/WebhooksApi.md#webhooks_update) | **PUT** /v2/webhooks | Updates a webhook

## Documentation For Models

 - [AddProductExtraDataRequests](docs/AddProductExtraDataRequests.md)
 - [AdvanceSettingsResponse](docs/AdvanceSettingsResponse.md)
 - [ApiResponse](docs/ApiResponse.md)
 - [BulkMerchantCreatePurchaseOrderInvoicesRequest](docs/BulkMerchantCreatePurchaseOrderInvoicesRequest.md)
 - [ChangePurchaseOrderShipmentLine](docs/ChangePurchaseOrderShipmentLine.md)
 - [ChannelCarrierCollectionMethodApi](docs/ChannelCarrierCollectionMethodApi.md)
 - [ChannelCarrierRecommendationApi](docs/ChannelCarrierRecommendationApi.md)
 - [ChannelChannelResponse](docs/ChannelChannelResponse.md)
 - [ChannelExportStatus](docs/ChannelExportStatus.md)
 - [ChannelGlobalChannelResponse](docs/ChannelGlobalChannelResponse.md)
 - [ChannelListedProductResponse](docs/ChannelListedProductResponse.md)
 - [CollectionOfChannelGlobalChannelResponse](docs/CollectionOfChannelGlobalChannelResponse.md)
 - [CollectionOfChannelListedProductResponse](docs/CollectionOfChannelListedProductResponse.md)
 - [CollectionOfCustomFieldResponse](docs/CollectionOfCustomFieldResponse.md)
 - [CollectionOfIPurchaseOrderByFilter](docs/CollectionOfIPurchaseOrderByFilter.md)
 - [CollectionOfIPurchaseOrderShipmentByFilter](docs/CollectionOfIPurchaseOrderShipmentByFilter.md)
 - [CollectionOfMerchantCancellationResponse](docs/CollectionOfMerchantCancellationResponse.md)
 - [CollectionOfMerchantFulfillmentStockStockLocationsResponse](docs/CollectionOfMerchantFulfillmentStockStockLocationsResponse.md)
 - [CollectionOfMerchantNotificationResponse](docs/CollectionOfMerchantNotificationResponse.md)
 - [CollectionOfMerchantOfferGetStockResponse](docs/CollectionOfMerchantOfferGetStockResponse.md)
 - [CollectionOfMerchantOrderResponse](docs/CollectionOfMerchantOrderResponse.md)
 - [CollectionOfMerchantProductAttributeGroupWithLinkedChannelsResponse](docs/CollectionOfMerchantProductAttributeGroupWithLinkedChannelsResponse.md)
 - [CollectionOfMerchantProductAttributeGroupWithProductExtraDataResponse](docs/CollectionOfMerchantProductAttributeGroupWithProductExtraDataResponse.md)
 - [CollectionOfMerchantProductBundleResponse](docs/CollectionOfMerchantProductBundleResponse.md)
 - [CollectionOfMerchantProductResponse](docs/CollectionOfMerchantProductResponse.md)
 - [CollectionOfMerchantProductWithBuyBoxPrice](docs/CollectionOfMerchantProductWithBuyBoxPrice.md)
 - [CollectionOfMerchantReturnResponse](docs/CollectionOfMerchantReturnResponse.md)
 - [CollectionOfMerchantSettlementReportsResponse](docs/CollectionOfMerchantSettlementReportsResponse.md)
 - [CollectionOfMerchantShipmentLabelCarrierResponse](docs/CollectionOfMerchantShipmentLabelCarrierResponse.md)
 - [CollectionOfMerchantShipmentResponse](docs/CollectionOfMerchantShipmentResponse.md)
 - [CollectionOfMerchantSingleOrderReturnResponse](docs/CollectionOfMerchantSingleOrderReturnResponse.md)
 - [CollectionOfMerchantStockLocationWithCountryIsoResponse](docs/CollectionOfMerchantStockLocationWithCountryIsoResponse.md)
 - [CollectionOfMerchantWebhookResponse](docs/CollectionOfMerchantWebhookResponse.md)
 - [Condition](docs/Condition.md)
 - [CreateEditTargetRequest](docs/CreateEditTargetRequest.md)
 - [CreateEditTargetView](docs/CreateEditTargetView.md)
 - [CreatePurchaseOrderShipment](docs/CreatePurchaseOrderShipment.md)
 - [CreatedByType](docs/CreatedByType.md)
 - [CreatorFilter](docs/CreatorFilter.md)
 - [CreatorType](docs/CreatorType.md)
 - [CustomFieldResponse](docs/CustomFieldResponse.md)
 - [DeleteTargetRequest](docs/DeleteTargetRequest.md)
 - [DeleteTargetResponseVm](docs/DeleteTargetResponseVm.md)
 - [DeleteTargetView](docs/DeleteTargetView.md)
 - [DeleteTargetsResponse](docs/DeleteTargetsResponse.md)
 - [ExtraDataType](docs/ExtraDataType.md)
 - [FreezeProductRequest](docs/FreezeProductRequest.md)
 - [FreezingActionRequest](docs/FreezingActionRequest.md)
 - [FulfillmentType](docs/FulfillmentType.md)
 - [Gender](docs/Gender.md)
 - [IImportInformation](docs/IImportInformation.md)
 - [IPurchaseOrderByFilter](docs/IPurchaseOrderByFilter.md)
 - [IPurchaseOrderLineByFilter](docs/IPurchaseOrderLineByFilter.md)
 - [IPurchaseOrderShipmentByFilter](docs/IPurchaseOrderShipmentByFilter.md)
 - [IPurchaseOrderShipmentLineByFilter](docs/IPurchaseOrderShipmentLineByFilter.md)
 - [IRefund](docs/IRefund.md)
 - [IRefundCurrency](docs/IRefundCurrency.md)
 - [IRefundLine](docs/IRefundLine.md)
 - [IReturn](docs/IReturn.md)
 - [IReturnLine](docs/IReturnLine.md)
 - [IReturnLineHandlingResult](docs/IReturnLineHandlingResult.md)
 - [IVendorParty](docs/IVendorParty.md)
 - [JsonPatchDocument](docs/JsonPatchDocument.md)
 - [ListedProductChannelStatus](docs/ListedProductChannelStatus.md)
 - [ListedProductExportStatus](docs/ListedProductExportStatus.md)
 - [MancoReason](docs/MancoReason.md)
 - [MerchantAcknowledgePurchaseOrder](docs/MerchantAcknowledgePurchaseOrder.md)
 - [MerchantAcknowledgePurchaseOrderLine](docs/MerchantAcknowledgePurchaseOrderLine.md)
 - [MerchantAcknowledgeRefund](docs/MerchantAcknowledgeRefund.md)
 - [MerchantAcknowledgeReturn](docs/MerchantAcknowledgeReturn.md)
 - [MerchantAddressResponse](docs/MerchantAddressResponse.md)
 - [MerchantCancellationLineRequest](docs/MerchantCancellationLineRequest.md)
 - [MerchantCancellationLineResponse](docs/MerchantCancellationLineResponse.md)
 - [MerchantCancellationRequest](docs/MerchantCancellationRequest.md)
 - [MerchantCancellationResponse](docs/MerchantCancellationResponse.md)
 - [MerchantChannelLabelShipmentRequest](docs/MerchantChannelLabelShipmentRequest.md)
 - [MerchantCreateRefund](docs/MerchantCreateRefund.md)
 - [MerchantCreateRefundLine](docs/MerchantCreateRefundLine.md)
 - [MerchantCreateReportResponse](docs/MerchantCreateReportResponse.md)
 - [MerchantCreateReturn](docs/MerchantCreateReturn.md)
 - [MerchantCreateReturnLine](docs/MerchantCreateReturnLine.md)
 - [MerchantCreateSettlementsReportRequest](docs/MerchantCreateSettlementsReportRequest.md)
 - [MerchantFulfillmentStockLocationItemResponse](docs/MerchantFulfillmentStockLocationItemResponse.md)
 - [MerchantFulfillmentStockStockLocationsResponse](docs/MerchantFulfillmentStockStockLocationsResponse.md)
 - [MerchantGetReportStatusResponse](docs/MerchantGetReportStatusResponse.md)
 - [MerchantHandleReturn](docs/MerchantHandleReturn.md)
 - [MerchantInvoiceUploadRequest](docs/MerchantInvoiceUploadRequest.md)
 - [MerchantNotificationResponse](docs/MerchantNotificationResponse.md)
 - [MerchantOfferGetStockResponse](docs/MerchantOfferGetStockResponse.md)
 - [MerchantOfferStockUpdateRequest](docs/MerchantOfferStockUpdateRequest.md)
 - [MerchantOrderAcknowledgementRequest](docs/MerchantOrderAcknowledgementRequest.md)
 - [MerchantOrderCommentUpdateRequest](docs/MerchantOrderCommentUpdateRequest.md)
 - [MerchantOrderLineExtraDataResponse](docs/MerchantOrderLineExtraDataResponse.md)
 - [MerchantOrderLineResponse](docs/MerchantOrderLineResponse.md)
 - [MerchantOrderNoInvoiceBody](docs/MerchantOrderNoInvoiceBody.md)
 - [MerchantOrderResponse](docs/MerchantOrderResponse.md)
 - [MerchantProductAttributeGroupChannelInfoResponse](docs/MerchantProductAttributeGroupChannelInfoResponse.md)
 - [MerchantProductAttributeGroupWithLinkedChannelsResponse](docs/MerchantProductAttributeGroupWithLinkedChannelsResponse.md)
 - [MerchantProductAttributeGroupWithProductExtraDataResponse](docs/MerchantProductAttributeGroupWithProductExtraDataResponse.md)
 - [MerchantProductBundlePartResponse](docs/MerchantProductBundlePartResponse.md)
 - [MerchantProductBundleResponse](docs/MerchantProductBundleResponse.md)
 - [MerchantProductExtraDataItemRequest](docs/MerchantProductExtraDataItemRequest.md)
 - [MerchantProductExtraDataItemResponse](docs/MerchantProductExtraDataItemResponse.md)
 - [MerchantProductExtraDataRequest](docs/MerchantProductExtraDataRequest.md)
 - [MerchantProductExtraDataResponse](docs/MerchantProductExtraDataResponse.md)
 - [MerchantProductRequest](docs/MerchantProductRequest.md)
 - [MerchantProductResponse](docs/MerchantProductResponse.md)
 - [MerchantProductWithBuyBoxPrice](docs/MerchantProductWithBuyBoxPrice.md)
 - [MerchantPurchaseOrderInvoice](docs/MerchantPurchaseOrderInvoice.md)
 - [MerchantPurchaseOrderInvoiceLine](docs/MerchantPurchaseOrderInvoiceLine.md)
 - [MerchantReturnAcknowledgeRequest](docs/MerchantReturnAcknowledgeRequest.md)
 - [MerchantReturnLineRequest](docs/MerchantReturnLineRequest.md)
 - [MerchantReturnLineResponse](docs/MerchantReturnLineResponse.md)
 - [MerchantReturnLineUpdateRequest](docs/MerchantReturnLineUpdateRequest.md)
 - [MerchantReturnRequest](docs/MerchantReturnRequest.md)
 - [MerchantReturnResponse](docs/MerchantReturnResponse.md)
 - [MerchantReturnUpdateRequest](docs/MerchantReturnUpdateRequest.md)
 - [MerchantSettingsResponse](docs/MerchantSettingsResponse.md)
 - [MerchantSettlementReportsResponse](docs/MerchantSettlementReportsResponse.md)
 - [MerchantShipmentLabelCarrierRequest](docs/MerchantShipmentLabelCarrierRequest.md)
 - [MerchantShipmentLabelCarrierResponse](docs/MerchantShipmentLabelCarrierResponse.md)
 - [MerchantShipmentLineRequest](docs/MerchantShipmentLineRequest.md)
 - [MerchantShipmentLineResponse](docs/MerchantShipmentLineResponse.md)
 - [MerchantShipmentPackageDimensionsRequest](docs/MerchantShipmentPackageDimensionsRequest.md)
 - [MerchantShipmentPackageWeightRequest](docs/MerchantShipmentPackageWeightRequest.md)
 - [MerchantShipmentRequest](docs/MerchantShipmentRequest.md)
 - [MerchantShipmentResponse](docs/MerchantShipmentResponse.md)
 - [MerchantShipmentTrackingRequest](docs/MerchantShipmentTrackingRequest.md)
 - [MerchantSingleOrderReturnLineResponse](docs/MerchantSingleOrderReturnLineResponse.md)
 - [MerchantSingleOrderReturnResponse](docs/MerchantSingleOrderReturnResponse.md)
 - [MerchantStockLocationAddressRequest](docs/MerchantStockLocationAddressRequest.md)
 - [MerchantStockLocationCreateRequest](docs/MerchantStockLocationCreateRequest.md)
 - [MerchantStockLocationResponse](docs/MerchantStockLocationResponse.md)
 - [MerchantStockLocationUpdateRequest](docs/MerchantStockLocationUpdateRequest.md)
 - [MerchantStockLocationWithCountryIsoResponse](docs/MerchantStockLocationWithCountryIsoResponse.md)
 - [MerchantStockPriceUpdateRequest](docs/MerchantStockPriceUpdateRequest.md)
 - [MerchantVendorParty](docs/MerchantVendorParty.md)
 - [MerchantWebhookRequest](docs/MerchantWebhookRequest.md)
 - [MerchantWebhookResponse](docs/MerchantWebhookResponse.md)
 - [ModuleFulfillmentType](docs/ModuleFulfillmentType.md)
 - [ModuleReturnReason](docs/ModuleReturnReason.md)
 - [ModuleReturnStatus](docs/ModuleReturnStatus.md)
 - [ModulesAdditionalDetailsType](docs/ModulesAdditionalDetailsType.md)
 - [ModulesAllowanceDetailsType](docs/ModulesAllowanceDetailsType.md)
 - [ModulesChargeDetailsType](docs/ModulesChargeDetailsType.md)
 - [ModulesPurchaseOrderInvoiceType](docs/ModulesPurchaseOrderInvoiceType.md)
 - [ModulesPurchaseOrderStatus](docs/ModulesPurchaseOrderStatus.md)
 - [ModulesPurchaseOrderType](docs/ModulesPurchaseOrderType.md)
 - [ModulesTaxRegistrationType](docs/ModulesTaxRegistrationType.md)
 - [ModulesTaxType](docs/ModulesTaxType.md)
 - [NotificationType](docs/NotificationType.md)
 - [Operation](docs/Operation.md)
 - [OrderIdentifier](docs/OrderIdentifier.md)
 - [OrderLineIdentifier](docs/OrderLineIdentifier.md)
 - [OrderStatusView](docs/OrderStatusView.md)
 - [OrderSupport](docs/OrderSupport.md)
 - [PackageDimensionsUnit](docs/PackageDimensionsUnit.md)
 - [PackageWeightUnit](docs/PackageWeightUnit.md)
 - [PatchMerchantProductDto](docs/PatchMerchantProductDto.md)
 - [ProductAttributeGroupRequest](docs/ProductAttributeGroupRequest.md)
 - [ProductCreationResult](docs/ProductCreationResult.md)
 - [ProductExtraDataRequest](docs/ProductExtraDataRequest.md)
 - [ProductMessage](docs/ProductMessage.md)
 - [PurchaseOrderAcknowledgementCode](docs/PurchaseOrderAcknowledgementCode.md)
 - [PurchaseOrderIdentifierType](docs/PurchaseOrderIdentifierType.md)
 - [PurchaseOrderInvoiceAdditionalDetails](docs/PurchaseOrderInvoiceAdditionalDetails.md)
 - [PurchaseOrderInvoiceAllowanceDetails](docs/PurchaseOrderInvoiceAllowanceDetails.md)
 - [PurchaseOrderInvoiceChargeDetails](docs/PurchaseOrderInvoiceChargeDetails.md)
 - [PurchaseOrderInvoiceTaxDetails](docs/PurchaseOrderInvoiceTaxDetails.md)
 - [PurchaseOrderLineIdentifierType](docs/PurchaseOrderLineIdentifierType.md)
 - [PurchaseOrderLineUnitOfMeasure](docs/PurchaseOrderLineUnitOfMeasure.md)
 - [PurchaseOrderRejectionReason](docs/PurchaseOrderRejectionReason.md)
 - [PurchaseOrderRelatedItemExportStatus](docs/PurchaseOrderRelatedItemExportStatus.md)
 - [PurchaseOrderShipmentIdentifierTypeValue](docs/PurchaseOrderShipmentIdentifierTypeValue.md)
 - [RefundByFilterIdentifier](docs/RefundByFilterIdentifier.md)
 - [RefundIdentifier](docs/RefundIdentifier.md)
 - [RefundReason](docs/RefundReason.md)
 - [RemoveProductExtraDataRequests](docs/RemoveProductExtraDataRequests.md)
 - [RenameProductAttributeGroupRequests](docs/RenameProductAttributeGroupRequests.md)
 - [ReportStatus](docs/ReportStatus.md)
 - [ReportType](docs/ReportType.md)
 - [ReturnByFilterIdentifier](docs/ReturnByFilterIdentifier.md)
 - [ReturnHandlingAction](docs/ReturnHandlingAction.md)
 - [ReturnIdentifier](docs/ReturnIdentifier.md)
 - [ReturnLineIdentifier](docs/ReturnLineIdentifier.md)
 - [ReturnReason](docs/ReturnReason.md)
 - [ReturnStatus](docs/ReturnStatus.md)
 - [SettingsResponse](docs/SettingsResponse.md)
 - [SettlementsUploadBody](docs/SettlementsUploadBody.md)
 - [ShipmentFulfillmentType](docs/ShipmentFulfillmentType.md)
 - [ShipmentLineStatus](docs/ShipmentLineStatus.md)
 - [ShipmentSettingsResponse](docs/ShipmentSettingsResponse.md)
 - [ShipmentType](docs/ShipmentType.md)
 - [SingleMerchantAcknowledgePurchaseOrderLinesRequest](docs/SingleMerchantAcknowledgePurchaseOrderLinesRequest.md)
 - [SingleMerchantAcknowledgeRefundRequest](docs/SingleMerchantAcknowledgeRefundRequest.md)
 - [SingleMerchantAcknowledgeReturnRequest](docs/SingleMerchantAcknowledgeReturnRequest.md)
 - [SingleMerchantCreatePurchaseOrderInvoiceRequest](docs/SingleMerchantCreatePurchaseOrderInvoiceRequest.md)
 - [SingleMerchantCreatePurchaseOrderShipmentRequest](docs/SingleMerchantCreatePurchaseOrderShipmentRequest.md)
 - [SingleMerchantCreateRefundRequest](docs/SingleMerchantCreateRefundRequest.md)
 - [SingleMerchantCreateReturnRequest](docs/SingleMerchantCreateReturnRequest.md)
 - [SingleMerchantHandleReturnRequest](docs/SingleMerchantHandleReturnRequest.md)
 - [SingleMerchantUpdatePurchaseOrderShipmentRequest](docs/SingleMerchantUpdatePurchaseOrderShipmentRequest.md)
 - [SingleOfApiResponse](docs/SingleOfApiResponse.md)
 - [SingleOfDeleteTargetsResponse](docs/SingleOfDeleteTargetsResponse.md)
 - [SingleOfDictionaryOfStringAndListOfString](docs/SingleOfDictionaryOfStringAndListOfString.md)
 - [SingleOfIRefund](docs/SingleOfIRefund.md)
 - [SingleOfIReturn](docs/SingleOfIReturn.md)
 - [SingleOfListOfTargetResponseVm](docs/SingleOfListOfTargetResponseVm.md)
 - [SingleOfMerchantProductResponse](docs/SingleOfMerchantProductResponse.md)
 - [SingleOfMerchantSettingsResponse](docs/SingleOfMerchantSettingsResponse.md)
 - [SingleOfProductCreationResult](docs/SingleOfProductCreationResult.md)
 - [TargetResponseVm](docs/TargetResponseVm.md)
 - [UpdatePurchaseOrderShipment](docs/UpdatePurchaseOrderShipment.md)
 - [VatRateType](docs/VatRateType.md)
 - [VatSettingsResponse](docs/VatSettingsResponse.md)
 - [VolumeUnitOfMeasure](docs/VolumeUnitOfMeasure.md)
 - [WebhookEventType](docs/WebhookEventType.md)
 - [WeightUnitOfMeasure](docs/WeightUnitOfMeasure.md)

## Documentation For Authorization


## apiKey

- **Type**: API key
- **API key parameter name**: apikey
- **Location**: URL query string


## Author


