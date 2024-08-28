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

class CreateEditTargetView(object):
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
        'target_incl_vat': 'float',
        'target_excl_vat': 'float',
        'month': 'int',
        'year': 'int'
    }

    attribute_map = {
        'target_incl_vat': 'TargetInclVat',
        'target_excl_vat': 'TargetExclVat',
        'month': 'Month',
        'year': 'Year'
    }

    def __init__(self, target_incl_vat=None, target_excl_vat=None, month=None, year=None):  # noqa: E501
        """CreateEditTargetView - a model defined in Swagger"""  # noqa: E501
        self._target_incl_vat = None
        self._target_excl_vat = None
        self._month = None
        self._year = None
        self.discriminator = None
        if target_incl_vat is not None:
            self.target_incl_vat = target_incl_vat
        if target_excl_vat is not None:
            self.target_excl_vat = target_excl_vat
        if month is not None:
            self.month = month
        if year is not None:
            self.year = year

    @property
    def target_incl_vat(self):
        """Gets the target_incl_vat of this CreateEditTargetView.  # noqa: E501


        :return: The target_incl_vat of this CreateEditTargetView.  # noqa: E501
        :rtype: float
        """
        return self._target_incl_vat

    @target_incl_vat.setter
    def target_incl_vat(self, target_incl_vat):
        """Sets the target_incl_vat of this CreateEditTargetView.


        :param target_incl_vat: The target_incl_vat of this CreateEditTargetView.  # noqa: E501
        :type: float
        """

        self._target_incl_vat = target_incl_vat

    @property
    def target_excl_vat(self):
        """Gets the target_excl_vat of this CreateEditTargetView.  # noqa: E501


        :return: The target_excl_vat of this CreateEditTargetView.  # noqa: E501
        :rtype: float
        """
        return self._target_excl_vat

    @target_excl_vat.setter
    def target_excl_vat(self, target_excl_vat):
        """Sets the target_excl_vat of this CreateEditTargetView.


        :param target_excl_vat: The target_excl_vat of this CreateEditTargetView.  # noqa: E501
        :type: float
        """

        self._target_excl_vat = target_excl_vat

    @property
    def month(self):
        """Gets the month of this CreateEditTargetView.  # noqa: E501


        :return: The month of this CreateEditTargetView.  # noqa: E501
        :rtype: int
        """
        return self._month

    @month.setter
    def month(self, month):
        """Sets the month of this CreateEditTargetView.


        :param month: The month of this CreateEditTargetView.  # noqa: E501
        :type: int
        """

        self._month = month

    @property
    def year(self):
        """Gets the year of this CreateEditTargetView.  # noqa: E501


        :return: The year of this CreateEditTargetView.  # noqa: E501
        :rtype: int
        """
        return self._year

    @year.setter
    def year(self, year):
        """Sets the year of this CreateEditTargetView.


        :param year: The year of this CreateEditTargetView.  # noqa: E501
        :type: int
        """

        self._year = year

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
        if issubclass(CreateEditTargetView, dict):
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
        if not isinstance(other, CreateEditTargetView):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
