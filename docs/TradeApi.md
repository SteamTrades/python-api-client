# steamtrades_api.TradeApi

All URIs are relative to *https://steamtrad.es/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**game_get**](TradeApi.md#game_get) | **GET** /game/ | List supported games
[**game_id_get**](TradeApi.md#game_id_get) | **GET** /game/{id}/ | Info about a game
[**item_mine_get**](TradeApi.md#item_mine_get) | **GET** /item/mine/ | List owned items
[**item_scan_user_inventory_post**](TradeApi.md#item_scan_user_inventory_post) | **POST** /item/scan_user_inventory/ | Scan Steam user inventory
[**item_user_inventory_get**](TradeApi.md#item_user_inventory_get) | **GET** /item/user_inventory/ | Get inventory scan results
[**trade_get**](TradeApi.md#trade_get) | **GET** /trade/ | List your trades
[**trade_id_get**](TradeApi.md#trade_id_get) | **GET** /trade/{id}/ | Get trade status
[**trade_request_items_post**](TradeApi.md#trade_request_items_post) | **POST** /trade/request_items/ | Request items
[**trade_send_items_post**](TradeApi.md#trade_send_items_post) | **POST** /trade/send_items/ | Send items
[**trade_transfer_items_post**](TradeApi.md#trade_transfer_items_post) | **POST** /trade/transfer_items/ | Transfer items
[**user_info_by_steam_id_get**](TradeApi.md#user_info_by_steam_id_get) | **GET** /user/info_by_steam_id/ | Steam user info by Steam ID
[**user_info_by_trade_url_get**](TradeApi.md#user_info_by_trade_url_get) | **GET** /user/info_by_trade_url/ | Steam user info by trade URL


# **game_get**
> list[Game] game_get()

List supported games

Obtains a list of all supported games.

### Example 
```python
from __future__ import print_statement
import time
import steamtrades_api
from steamtrades_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
steamtrades_api.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# steamtrades_api.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = steamtrades_api.TradeApi()

try: 
    # List supported games
    api_response = api_instance.game_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TradeApi->game_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Game]**](Game.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_id_get**
> Game game_id_get(id)

Info about a game

Obtains information about a single supported game.

### Example 
```python
from __future__ import print_statement
import time
import steamtrades_api
from steamtrades_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
steamtrades_api.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# steamtrades_api.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = steamtrades_api.TradeApi()
id = 'id_example' # str | Game ID (e.g. 730 for CS:GO).

try: 
    # Info about a game
    api_response = api_instance.game_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TradeApi->game_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Game ID (e.g. 730 for CS:GO). | 

### Return type

[**Game**](Game.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **item_mine_get**
> InlineResponse200 item_mine_get(context_id=context_id, offset=offset, limit=limit)

List owned items

Queries the list of items owned by you.

### Example 
```python
from __future__ import print_statement
import time
import steamtrades_api
from steamtrades_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
steamtrades_api.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# steamtrades_api.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = steamtrades_api.TradeApi()
context_id = 'context_id_example' # str | Inventory context ID for filtering. (optional)
offset = 0 # int | Offset to start listing (optional) (default to 0)
limit = 250 # int | Number of trades to retrieve (optional) (default to 250)

try: 
    # List owned items
    api_response = api_instance.item_mine_get(context_id=context_id, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TradeApi->item_mine_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **context_id** | **str**| Inventory context ID for filtering. | [optional] 
 **offset** | **int**| Offset to start listing | [optional] [default to 0]
 **limit** | **int**| Number of trades to retrieve | [optional] [default to 250]

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **item_scan_user_inventory_post**
> InlineResponse2001 item_scan_user_inventory_post(trade_url, context_id, force_refresh=force_refresh)

Scan Steam user inventory

Queries information about the inventory scan state of a Steam user. If no scan is in progress and if there are no previous scans or all previous scans are invalid, a new scan is queued. Scans are considered invalid if they are outdated, if `force_refresh` was passed or is they simply do not exist, yet. 

### Example 
```python
from __future__ import print_statement
import time
import steamtrades_api
from steamtrades_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
steamtrades_api.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# steamtrades_api.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = steamtrades_api.TradeApi()
trade_url = 'trade_url_example' # str | Trade URL of the target user.
context_id = 'context_id_example' # str | Inventory context ID to retrieve items for.
force_refresh = true # bool | Do not use cached info (if exists), force rescan. (optional)

try: 
    # Scan Steam user inventory
    api_response = api_instance.item_scan_user_inventory_post(trade_url, context_id, force_refresh=force_refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TradeApi->item_scan_user_inventory_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trade_url** | **str**| Trade URL of the target user. | 
 **context_id** | **str**| Inventory context ID to retrieve items for. | 
 **force_refresh** | **bool**| Do not use cached info (if exists), force rescan. | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **item_user_inventory_get**
> list[ScannedItem] item_user_inventory_get(trade_url, context_id)

Get inventory scan results

Queries the cached list of items owned by a Steam user.

### Example 
```python
from __future__ import print_statement
import time
import steamtrades_api
from steamtrades_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
steamtrades_api.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# steamtrades_api.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = steamtrades_api.TradeApi()
trade_url = 'trade_url_example' # str | Trade URL of the target user.
context_id = 'context_id_example' # str | Inventory context ID to retrieve items for.

try: 
    # Get inventory scan results
    api_response = api_instance.item_user_inventory_get(trade_url, context_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TradeApi->item_user_inventory_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trade_url** | **str**| Trade URL of the target user. | 
 **context_id** | **str**| Inventory context ID to retrieve items for. | 

### Return type

[**list[ScannedItem]**](ScannedItem.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trade_get**
> InlineResponse2002 trade_get(filter_ids=filter_ids, offset=offset, limit=limit)

List your trades

Queries a list of your trades, oldest trades first.

### Example 
```python
from __future__ import print_statement
import time
import steamtrades_api
from steamtrades_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
steamtrades_api.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# steamtrades_api.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = steamtrades_api.TradeApi()
filter_ids = ['filter_ids_example'] # list[str] | If passed, returns only trades with given IDs (optional)
offset = 0 # int | Offset to start listing (optional) (default to 0)
limit = 250 # int | Number of trades to retrieve (optional) (default to 250)

try: 
    # List your trades
    api_response = api_instance.trade_get(filter_ids=filter_ids, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TradeApi->trade_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_ids** | [**list[str]**](str.md)| If passed, returns only trades with given IDs | [optional] 
 **offset** | **int**| Offset to start listing | [optional] [default to 0]
 **limit** | **int**| Number of trades to retrieve | [optional] [default to 250]

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trade_id_get**
> Trade trade_id_get(id)

Get trade status

Queries the status of a previously initiated trade.

### Example 
```python
from __future__ import print_statement
import time
import steamtrades_api
from steamtrades_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
steamtrades_api.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# steamtrades_api.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = steamtrades_api.TradeApi()
id = 'id_example' # str | Trade ID to query information for.

try: 
    # Get trade status
    api_response = api_instance.trade_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TradeApi->trade_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Trade ID to query information for. | 

### Return type

[**Trade**](Trade.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trade_request_items_post**
> InlineResponse2003 trade_request_items_post(trade_url, context_id, asset_ids, message=message)

Request items

Sends a trade offer to a Steam user requesting items.

### Example 
```python
from __future__ import print_statement
import time
import steamtrades_api
from steamtrades_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
steamtrades_api.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# steamtrades_api.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = steamtrades_api.TradeApi()
trade_url = 'trade_url_example' # str | Trade URL of the user to request items from.
context_id = 'context_id_example' # str | The context ID the asset IDs belong to.
asset_ids = ['asset_ids_example'] # list[str] | Steam asset IDs of the items to request, separated by commas. 
message = 'message_example' # str | Message sent with this trade. You may use `{verify_url}` to define where the trade verification URL is inserted. If `{verify_url}` isn't used, the URL is just appended. You message is limited to 65 characters (excluding URL).  (optional)

try: 
    # Request items
    api_response = api_instance.trade_request_items_post(trade_url, context_id, asset_ids, message=message)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TradeApi->trade_request_items_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trade_url** | **str**| Trade URL of the user to request items from. | 
 **context_id** | **str**| The context ID the asset IDs belong to. | 
 **asset_ids** | [**list[str]**](str.md)| Steam asset IDs of the items to request, separated by commas.  | 
 **message** | **str**| Message sent with this trade. You may use &#x60;{verify_url}&#x60; to define where the trade verification URL is inserted. If &#x60;{verify_url}&#x60; isn&#39;t used, the URL is just appended. You message is limited to 65 characters (excluding URL).  | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trade_send_items_post**
> InlineResponse2005 trade_send_items_post(trade_url, items, message=message)

Send items

Sends a trade offer to a Steam user offering a list of your items.

### Example 
```python
from __future__ import print_statement
import time
import steamtrades_api
from steamtrades_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
steamtrades_api.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# steamtrades_api.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = steamtrades_api.TradeApi()
trade_url = 'trade_url_example' # str | Trade URL of the user to send items to.
items = ['items_example'] # list[str] | IDs of the items to send, separated by commas. 
message = 'message_example' # str | Message sent with this trade. You may use `{verify_url}` to define where the trade verification URL is inserted. If `{verify_url}` isn't used, the URL is just appended. You message is limited to 65 characters (excluding URL).  (optional)

try: 
    # Send items
    api_response = api_instance.trade_send_items_post(trade_url, items, message=message)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TradeApi->trade_send_items_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trade_url** | **str**| Trade URL of the user to send items to. | 
 **items** | [**list[str]**](str.md)| IDs of the items to send, separated by commas.  | 
 **message** | **str**| Message sent with this trade. You may use &#x60;{verify_url}&#x60; to define where the trade verification URL is inserted. If &#x60;{verify_url}&#x60; isn&#39;t used, the URL is just appended. You message is limited to 65 characters (excluding URL).  | [optional] 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trade_transfer_items_post**
> InlineResponse2004 trade_transfer_items_post(items, dst_app_id, allow_foreign_dst=allow_foreign_dst, move_physically=move_physically)

Transfer items

Transfers items from this app to another (SteamTrades internal transfer). Other than trades with Steam users, these \"trades\" are performed instantly and no actual trade object is created unless when you using `move_physically`, which, when required, creates a regular trade. 

### Example 
```python
from __future__ import print_statement
import time
import steamtrades_api
from steamtrades_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
steamtrades_api.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# steamtrades_api.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = steamtrades_api.TradeApi()
items = ['items_example'] # list[str] | IDs of the items to transfer, separated by commas. 
dst_app_id = 56 # int | ID of the app receiving the items.
allow_foreign_dst = false # bool | Whether to allow transfer to apps of other users. (optional) (default to false)
move_physically = false # bool | Whether to physically move the item to bots of the destination app (in case either the source or destination app, or both, have dedicated bots). Items are only moved phisically if this is required because source and destination app have different storage locations. All items that are in the physical trade (and thus not moved instantly) are listed in `items_in_trade`.  (optional) (default to false)

try: 
    # Transfer items
    api_response = api_instance.trade_transfer_items_post(items, dst_app_id, allow_foreign_dst=allow_foreign_dst, move_physically=move_physically)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TradeApi->trade_transfer_items_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **items** | [**list[str]**](str.md)| IDs of the items to transfer, separated by commas.  | 
 **dst_app_id** | **int**| ID of the app receiving the items. | 
 **allow_foreign_dst** | **bool**| Whether to allow transfer to apps of other users. | [optional] [default to false]
 **move_physically** | **bool**| Whether to physically move the item to bots of the destination app (in case either the source or destination app, or both, have dedicated bots). Items are only moved phisically if this is required because source and destination app have different storage locations. All items that are in the physical trade (and thus not moved instantly) are listed in &#x60;items_in_trade&#x60;.  | [optional] [default to false]

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_info_by_steam_id_get**
> UserInfo user_info_by_steam_id_get(steam_id, force_refresh=force_refresh)

Steam user info by Steam ID

Queries information about a Steam user, by its Steam ID.

### Example 
```python
from __future__ import print_statement
import time
import steamtrades_api
from steamtrades_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
steamtrades_api.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# steamtrades_api.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = steamtrades_api.TradeApi()
steam_id = 'steam_id_example' # str | Steam ID (64-bit) of the target user.
force_refresh = true # bool | Don't use cached results, force refresh. Defaults to `false`. (optional)

try: 
    # Steam user info by Steam ID
    api_response = api_instance.user_info_by_steam_id_get(steam_id, force_refresh=force_refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TradeApi->user_info_by_steam_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **steam_id** | **str**| Steam ID (64-bit) of the target user. | 
 **force_refresh** | **bool**| Don&#39;t use cached results, force refresh. Defaults to &#x60;false&#x60;. | [optional] 

### Return type

[**UserInfo**](UserInfo.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_info_by_trade_url_get**
> UserInfo user_info_by_trade_url_get(trade_url, force_refresh=force_refresh)

Steam user info by trade URL

Queries information about a Steam user, by its trade URL.

### Example 
```python
from __future__ import print_statement
import time
import steamtrades_api
from steamtrades_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
steamtrades_api.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# steamtrades_api.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = steamtrades_api.TradeApi()
trade_url = 'trade_url_example' # str | Trade URL of the target user.
force_refresh = true # bool | Don't use cached results, force refresh. Defaults to `false`. (optional)

try: 
    # Steam user info by trade URL
    api_response = api_instance.user_info_by_trade_url_get(trade_url, force_refresh=force_refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TradeApi->user_info_by_trade_url_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trade_url** | **str**| Trade URL of the target user. | 
 **force_refresh** | **bool**| Don&#39;t use cached results, force refresh. Defaults to &#x60;false&#x60;. | [optional] 

### Return type

[**UserInfo**](UserInfo.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

