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

class MerchantProductBundlePartResponse(object):
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
        'merchant_product_no': 'str',
        'ean': 'str',
        'name': 'str',
        'quantity': 'int',
        'price': 'float'
    }

    attribute_map = {
        'merchant_product_no': 'MerchantProductNo',
        'ean': 'Ean',
        'name': 'Name',
        'quantity': 'Quantity',
        'price': 'Price'
    }

    def __init__(self, merchant_product_no=None, ean=None, name=None, quantity=None, price=None):  # noqa: E501
        """MerchantProductBundlePartResponse - a model defined in Swagger"""  # noqa: E501
        self._merchant_product_no = None
        self._ean = None
        self._name = None
        self._quantity = None
        self._price = None
        self.discriminator = None
        if merchant_product_no is not None:
            self.merchant_product_no = merchant_product_no
        if ean is not None:
            self.ean = ean
        if name is not None:
            self.name = name
        if quantity is not None:
            self.quantity = quantity
        if price is not None:
            self.price = price

    @property
    def merchant_product_no(self):
        """Gets the merchant_product_no of this MerchantProductBundlePartResponse.  # noqa: E501


        :return: The merchant_product_no of this MerchantProductBundlePartResponse.  # noqa: E501
        :rtype: str
        """
        return self._merchant_product_no

    @merchant_product_no.setter
    def merchant_product_no(self, merchant_product_no):
        """Sets the merchant_product_no of this MerchantProductBundlePartResponse.


        :param merchant_product_no: The merchant_product_no of this MerchantProductBundlePartResponse.  # noqa: E501
        :type: str
        """

        self._merchant_product_no = merchant_product_no

    @property
    def ean(self):
        """Gets the ean of this MerchantProductBundlePartResponse.  # noqa: E501


        :return: The ean of this MerchantProductBundlePartResponse.  # noqa: E501
        :rtype: str
        """
        return self._ean

    @ean.setter
    def ean(self, ean):
        """Sets the ean of this MerchantProductBundlePartResponse.


        :param ean: The ean of this MerchantProductBundlePartResponse.  # noqa: E501
        :type: str
        """

        self._ean = ean

    @property
    def name(self):
        """Gets the name of this MerchantProductBundlePartResponse.  # noqa: E501


        :return: The name of this MerchantProductBundlePartResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MerchantProductBundlePartResponse.


        :param name: The name of this MerchantProductBundlePartResponse.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def quantity(self):
        """Gets the quantity of this MerchantProductBundlePartResponse.  # noqa: E501


        :return: The quantity of this MerchantProductBundlePartResponse.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this MerchantProductBundlePartResponse.


        :param quantity: The quantity of this MerchantProductBundlePartResponse.  # noqa: E501
        :type: int
        """

        self._quantity = quantity

    @property
    def price(self):
        """Gets the price of this MerchantProductBundlePartResponse.  # noqa: E501


        :return: The price of this MerchantProductBundlePartResponse.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this MerchantProductBundlePartResponse.


        :param price: The price of this MerchantProductBundlePartResponse.  # noqa: E501
        :type: float
        """

        self._price = price

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
        if issubclass(MerchantProductBundlePartResponse, dict):
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
        if not isinstance(other, MerchantProductBundlePartResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
