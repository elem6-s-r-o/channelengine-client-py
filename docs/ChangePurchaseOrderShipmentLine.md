# ChangePurchaseOrderShipmentLine

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_order_no** | **str** | Channel&#x27;s identifier of the purchase order | 
**merchant_product_no** | **str** | Merchant&#x27;s identifier of the product.  The combination of ChannelOrderNo + MerchantProductNo identifies the order line this shipment line  ships. | 
**quantity_unit_of_measure** | [**PurchaseOrderLineUnitOfMeasure**](PurchaseOrderLineUnitOfMeasure.md) |  | [optional] 
**quantity** | **int** | The quantity | [optional] 
**quantity_unit_size** | **int** | The case size, when QuantityUnitOfMeasure is &#x27;CASES&#x27;. Otherwise, it is 1. | [optional] 
**expiry_date** | **datetime** | The date that determines the limit of consumption or use of a product.  For perishable products. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

