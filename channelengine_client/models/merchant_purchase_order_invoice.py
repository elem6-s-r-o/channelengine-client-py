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

class MerchantPurchaseOrderInvoice(object):
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
        'invoice_no': 'str',
        'invoice_type': 'ModulesPurchaseOrderInvoiceType',
        'invoice_total_amount': 'float',
        'invoice_total_currency_code': 'str',
        'remit_to_party': 'MerchantVendorParty',
        'ship_to_party_id': 'int',
        'bill_to_party_id': 'int',
        'additional_details': 'list[PurchaseOrderInvoiceAdditionalDetails]',
        'lines': 'list[MerchantPurchaseOrderInvoiceLine]'
    }

    attribute_map = {
        'invoice_no': 'InvoiceNo',
        'invoice_type': 'InvoiceType',
        'invoice_total_amount': 'InvoiceTotalAmount',
        'invoice_total_currency_code': 'InvoiceTotalCurrencyCode',
        'remit_to_party': 'RemitToParty',
        'ship_to_party_id': 'ShipToPartyId',
        'bill_to_party_id': 'BillToPartyId',
        'additional_details': 'AdditionalDetails',
        'lines': 'Lines'
    }

    def __init__(self, invoice_no=None, invoice_type=None, invoice_total_amount=None, invoice_total_currency_code=None, remit_to_party=None, ship_to_party_id=None, bill_to_party_id=None, additional_details=None, lines=None):  # noqa: E501
        """MerchantPurchaseOrderInvoice - a model defined in Swagger"""  # noqa: E501
        self._invoice_no = None
        self._invoice_type = None
        self._invoice_total_amount = None
        self._invoice_total_currency_code = None
        self._remit_to_party = None
        self._ship_to_party_id = None
        self._bill_to_party_id = None
        self._additional_details = None
        self._lines = None
        self.discriminator = None
        if invoice_no is not None:
            self.invoice_no = invoice_no
        if invoice_type is not None:
            self.invoice_type = invoice_type
        if invoice_total_amount is not None:
            self.invoice_total_amount = invoice_total_amount
        if invoice_total_currency_code is not None:
            self.invoice_total_currency_code = invoice_total_currency_code
        if remit_to_party is not None:
            self.remit_to_party = remit_to_party
        if ship_to_party_id is not None:
            self.ship_to_party_id = ship_to_party_id
        if bill_to_party_id is not None:
            self.bill_to_party_id = bill_to_party_id
        if additional_details is not None:
            self.additional_details = additional_details
        if lines is not None:
            self.lines = lines

    @property
    def invoice_no(self):
        """Gets the invoice_no of this MerchantPurchaseOrderInvoice.  # noqa: E501


        :return: The invoice_no of this MerchantPurchaseOrderInvoice.  # noqa: E501
        :rtype: str
        """
        return self._invoice_no

    @invoice_no.setter
    def invoice_no(self, invoice_no):
        """Sets the invoice_no of this MerchantPurchaseOrderInvoice.


        :param invoice_no: The invoice_no of this MerchantPurchaseOrderInvoice.  # noqa: E501
        :type: str
        """

        self._invoice_no = invoice_no

    @property
    def invoice_type(self):
        """Gets the invoice_type of this MerchantPurchaseOrderInvoice.  # noqa: E501


        :return: The invoice_type of this MerchantPurchaseOrderInvoice.  # noqa: E501
        :rtype: ModulesPurchaseOrderInvoiceType
        """
        return self._invoice_type

    @invoice_type.setter
    def invoice_type(self, invoice_type):
        """Sets the invoice_type of this MerchantPurchaseOrderInvoice.


        :param invoice_type: The invoice_type of this MerchantPurchaseOrderInvoice.  # noqa: E501
        :type: ModulesPurchaseOrderInvoiceType
        """

        self._invoice_type = invoice_type

    @property
    def invoice_total_amount(self):
        """Gets the invoice_total_amount of this MerchantPurchaseOrderInvoice.  # noqa: E501


        :return: The invoice_total_amount of this MerchantPurchaseOrderInvoice.  # noqa: E501
        :rtype: float
        """
        return self._invoice_total_amount

    @invoice_total_amount.setter
    def invoice_total_amount(self, invoice_total_amount):
        """Sets the invoice_total_amount of this MerchantPurchaseOrderInvoice.


        :param invoice_total_amount: The invoice_total_amount of this MerchantPurchaseOrderInvoice.  # noqa: E501
        :type: float
        """

        self._invoice_total_amount = invoice_total_amount

    @property
    def invoice_total_currency_code(self):
        """Gets the invoice_total_currency_code of this MerchantPurchaseOrderInvoice.  # noqa: E501


        :return: The invoice_total_currency_code of this MerchantPurchaseOrderInvoice.  # noqa: E501
        :rtype: str
        """
        return self._invoice_total_currency_code

    @invoice_total_currency_code.setter
    def invoice_total_currency_code(self, invoice_total_currency_code):
        """Sets the invoice_total_currency_code of this MerchantPurchaseOrderInvoice.


        :param invoice_total_currency_code: The invoice_total_currency_code of this MerchantPurchaseOrderInvoice.  # noqa: E501
        :type: str
        """

        self._invoice_total_currency_code = invoice_total_currency_code

    @property
    def remit_to_party(self):
        """Gets the remit_to_party of this MerchantPurchaseOrderInvoice.  # noqa: E501


        :return: The remit_to_party of this MerchantPurchaseOrderInvoice.  # noqa: E501
        :rtype: MerchantVendorParty
        """
        return self._remit_to_party

    @remit_to_party.setter
    def remit_to_party(self, remit_to_party):
        """Sets the remit_to_party of this MerchantPurchaseOrderInvoice.


        :param remit_to_party: The remit_to_party of this MerchantPurchaseOrderInvoice.  # noqa: E501
        :type: MerchantVendorParty
        """

        self._remit_to_party = remit_to_party

    @property
    def ship_to_party_id(self):
        """Gets the ship_to_party_id of this MerchantPurchaseOrderInvoice.  # noqa: E501


        :return: The ship_to_party_id of this MerchantPurchaseOrderInvoice.  # noqa: E501
        :rtype: int
        """
        return self._ship_to_party_id

    @ship_to_party_id.setter
    def ship_to_party_id(self, ship_to_party_id):
        """Sets the ship_to_party_id of this MerchantPurchaseOrderInvoice.


        :param ship_to_party_id: The ship_to_party_id of this MerchantPurchaseOrderInvoice.  # noqa: E501
        :type: int
        """

        self._ship_to_party_id = ship_to_party_id

    @property
    def bill_to_party_id(self):
        """Gets the bill_to_party_id of this MerchantPurchaseOrderInvoice.  # noqa: E501


        :return: The bill_to_party_id of this MerchantPurchaseOrderInvoice.  # noqa: E501
        :rtype: int
        """
        return self._bill_to_party_id

    @bill_to_party_id.setter
    def bill_to_party_id(self, bill_to_party_id):
        """Sets the bill_to_party_id of this MerchantPurchaseOrderInvoice.


        :param bill_to_party_id: The bill_to_party_id of this MerchantPurchaseOrderInvoice.  # noqa: E501
        :type: int
        """

        self._bill_to_party_id = bill_to_party_id

    @property
    def additional_details(self):
        """Gets the additional_details of this MerchantPurchaseOrderInvoice.  # noqa: E501


        :return: The additional_details of this MerchantPurchaseOrderInvoice.  # noqa: E501
        :rtype: list[PurchaseOrderInvoiceAdditionalDetails]
        """
        return self._additional_details

    @additional_details.setter
    def additional_details(self, additional_details):
        """Sets the additional_details of this MerchantPurchaseOrderInvoice.


        :param additional_details: The additional_details of this MerchantPurchaseOrderInvoice.  # noqa: E501
        :type: list[PurchaseOrderInvoiceAdditionalDetails]
        """

        self._additional_details = additional_details

    @property
    def lines(self):
        """Gets the lines of this MerchantPurchaseOrderInvoice.  # noqa: E501


        :return: The lines of this MerchantPurchaseOrderInvoice.  # noqa: E501
        :rtype: list[MerchantPurchaseOrderInvoiceLine]
        """
        return self._lines

    @lines.setter
    def lines(self, lines):
        """Sets the lines of this MerchantPurchaseOrderInvoice.


        :param lines: The lines of this MerchantPurchaseOrderInvoice.  # noqa: E501
        :type: list[MerchantPurchaseOrderInvoiceLine]
        """

        self._lines = lines

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
        if issubclass(MerchantPurchaseOrderInvoice, dict):
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
        if not isinstance(other, MerchantPurchaseOrderInvoice):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
