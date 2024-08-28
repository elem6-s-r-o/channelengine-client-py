# MerchantStockPriceUpdateRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_product_no** | **str** | The unique product reference used by the Merchant (sku). | 
**stock** | **int** | The stock of the product. Should not be negative. | [optional] 
**price** | **float** | The price of the product. Should not be negative. | [optional] 
**stock_location_id** | **int** | The stock location id of the updated stock. If not provided, the stock from the default stock location will be updated. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

