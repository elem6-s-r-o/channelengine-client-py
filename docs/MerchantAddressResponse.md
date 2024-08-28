# MerchantAddressResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line1** | **str** | The first address line, use this field if address validation is disabled in ChannelEngine. | [optional] 
**line2** | **str** | The second address line, use this field if address validation is disabled in ChannelEngine. | [optional] 
**line3** | **str** | The third address line, use this field if address validation is disabled in ChannelEngine. | [optional] 
**gender** | [**Gender**](Gender.md) |  | [optional] 
**company_name** | **str** | Optional. Company addressed too. | [optional] 
**first_name** | **str** | The first name of the customer. | [optional] 
**last_name** | **str** | The last name of the customer (includes the surname prefix [tussenvoegsel] like &#x27;de&#x27;, &#x27;van&#x27;, &#x27;du&#x27;). | [optional] 
**street_name** | **str** | The name of the street (without house number information)  This field might be empty if address validation is disabled in ChannelEngine. | [optional] 
**house_nr** | **str** | The house number  This field might be empty if address validation is disabled in ChannelEngine. | [optional] 
**house_nr_addition** | **str** | Optional. Addition to the house number  If the address is: Groenhazengracht 2c, the address will be:  StreetName: Groenhazengracht  HouseNo: 2  HouseNrAddition: c  This field might be empty if address validation is disabled in ChannelEngine. | [optional] 
**zip_code** | **str** | The zip or postal code. | [optional] 
**city** | **str** | The name of the city. | [optional] 
**region** | **str** | Optional. State/province/region. | [optional] 
**country_iso** | **str** | For example: NL, BE, FR. | [optional] 
**original** | **str** | Optional. The address as a single string: use in case the address lines are entered  as single lines and later parsed into street, house number and house number addition. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

