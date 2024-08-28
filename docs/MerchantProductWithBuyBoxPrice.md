# MerchantProductWithBuyBoxPrice

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sku** | **str** | Product SKU number | [optional] 
**gtin** | **str** | Product GTIN | [optional] 
**buy_box_price** | **float** | Price of Buy box winner (excl. shipping cost)  Note: not all channels have a separate shipping cost field (e.g. bol.com), so can be the same as BuyBoxPriceInclShipping | [optional] 
**buy_box_price_incl_shipping** | **float** | Price of Buy box winner (incl. shipping cost).  If null, then there is no data or no Buy box winner | [optional] 
**is_merchant_buy_box_winner** | **bool** | Are you the Buy box winner or not? | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

