# QueriKornerOpenApi30.UserApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**changeUser**](UserApi.md#changeUser) | **PUT** /user/{userId} | Change data of user
[**createUser**](UserApi.md#createUser) | **POST** /user | Create user
[**deleteUser**](UserApi.md#deleteUser) | **DELETE** /user/{userId} | Delete an user
[**getUserData**](UserApi.md#getUserData) | **GET** /user/{userId} | Get user data
[**loginUser**](UserApi.md#loginUser) | **GET** /user/login | Login user
[**logoutUser**](UserApi.md#logoutUser) | **GET** /user/logout | Logout user
[**signUpUser**](UserApi.md#signUpUser) | **POST** /user/signup | Create user

<a name="changeUser"></a>
# **changeUser**
> User changeUser(opts)

Change data of user

Change data of user

### Example
```javascript
import {QueriKornerOpenApi30} from 'queri_korner___open_api_30';
let defaultClient = QueriKornerOpenApi30.ApiClient.instance;

// Configure OAuth2 access token for authorization: ask_auth
let ask_auth = defaultClient.authentications['ask_auth'];
ask_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new QueriKornerOpenApi30.UserApi();
let opts = { 
  'userId': "userId_example" // String | User id
};
apiInstance.changeUser(opts, (error, data, response) => {
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
 **userId** | **String**| User id | [optional] 

### Return type

[**User**](User.md)

### Authorization

[ask_auth](../README.md#ask_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

<a name="createUser"></a>
# **createUser**
> User createUser(body)

Create user

Create user

### Example
```javascript
import {QueriKornerOpenApi30} from 'queri_korner___open_api_30';
let defaultClient = QueriKornerOpenApi30.ApiClient.instance;

// Configure OAuth2 access token for authorization: ask_auth
let ask_auth = defaultClient.authentications['ask_auth'];
ask_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new QueriKornerOpenApi30.UserApi();
let body = new QueriKornerOpenApi30.User(); // User | User to be added to the database

apiInstance.createUser(body, (error, data, response) => {
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
 **body** | [**User**](User.md)| User to be added to the database | 

### Return type

[**User**](User.md)

### Authorization

[ask_auth](../README.md#ask_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

<a name="deleteUser"></a>
# **deleteUser**
> User deleteUser(opts)

Delete an user

Delete an user

### Example
```javascript
import {QueriKornerOpenApi30} from 'queri_korner___open_api_30';
let defaultClient = QueriKornerOpenApi30.ApiClient.instance;

// Configure OAuth2 access token for authorization: ask_auth
let ask_auth = defaultClient.authentications['ask_auth'];
ask_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new QueriKornerOpenApi30.UserApi();
let opts = { 
  'userId': "userId_example" // String | User id
};
apiInstance.deleteUser(opts, (error, data, response) => {
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
 **userId** | **String**| User id | [optional] 

### Return type

[**User**](User.md)

### Authorization

[ask_auth](../README.md#ask_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

<a name="getUserData"></a>
# **getUserData**
> User getUserData(opts)

Get user data

Get user data

### Example
```javascript
import {QueriKornerOpenApi30} from 'queri_korner___open_api_30';
let defaultClient = QueriKornerOpenApi30.ApiClient.instance;

// Configure OAuth2 access token for authorization: ask_auth
let ask_auth = defaultClient.authentications['ask_auth'];
ask_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new QueriKornerOpenApi30.UserApi();
let opts = { 
  'userId': "userId_example" // String | User id
};
apiInstance.getUserData(opts, (error, data, response) => {
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
 **userId** | **String**| User id | [optional] 

### Return type

[**User**](User.md)

### Authorization

[ask_auth](../README.md#ask_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

<a name="loginUser"></a>
# **loginUser**
> User loginUser(opts)

Login user

Login user

### Example
```javascript
import {QueriKornerOpenApi30} from 'queri_korner___open_api_30';
let defaultClient = QueriKornerOpenApi30.ApiClient.instance;

// Configure OAuth2 access token for authorization: ask_auth
let ask_auth = defaultClient.authentications['ask_auth'];
ask_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new QueriKornerOpenApi30.UserApi();
let opts = { 
  'username': "username_example", // String | Username
  'password': "password_example" // String | Password
};
apiInstance.loginUser(opts, (error, data, response) => {
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
 **username** | **String**| Username | [optional] 
 **password** | **String**| Password | [optional] 

### Return type

[**User**](User.md)

### Authorization

[ask_auth](../README.md#ask_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

<a name="logoutUser"></a>
# **logoutUser**
> User logoutUser()

Logout user

Logout user

### Example
```javascript
import {QueriKornerOpenApi30} from 'queri_korner___open_api_30';
let defaultClient = QueriKornerOpenApi30.ApiClient.instance;

// Configure OAuth2 access token for authorization: ask_auth
let ask_auth = defaultClient.authentications['ask_auth'];
ask_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new QueriKornerOpenApi30.UserApi();
apiInstance.logoutUser((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**User**](User.md)

### Authorization

[ask_auth](../README.md#ask_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

<a name="signUpUser"></a>
# **signUpUser**
> User signUpUser(body, opts)

Create user

Create user

### Example
```javascript
import {QueriKornerOpenApi30} from 'queri_korner___open_api_30';
let defaultClient = QueriKornerOpenApi30.ApiClient.instance;

// Configure OAuth2 access token for authorization: ask_auth
let ask_auth = defaultClient.authentications['ask_auth'];
ask_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new QueriKornerOpenApi30.UserApi();
let body = new QueriKornerOpenApi30.User(); // User | User to be added to the database
let opts = { 
  'username': "username_example", // String | 
  'email': "email_example", // String | 
  'password': "password_example" // String | 
};
apiInstance.signUpUser(body, opts, (error, data, response) => {
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
 **body** | [**User**](User.md)| User to be added to the database | 
 **username** | **String**|  | [optional] 
 **email** | **String**|  | [optional] 
 **password** | **String**|  | [optional] 

### Return type

[**User**](User.md)

### Authorization

[ask_auth](../README.md#ask_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

