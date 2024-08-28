# MerchantWebhookRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The unique name of a webhook. | 
**url** | **str** | The callback URL used by a webhook. E.g.: https://test-store.com/callback. | 
**is_active** | **bool** | Determines if a webhook is active, and callbacks should proceed. | [optional] 
**events** | [**list[WebhookEventType]**](WebhookEventType.md) | The events supported by the webhook. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

