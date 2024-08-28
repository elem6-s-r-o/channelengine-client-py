# MerchantProductRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent_merchant_product_no** | **str** | If this product is a different version of another  product (for example, all fields are the same except  size), then this field should contain  the &#x27;MerchantProductNo&#x27; of the parent. The parent  should already exist (or be present between the products  in the content of the API call, it does not matter whether  the parent is behind the child in the list). | [optional] 
**parent_merchant_product_no2** | **str** | If this product is a different version of another  product (for example, all fields are the same except  color) and itself is a parent with child products (e.g. of sizes),  then this field should contain the &#x27;MerchantProductNo&#x27; of the grandparent. The grandparent  should already exist (or be present between the products  in the content of the API call, it does not matter whether  the grandparent is behind the child in the list).  When you set this field, the ParentMerchantProductNo should be left empty.                Use this field in case of three level product hierarchy,  e.g. model - color - size.  This is required for channels like Otto. | [optional] 
**extra_data** | [**list[MerchantProductExtraDataItemRequest]**](MerchantProductExtraDataItemRequest.md) | An optional list of key-value pairs containing  extra data about this product. This data can be  sent to channels or used for filtering products. | [optional] 
**name** | **str** | The name of the product. | [optional] 
**description** | **str** | A description of the product. Can contain these HTML tags:  div, span, pre, p, br, hr, hgroup, h1, h2, h3, h4, h5, h6, ul, ol, li, dl, dt, dd, strong, em, b, i, u, img, a, abbr, address, blockquote, area, audio, video, caption, table, tbody, td, tfoot, th, thead, tr. | [optional] 
**brand** | **str** | The brand of the product. | [optional] 
**size** | **str** | Optional. The size of the product (variant). E.g. fashion size (S-XL, 46-56, etc), width of the watch, etc.. | [optional] 
**color** | **str** | Optional. The color of the product (variant). | [optional] 
**ean** | **str** | The EAN of GTIN of the product. | [optional] 
**manufacturer_product_number** | **str** | The unique product reference used by the manufacturer/vendor of the product. | [optional] 
**merchant_product_no** | **str** | A unique identifier of the product. (sku). | 
**stock** | **int** | The number of items in stock. | [optional] 
**price** | **float** | Price, including VAT. | [optional] 
**min_price** | **float** | Min price, including VAT. | [optional] 
**max_price** | **float** | Max price, including VAT. | [optional] 
**msrp** | **float** | Manufacturer&#x27;s suggested retail price. | [optional] 
**purchase_price** | **float** | Optional. The purchase price of the product. Useful for repricing. | [optional] 
**vat_rate_type** | [**VatRateType**](VatRateType.md) |  | [optional] 
**shipping_cost** | **float** | Shipping cost of the product. | [optional] 
**shipping_time** | **str** | A textual representation of the shippingtime.  For example, in Dutch: &#x27;Op werkdagen voor 22:00 uur besteld, morgen in huis&#x27;. | [optional] 
**url** | **str** | A URL pointing to the merchant&#x27;s webpage  which displays this product. | [optional] 
**image_url** | **str** | A URL at which an image of this product  can be found. | [optional] 
**extra_image_url1** | **str** | Url to an additional image of product (1). | [optional] 
**extra_image_url2** | **str** | Url to an additional image of product (2). | [optional] 
**extra_image_url3** | **str** | Url to an additional image of product (3). | [optional] 
**extra_image_url4** | **str** | Url to an additional image of product (4). | [optional] 
**extra_image_url5** | **str** | Url to an additional image of product (5). | [optional] 
**extra_image_url6** | **str** | Url to an additional image of product (6). | [optional] 
**extra_image_url7** | **str** | Url to an additional image of product (7). | [optional] 
**extra_image_url8** | **str** | Url to an additional image of product (8). | [optional] 
**extra_image_url9** | **str** | Url to an additional image of product (9). | [optional] 
**is_frozen** | **bool** | Specifies whether Product is disabled on all channels. | [optional] 
**category_trail** | **str** | The category to which this product belongs.  Please supply this field in the following format:  &#x27;maincategory &gt; category &gt; subcategory&#x27;  For example:  &#x27;vehicles &gt; bikes &gt; mountainbike&#x27;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

