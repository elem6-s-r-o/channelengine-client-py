# MerchantCreateRefund

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_identifier** | **str** |  | [optional] 
**merchant_refund_no** | **str** |  | [optional] 
**reason** | [**RefundReason**](RefundReason.md) |  | [optional] 
**merchant_comment** | **str** |  | [optional] 
**additional_amount_incl_tax** | **float** |  | [optional] 
**shipping_amount_incl_tax** | **float** |  | [optional] 
**refund_date** | **datetime** |  | [optional] 
**extra_data** | **dict(str, str)** |  | [optional] 
**lines** | [**list[MerchantCreateRefundLine]**](MerchantCreateRefundLine.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

