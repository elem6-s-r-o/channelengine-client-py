# channelengine_client.ReportsApi

All URIs are relative to *https://demo.channelengine.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**report_create_settlements_report**](ReportsApi.md#report_create_settlements_report) | **POST** /v2/reports/settlements | Creates a settlement report
[**report_get_report**](ReportsApi.md#report_get_report) | **GET** /v2/reports/{reportId} | Gets a settlement report
[**report_get_status**](ReportsApi.md#report_get_status) | **GET** /v2/reports/{reportId}/status | Gets the status of a settlement report

# **report_create_settlements_report**
> MerchantCreateReportResponse report_create_settlements_report(body)

Creates a settlement report

Creates a settlement report based on the **Settlement ID** provided. There are 2 types of reports:<br />**DETAILED** - a detailed report containing all transactions.<br />**CUSTOM_JSON** - a report grouped by orders, you can name the csv columns with a JSON file. This JSON file should be defined<br />in the settlement export plugin.<br /> <br />All the settlements are automatically acknowledged if that was not already the case.<br />**NB:** depending on the number of transactions within the settlement, it can take a few minutes for the report to be generated.

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
api_instance = channelengine_client.ReportsApi(channelengine_client.ApiClient(configuration))
body = channelengine_client.MerchantCreateSettlementsReportRequest() # MerchantCreateSettlementsReportRequest | To provide settlementIds and type of report DETAILED or CUSTOM_JSON.

try:
    # Creates a settlement report
    api_response = api_instance.report_create_settlements_report(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->report_create_settlements_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MerchantCreateSettlementsReportRequest**](MerchantCreateSettlementsReportRequest.md)| To provide settlementIds and type of report DETAILED or CUSTOM_JSON. | 

### Return type

[**MerchantCreateReportResponse**](MerchantCreateReportResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **report_get_report**
> file report_get_report(report_id)

Gets a settlement report

Gets a settlement report based on the **Report ID** provided. The generated report is a CSV file with a semicolon (;) as a delimiter.<br />If a field has a comma (,) then it is enclosed in quotes (\"\").

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
api_instance = channelengine_client.ReportsApi(channelengine_client.ApiClient(configuration))
report_id = 'report_id_example' # str | 

try:
    # Gets a settlement report
    api_response = api_instance.report_get_report(report_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->report_get_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_id** | **str**|  | 

### Return type

[**file**](file.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **report_get_status**
> MerchantGetReportStatusResponse report_get_status(report_id)

Gets the status of a settlement report

Returns a report status based on the **Report ID** provided. There are four statuses:<br />**IN_PROGRESS** - the report is still being created.<br />**DONE** - the report has been created.<br />**FAILED** - the report creation failed.<br />**NOT_FOUND** - the Report ID was not found.<br /> <br />**NB:** if the status is **DONE**, the response contains a URL with a download path.

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
api_instance = channelengine_client.ReportsApi(channelengine_client.ApiClient(configuration))
report_id = 'report_id_example' # str | 

try:
    # Gets the status of a settlement report
    api_response = api_instance.report_get_status(report_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->report_get_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_id** | **str**|  | 

### Return type

[**MerchantGetReportStatusResponse**](MerchantGetReportStatusResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

