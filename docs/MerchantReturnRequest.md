# MerchantReturnRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_order_no** | **str** | The unique order reference used by the Merchant (sku). | 
**merchant_return_no** | **str** | The unique return reference used by the Merchant (sku). | 
**lines** | [**list[MerchantReturnLineRequest]**](MerchantReturnLineRequest.md) |  | 
**id** | **int** | The unique return reference used by ChannelEngine. | [optional] 
**reason** | [**ReturnReason**](ReturnReason.md) |  | [optional] 
**customer_comment** | **str** | Optional. Comment of customer on the (reason of) the return. | [optional] 
**merchant_comment** | **str** | Optional. Comment of merchant on the return. | [optional] 
**refund_incl_vat** | **float** | Refund amount incl. VAT. | [optional] 
**refund_excl_vat** | **float** | Refund amount excl. VAT. | [optional] 
**return_date** | **datetime** | The date at which the return was originally created in the source system (if available). | [optional] 
**extra_data** | **dict(str, str)** | Extra data on the return. Each item must have an unqiue key | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

