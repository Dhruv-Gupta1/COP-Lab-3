# QueriKornerOpenApi30.SearchApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**searchTags**](SearchApi.md#searchTags) | **GET** /search/tags | Search tags
[**sortQuestions**](SearchApi.md#sortQuestions) | **GET** /search/{sortId} | Sort questions

<a name="searchTags"></a>
# **searchTags**
> Search searchTags(opts)

Search tags

Search tags

### Example
```javascript
import {QueriKornerOpenApi30} from 'queri_korner___open_api_30';
let defaultClient = QueriKornerOpenApi30.ApiClient.instance;

// Configure OAuth2 access token for authorization: ask_auth
let ask_auth = defaultClient.authentications['ask_auth'];
ask_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new QueriKornerOpenApi30.SearchApi();
let opts = { 
  'tags': ["tags_example"] // [String] | Tags to search
};
apiInstance.searchTags(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tags** | [**[String]**](String.md)| Tags to search | [optional] 

### Return type

[**Search**](Search.md)

### Authorization

[ask_auth](../README.md#ask_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

<a name="sortQuestions"></a>
# **sortQuestions**
> Search sortQuestions(opts)

Sort questions

Sort questions

### Example
```javascript
import {QueriKornerOpenApi30} from 'queri_korner___open_api_30';
let defaultClient = QueriKornerOpenApi30.ApiClient.instance;

// Configure OAuth2 access token for authorization: ask_auth
let ask_auth = defaultClient.authentications['ask_auth'];
ask_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new QueriKornerOpenApi30.SearchApi();
let opts = { 
  'sortId': "sortId_example" // String | Sort id
};
apiInstance.sortQuestions(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortId** | **String**| Sort id | [optional] 

### Return type

[**Search**](Search.md)

### Authorization

[ask_auth](../README.md#ask_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

