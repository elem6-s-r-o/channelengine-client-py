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

class PurchaseOrderInvoiceTaxDetails(object):
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
        'tax_type': 'ModulesTaxType',
        'tax_rate': 'float',
        'tax_amount': 'float',
        'tax_amount_currency_code': 'str',
        'taxable_amount': 'float',
        'taxable_amount_currency_code': 'str'
    }

    attribute_map = {
        'tax_type': 'TaxType',
        'tax_rate': 'TaxRate',
        'tax_amount': 'TaxAmount',
        'tax_amount_currency_code': 'TaxAmountCurrencyCode',
        'taxable_amount': 'TaxableAmount',
        'taxable_amount_currency_code': 'TaxableAmountCurrencyCode'
    }

    def __init__(self, tax_type=None, tax_rate=None, tax_amount=None, tax_amount_currency_code=None, taxable_amount=None, taxable_amount_currency_code=None):  # noqa: E501
        """PurchaseOrderInvoiceTaxDetails - a model defined in Swagger"""  # noqa: E501
        self._tax_type = None
        self._tax_rate = None
        self._tax_amount = None
        self._tax_amount_currency_code = None
        self._taxable_amount = None
        self._taxable_amount_currency_code = None
        self.discriminator = None
        if tax_type is not None:
            self.tax_type = tax_type
        if tax_rate is not None:
            self.tax_rate = tax_rate
        if tax_amount is not None:
            self.tax_amount = tax_amount
        if tax_amount_currency_code is not None:
            self.tax_amount_currency_code = tax_amount_currency_code
        if taxable_amount is not None:
            self.taxable_amount = taxable_amount
        if taxable_amount_currency_code is not None:
            self.taxable_amount_currency_code = taxable_amount_currency_code

    @property
    def tax_type(self):
        """Gets the tax_type of this PurchaseOrderInvoiceTaxDetails.  # noqa: E501


        :return: The tax_type of this PurchaseOrderInvoiceTaxDetails.  # noqa: E501
        :rtype: ModulesTaxType
        """
        return self._tax_type

    @tax_type.setter
    def tax_type(self, tax_type):
        """Sets the tax_type of this PurchaseOrderInvoiceTaxDetails.


        :param tax_type: The tax_type of this PurchaseOrderInvoiceTaxDetails.  # noqa: E501
        :type: ModulesTaxType
        """

        self._tax_type = tax_type

    @property
    def tax_rate(self):
        """Gets the tax_rate of this PurchaseOrderInvoiceTaxDetails.  # noqa: E501


        :return: The tax_rate of this PurchaseOrderInvoiceTaxDetails.  # noqa: E501
        :rtype: float
        """
        return self._tax_rate

    @tax_rate.setter
    def tax_rate(self, tax_rate):
        """Sets the tax_rate of this PurchaseOrderInvoiceTaxDetails.


        :param tax_rate: The tax_rate of this PurchaseOrderInvoiceTaxDetails.  # noqa: E501
        :type: float
        """

        self._tax_rate = tax_rate

    @property
    def tax_amount(self):
        """Gets the tax_amount of this PurchaseOrderInvoiceTaxDetails.  # noqa: E501


        :return: The tax_amount of this PurchaseOrderInvoiceTaxDetails.  # noqa: E501
        :rtype: float
        """
        return self._tax_amount

    @tax_amount.setter
    def tax_amount(self, tax_amount):
        """Sets the tax_amount of this PurchaseOrderInvoiceTaxDetails.


        :param tax_amount: The tax_amount of this PurchaseOrderInvoiceTaxDetails.  # noqa: E501
        :type: float
        """

        self._tax_amount = tax_amount

    @property
    def tax_amount_currency_code(self):
        """Gets the tax_amount_currency_code of this PurchaseOrderInvoiceTaxDetails.  # noqa: E501


        :return: The tax_amount_currency_code of this PurchaseOrderInvoiceTaxDetails.  # noqa: E501
        :rtype: str
        """
        return self._tax_amount_currency_code

    @tax_amount_currency_code.setter
    def tax_amount_currency_code(self, tax_amount_currency_code):
        """Sets the tax_amount_currency_code of this PurchaseOrderInvoiceTaxDetails.


        :param tax_amount_currency_code: The tax_amount_currency_code of this PurchaseOrderInvoiceTaxDetails.  # noqa: E501
        :type: str
        """

        self._tax_amount_currency_code = tax_amount_currency_code

    @property
    def taxable_amount(self):
        """Gets the taxable_amount of this PurchaseOrderInvoiceTaxDetails.  # noqa: E501


        :return: The taxable_amount of this PurchaseOrderInvoiceTaxDetails.  # noqa: E501
        :rtype: float
        """
        return self._taxable_amount

    @taxable_amount.setter
    def taxable_amount(self, taxable_amount):
        """Sets the taxable_amount of this PurchaseOrderInvoiceTaxDetails.


        :param taxable_amount: The taxable_amount of this PurchaseOrderInvoiceTaxDetails.  # noqa: E501
        :type: float
        """

        self._taxable_amount = taxable_amount

    @property
    def taxable_amount_currency_code(self):
        """Gets the taxable_amount_currency_code of this PurchaseOrderInvoiceTaxDetails.  # noqa: E501


        :return: The taxable_amount_currency_code of this PurchaseOrderInvoiceTaxDetails.  # noqa: E501
        :rtype: str
        """
        return self._taxable_amount_currency_code

    @taxable_amount_currency_code.setter
    def taxable_amount_currency_code(self, taxable_amount_currency_code):
        """Sets the taxable_amount_currency_code of this PurchaseOrderInvoiceTaxDetails.


        :param taxable_amount_currency_code: The taxable_amount_currency_code of this PurchaseOrderInvoiceTaxDetails.  # noqa: E501
        :type: str
        """

        self._taxable_amount_currency_code = taxable_amount_currency_code

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
        if issubclass(PurchaseOrderInvoiceTaxDetails, dict):
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
        if not isinstance(other, PurchaseOrderInvoiceTaxDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
