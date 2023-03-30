# QueriKornerOpenApi30.QuestionApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**askQuery**](QuestionApi.md#askQuery) | **POST** /question | Ask your query
[**changeQuestion**](QuestionApi.md#changeQuestion) | **PUT** /question/{questionId} | Change question data
[**deleteQuery**](QuestionApi.md#deleteQuery) | **DELETE** /question/{questionId} | Delete a query
[**getData**](QuestionApi.md#getData) | **GET** /question/{questionId} | Get all query data
[**upvoteQuestion**](QuestionApi.md#upvoteQuestion) | **PUT** /question/votes/{questionId} | Upvote/Downvote a question

<a name="askQuery"></a>
# **askQuery**
> Question askQuery(body)

Ask your query

Ask your query

### Example
```javascript
import {QueriKornerOpenApi30} from 'queri_korner___open_api_30';
let defaultClient = QueriKornerOpenApi30.ApiClient.instance;

// Configure OAuth2 access token for authorization: ask_auth
let ask_auth = defaultClient.authentications['ask_auth'];
ask_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new QueriKornerOpenApi30.QuestionApi();
let body = new QueriKornerOpenApi30.Question(); // Question | Query to be added to the database

apiInstance.askQuery(body, (error, data, response) => {
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
 **body** | [**Question**](Question.md)| Query to be added to the database | 

### Return type

[**Question**](Question.md)

### Authorization

[ask_auth](../README.md#ask_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

<a name="changeQuestion"></a>
# **changeQuestion**
> Question changeQuestion(body, opts)

Change question data

Change question data

### Example
```javascript
import {QueriKornerOpenApi30} from 'queri_korner___open_api_30';
let defaultClient = QueriKornerOpenApi30.ApiClient.instance;

// Configure OAuth2 access token for authorization: ask_auth
let ask_auth = defaultClient.authentications['ask_auth'];
ask_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new QueriKornerOpenApi30.QuestionApi();
let body = new QueriKornerOpenApi30.Question(); // Question | Query to be added to the database
let opts = { 
  'questionId': "questionId_example" // String | Query data
};
apiInstance.changeQuestion(body, opts, (error, data, response) => {
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
 **body** | [**Question**](Question.md)| Query to be added to the database | 
 **questionId** | **String**| Query data | [optional] 

### Return type

[**Question**](Question.md)

### Authorization

[ask_auth](../README.md#ask_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

<a name="deleteQuery"></a>
# **deleteQuery**
> Question deleteQuery(opts)

Delete a query

Delete a query

### Example
```javascript
import {QueriKornerOpenApi30} from 'queri_korner___open_api_30';
let defaultClient = QueriKornerOpenApi30.ApiClient.instance;

// Configure OAuth2 access token for authorization: ask_auth
let ask_auth = defaultClient.authentications['ask_auth'];
ask_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new QueriKornerOpenApi30.QuestionApi();
let opts = { 
  'questionId': "questionId_example" // String | Query data
};
apiInstance.deleteQuery(opts, (error, data, response) => {
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
 **questionId** | **String**| Query data | [optional] 

### Return type

[**Question**](Question.md)

### Authorization

[ask_auth](../README.md#ask_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

<a name="getData"></a>
# **getData**
> Question getData(opts)

Get all query data

Get all query data

### Example
```javascript
import {QueriKornerOpenApi30} from 'queri_korner___open_api_30';
let defaultClient = QueriKornerOpenApi30.ApiClient.instance;

// Configure OAuth2 access token for authorization: ask_auth
let ask_auth = defaultClient.authentications['ask_auth'];
ask_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new QueriKornerOpenApi30.QuestionApi();
let opts = { 
  'questionId': "questionId_example" // String | Query data
};
apiInstance.getData(opts, (error, data, response) => {
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
 **questionId** | **String**| Query data | [optional] 

### Return type

[**Question**](Question.md)

### Authorization

[ask_auth](../README.md#ask_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

<a name="upvoteQuestion"></a>
# **upvoteQuestion**
> Question upvoteQuestion(body, opts)

Upvote/Downvote a question

Upvote/Downvote a question

### Example
```javascript
import {QueriKornerOpenApi30} from 'queri_korner___open_api_30';
let defaultClient = QueriKornerOpenApi30.ApiClient.instance;

// Configure OAuth2 access token for authorization: ask_auth
let ask_auth = defaultClient.authentications['ask_auth'];
ask_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new QueriKornerOpenApi30.QuestionApi();
let body = new QueriKornerOpenApi30.Question(); // Question | Query to be added to the database
let opts = { 
  'questionId': "questionId_example" // String | Question id
};
apiInstance.upvoteQuestion(body, opts, (error, data, response) => {
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
 **body** | [**Question**](Question.md)| Query to be added to the database | 
 **questionId** | **String**| Question id | [optional] 

### Return type

[**Question**](Question.md)

### Authorization

[ask_auth](../README.md#ask_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

