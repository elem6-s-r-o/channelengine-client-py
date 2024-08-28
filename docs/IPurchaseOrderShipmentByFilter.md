# IPurchaseOrderShipmentByFilter

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ChannelEngine identifier of the shipment | [optional] 
**merchant_shipment_no** | **str** | The number the merchant uses to id this PO shipment | [optional] 
**channel_shipment_no** | **str** | The number the channel uses to id this PO shipment | [optional] 
**shipment_type** | [**ShipmentType**](ShipmentType.md) |  | [optional] 
**shipped_date** | **datetime** | When the shipment was shipped | [optional] 
**estimated_delivery_date** | **datetime** | Estimated delivery time in the channel&#x27;s warehouse | [optional] 
**carrier_name** | **str** | Name of the carrier | [optional] 
**carrier_shipment_no** | **str** | The number the carrier uses to id this PO shipment | [optional] 
**bill_of_lading_number** | **str** | Bill of Lading number (not unique for a shipment) | [optional] 
**shipment_weight_unit_of_measure** | [**WeightUnitOfMeasure**](WeightUnitOfMeasure.md) |  | [optional] 
**shipment_weight** | **float** | The shipment&#x27;s weight | [optional] 
**shipment_volume_unit_of_measure** | [**VolumeUnitOfMeasure**](VolumeUnitOfMeasure.md) |  | [optional] 
**shipment_volume** | **float** | The shipment&#x27;s volume | [optional] 
**last_merchant_updated_at** | **datetime** | The last time the shipment was updated by the merchant | [optional] 
**last_exported_at** | **datetime** | The last time the shipment was exported to the channel | [optional] 
**last_export_status** | [**PurchaseOrderRelatedItemExportStatus**](PurchaseOrderRelatedItemExportStatus.md) |  | [optional] 
**lines** | [**list[IPurchaseOrderShipmentLineByFilter]**](IPurchaseOrderShipmentLineByFilter.md) | The products in this PO shipment | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

