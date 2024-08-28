# MerchantShipmentLineResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_product_no** | **str** | The unique product reference used by the Merchant. | 
**merchant_bundle_product_no** | **str** | The unique bundle product reference used by the Merchant. | [optional] 
**channel_product_no** | **str** | The unique product reference used by the Channel. | [optional] 
**order_line** | [**MerchantOrderLineResponse**](MerchantOrderLineResponse.md) |  | [optional] 
**shipment_status** | [**ShipmentLineStatus**](ShipmentLineStatus.md) |  | [optional] 
**extra_data** | **dict(str, str)** | Extra data on the shipment line. Each item must have an unqiue key | [optional] 
**quantity** | **int** | Number of items of the product in the shipment. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

