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


class InlineResponse423(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, locked_items=None):
        """
        InlineResponse423 - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'locked_items': 'list[str]'
        }

        self.attribute_map = {
            'locked_items': 'locked_items'
        }

        self._locked_items = locked_items

    @property
    def locked_items(self):
        """
        Gets the locked_items of this InlineResponse423.
        List of the locked items, causing this error

        :return: The locked_items of this InlineResponse423.
        :rtype: list[str]
        """
        return self._locked_items

    @locked_items.setter
    def locked_items(self, locked_items):
        """
        Sets the locked_items of this InlineResponse423.
        List of the locked items, causing this error

        :param locked_items: The locked_items of this InlineResponse423.
        :type: list[str]
        """
        if locked_items is None:
            raise ValueError("Invalid value for `locked_items`, must not be `None`")

        self._locked_items = locked_items

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
        if not isinstance(other, InlineResponse423):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other