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

class MerchantProductExtraDataItemResponse(object):
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
        'key': 'str',
        'value': 'str',
        'type': 'ExtraDataType',
        'is_public': 'bool',
        'language_iso_code': 'str'
    }

    attribute_map = {
        'key': 'Key',
        'value': 'Value',
        'type': 'Type',
        'is_public': 'IsPublic',
        'language_iso_code': 'LanguageIsoCode'
    }

    def __init__(self, key=None, value=None, type=None, is_public=None, language_iso_code=None):  # noqa: E501
        """MerchantProductExtraDataItemResponse - a model defined in Swagger"""  # noqa: E501
        self._key = None
        self._value = None
        self._type = None
        self._is_public = None
        self._language_iso_code = None
        self.discriminator = None
        self.key = key
        if value is not None:
            self.value = value
        if type is not None:
            self.type = type
        if is_public is not None:
            self.is_public = is_public
        if language_iso_code is not None:
            self.language_iso_code = language_iso_code

    @property
    def key(self):
        """Gets the key of this MerchantProductExtraDataItemResponse.  # noqa: E501

        Name of the extra data field.  # noqa: E501

        :return: The key of this MerchantProductExtraDataItemResponse.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this MerchantProductExtraDataItemResponse.

        Name of the extra data field.  # noqa: E501

        :param key: The key of this MerchantProductExtraDataItemResponse.  # noqa: E501
        :type: str
        """
        if key is None:
            raise ValueError("Invalid value for `key`, must not be `None`")  # noqa: E501

        self._key = key

    @property
    def value(self):
        """Gets the value of this MerchantProductExtraDataItemResponse.  # noqa: E501

        Value of the extra data field.  # noqa: E501

        :return: The value of this MerchantProductExtraDataItemResponse.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this MerchantProductExtraDataItemResponse.

        Value of the extra data field.  # noqa: E501

        :param value: The value of this MerchantProductExtraDataItemResponse.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def type(self):
        """Gets the type of this MerchantProductExtraDataItemResponse.  # noqa: E501


        :return: The type of this MerchantProductExtraDataItemResponse.  # noqa: E501
        :rtype: ExtraDataType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this MerchantProductExtraDataItemResponse.


        :param type: The type of this MerchantProductExtraDataItemResponse.  # noqa: E501
        :type: ExtraDataType
        """

        self._type = type

    @property
    def is_public(self):
        """Gets the is_public of this MerchantProductExtraDataItemResponse.  # noqa: E501

        Add this field to the export of the product feed to the channel.  # noqa: E501

        :return: The is_public of this MerchantProductExtraDataItemResponse.  # noqa: E501
        :rtype: bool
        """
        return self._is_public

    @is_public.setter
    def is_public(self, is_public):
        """Sets the is_public of this MerchantProductExtraDataItemResponse.

        Add this field to the export of the product feed to the channel.  # noqa: E501

        :param is_public: The is_public of this MerchantProductExtraDataItemResponse.  # noqa: E501
        :type: bool
        """

        self._is_public = is_public

    @property
    def language_iso_code(self):
        """Gets the language_iso_code of this MerchantProductExtraDataItemResponse.  # noqa: E501

        The 2-letter ISO code of the extra data  # noqa: E501

        :return: The language_iso_code of this MerchantProductExtraDataItemResponse.  # noqa: E501
        :rtype: str
        """
        return self._language_iso_code

    @language_iso_code.setter
    def language_iso_code(self, language_iso_code):
        """Sets the language_iso_code of this MerchantProductExtraDataItemResponse.

        The 2-letter ISO code of the extra data  # noqa: E501

        :param language_iso_code: The language_iso_code of this MerchantProductExtraDataItemResponse.  # noqa: E501
        :type: str
        """

        self._language_iso_code = language_iso_code

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
        if issubclass(MerchantProductExtraDataItemResponse, dict):
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
        if not isinstance(other, MerchantProductExtraDataItemResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
