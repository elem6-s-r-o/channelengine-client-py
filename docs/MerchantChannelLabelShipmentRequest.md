# MerchantChannelLabelShipmentRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dimensions** | [**MerchantShipmentPackageDimensionsRequest**](MerchantShipmentPackageDimensionsRequest.md) |  | 
**weight** | [**MerchantShipmentPackageWeightRequest**](MerchantShipmentPackageWeightRequest.md) |  | 
**channel_method_code** | **str** |  | 
**merchant_shipment_no** | **str** | The unique shipment reference used by the Merchant. | 
**merchant_order_no** | **str** | The unique order reference used by the Merchant. | 
**shipped_from_country_code** | **str** | The code of the country from where the package is being shipped. | [optional] 
**shipped_from_stock_location_id** | **int** |  | [optional] 
**lines** | [**list[MerchantShipmentLineRequest]**](MerchantShipmentLineRequest.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

