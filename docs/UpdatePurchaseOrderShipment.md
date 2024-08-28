# UpdatePurchaseOrderShipment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_shipment_no** | **str** | The number the merchant uses to identify this PO shipment | [optional] 
**shipment_type** | [**ShipmentType**](ShipmentType.md) |  | [optional] 
**shipped_date** | **datetime** | When the shipment will be/was shipped | [optional] 
**estimated_delivery_date** | **datetime** | Estimated delivery time in the channel&#x27;s warehouse | [optional] 
**selling_party_id** | **str** | The merchant&#x27;s identifying &#x27;selling party number&#x27; at the channel | [optional] 
**ship_to_party_id** | **str** | The destination&#x27;s &#x27;ship to party&#x27; number at the channel | [optional] 
**bill_of_lading_number** | **str** | Bill Of Lading (BOL) number is the unique number assigned by the vendor. The BOL present in the Shipment Confirmation message ideally matches the paper BOL provided with the shipment, but that is no must. Instead of BOL, an alternative reference number (like Delivery Note Number) for the shipment can also be sent in this field. | [optional] 
**shipment_weight_unit_of_measure** | [**WeightUnitOfMeasure**](WeightUnitOfMeasure.md) |  | [optional] 
**shipment_weight** | **float** | The shipment&#x27;s weight | [optional] 
**shipment_volume_unit_of_measure** | [**VolumeUnitOfMeasure**](VolumeUnitOfMeasure.md) |  | [optional] 
**shipment_volume** | **float** | The shipment&#x27;s volume | [optional] 
**lines** | [**list[ChangePurchaseOrderShipmentLine]**](ChangePurchaseOrderShipmentLine.md) | Shipment information for each shipped product | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

