# swagger_client.DefaultApi

All URIs are relative to *http://api.giphy.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**gifs_categories_category_get**](DefaultApi.md#gifs_categories_category_get) | **GET** /gifs/categories/{category} | Category Tags Endpoint.
[**gifs_categories_category_tag_get**](DefaultApi.md#gifs_categories_category_tag_get) | **GET** /gifs/categories/{category}/{tag} | Tagged Gifs Endpoint.
[**gifs_categories_get**](DefaultApi.md#gifs_categories_get) | **GET** /gifs/categories | Categories Endpoint.
[**gifs_get**](DefaultApi.md#gifs_get) | **GET** /gifs | Get GIFs by ID Endpoint
[**gifs_gif_id_get**](DefaultApi.md#gifs_gif_id_get) | **GET** /gifs/{gif_id} | Get GIF by ID Endpoint
[**gifs_random_get**](DefaultApi.md#gifs_random_get) | **GET** /gifs/random | Random Endpoint
[**gifs_search_get**](DefaultApi.md#gifs_search_get) | **GET** /gifs/search | Search Endpoint
[**gifs_translate_get**](DefaultApi.md#gifs_translate_get) | **GET** /gifs/translate | Translate Endpoint
[**gifs_trending_get**](DefaultApi.md#gifs_trending_get) | **GET** /gifs/trending | Trending GIFs Endpoint
[**stickers_random_get**](DefaultApi.md#stickers_random_get) | **GET** /stickers/random | Random Sticker Endpoint
[**stickers_search_get**](DefaultApi.md#stickers_search_get) | **GET** /stickers/search | Sticker Search Endpoint
[**stickers_translate_get**](DefaultApi.md#stickers_translate_get) | **GET** /stickers/translate | Sticker Translate Endpoint
[**stickers_trending_get**](DefaultApi.md#stickers_trending_get) | **GET** /stickers/trending | Trending Stickers Endpoint


# **gifs_categories_category_get**
> InlineResponse2004 gifs_categories_category_get(api_key, category, limit=limit, offset=offset)

Category Tags Endpoint.

Returns a list of tags for a given category. NOTE `limit` and `offset` must both be set; otherwise they're ignored.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
api_key = 'dc6zaTOxFJmzC' # str | Giphy API Key.
category = 'category_example' # str | Filters results by category.
limit = 25 # int | The maximum number of records to return. (optional) (default to 25)
offset = 0 # int | An optional results offset. Defaults to 0. (optional) (default to 0)

try: 
    # Category Tags Endpoint.
    api_response = api_instance.gifs_categories_category_get(api_key, category, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->gifs_categories_category_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| Giphy API Key. | 
 **category** | **str**| Filters results by category. | 
 **limit** | **int**| The maximum number of records to return. | [optional] [default to 25]
 **offset** | **int**| An optional results offset. Defaults to 0. | [optional] [default to 0]

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gifs_categories_category_tag_get**
> InlineResponse2005 gifs_categories_category_tag_get(api_key, category, tag, limit=limit, offset=offset)

Tagged Gifs Endpoint.

Returns a list of gifs for a given tag (alias to `/gif/search`).

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
api_key = 'dc6zaTOxFJmzC' # str | Giphy API Key.
category = 'category_example' # str | Filters results by category.
tag = 'tag_example' # str | Filters results by tag.
limit = 25 # int | The maximum number of records to return. (optional) (default to 25)
offset = 0 # int | An optional results offset. Defaults to 0. (optional) (default to 0)

try: 
    # Tagged Gifs Endpoint.
    api_response = api_instance.gifs_categories_category_tag_get(api_key, category, tag, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->gifs_categories_category_tag_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| Giphy API Key. | 
 **category** | **str**| Filters results by category. | 
 **tag** | **str**| Filters results by tag. | 
 **limit** | **int**| The maximum number of records to return. | [optional] [default to 25]
 **offset** | **int**| An optional results offset. Defaults to 0. | [optional] [default to 0]

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gifs_categories_get**
> InlineResponse2003 gifs_categories_get(api_key, limit=limit)

Categories Endpoint.

Returns a list of categories.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
api_key = 'dc6zaTOxFJmzC' # str | Giphy API Key.
limit = 25 # int | The maximum number of records to return. (optional) (default to 25)

try: 
    # Categories Endpoint.
    api_response = api_instance.gifs_categories_get(api_key, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->gifs_categories_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| Giphy API Key. | 
 **limit** | **int**| The maximum number of records to return. | [optional] [default to 25]

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gifs_get**
> InlineResponse200 gifs_get(api_key, ids)

Get GIFs by ID Endpoint

A multiget version of the get GIF by ID endpoint.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
api_key = 'dc6zaTOxFJmzC' # str | Giphy API Key.
ids = 'feqkVgjJpYtjy,7rzbxdu0ZEXLy' # str | Filters results by specified GIF IDs, separated by commas.

try: 
    # Get GIFs by ID Endpoint
    api_response = api_instance.gifs_get(api_key, ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->gifs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| Giphy API Key. | 
 **ids** | **str**| Filters results by specified GIF IDs, separated by commas. | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gifs_gif_id_get**
> InlineResponse2001 gifs_gif_id_get(api_key, gif_id)

Get GIF by ID Endpoint

Returns a GIF given that GIF's unique ID

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
api_key = 'dc6zaTOxFJmzC' # str | Giphy API Key.
gif_id = 'gif_id_example' # str | Filters results by specified GIF ID.

try: 
    # Get GIF by ID Endpoint
    api_response = api_instance.gifs_gif_id_get(api_key, gif_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->gifs_gif_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| Giphy API Key. | 
 **gif_id** | **str**| Filters results by specified GIF ID. | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gifs_random_get**
> InlineResponse2002 gifs_random_get(api_key, tag=tag, rating=rating, fmt=fmt)

Random Endpoint

Returns a random GIF, limited by tag. Excluding the tag parameter will return a random GIF from the GIPHY catalog.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
api_key = 'dc6zaTOxFJmzC' # str | Giphy API Key.
tag = 'burrito' # str | Filters results by specified tag. (optional)
rating = 'g' # str | Filters results by specified rating. (optional)
fmt = 'json' # str | Used to indicate the expected response format. Default is Json. (optional) (default to json)

try: 
    # Random Endpoint
    api_response = api_instance.gifs_random_get(api_key, tag=tag, rating=rating, fmt=fmt)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->gifs_random_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| Giphy API Key. | 
 **tag** | **str**| Filters results by specified tag. | [optional] 
 **rating** | **str**| Filters results by specified rating. | [optional] 
 **fmt** | **str**| Used to indicate the expected response format. Default is Json. | [optional] [default to json]

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gifs_search_get**
> InlineResponse200 gifs_search_get(api_key, q, limit=limit, offset=offset, rating=rating, lang=lang, fmt=fmt)

Search Endpoint

Search all Giphy GIFs for a word or phrase. Punctuation will be stripped and ignored. Use a plus or url encode for phrases. Example paul+rudd, ryan+gosling or american+psycho.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
api_key = 'dc6zaTOxFJmzC' # str | Giphy API Key.
q = 'cheeseburgers' # str | Search query term or prhase.
limit = 25 # int | The maximum number of records to return. (optional) (default to 25)
offset = 0 # int | An optional results offset. Defaults to 0. (optional) (default to 0)
rating = 'g' # str | Filters results by specified rating. (optional)
lang = 'en' # str | Specify default country for regional content; use a 2-letter ISO 639-1 country code. See list of supported languages <a href = \"../language-support\">here</a>. (optional)
fmt = 'json' # str | Used to indicate the expected response format. Default is Json. (optional) (default to json)

try: 
    # Search Endpoint
    api_response = api_instance.gifs_search_get(api_key, q, limit=limit, offset=offset, rating=rating, lang=lang, fmt=fmt)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| Giphy API Key. | 
 **q** | **str**| Search query term or prhase. | 
 **limit** | **int**| The maximum number of records to return. | [optional] [default to 25]
 **offset** | **int**| An optional results offset. Defaults to 0. | [optional] [default to 0]
 **rating** | **str**| Filters results by specified rating. | [optional] 
 **lang** | **str**| Specify default country for regional content; use a 2-letter ISO 639-1 country code. See list of supported languages &lt;a href &#x3D; \&quot;../language-support\&quot;&gt;here&lt;/a&gt;. | [optional] 
 **fmt** | **str**| Used to indicate the expected response format. Default is Json. | [optional] [default to json]

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gifs_translate_get**
> InlineResponse2001 gifs_translate_get(api_key, s)

Translate Endpoint

The translate API draws on search, but uses the Giphy `special sauce` to handle translating from one vocabulary to another. In this case, words and phrases to GIFs.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
api_key = 'dc6zaTOxFJmzC' # str | Giphy API Key.
s = 'ryan gosling' # str | Search term.

try: 
    # Translate Endpoint
    api_response = api_instance.gifs_translate_get(api_key, s)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->gifs_translate_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| Giphy API Key. | 
 **s** | **str**| Search term. | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gifs_trending_get**
> InlineResponse200 gifs_trending_get(api_key, limit=limit, rating=rating, fmt=fmt)

Trending GIFs Endpoint

Fetch GIFs currently trending online. Hand curated by the GIPHY editorial team. The data returned mirrors the GIFs showcased on the <a href = \"http://www.giphy.com\">GIPHY homepage</a>. Returns 25 results by default.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
api_key = 'dc6zaTOxFJmzC' # str | Giphy API Key.
limit = 25 # int | The maximum number of records to return. (optional) (default to 25)
rating = 'g' # str | Filters results by specified rating. (optional)
fmt = 'json' # str | Used to indicate the expected response format. Default is Json. (optional) (default to json)

try: 
    # Trending GIFs Endpoint
    api_response = api_instance.gifs_trending_get(api_key, limit=limit, rating=rating, fmt=fmt)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->gifs_trending_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| Giphy API Key. | 
 **limit** | **int**| The maximum number of records to return. | [optional] [default to 25]
 **rating** | **str**| Filters results by specified rating. | [optional] 
 **fmt** | **str**| Used to indicate the expected response format. Default is Json. | [optional] [default to json]

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stickers_random_get**
> InlineResponse2002 stickers_random_get(api_key, tag=tag, rating=rating, fmt=fmt)

Random Sticker Endpoint

Returns a random GIF, limited by tag. Excluding the tag parameter will return a random GIF from the GIPHY catalog.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
api_key = 'dc6zaTOxFJmzC' # str | Giphy API Key.
tag = 'burrito' # str | Filters results by specified tag. (optional)
rating = 'g' # str | Filters results by specified rating. (optional)
fmt = 'json' # str | Used to indicate the expected response format. Default is Json. (optional) (default to json)

try: 
    # Random Sticker Endpoint
    api_response = api_instance.stickers_random_get(api_key, tag=tag, rating=rating, fmt=fmt)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->stickers_random_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| Giphy API Key. | 
 **tag** | **str**| Filters results by specified tag. | [optional] 
 **rating** | **str**| Filters results by specified rating. | [optional] 
 **fmt** | **str**| Used to indicate the expected response format. Default is Json. | [optional] [default to json]

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stickers_search_get**
> InlineResponse200 stickers_search_get(api_key, q, limit=limit, offset=offset, rating=rating, lang=lang, fmt=fmt)

Sticker Search Endpoint

Replicates the functionality and requirements of the classic GIPHY search, but returns animated stickers rather than GIFs.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
api_key = 'dc6zaTOxFJmzC' # str | Giphy API Key.
q = 'cheeseburgers' # str | Search query term or prhase.
limit = 25 # int | The maximum number of records to return. (optional) (default to 25)
offset = 0 # int | An optional results offset. Defaults to 0. (optional) (default to 0)
rating = 'g' # str | Filters results by specified rating. (optional)
lang = 'en' # str | Specify default country for regional content; use a 2-letter ISO 639-1 country code. See list of supported languages <a href = \"../language-support\">here</a>. (optional)
fmt = 'json' # str | Used to indicate the expected response format. Default is Json. (optional) (default to json)

try: 
    # Sticker Search Endpoint
    api_response = api_instance.stickers_search_get(api_key, q, limit=limit, offset=offset, rating=rating, lang=lang, fmt=fmt)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->stickers_search_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| Giphy API Key. | 
 **q** | **str**| Search query term or prhase. | 
 **limit** | **int**| The maximum number of records to return. | [optional] [default to 25]
 **offset** | **int**| An optional results offset. Defaults to 0. | [optional] [default to 0]
 **rating** | **str**| Filters results by specified rating. | [optional] 
 **lang** | **str**| Specify default country for regional content; use a 2-letter ISO 639-1 country code. See list of supported languages &lt;a href &#x3D; \&quot;../language-support\&quot;&gt;here&lt;/a&gt;. | [optional] 
 **fmt** | **str**| Used to indicate the expected response format. Default is Json. | [optional] [default to json]

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stickers_translate_get**
> InlineResponse2001 stickers_translate_get(api_key, s)

Sticker Translate Endpoint

The translate API draws on search, but uses the Giphy `special sauce` to handle translating from one vocabulary to another. In this case, words and phrases to GIFs.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
api_key = 'dc6zaTOxFJmzC' # str | Giphy API Key.
s = 'ryan gosling' # str | Search term.

try: 
    # Sticker Translate Endpoint
    api_response = api_instance.stickers_translate_get(api_key, s)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->stickers_translate_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| Giphy API Key. | 
 **s** | **str**| Search term. | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stickers_trending_get**
> InlineResponse200 stickers_trending_get(api_key, limit=limit, rating=rating, fmt=fmt)

Trending Stickers Endpoint

Fetch GIFs currently trending online. Hand curated by the GIPHY editorial team. The data returned mirrors the GIFs showcased on the <a href = \"http://www.giphy.com\">GIPHY homepage</a>. Returns 25 results by default.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
api_key = 'dc6zaTOxFJmzC' # str | Giphy API Key.
limit = 25 # int | The maximum number of records to return. (optional) (default to 25)
rating = 'g' # str | Filters results by specified rating. (optional)
fmt = 'json' # str | Used to indicate the expected response format. Default is Json. (optional) (default to json)

try: 
    # Trending Stickers Endpoint
    api_response = api_instance.stickers_trending_get(api_key, limit=limit, rating=rating, fmt=fmt)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->stickers_trending_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| Giphy API Key. | 
 **limit** | **int**| The maximum number of records to return. | [optional] [default to 25]
 **rating** | **str**| Filters results by specified rating. | [optional] 
 **fmt** | **str**| Used to indicate the expected response format. Default is Json. | [optional] [default to json]

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

