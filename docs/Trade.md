# Trade

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Our internal ID uniquely identifying this trade | 
**status** | **str** |  | 
**message** | **str** | Message sent with this trade. | 
**initiation_time** | **datetime** | Timestamp the trade was initiated | 
**completion_time** | **datetime** | Timestamp the trade was completed or blank if not yet completed  | 
**tradeoffer_url** | **str** | The URL to the tradeoffer sent to the trade partner. Only set if the trade is in &#x60;in_progress&#x60; state, else absent.  | 
**denial_reason** | **str** | If trade status is &#x60;denied&#x60;, the reason why the trade was denied, else absent.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


