# QueriKornerOpenApi30.AnswerApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**changeAnswer**](AnswerApi.md#changeAnswer) | **PUT** /answer/{answerId} | Change data of answer
[**deleteAnswer**](AnswerApi.md#deleteAnswer) | **DELETE** /answer/{answerId} | Delete an answer
[**getDatafromAnswer**](AnswerApi.md#getDatafromAnswer) | **GET** /answer/{answerId} | Get all answer data
[**postAnswer**](AnswerApi.md#postAnswer) | **POST** /answer/{questionId} | Post your answer
[**upvoteAnswer**](AnswerApi.md#upvoteAnswer) | **PUT** /answer/votes/{answerId} | Upvote/Downvote an answer

<a name="changeAnswer"></a>
# **changeAnswer**
> Answer changeAnswer(opts)

Change data of answer

Change data of answer

### Example
```javascript
import {QueriKornerOpenApi30} from 'queri_korner___open_api_30';
let defaultClient = QueriKornerOpenApi30.ApiClient.instance;

// Configure OAuth2 access token for authorization: ask_auth
let ask_auth = defaultClient.authentications['ask_auth'];
ask_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new QueriKornerOpenApi30.AnswerApi();
let opts = { 
  'answerId': "answerId_example" // String | Answer data
};
apiInstance.changeAnswer(opts, (error, data, response) => {
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
 **answerId** | **String**| Answer data | [optional] 

### Return type

[**Answer**](Answer.md)

### Authorization

[ask_auth](../README.md#ask_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

<a name="deleteAnswer"></a>
# **deleteAnswer**
> Answer deleteAnswer(opts)

Delete an answer

Delete an answer

### Example
```javascript
import {QueriKornerOpenApi30} from 'queri_korner___open_api_30';
let defaultClient = QueriKornerOpenApi30.ApiClient.instance;

// Configure OAuth2 access token for authorization: ask_auth
let ask_auth = defaultClient.authentications['ask_auth'];
ask_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new QueriKornerOpenApi30.AnswerApi();
let opts = { 
  'answerId': "answerId_example" // String | Answer data
};
apiInstance.deleteAnswer(opts, (error, data, response) => {
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
 **answerId** | **String**| Answer data | [optional] 

### Return type

[**Answer**](Answer.md)

### Authorization

[ask_auth](../README.md#ask_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

<a name="getDatafromAnswer"></a>
# **getDatafromAnswer**
> Answer getDatafromAnswer(opts)

Get all answer data

Get all answer data

### Example
```javascript
import {QueriKornerOpenApi30} from 'queri_korner___open_api_30';
let defaultClient = QueriKornerOpenApi30.ApiClient.instance;

// Configure OAuth2 access token for authorization: ask_auth
let ask_auth = defaultClient.authentications['ask_auth'];
ask_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new QueriKornerOpenApi30.AnswerApi();
let opts = { 
  'answerId': "answerId_example" // String | Answer data
};
apiInstance.getDatafromAnswer(opts, (error, data, response) => {
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
 **answerId** | **String**| Answer data | [optional] 

### Return type

[**Answer**](Answer.md)

### Authorization

[ask_auth](../README.md#ask_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

<a name="postAnswer"></a>
# **postAnswer**
> Answer postAnswer(body, opts)

Post your answer

Post your answer

### Example
```javascript
import {QueriKornerOpenApi30} from 'queri_korner___open_api_30';
let defaultClient = QueriKornerOpenApi30.ApiClient.instance;

// Configure OAuth2 access token for authorization: ask_auth
let ask_auth = defaultClient.authentications['ask_auth'];
ask_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new QueriKornerOpenApi30.AnswerApi();
let body = new QueriKornerOpenApi30.Answer(); // Answer | Answer to be added to the database
let opts = { 
  'questionId': "questionId_example" // String | Query data
};
apiInstance.postAnswer(body, opts, (error, data, response) => {
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
 **body** | [**Answer**](Answer.md)| Answer to be added to the database | 
 **questionId** | **String**| Query data | [optional] 

### Return type

[**Answer**](Answer.md)

### Authorization

[ask_auth](../README.md#ask_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

<a name="upvoteAnswer"></a>
# **upvoteAnswer**
> Answer upvoteAnswer(opts)

Upvote/Downvote an answer

Upvote/Downvote an answer

### Example
```javascript
import {QueriKornerOpenApi30} from 'queri_korner___open_api_30';
let defaultClient = QueriKornerOpenApi30.ApiClient.instance;

// Configure OAuth2 access token for authorization: ask_auth
let ask_auth = defaultClient.authentications['ask_auth'];
ask_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new QueriKornerOpenApi30.AnswerApi();
let opts = { 
  'answerId': "answerId_example" // String | Answer id
};
apiInstance.upvoteAnswer(opts, (error, data, response) => {
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
 **answerId** | **String**| Answer id | [optional] 

### Return type

[**Answer**](Answer.md)

### Authorization

[ask_auth](../README.md#ask_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

