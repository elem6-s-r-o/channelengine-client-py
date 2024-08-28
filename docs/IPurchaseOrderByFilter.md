# IPurchaseOrderByFilter

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**channel_id** | **int** |  | [optional] 
**channel_name** | **str** |  | [optional] 
**global_channel_name** | **str** |  | [optional] 
**global_channel_id** | **int** |  | [optional] 
**channel_purchase_order_no** | **str** |  | [optional] 
**merchant_purchase_order_no** | **str** |  | [optional] 
**status** | [**ModulesPurchaseOrderStatus**](ModulesPurchaseOrderStatus.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**type** | [**ModulesPurchaseOrderType**](ModulesPurchaseOrderType.md) |  | [optional] 
**from_ship_date** | **datetime** |  | [optional] 
**to_ship_date** | **datetime** |  | [optional] 
**from_delivery_date** | **datetime** |  | [optional] 
**to_delivery_date** | **datetime** |  | [optional] 
**import_information** | [**IImportInformation**](IImportInformation.md) |  | [optional] 
**selling_party** | [**IVendorParty**](IVendorParty.md) |  | [optional] 
**ship_to_party** | [**IVendorParty**](IVendorParty.md) |  | [optional] 
**buying_party** | [**IVendorParty**](IVendorParty.md) |  | [optional] 
**billing_party** | [**IVendorParty**](IVendorParty.md) |  | [optional] 
**lines** | [**list[IPurchaseOrderLineByFilter]**](IPurchaseOrderLineByFilter.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

