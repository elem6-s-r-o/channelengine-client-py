# MerchantCancellationResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique cancellation identifier used by ChannelEngine. | [optional] 
**merchant_cancellation_no** | **str** | The unique cancellation reference used by the Merchant (sku). | 
**merchant_order_no** | **str** | The unique order reference used by the Merchant. | 
**channel_order_no** | **str** | The unique order reference used by the Channel. | [optional] 
**lines** | [**list[MerchantCancellationLineResponse]**](MerchantCancellationLineResponse.md) |  | 
**created_at** | **datetime** | The date at which the cancellation was created in ChannelEngine. | [optional] 
**reason** | **str** | Reason for cancellation (text). | [optional] 
**reason_code** | [**MancoReason**](MancoReason.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

