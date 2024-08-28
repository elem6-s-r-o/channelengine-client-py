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

class AdvanceSettingsResponse(object):
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
        'manage_stock': 'bool',
        'disable_address_validation': 'bool',
        'skip_house_number_validation': 'bool',
        'skip_house_number_validation_for_country_codes': 'list[str]',
        'set_orders_to_closed_on_import': 'bool',
        'disable_stock_reservation': 'bool',
        'disable_auto_order_cancellation': 'bool',
        'automatically_set_phone_number_if_empty': 'str',
        'default_vat_rate': 'float',
        'order_too_long_on_new_hours_offset': 'int'
    }

    attribute_map = {
        'manage_stock': 'ManageStock',
        'disable_address_validation': 'DisableAddressValidation',
        'skip_house_number_validation': 'SkipHouseNumberValidation',
        'skip_house_number_validation_for_country_codes': 'SkipHouseNumberValidationForCountryCodes',
        'set_orders_to_closed_on_import': 'SetOrdersToClosedOnImport',
        'disable_stock_reservation': 'DisableStockReservation',
        'disable_auto_order_cancellation': 'DisableAutoOrderCancellation',
        'automatically_set_phone_number_if_empty': 'AutomaticallySetPhoneNumberIfEmpty',
        'default_vat_rate': 'DefaultVatRate',
        'order_too_long_on_new_hours_offset': 'OrderTooLongOnNewHoursOffset'
    }

    def __init__(self, manage_stock=None, disable_address_validation=None, skip_house_number_validation=None, skip_house_number_validation_for_country_codes=None, set_orders_to_closed_on_import=None, disable_stock_reservation=None, disable_auto_order_cancellation=None, automatically_set_phone_number_if_empty=None, default_vat_rate=None, order_too_long_on_new_hours_offset=None):  # noqa: E501
        """AdvanceSettingsResponse - a model defined in Swagger"""  # noqa: E501
        self._manage_stock = None
        self._disable_address_validation = None
        self._skip_house_number_validation = None
        self._skip_house_number_validation_for_country_codes = None
        self._set_orders_to_closed_on_import = None
        self._disable_stock_reservation = None
        self._disable_auto_order_cancellation = None
        self._automatically_set_phone_number_if_empty = None
        self._default_vat_rate = None
        self._order_too_long_on_new_hours_offset = None
        self.discriminator = None
        if manage_stock is not None:
            self.manage_stock = manage_stock
        if disable_address_validation is not None:
            self.disable_address_validation = disable_address_validation
        if skip_house_number_validation is not None:
            self.skip_house_number_validation = skip_house_number_validation
        if skip_house_number_validation_for_country_codes is not None:
            self.skip_house_number_validation_for_country_codes = skip_house_number_validation_for_country_codes
        if set_orders_to_closed_on_import is not None:
            self.set_orders_to_closed_on_import = set_orders_to_closed_on_import
        if disable_stock_reservation is not None:
            self.disable_stock_reservation = disable_stock_reservation
        if disable_auto_order_cancellation is not None:
            self.disable_auto_order_cancellation = disable_auto_order_cancellation
        if automatically_set_phone_number_if_empty is not None:
            self.automatically_set_phone_number_if_empty = automatically_set_phone_number_if_empty
        if default_vat_rate is not None:
            self.default_vat_rate = default_vat_rate
        if order_too_long_on_new_hours_offset is not None:
            self.order_too_long_on_new_hours_offset = order_too_long_on_new_hours_offset

    @property
    def manage_stock(self):
        """Gets the manage_stock of this AdvanceSettingsResponse.  # noqa: E501


        :return: The manage_stock of this AdvanceSettingsResponse.  # noqa: E501
        :rtype: bool
        """
        return self._manage_stock

    @manage_stock.setter
    def manage_stock(self, manage_stock):
        """Sets the manage_stock of this AdvanceSettingsResponse.


        :param manage_stock: The manage_stock of this AdvanceSettingsResponse.  # noqa: E501
        :type: bool
        """

        self._manage_stock = manage_stock

    @property
    def disable_address_validation(self):
        """Gets the disable_address_validation of this AdvanceSettingsResponse.  # noqa: E501


        :return: The disable_address_validation of this AdvanceSettingsResponse.  # noqa: E501
        :rtype: bool
        """
        return self._disable_address_validation

    @disable_address_validation.setter
    def disable_address_validation(self, disable_address_validation):
        """Sets the disable_address_validation of this AdvanceSettingsResponse.


        :param disable_address_validation: The disable_address_validation of this AdvanceSettingsResponse.  # noqa: E501
        :type: bool
        """

        self._disable_address_validation = disable_address_validation

    @property
    def skip_house_number_validation(self):
        """Gets the skip_house_number_validation of this AdvanceSettingsResponse.  # noqa: E501


        :return: The skip_house_number_validation of this AdvanceSettingsResponse.  # noqa: E501
        :rtype: bool
        """
        return self._skip_house_number_validation

    @skip_house_number_validation.setter
    def skip_house_number_validation(self, skip_house_number_validation):
        """Sets the skip_house_number_validation of this AdvanceSettingsResponse.


        :param skip_house_number_validation: The skip_house_number_validation of this AdvanceSettingsResponse.  # noqa: E501
        :type: bool
        """

        self._skip_house_number_validation = skip_house_number_validation

    @property
    def skip_house_number_validation_for_country_codes(self):
        """Gets the skip_house_number_validation_for_country_codes of this AdvanceSettingsResponse.  # noqa: E501


        :return: The skip_house_number_validation_for_country_codes of this AdvanceSettingsResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._skip_house_number_validation_for_country_codes

    @skip_house_number_validation_for_country_codes.setter
    def skip_house_number_validation_for_country_codes(self, skip_house_number_validation_for_country_codes):
        """Sets the skip_house_number_validation_for_country_codes of this AdvanceSettingsResponse.


        :param skip_house_number_validation_for_country_codes: The skip_house_number_validation_for_country_codes of this AdvanceSettingsResponse.  # noqa: E501
        :type: list[str]
        """

        self._skip_house_number_validation_for_country_codes = skip_house_number_validation_for_country_codes

    @property
    def set_orders_to_closed_on_import(self):
        """Gets the set_orders_to_closed_on_import of this AdvanceSettingsResponse.  # noqa: E501


        :return: The set_orders_to_closed_on_import of this AdvanceSettingsResponse.  # noqa: E501
        :rtype: bool
        """
        return self._set_orders_to_closed_on_import

    @set_orders_to_closed_on_import.setter
    def set_orders_to_closed_on_import(self, set_orders_to_closed_on_import):
        """Sets the set_orders_to_closed_on_import of this AdvanceSettingsResponse.


        :param set_orders_to_closed_on_import: The set_orders_to_closed_on_import of this AdvanceSettingsResponse.  # noqa: E501
        :type: bool
        """

        self._set_orders_to_closed_on_import = set_orders_to_closed_on_import

    @property
    def disable_stock_reservation(self):
        """Gets the disable_stock_reservation of this AdvanceSettingsResponse.  # noqa: E501


        :return: The disable_stock_reservation of this AdvanceSettingsResponse.  # noqa: E501
        :rtype: bool
        """
        return self._disable_stock_reservation

    @disable_stock_reservation.setter
    def disable_stock_reservation(self, disable_stock_reservation):
        """Sets the disable_stock_reservation of this AdvanceSettingsResponse.


        :param disable_stock_reservation: The disable_stock_reservation of this AdvanceSettingsResponse.  # noqa: E501
        :type: bool
        """

        self._disable_stock_reservation = disable_stock_reservation

    @property
    def disable_auto_order_cancellation(self):
        """Gets the disable_auto_order_cancellation of this AdvanceSettingsResponse.  # noqa: E501


        :return: The disable_auto_order_cancellation of this AdvanceSettingsResponse.  # noqa: E501
        :rtype: bool
        """
        return self._disable_auto_order_cancellation

    @disable_auto_order_cancellation.setter
    def disable_auto_order_cancellation(self, disable_auto_order_cancellation):
        """Sets the disable_auto_order_cancellation of this AdvanceSettingsResponse.


        :param disable_auto_order_cancellation: The disable_auto_order_cancellation of this AdvanceSettingsResponse.  # noqa: E501
        :type: bool
        """

        self._disable_auto_order_cancellation = disable_auto_order_cancellation

    @property
    def automatically_set_phone_number_if_empty(self):
        """Gets the automatically_set_phone_number_if_empty of this AdvanceSettingsResponse.  # noqa: E501


        :return: The automatically_set_phone_number_if_empty of this AdvanceSettingsResponse.  # noqa: E501
        :rtype: str
        """
        return self._automatically_set_phone_number_if_empty

    @automatically_set_phone_number_if_empty.setter
    def automatically_set_phone_number_if_empty(self, automatically_set_phone_number_if_empty):
        """Sets the automatically_set_phone_number_if_empty of this AdvanceSettingsResponse.


        :param automatically_set_phone_number_if_empty: The automatically_set_phone_number_if_empty of this AdvanceSettingsResponse.  # noqa: E501
        :type: str
        """

        self._automatically_set_phone_number_if_empty = automatically_set_phone_number_if_empty

    @property
    def default_vat_rate(self):
        """Gets the default_vat_rate of this AdvanceSettingsResponse.  # noqa: E501


        :return: The default_vat_rate of this AdvanceSettingsResponse.  # noqa: E501
        :rtype: float
        """
        return self._default_vat_rate

    @default_vat_rate.setter
    def default_vat_rate(self, default_vat_rate):
        """Sets the default_vat_rate of this AdvanceSettingsResponse.


        :param default_vat_rate: The default_vat_rate of this AdvanceSettingsResponse.  # noqa: E501
        :type: float
        """

        self._default_vat_rate = default_vat_rate

    @property
    def order_too_long_on_new_hours_offset(self):
        """Gets the order_too_long_on_new_hours_offset of this AdvanceSettingsResponse.  # noqa: E501


        :return: The order_too_long_on_new_hours_offset of this AdvanceSettingsResponse.  # noqa: E501
        :rtype: int
        """
        return self._order_too_long_on_new_hours_offset

    @order_too_long_on_new_hours_offset.setter
    def order_too_long_on_new_hours_offset(self, order_too_long_on_new_hours_offset):
        """Sets the order_too_long_on_new_hours_offset of this AdvanceSettingsResponse.


        :param order_too_long_on_new_hours_offset: The order_too_long_on_new_hours_offset of this AdvanceSettingsResponse.  # noqa: E501
        :type: int
        """

        self._order_too_long_on_new_hours_offset = order_too_long_on_new_hours_offset

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
        if issubclass(AdvanceSettingsResponse, dict):
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
        if not isinstance(other, AdvanceSettingsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
