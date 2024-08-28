# IRefund

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**reason** | [**RefundReason**](RefundReason.md) |  | [optional] 
**channel_export_status** | [**ChannelExportStatus**](ChannelExportStatus.md) |  | [optional] 
**sub_total_incl_tax** | **float** |  | [optional] 
**original_sub_total_incl_tax** | **float** |  | [optional] 
**additional_amount_incl_tax** | **float** |  | [optional] 
**original_additional_amount_incl_tax** | **float** |  | [optional] 
**shipping_cost_incl_tax** | **float** |  | [optional] 
**original_shipping_cost_incl_tax** | **float** |  | [optional] 
**total_incl_tax** | **float** |  | [optional] 
**original_total_incl_tax** | **float** |  | [optional] 
**merchant_comment** | **str** |  | [optional] 
**merchant_refund_no** | **str** |  | [optional] 
**channel_refund_no** | **str** |  | [optional] 
**channel_order_no** | **str** |  | [optional] 
**created_by_type** | [**CreatedByType**](CreatedByType.md) |  | [optional] 
**refund_date** | **datetime** |  | [optional] 
**external_batch_no** | **str** |  | [optional] 
**channel_acknowledged_date** | **datetime** |  | [optional] 
**merchant_acknowledged_date** | **datetime** |  | [optional] 
**order_id** | **int** |  | [optional] 
**channel_id** | **int** |  | [optional] 
**return_id** | **int** |  | [optional] 
**currency** | [**IRefundCurrency**](IRefundCurrency.md) |  | [optional] 
**lines** | [**list[IRefundLine]**](IRefundLine.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**deleted_at** | **datetime** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

