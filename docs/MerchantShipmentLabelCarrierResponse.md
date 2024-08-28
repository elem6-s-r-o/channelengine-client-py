# MerchantShipmentLabelCarrierResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The channel&#x27;s name for the shipping label carrier | [optional] 
**code** | **str** | The channel&#x27;s code for the shipping label carrier | [optional] 
**restrictions** | **str** | Optional. Any restrictions on this carriers, e.g. weight and/or dimensions | [optional] 
**price** | **float** | Optional. Price for this shipping label | [optional] 
**recommendation** | [**ChannelCarrierRecommendationApi**](ChannelCarrierRecommendationApi.md) |  | [optional] 
**collection_method** | [**ChannelCarrierCollectionMethodApi**](ChannelCarrierCollectionMethodApi.md) |  | [optional] 
**handover_date_time** | **datetime** | Optional. When to handover the package to the carrier  It is in the ISO format including the timezone offset.  E.g. 2020-10-03T18:00:00+02:00  which is 3rd Oct 2020, at 18:00 PM in Amsterdam (Summer Time aka CEST: UTC +2:00 ) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

