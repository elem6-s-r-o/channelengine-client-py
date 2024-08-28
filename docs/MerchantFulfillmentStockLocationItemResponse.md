# MerchantFulfillmentStockLocationItemResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ChannelEngine id of the stock location. | [optional] 
**name** | **str** | The ChannelEngine name of the stock location. | [optional] 
**reserved_quantity** | **int** | Total quantity reserved for orders. | [optional] 
**available_quantity** | **int** | The quantity that is available for fulfillment orders. | [optional] 
**allocated_quantity** | **int** | Quantity pending customer order | [optional] 
**in_transit_quantity** | **int** | Quantity in transit / &#x27;transshipment&#x27; (Amazon) | [optional] 
**fulfillment_center_processing_quantity** | **int** | Quantity that is in processing at the fulfillment warehouse (center) | [optional] 
**defective_quantity** | **int** | The number of units in defective disposition. | [optional] 
**expired_quantity** | **int** | The number of units in expired disposition. | [optional] 
**warehouse_damaged_quantity** | **int** | The number of units in warehouse damaged disposition. | [optional] 
**customer_damaged_quantity** | **int** | The number of units in customer damaged disposition. | [optional] 
**carrier_damaged_quantity** | **int** | The number of units in carrier damaged disposition. | [optional] 
**pending_pickup_quantity** | **int** | The number of units in pending pickup disposition. | [optional] 
**inbound_quantity** | **int** | Total quantity that is inbound (in inbound [aka fulfillment] shipment from the seller to the fulfillment warehouse) | [optional] 
**return_quantity** | **int** | Total quantity in on going returns | [optional] 
**researching_quantity** | **int** | Quantity that is being researched | [optional] 
**updated_at** | **datetime** | The timestamp of the last stock update for the stock location. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

