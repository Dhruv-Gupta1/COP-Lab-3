# QueriKornerOpenApi30.TagsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createTag**](TagsApi.md#createTag) | **POST** /tags | Create tag
[**deleteTag**](TagsApi.md#deleteTag) | **DELETE** /tags/{tagId} | Delete an tag
[**getTagData**](TagsApi.md#getTagData) | **GET** /tags/{tagId} | Get tag data

<a name="createTag"></a>
# **createTag**
> Tag createTag(body)

Create tag

Create tag

### Example
```javascript
import {QueriKornerOpenApi30} from 'queri_korner___open_api_30';
let defaultClient = QueriKornerOpenApi30.ApiClient.instance;

// Configure OAuth2 access token for authorization: ask_auth
let ask_auth = defaultClient.authentications['ask_auth'];
ask_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new QueriKornerOpenApi30.TagsApi();
let body = new QueriKornerOpenApi30.Tag(); // Tag | Tag to be added to the database

apiInstance.createTag(body, (error, data, response) => {
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
 **body** | [**Tag**](Tag.md)| Tag to be added to the database | 

### Return type

[**Tag**](Tag.md)

### Authorization

[ask_auth](../README.md#ask_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

<a name="deleteTag"></a>
# **deleteTag**
> Tag deleteTag(opts)

Delete an tag

Delete an tag

### Example
```javascript
import {QueriKornerOpenApi30} from 'queri_korner___open_api_30';
let defaultClient = QueriKornerOpenApi30.ApiClient.instance;

// Configure OAuth2 access token for authorization: ask_auth
let ask_auth = defaultClient.authentications['ask_auth'];
ask_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new QueriKornerOpenApi30.TagsApi();
let opts = { 
  'tagId': "tagId_example" // String | Tag id
};
apiInstance.deleteTag(opts, (error, data, response) => {
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
 **tagId** | **String**| Tag id | [optional] 

### Return type

[**Tag**](Tag.md)

### Authorization

[ask_auth](../README.md#ask_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

<a name="getTagData"></a>
# **getTagData**
> Tag getTagData(opts)

Get tag data

Get tag data

### Example
```javascript
import {QueriKornerOpenApi30} from 'queri_korner___open_api_30';
let defaultClient = QueriKornerOpenApi30.ApiClient.instance;

// Configure OAuth2 access token for authorization: ask_auth
let ask_auth = defaultClient.authentications['ask_auth'];
ask_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new QueriKornerOpenApi30.TagsApi();
let opts = { 
  'tagId': "tagId_example" // String | Tag id
};
apiInstance.getTagData(opts, (error, data, response) => {
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
 **tagId** | **String**| Tag id | [optional] 

### Return type

[**Tag**](Tag.md)

### Authorization

[ask_auth](../README.md#ask_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

