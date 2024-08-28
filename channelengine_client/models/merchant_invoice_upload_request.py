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

class MerchantInvoiceUploadRequest(object):
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
        'invoice_content': 'str',
        'invoice_number': 'str'
    }

    attribute_map = {
        'invoice_content': 'InvoiceContent',
        'invoice_number': 'InvoiceNumber'
    }

    def __init__(self, invoice_content=None, invoice_number=None):  # noqa: E501
        """MerchantInvoiceUploadRequest - a model defined in Swagger"""  # noqa: E501
        self._invoice_content = None
        self._invoice_number = None
        self.discriminator = None
        self.invoice_content = invoice_content
        self.invoice_number = invoice_number

    @property
    def invoice_content(self):
        """Gets the invoice_content of this MerchantInvoiceUploadRequest.  # noqa: E501

        Data needed to upload an invoice.  # noqa: E501

        :return: The invoice_content of this MerchantInvoiceUploadRequest.  # noqa: E501
        :rtype: str
        """
        return self._invoice_content

    @invoice_content.setter
    def invoice_content(self, invoice_content):
        """Sets the invoice_content of this MerchantInvoiceUploadRequest.

        Data needed to upload an invoice.  # noqa: E501

        :param invoice_content: The invoice_content of this MerchantInvoiceUploadRequest.  # noqa: E501
        :type: str
        """
        if invoice_content is None:
            raise ValueError("Invalid value for `invoice_content`, must not be `None`")  # noqa: E501

        self._invoice_content = invoice_content

    @property
    def invoice_number(self):
        """Gets the invoice_number of this MerchantInvoiceUploadRequest.  # noqa: E501

        The invoice number used in the invoice.  # noqa: E501

        :return: The invoice_number of this MerchantInvoiceUploadRequest.  # noqa: E501
        :rtype: str
        """
        return self._invoice_number

    @invoice_number.setter
    def invoice_number(self, invoice_number):
        """Sets the invoice_number of this MerchantInvoiceUploadRequest.

        The invoice number used in the invoice.  # noqa: E501

        :param invoice_number: The invoice_number of this MerchantInvoiceUploadRequest.  # noqa: E501
        :type: str
        """
        if invoice_number is None:
            raise ValueError("Invalid value for `invoice_number`, must not be `None`")  # noqa: E501

        self._invoice_number = invoice_number

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
        if issubclass(MerchantInvoiceUploadRequest, dict):
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
        if not isinstance(other, MerchantInvoiceUploadRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
