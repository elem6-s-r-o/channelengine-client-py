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

class PurchaseOrderInvoiceChargeDetails(object):
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
        'type': 'ModulesChargeDetailsType',
        'description': 'str',
        'charge_amount': 'float',
        'charge_amount_currency_code': 'str',
        'tax_details': 'PurchaseOrderInvoiceTaxDetails'
    }

    attribute_map = {
        'type': 'Type',
        'description': 'Description',
        'charge_amount': 'ChargeAmount',
        'charge_amount_currency_code': 'ChargeAmountCurrencyCode',
        'tax_details': 'TaxDetails'
    }

    def __init__(self, type=None, description=None, charge_amount=None, charge_amount_currency_code=None, tax_details=None):  # noqa: E501
        """PurchaseOrderInvoiceChargeDetails - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._description = None
        self._charge_amount = None
        self._charge_amount_currency_code = None
        self._tax_details = None
        self.discriminator = None
        if type is not None:
            self.type = type
        if description is not None:
            self.description = description
        if charge_amount is not None:
            self.charge_amount = charge_amount
        if charge_amount_currency_code is not None:
            self.charge_amount_currency_code = charge_amount_currency_code
        if tax_details is not None:
            self.tax_details = tax_details

    @property
    def type(self):
        """Gets the type of this PurchaseOrderInvoiceChargeDetails.  # noqa: E501


        :return: The type of this PurchaseOrderInvoiceChargeDetails.  # noqa: E501
        :rtype: ModulesChargeDetailsType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PurchaseOrderInvoiceChargeDetails.


        :param type: The type of this PurchaseOrderInvoiceChargeDetails.  # noqa: E501
        :type: ModulesChargeDetailsType
        """

        self._type = type

    @property
    def description(self):
        """Gets the description of this PurchaseOrderInvoiceChargeDetails.  # noqa: E501


        :return: The description of this PurchaseOrderInvoiceChargeDetails.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PurchaseOrderInvoiceChargeDetails.


        :param description: The description of this PurchaseOrderInvoiceChargeDetails.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def charge_amount(self):
        """Gets the charge_amount of this PurchaseOrderInvoiceChargeDetails.  # noqa: E501


        :return: The charge_amount of this PurchaseOrderInvoiceChargeDetails.  # noqa: E501
        :rtype: float
        """
        return self._charge_amount

    @charge_amount.setter
    def charge_amount(self, charge_amount):
        """Sets the charge_amount of this PurchaseOrderInvoiceChargeDetails.


        :param charge_amount: The charge_amount of this PurchaseOrderInvoiceChargeDetails.  # noqa: E501
        :type: float
        """

        self._charge_amount = charge_amount

    @property
    def charge_amount_currency_code(self):
        """Gets the charge_amount_currency_code of this PurchaseOrderInvoiceChargeDetails.  # noqa: E501


        :return: The charge_amount_currency_code of this PurchaseOrderInvoiceChargeDetails.  # noqa: E501
        :rtype: str
        """
        return self._charge_amount_currency_code

    @charge_amount_currency_code.setter
    def charge_amount_currency_code(self, charge_amount_currency_code):
        """Sets the charge_amount_currency_code of this PurchaseOrderInvoiceChargeDetails.


        :param charge_amount_currency_code: The charge_amount_currency_code of this PurchaseOrderInvoiceChargeDetails.  # noqa: E501
        :type: str
        """

        self._charge_amount_currency_code = charge_amount_currency_code

    @property
    def tax_details(self):
        """Gets the tax_details of this PurchaseOrderInvoiceChargeDetails.  # noqa: E501


        :return: The tax_details of this PurchaseOrderInvoiceChargeDetails.  # noqa: E501
        :rtype: PurchaseOrderInvoiceTaxDetails
        """
        return self._tax_details

    @tax_details.setter
    def tax_details(self, tax_details):
        """Sets the tax_details of this PurchaseOrderInvoiceChargeDetails.


        :param tax_details: The tax_details of this PurchaseOrderInvoiceChargeDetails.  # noqa: E501
        :type: PurchaseOrderInvoiceTaxDetails
        """

        self._tax_details = tax_details

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
        if issubclass(PurchaseOrderInvoiceChargeDetails, dict):
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
        if not isinstance(other, PurchaseOrderInvoiceChargeDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other