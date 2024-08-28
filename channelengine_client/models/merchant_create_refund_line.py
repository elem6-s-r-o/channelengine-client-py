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

class MerchantCreateRefundLine(object):
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
        'order_line_identifier': 'str',
        'line_amount_incl_tax': 'float',
        'merchant_refund_line_no': 'str',
        'extra_data': 'dict(str, str)'
    }

    attribute_map = {
        'order_line_identifier': 'OrderLineIdentifier',
        'line_amount_incl_tax': 'LineAmountInclTax',
        'merchant_refund_line_no': 'MerchantRefundLineNo',
        'extra_data': 'ExtraData'
    }

    def __init__(self, order_line_identifier=None, line_amount_incl_tax=None, merchant_refund_line_no=None, extra_data=None):  # noqa: E501
        """MerchantCreateRefundLine - a model defined in Swagger"""  # noqa: E501
        self._order_line_identifier = None
        self._line_amount_incl_tax = None
        self._merchant_refund_line_no = None
        self._extra_data = None
        self.discriminator = None
        if order_line_identifier is not None:
            self.order_line_identifier = order_line_identifier
        if line_amount_incl_tax is not None:
            self.line_amount_incl_tax = line_amount_incl_tax
        if merchant_refund_line_no is not None:
            self.merchant_refund_line_no = merchant_refund_line_no
        if extra_data is not None:
            self.extra_data = extra_data

    @property
    def order_line_identifier(self):
        """Gets the order_line_identifier of this MerchantCreateRefundLine.  # noqa: E501


        :return: The order_line_identifier of this MerchantCreateRefundLine.  # noqa: E501
        :rtype: str
        """
        return self._order_line_identifier

    @order_line_identifier.setter
    def order_line_identifier(self, order_line_identifier):
        """Sets the order_line_identifier of this MerchantCreateRefundLine.


        :param order_line_identifier: The order_line_identifier of this MerchantCreateRefundLine.  # noqa: E501
        :type: str
        """

        self._order_line_identifier = order_line_identifier

    @property
    def line_amount_incl_tax(self):
        """Gets the line_amount_incl_tax of this MerchantCreateRefundLine.  # noqa: E501


        :return: The line_amount_incl_tax of this MerchantCreateRefundLine.  # noqa: E501
        :rtype: float
        """
        return self._line_amount_incl_tax

    @line_amount_incl_tax.setter
    def line_amount_incl_tax(self, line_amount_incl_tax):
        """Sets the line_amount_incl_tax of this MerchantCreateRefundLine.


        :param line_amount_incl_tax: The line_amount_incl_tax of this MerchantCreateRefundLine.  # noqa: E501
        :type: float
        """

        self._line_amount_incl_tax = line_amount_incl_tax

    @property
    def merchant_refund_line_no(self):
        """Gets the merchant_refund_line_no of this MerchantCreateRefundLine.  # noqa: E501


        :return: The merchant_refund_line_no of this MerchantCreateRefundLine.  # noqa: E501
        :rtype: str
        """
        return self._merchant_refund_line_no

    @merchant_refund_line_no.setter
    def merchant_refund_line_no(self, merchant_refund_line_no):
        """Sets the merchant_refund_line_no of this MerchantCreateRefundLine.


        :param merchant_refund_line_no: The merchant_refund_line_no of this MerchantCreateRefundLine.  # noqa: E501
        :type: str
        """

        self._merchant_refund_line_no = merchant_refund_line_no

    @property
    def extra_data(self):
        """Gets the extra_data of this MerchantCreateRefundLine.  # noqa: E501


        :return: The extra_data of this MerchantCreateRefundLine.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._extra_data

    @extra_data.setter
    def extra_data(self, extra_data):
        """Sets the extra_data of this MerchantCreateRefundLine.


        :param extra_data: The extra_data of this MerchantCreateRefundLine.  # noqa: E501
        :type: dict(str, str)
        """

        self._extra_data = extra_data

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
        if issubclass(MerchantCreateRefundLine, dict):
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
        if not isinstance(other, MerchantCreateRefundLine):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other