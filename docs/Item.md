# Item

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Our item ID used to identify the item on all of our API endpoints | 
**asset_id** | **str** | Current Steam asset ID of this item. Changes in trades. | 
**category** | [**ItemCategory**](ItemCategory.md) | Item category this item belongs to | 
**locked** | **bool** | &#x60;true&#x60; if the item is locked, else &#x60;false&#x60;  | 
**lock_reason** | **str** | &#x60;active_trade&#x60; is encountered when the item is currently subject of an active trade. The kind of circumstances required to cause an &#x60;admin&#x60; lock are extremely rare and notifications are sent to our staff. If an item is admin-locked for a longer duration, please contact our support. &#x60;disabled_bot&#x60; may occurr if there are temporary problems with the bot holding the item.  | 
**steam_class_id** | **str** | Steam item class ID | 
**steam_instance_id** | **str** | Steam item instance ID | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


