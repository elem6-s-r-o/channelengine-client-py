# coding: utf-8

"""
    ChannelEngine Merchant API

    ChannelEngine API for merchants  # noqa: E501

    OpenAPI spec version: 2.17.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class MerchantHandleReturn(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'return_identifier': 'str',
        'return_line_identifier': 'str',
        'quantity': 'int',
        'action': 'ReturnHandlingAction'
    }

    attribute_map = {
        'return_identifier': 'ReturnIdentifier',
        'return_line_identifier': 'ReturnLineIdentifier',
        'quantity': 'Quantity',
        'action': 'Action'
    }

    def __init__(self, return_identifier=None, return_line_identifier=None, quantity=None, action=None):  # noqa: E501
        """MerchantHandleReturn - a model defined in Swagger"""  # noqa: E501
        self._return_identifier = None
        self._return_line_identifier = None
        self._quantity = None
        self._action = None
        self.discriminator = None
        if return_identifier is not None:
            self.return_identifier = return_identifier
        if return_line_identifier is not None:
            self.return_line_identifier = return_line_identifier
        if quantity is not None:
            self.quantity = quantity
        if action is not None:
            self.action = action

    @property
    def return_identifier(self):
        """Gets the return_identifier of this MerchantHandleReturn.  # noqa: E501


        :return: The return_identifier of this MerchantHandleReturn.  # noqa: E501
        :rtype: str
        """
        return self._return_identifier

    @return_identifier.setter
    def return_identifier(self, return_identifier):
        """Sets the return_identifier of this MerchantHandleReturn.


        :param return_identifier: The return_identifier of this MerchantHandleReturn.  # noqa: E501
        :type: str
        """

        self._return_identifier = return_identifier

    @property
    def return_line_identifier(self):
        """Gets the return_line_identifier of this MerchantHandleReturn.  # noqa: E501


        :return: The return_line_identifier of this MerchantHandleReturn.  # noqa: E501
        :rtype: str
        """
        return self._return_line_identifier

    @return_line_identifier.setter
    def return_line_identifier(self, return_line_identifier):
        """Sets the return_line_identifier of this MerchantHandleReturn.


        :param return_line_identifier: The return_line_identifier of this MerchantHandleReturn.  # noqa: E501
        :type: str
        """

        self._return_line_identifier = return_line_identifier

    @property
    def quantity(self):
        """Gets the quantity of this MerchantHandleReturn.  # noqa: E501


        :return: The quantity of this MerchantHandleReturn.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this MerchantHandleReturn.


        :param quantity: The quantity of this MerchantHandleReturn.  # noqa: E501
        :type: int
        """

        self._quantity = quantity

    @property
    def action(self):
        """Gets the action of this MerchantHandleReturn.  # noqa: E501


        :return: The action of this MerchantHandleReturn.  # noqa: E501
        :rtype: ReturnHandlingAction
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this MerchantHandleReturn.


        :param action: The action of this MerchantHandleReturn.  # noqa: E501
        :type: ReturnHandlingAction
        """

        self._action = action

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(MerchantHandleReturn, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MerchantHandleReturn):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
