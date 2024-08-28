# channelengine_client.ProductsApi

All URIs are relative to *https://demo.channelengine.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**product_bulk_delete**](ProductsApi.md#product_bulk_delete) | **POST** /v2/products/bulkdelete | Deletes products
[**product_bulk_patch**](ProductsApi.md#product_bulk_patch) | **PATCH** /v2/products | Updates products attributes
[**product_bulk_patch_extra_data_items**](ProductsApi.md#product_bulk_patch_extra_data_items) | **PATCH** /v2/products/extra-data/bulk | Adds, updates, or deletes custom attributes
[**product_create**](ProductsApi.md#product_create) | **POST** /v2/products | Updates or creates products
[**product_delete**](ProductsApi.md#product_delete) | **DELETE** /v2/products/{merchantProductNo} | Deletes a product
[**product_freeze**](ProductsApi.md#product_freeze) | **POST** /v2/products/freeze | Updates selected products and sets them either to frozen or not-frozen status.
[**product_get_by_filter**](ProductsApi.md#product_get_by_filter) | **GET** /v2/products | Gets products
[**product_get_by_merchant_product_no**](ProductsApi.md#product_get_by_merchant_product_no) | **GET** /v2/products/{merchantProductNo} | Gets a product
[**product_patch**](ProductsApi.md#product_patch) | **PATCH** /v2/products/{merchantProductNo} | Updates product attributes
[**product_patch_extra_data_items**](ProductsApi.md#product_patch_extra_data_items) | **PATCH** /v2/products/extra-data | Adds, updates, or deletes a custom attribute

# **product_bulk_delete**
> ApiResponse product_bulk_delete(body)

Deletes products

Deletes a products based on the **Merchant product number**.<br /> <br />**NB:** ChannelEngine deactivates but does not delete the products entirely, as they might be still referenced in orders.<br />Therefore, the references used for these products cannot be reused.

### Example
```python
from __future__ import print_function
import time
import channelengine_client
from channelengine_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = channelengine_client.Configuration()
configuration.api_key['apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# create an instance of the API class
api_instance = channelengine_client.ProductsApi(channelengine_client.ApiClient(configuration))
body = ['body_example'] # list[str] | The list of MerchantProductNo of the products you wish to delete.

try:
    # Deletes products
    api_response = api_instance.product_bulk_delete(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->product_bulk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[str]**](str.md)| The list of MerchantProductNo of the products you wish to delete. | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_bulk_patch**
> SingleOfProductCreationResult product_bulk_patch(body=body)

Updates products attributes

Updates specific attributes of product data. You can update single or multiple attributes for one or multiple products.<br />You can also add custom attributes via this endpoint. The format of this endpoint is JSON Patch.<br />Products are updated for the fields listed in the array **PropertiesToUpdate**:<br />[name, <br />description, <br />details, <br />brand, <br />size, <br />color, <br />ean, <br />groupno **or** ParentMerchantProductNo, <br />groupno2 **or** ParentMerchantProductNo2, <br />type, <br />merchantproductno,<br />vendorproductno, <br />stock, <br />price, <br />listprice **or** MSRP, <br />purchaseprice, <br />minprice, <br />maxprice, <br />discountrate, <br />vatrate, <br />margin, <br />shippingcost, <br />shippingtime, <br />url, <br />imageurl, <br />extraimageurl1, <br />extraimageurl2, <br />extraimageurl3, <br />extraimageurl4, <br />extraimageurl5, <br />extraimageurl6, <br />extraimageurl7, <br />extraimageurl8, <br />extraimageurl9, <br />categoryid,<br />vatratetype]<br /> <br />Sample request:<br /><pre><br />PATCH /v2/products<br />{<br /> \"PropertiesToUpdate\": [<br /> \"name\",<br /> \"description\"<br /> ],<br /> \"MerchantProductRequestModels\": [<br /> {<br /> \"MerchantProductNo\": \"testMerchantProductNo\",<br /> \"Name\": \"testName\",<br /> \"Description\": \"testDescription\",<br /> },<br /> {<br /> \"MerchantProductNo\": \"testMerchantProductNo2\",<br /> \"Name\": \"testName3\",<br /> \"Description\": \"testDescription1\",<br /> }<br /> ]<br />}<br /></pre>

### Example
```python
from __future__ import print_function
import time
import channelengine_client
from channelengine_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = channelengine_client.Configuration()
configuration.api_key['apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# create an instance of the API class
api_instance = channelengine_client.ProductsApi(channelengine_client.ApiClient(configuration))
body = channelengine_client.PatchMerchantProductDto() # PatchMerchantProductDto | 1) PropertiesToUpdate: Fields to update<br />2) MerchantProductRequestModels: Products to be updated (optional)

try:
    # Updates products attributes
    api_response = api_instance.product_bulk_patch(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->product_bulk_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PatchMerchantProductDto**](PatchMerchantProductDto.md)| 1) PropertiesToUpdate: Fields to update&lt;br /&gt;2) MerchantProductRequestModels: Products to be updated | [optional] 

### Return type

[**SingleOfProductCreationResult**](SingleOfProductCreationResult.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_bulk_patch_extra_data_items**
> SingleOfProductCreationResult product_bulk_patch_extra_data_items(body=body)

Adds, updates, or deletes custom attributes

Adds, updates, or deletes the custom attributes (a.k.a. extra data keys) for multiple products.<br />You can update single or multiple attributes for one or multiple products. The format of this endpoint is [JSON Patch](http://jsonpatch.com/).<br /><br />**NB:** the **Merchant product number** must be unique.<br /><br />Sample request:<br /><pre><br />PATCH /v2/products/extra-data/bulk<br />[<br /> {<br /> \"MerchantProductNo\": \"{merchantProductNo}\",<br /> \"Operations\": [<br /> {<br /> \"Op\": \"add\",<br /> \"Key\": \"{Key}\",<br /> \"Value\": \"{Value}\"<br /> }<br /> ]<br /> },<br /> {<br /> \"MerchantProductNo\": \"{merchantProductNo}\",<br /> \"Operations\": [<br /> {<br /> \"Op\": \"replace\",<br /> \"Key\": \"{Key}\",<br /> \"Value\": \"{Value}\"<br /> },<br /> {<br /> \"Op\": \"add\",<br /> \"Key\": \"{Key}\",<br /> \"Value\": \"{Value}\"<br /> }<br /> ]<br /> },<br /> {<br /> \"MerchantProductNo\": \"{merchantProductNo}\",<br /> \"Operations\": [<br /> {<br /> \"Op\": \"remove\",<br /> \"Key\": \"{Key}\",<br /> \"Value\": \"{Value}\"<br /> }<br /> ]<br /> }<br /> ]<br /></pre>

### Example
```python
from __future__ import print_function
import time
import channelengine_client
from channelengine_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = channelengine_client.Configuration()
configuration.api_key['apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# create an instance of the API class
api_instance = channelengine_client.ProductsApi(channelengine_client.ApiClient(configuration))
body = [channelengine_client.MerchantProductExtraDataRequest()] # list[MerchantProductExtraDataRequest] |  (optional)

try:
    # Adds, updates, or deletes custom attributes
    api_response = api_instance.product_bulk_patch_extra_data_items(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->product_bulk_patch_extra_data_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[MerchantProductExtraDataRequest]**](MerchantProductExtraDataRequest.md)|  | [optional] 

### Return type

[**SingleOfProductCreationResult**](SingleOfProductCreationResult.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_create**
> SingleOfProductCreationResult product_create(body, ignore_stock=ignore_stock, ignore_price=ignore_price)

Updates or creates products

Updates or creates products. The endpoint is purge and replace.<br />If you do not include an attribute, it is overwritten with null.<br />Extra data arrays are not effected by purge and replace, and remain unchanged.<br />To exclude stock from the update, set the **Ignore stock** attribute to **true**.<br />To exclude price from the update, set the **Ignore price** attribute to **true**.<br /><br />**NB:** the **Merchant product number** must be unique.

### Example
```python
from __future__ import print_function
import time
import channelengine_client
from channelengine_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = channelengine_client.Configuration()
configuration.api_key['apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# create an instance of the API class
api_instance = channelengine_client.ProductsApi(channelengine_client.ApiClient(configuration))
body = [channelengine_client.MerchantProductRequest()] # list[MerchantProductRequest] | 
ignore_stock = false # bool |  (optional) (default to false)
ignore_price = false # bool |  (optional) (default to false)

try:
    # Updates or creates products
    api_response = api_instance.product_create(body, ignore_stock=ignore_stock, ignore_price=ignore_price)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->product_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[MerchantProductRequest]**](MerchantProductRequest.md)|  | 
 **ignore_stock** | **bool**|  | [optional] [default to false]
 **ignore_price** | **bool**|  | [optional] [default to false]

### Return type

[**SingleOfProductCreationResult**](SingleOfProductCreationResult.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_delete**
> ApiResponse product_delete(merchant_product_no)

Deletes a product

Deletes a product based on the **Merchant product number**.<br /> <br />**NB:** ChannelEngine deactivates but does not delete the product entirely, as it might be still referenced in orders.<br />Therefore, the references used for this product cannot be reused.

### Example
```python
from __future__ import print_function
import time
import channelengine_client
from channelengine_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = channelengine_client.Configuration()
configuration.api_key['apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# create an instance of the API class
api_instance = channelengine_client.ProductsApi(channelengine_client.ApiClient(configuration))
merchant_product_no = 'merchant_product_no_example' # str | The MerchantProductNo of the product you wish to delete.

try:
    # Deletes a product
    api_response = api_instance.product_delete(merchant_product_no)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->product_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_product_no** | **str**| The MerchantProductNo of the product you wish to delete. | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_freeze**
> SingleOfApiResponse product_freeze(body=body)

Updates selected products and sets them either to frozen or not-frozen status.

Changes state of products by updating it with FREEZE or UNFREEZE state.<br />All fields are required.

### Example
```python
from __future__ import print_function
import time
import channelengine_client
from channelengine_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = channelengine_client.Configuration()
configuration.api_key['apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# create an instance of the API class
api_instance = channelengine_client.ProductsApi(channelengine_client.ApiClient(configuration))
body = [channelengine_client.FreezeProductRequest()] # list[FreezeProductRequest] |  (optional)

try:
    # Updates selected products and sets them either to frozen or not-frozen status.
    api_response = api_instance.product_freeze(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->product_freeze: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[FreezeProductRequest]**](FreezeProductRequest.md)|  | [optional] 

### Return type

[**SingleOfApiResponse**](SingleOfApiResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_get_by_filter**
> CollectionOfMerchantProductResponse product_get_by_filter(search=search, ean_list=ean_list, merchant_product_no_list=merchant_product_no_list, page=page)

Gets products

Retrieve all products. Apply available filters to narrow down your search.

### Example
```python
from __future__ import print_function
import time
import channelengine_client
from channelengine_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = channelengine_client.Configuration()
configuration.api_key['apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# create an instance of the API class
api_instance = channelengine_client.ProductsApi(channelengine_client.ApiClient(configuration))
search = 'search_example' # str | Search product(s) by Name, MerchantProductNo, Ean or Brand<br />This search is applied to the result after applying the other filters. (optional)
ean_list = ['ean_list_example'] # list[str] | Search products by submitting a list of EAN's. (optional)
merchant_product_no_list = ['merchant_product_no_list_example'] # list[str] | Search products by submitting a list of MerchantProductNo's. (optional)
page = 56 # int | The page to filter on. Starts at 1. (optional)

try:
    # Gets products
    api_response = api_instance.product_get_by_filter(search=search, ean_list=ean_list, merchant_product_no_list=merchant_product_no_list, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->product_get_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Search product(s) by Name, MerchantProductNo, Ean or Brand&lt;br /&gt;This search is applied to the result after applying the other filters. | [optional] 
 **ean_list** | [**list[str]**](str.md)| Search products by submitting a list of EAN&#x27;s. | [optional] 
 **merchant_product_no_list** | [**list[str]**](str.md)| Search products by submitting a list of MerchantProductNo&#x27;s. | [optional] 
 **page** | **int**| The page to filter on. Starts at 1. | [optional] 

### Return type

[**CollectionOfMerchantProductResponse**](CollectionOfMerchantProductResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_get_by_merchant_product_no**
> SingleOfMerchantProductResponse product_get_by_merchant_product_no(merchant_product_no)

Gets a product

Retrieves a product based on the **Merchant product number**.

### Example
```python
from __future__ import print_function
import time
import channelengine_client
from channelengine_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = channelengine_client.Configuration()
configuration.api_key['apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# create an instance of the API class
api_instance = channelengine_client.ProductsApi(channelengine_client.ApiClient(configuration))
merchant_product_no = 'merchant_product_no_example' # str | The unique product reference used by the Merchant (sku).

try:
    # Gets a product
    api_response = api_instance.product_get_by_merchant_product_no(merchant_product_no)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->product_get_by_merchant_product_no: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_product_no** | **str**| The unique product reference used by the Merchant (sku). | 

### Return type

[**SingleOfMerchantProductResponse**](SingleOfMerchantProductResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_patch**
> SingleOfProductCreationResult product_patch(merchant_product_no, body=body)

Updates product attributes

Updates specific attributes of a single product based on the **Merchant product number**. The endpoint uses the [JSON Patch](http://jsonpatch.com/).<br /><br />Sample request:<br /><pre><br /> PATCH /v2/products/{merchantProductNo}<br /> {<br /> \"value\": \"Value\",<br /> \"path\": \"Name\",<br /> \"op\": \"replace\"<br /> }<br /></pre><br />Adding ExtraData:<br /><pre><br /> PATCH /v2/products/{merchantProductNo}<br /> {<br /> \"value\": {\"key\": \"Key1\", \"value\": \"value1\"},<br /> \"path\": \"extraData/0\",<br /> \"op\": \"add\"<br /> }<br /></pre><br />Replacing ExtraData (will replace entire ExtraData collection):<br /><pre><br /> PATCH /v2/products/{merchantProductNo}<br /> {<br /> \"value\": [{\"key\": \"Key1\", \"value\": \"value1\"}],<br /> \"path\": \"extraData\",<br /> \"op\": \"replace\"<br /> }<br /></pre><br />Removing all ExtraData:<br /><pre><br /> PATCH /v2/products/{merchantProductNo}<br /> {<br /> \"path\": \"extraData\",<br /> \"op\": \"replace\"<br /> }<br /></pre><br /> Or:<br /><pre><br /> PATCH /v2/products/{merchantProductNo}<br /> {<br /> \"path\": \"extraData\",<br /> \"op\": \"remove\"<br /> }<br /></pre>

### Example
```python
from __future__ import print_function
import time
import channelengine_client
from channelengine_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = channelengine_client.Configuration()
configuration.api_key['apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# create an instance of the API class
api_instance = channelengine_client.ProductsApi(channelengine_client.ApiClient(configuration))
merchant_product_no = 'merchant_product_no_example' # str | The MerchantProductNo of the product you wish to patch
body = [channelengine_client.Operation()] # list[Operation] | The JsonPatchDocument providing the operations you wish to perform on the product. <br /> Value contains the value you wish to set on the property you're updating (used with operations "add" and "replace").<br /> Path contains the path to the property you're updating (e.g. Description). Every property in the model used for creation an updating can be used.<br /> Op contains the operation you wish to perform ("add","replace","remove").<br /> From is only used when using the "move" operation. It refers to the source path of the value to be moved. (optional)

try:
    # Updates product attributes
    api_response = api_instance.product_patch(merchant_product_no, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->product_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_product_no** | **str**| The MerchantProductNo of the product you wish to patch | 
 **body** | [**list[Operation]**](Operation.md)| The JsonPatchDocument providing the operations you wish to perform on the product. &lt;br /&gt; Value contains the value you wish to set on the property you&#x27;re updating (used with operations &quot;add&quot; and &quot;replace&quot;).&lt;br /&gt; Path contains the path to the property you&#x27;re updating (e.g. Description). Every property in the model used for creation an updating can be used.&lt;br /&gt; Op contains the operation you wish to perform (&quot;add&quot;,&quot;replace&quot;,&quot;remove&quot;).&lt;br /&gt; From is only used when using the &quot;move&quot; operation. It refers to the source path of the value to be moved. | [optional] 

### Return type

[**SingleOfProductCreationResult**](SingleOfProductCreationResult.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_patch_extra_data_items**
> SingleOfProductCreationResult product_patch_extra_data_items(body=body)

Adds, updates, or deletes a custom attribute

Adds, updates, or deletes the specific custom attribute (a.k.a. extra data key) for a single product.<br />You can update a single attribute for a product. The format of this endpoint is [JSON Patch](http://jsonpatch.com/).<br /><br />**NB:** the **Merchant product number** must be unique.<br /><br />Sample requests:<br /> <br />Adding ExtraData:<br /><pre><br /> PATCH /v2/products/extra-data<br /> {<br /> \"MerchantProductNo\": \"{merchantProductNo}\",<br /> \"Operations\": [<br /> {<br /> \"Op\": \"add\",<br /> \"Key\": \"{Key}\",<br /> \"Value\": \"{Value}\"<br /> }<br /> ]<br /> }<br /> </pre><br />Updating ExtraData:<br /><pre><br /> PATCH /v2/products/extra-data<br /> {<br /> \"MerchantProductNo\": \"{merchantProductNo}\",<br /> \"Operations\": [<br /> {<br /> \"Op\": \"replace\",<br /> \"Key\": \"{Key}\",<br /> \"Value\": \"{Value}\"<br /> }<br /> ]<br /> }<br /></pre><br />Removing ExtraData with key:<br /><pre><br /> PATCH /v2/products/extra-data<br /> {<br /> \"MerchantProductNo\": \"{merchantProductNo}\",<br /> \"Operations\": [<br /> {<br /> \"Op\": \"remove\",<br /> \"Key\": \"{Key}\",<br /> }<br /> ]<br /> }<br /></pre>

### Example
```python
from __future__ import print_function
import time
import channelengine_client
from channelengine_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = channelengine_client.Configuration()
configuration.api_key['apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# create an instance of the API class
api_instance = channelengine_client.ProductsApi(channelengine_client.ApiClient(configuration))
body = channelengine_client.MerchantProductExtraDataRequest() # MerchantProductExtraDataRequest |  (optional)

try:
    # Adds, updates, or deletes a custom attribute
    api_response = api_instance.product_patch_extra_data_items(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->product_patch_extra_data_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MerchantProductExtraDataRequest**](MerchantProductExtraDataRequest.md)|  | [optional] 

### Return type

[**SingleOfProductCreationResult**](SingleOfProductCreationResult.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

