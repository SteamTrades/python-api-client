# coding: utf-8

"""
    SteamTrades API

    API Explorer for SteamTrades' RESTful API.

    OpenAPI spec version: 1.0
    Contact: devs@steamtrad.es
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class InlineResponse2005(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, trade_id=None):
        """
        InlineResponse2005 - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'trade_id': 'str'
        }

        self.attribute_map = {
            'trade_id': 'trade_id'
        }

        self._trade_id = trade_id

    @property
    def trade_id(self):
        """
        Gets the trade_id of this InlineResponse2005.
        ID of the newly created trade

        :return: The trade_id of this InlineResponse2005.
        :rtype: str
        """
        return self._trade_id

    @trade_id.setter
    def trade_id(self, trade_id):
        """
        Sets the trade_id of this InlineResponse2005.
        ID of the newly created trade

        :param trade_id: The trade_id of this InlineResponse2005.
        :type: str
        """
        if trade_id is None:
            raise ValueError("Invalid value for `trade_id`, must not be `None`")

        self._trade_id = trade_id

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, InlineResponse2005):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
