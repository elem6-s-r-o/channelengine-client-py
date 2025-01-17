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

class MerchantShipmentPackageDimensionsRequest(object):
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
        'height': 'float',
        'width': 'float',
        'length': 'float',
        'unit': 'PackageDimensionsUnit'
    }

    attribute_map = {
        'height': 'Height',
        'width': 'Width',
        'length': 'Length',
        'unit': 'Unit'
    }

    def __init__(self, height=None, width=None, length=None, unit=None):  # noqa: E501
        """MerchantShipmentPackageDimensionsRequest - a model defined in Swagger"""  # noqa: E501
        self._height = None
        self._width = None
        self._length = None
        self._unit = None
        self.discriminator = None
        if height is not None:
            self.height = height
        if width is not None:
            self.width = width
        if length is not None:
            self.length = length
        if unit is not None:
            self.unit = unit

    @property
    def height(self):
        """Gets the height of this MerchantShipmentPackageDimensionsRequest.  # noqa: E501


        :return: The height of this MerchantShipmentPackageDimensionsRequest.  # noqa: E501
        :rtype: float
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this MerchantShipmentPackageDimensionsRequest.


        :param height: The height of this MerchantShipmentPackageDimensionsRequest.  # noqa: E501
        :type: float
        """

        self._height = height

    @property
    def width(self):
        """Gets the width of this MerchantShipmentPackageDimensionsRequest.  # noqa: E501


        :return: The width of this MerchantShipmentPackageDimensionsRequest.  # noqa: E501
        :rtype: float
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this MerchantShipmentPackageDimensionsRequest.


        :param width: The width of this MerchantShipmentPackageDimensionsRequest.  # noqa: E501
        :type: float
        """

        self._width = width

    @property
    def length(self):
        """Gets the length of this MerchantShipmentPackageDimensionsRequest.  # noqa: E501


        :return: The length of this MerchantShipmentPackageDimensionsRequest.  # noqa: E501
        :rtype: float
        """
        return self._length

    @length.setter
    def length(self, length):
        """Sets the length of this MerchantShipmentPackageDimensionsRequest.


        :param length: The length of this MerchantShipmentPackageDimensionsRequest.  # noqa: E501
        :type: float
        """

        self._length = length

    @property
    def unit(self):
        """Gets the unit of this MerchantShipmentPackageDimensionsRequest.  # noqa: E501


        :return: The unit of this MerchantShipmentPackageDimensionsRequest.  # noqa: E501
        :rtype: PackageDimensionsUnit
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this MerchantShipmentPackageDimensionsRequest.


        :param unit: The unit of this MerchantShipmentPackageDimensionsRequest.  # noqa: E501
        :type: PackageDimensionsUnit
        """

        self._unit = unit

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
        if issubclass(MerchantShipmentPackageDimensionsRequest, dict):
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
        if not isinstance(other, MerchantShipmentPackageDimensionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
