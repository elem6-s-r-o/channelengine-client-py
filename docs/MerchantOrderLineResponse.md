# MerchantOrderLineResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier used by ChannelEngine. | [optional] 
**channel_order_line_no** | **str** | The order line reference used by the channel. | [optional] 
**status** | [**OrderStatusView**](OrderStatusView.md) |  | [optional] 
**is_fulfillment_by_marketplace** | **bool** | Is the order fulfilled by the marketplace (amazon: FBA, bol: LVB, etc.)?. | [optional] 
**gtin** | **str** | Either the GTIN (EAN, ISBN, UPC etc) provided by the channel, or the the GTIN belonging to the MerchantProductNo in ChannelEngine. | [optional] 
**description** | **str** | The product description (or title) provided by the channel. | [optional] 
**stock_location** | [**MerchantStockLocationResponse**](MerchantStockLocationResponse.md) |  | [optional] 
**unit_vat** | **float** | The total amount of VAT charged over the value of a single unit of the ordered product  (in the shop&#x27;s base currency calculated using the exchange rate at the time of ordering). | [optional] 
**line_total_incl_vat** | **float** | The total value of the order line (quantity * unit price) including VAT  (in the shop&#x27;s base currency calculated using the exchange rate at the time of ordering). | [optional] 
**line_vat** | **float** | The total amount of VAT charged over the total value of the order line (quantity * unit price)  (in the shop&#x27;s base currency calculated using the exchange rate at the time of ordering). | [optional] 
**original_unit_price_incl_vat** | **float** | The value of a single unit of the ordered product including VAT  (in the currency in which the order was paid for, see CurrencyCode). | [optional] 
**original_unit_vat** | **float** | The total amount of VAT charged over the value of a single unit of the ordered product  (in the currency in which the order was paid for, see CurrencyCode). | [optional] 
**original_line_total_incl_vat** | **float** | The total value of the order line (quantity * unit price) including VAT  (in the currency in which the order was paid for, see CurrencyCode). | [optional] 
**original_line_vat** | **float** | The total amount of VAT charged over the total value of the order line (quantity * unit price)  (in the currency in which the order was paid for, see CurrencyCode). | [optional] 
**original_fee_fixed** | **float** | A percentage fee that is charged by the Channel for this orderline.  This fee rate is based on the currency of client  This field is optional, send 0 if not applicable. | [optional] 
**bundle_product_merchant_product_no** | **str** | If the product is ordered part of a bundle, this field contains the MerchantProductNo of  the product bundle. | [optional] 
**juris_code** | **str** | State assigned code identifying the jurisdiction. | [optional] 
**juris_name** | **str** | Name of a tax jurisdiction. | [optional] 
**vat_rate** | **float** | VAT rate of the orderline. | [optional] 
**unit_price_excl_vat** | **float** |  | [optional] 
**line_total_excl_vat** | **float** |  | [optional] 
**original_unit_price_excl_vat** | **float** |  | [optional] 
**original_line_total_excl_vat** | **float** |  | [optional] 
**extra_data** | [**list[MerchantOrderLineExtraDataResponse]**](MerchantOrderLineExtraDataResponse.md) |  | [optional] 
**channel_product_no** | **str** | The unique product reference used by the channel. | 
**merchant_product_no** | **str** | The unique product reference used by the merchant. | [optional] 
**quantity** | **int** | The number of items of the product. | 
**cancellation_requested_quantity** | **int** | The number of items for which cancellation was requested by the customer.  Some channels allow a customer to cancel an order until it has been shipped.  When an order has already been acknowledged in ChannelEngine, it can only be cancelled by creating a cancellation.  Use this field to check whether it is still possible to cancel the order. If this is the case, submit a cancellation to ChannelEngine. | [optional] 
**unit_price_incl_vat** | **float** | The value of a single unit of the ordered product including VAT  (in the shop&#x27;s base currency calculated using the exchange rate at the time of ordering). | 
**fee_fixed** | **float** | A fixed fee that is charged by the Channel for this orderline.  This fee rate is based on the currency of the Channel  This field is optional, send 0 if not applicable. | [optional] 
**fee_rate** | **float** | A percentage fee that is charged by the Channel for this orderline.  This field is optional, send 0 if not applicable. | [optional] 
**condition** | [**Condition**](Condition.md) |  | [optional] 
**exact_delivery_date** | **datetime** | The exact date when the order (line) must be delivered. Delivery cannot occur before or after this date.  This can be empty if the channel does not provide this info. | [optional] 
**expected_delivery_date** | **datetime** | The date when the order should be delivered. This field must always contain a value, either the exact date or the latest possible date.  If this value is not set, the system defaults to using the order date plus two days as the expected delivery date.  This field is used for backwards compatibility. | [optional] 
**latest_delivery_date** | **datetime** | The latest possible date when the order (line) must be delivered. Delivery can occur on or before this date, but not after.  This can be empty if the channel does not provide this info. | [optional] 
**expected_shipment_date** | **datetime** | The date when when the order (line) should be shipped.  This can be empty if the channel does not provide this info. | [optional] 
**latest_shipment_date** | **datetime** | The latest possible date when the order (line) must be shipped. Shipment can occur on or before this date, but not after.  This can be empty if the channel does not provide this info. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

