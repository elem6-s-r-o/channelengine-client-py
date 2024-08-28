# MerchantCancellationRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_cancellation_no** | **str** | The unique cancellation reference used by the Merchant (sku). | 
**merchant_order_no** | **str** | The unique order reference used by the Merchant (sku). | 
**lines** | [**list[MerchantCancellationLineRequest]**](MerchantCancellationLineRequest.md) |  | 
**reason** | **str** | Reason for cancellation (text). | [optional] 
**reason_code** | [**MancoReason**](MancoReason.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

