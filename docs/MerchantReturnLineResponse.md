# MerchantReturnLineResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_product_no** | **str** | The unique product reference used by the Merchant (sku). | [optional] 
**order_line** | [**MerchantOrderLineResponse**](MerchantOrderLineResponse.md) |  | [optional] 
**shipment_status** | [**ShipmentLineStatus**](ShipmentLineStatus.md) |  | [optional] 
**stock_location** | [**MerchantStockLocationResponse**](MerchantStockLocationResponse.md) |  | [optional] 
**quantity** | **int** | Number of items of the product in this return. | 
**extra_data** | **dict(str, str)** | Extra data on the returnline. Each item must have an unqiue key | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
