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

class IVendorParty(object):
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
        'party_id': 'str',
        'tax_registration_type': 'ModulesTaxRegistrationType',
        'tax_registration_no': 'str',
        'name': 'str',
        'address_line1': 'str',
        'address_line2': 'str',
        'address_line3': 'str',
        'city': 'str',
        'county': 'str',
        'district': 'str',
        'state_or_region': 'str',
        'postal_code': 'str',
        'country_code': 'str',
        'phone': 'str'
    }

    attribute_map = {
        'party_id': 'PartyId',
        'tax_registration_type': 'TaxRegistrationType',
        'tax_registration_no': 'TaxRegistrationNo',
        'name': 'Name',
        'address_line1': 'AddressLine1',
        'address_line2': 'AddressLine2',
        'address_line3': 'AddressLine3',
        'city': 'City',
        'county': 'County',
        'district': 'District',
        'state_or_region': 'StateOrRegion',
        'postal_code': 'PostalCode',
        'country_code': 'CountryCode',
        'phone': 'Phone'
    }

    def __init__(self, party_id=None, tax_registration_type=None, tax_registration_no=None, name=None, address_line1=None, address_line2=None, address_line3=None, city=None, county=None, district=None, state_or_region=None, postal_code=None, country_code=None, phone=None):  # noqa: E501
        """IVendorParty - a model defined in Swagger"""  # noqa: E501
        self._party_id = None
        self._tax_registration_type = None
        self._tax_registration_no = None
        self._name = None
        self._address_line1 = None
        self._address_line2 = None
        self._address_line3 = None
        self._city = None
        self._county = None
        self._district = None
        self._state_or_region = None
        self._postal_code = None
        self._country_code = None
        self._phone = None
        self.discriminator = None
        if party_id is not None:
            self.party_id = party_id
        if tax_registration_type is not None:
            self.tax_registration_type = tax_registration_type
        if tax_registration_no is not None:
            self.tax_registration_no = tax_registration_no
        if name is not None:
            self.name = name
        if address_line1 is not None:
            self.address_line1 = address_line1
        if address_line2 is not None:
            self.address_line2 = address_line2
        if address_line3 is not None:
            self.address_line3 = address_line3
        if city is not None:
            self.city = city
        if county is not None:
            self.county = county
        if district is not None:
            self.district = district
        if state_or_region is not None:
            self.state_or_region = state_or_region
        if postal_code is not None:
            self.postal_code = postal_code
        if country_code is not None:
            self.country_code = country_code
        if phone is not None:
            self.phone = phone

    @property
    def party_id(self):
        """Gets the party_id of this IVendorParty.  # noqa: E501


        :return: The party_id of this IVendorParty.  # noqa: E501
        :rtype: str
        """
        return self._party_id

    @party_id.setter
    def party_id(self, party_id):
        """Sets the party_id of this IVendorParty.


        :param party_id: The party_id of this IVendorParty.  # noqa: E501
        :type: str
        """

        self._party_id = party_id

    @property
    def tax_registration_type(self):
        """Gets the tax_registration_type of this IVendorParty.  # noqa: E501


        :return: The tax_registration_type of this IVendorParty.  # noqa: E501
        :rtype: ModulesTaxRegistrationType
        """
        return self._tax_registration_type

    @tax_registration_type.setter
    def tax_registration_type(self, tax_registration_type):
        """Sets the tax_registration_type of this IVendorParty.


        :param tax_registration_type: The tax_registration_type of this IVendorParty.  # noqa: E501
        :type: ModulesTaxRegistrationType
        """

        self._tax_registration_type = tax_registration_type

    @property
    def tax_registration_no(self):
        """Gets the tax_registration_no of this IVendorParty.  # noqa: E501


        :return: The tax_registration_no of this IVendorParty.  # noqa: E501
        :rtype: str
        """
        return self._tax_registration_no

    @tax_registration_no.setter
    def tax_registration_no(self, tax_registration_no):
        """Sets the tax_registration_no of this IVendorParty.


        :param tax_registration_no: The tax_registration_no of this IVendorParty.  # noqa: E501
        :type: str
        """

        self._tax_registration_no = tax_registration_no

    @property
    def name(self):
        """Gets the name of this IVendorParty.  # noqa: E501


        :return: The name of this IVendorParty.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IVendorParty.


        :param name: The name of this IVendorParty.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def address_line1(self):
        """Gets the address_line1 of this IVendorParty.  # noqa: E501


        :return: The address_line1 of this IVendorParty.  # noqa: E501
        :rtype: str
        """
        return self._address_line1

    @address_line1.setter
    def address_line1(self, address_line1):
        """Sets the address_line1 of this IVendorParty.


        :param address_line1: The address_line1 of this IVendorParty.  # noqa: E501
        :type: str
        """

        self._address_line1 = address_line1

    @property
    def address_line2(self):
        """Gets the address_line2 of this IVendorParty.  # noqa: E501


        :return: The address_line2 of this IVendorParty.  # noqa: E501
        :rtype: str
        """
        return self._address_line2

    @address_line2.setter
    def address_line2(self, address_line2):
        """Sets the address_line2 of this IVendorParty.


        :param address_line2: The address_line2 of this IVendorParty.  # noqa: E501
        :type: str
        """

        self._address_line2 = address_line2

    @property
    def address_line3(self):
        """Gets the address_line3 of this IVendorParty.  # noqa: E501


        :return: The address_line3 of this IVendorParty.  # noqa: E501
        :rtype: str
        """
        return self._address_line3

    @address_line3.setter
    def address_line3(self, address_line3):
        """Sets the address_line3 of this IVendorParty.


        :param address_line3: The address_line3 of this IVendorParty.  # noqa: E501
        :type: str
        """

        self._address_line3 = address_line3

    @property
    def city(self):
        """Gets the city of this IVendorParty.  # noqa: E501


        :return: The city of this IVendorParty.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this IVendorParty.


        :param city: The city of this IVendorParty.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def county(self):
        """Gets the county of this IVendorParty.  # noqa: E501


        :return: The county of this IVendorParty.  # noqa: E501
        :rtype: str
        """
        return self._county

    @county.setter
    def county(self, county):
        """Sets the county of this IVendorParty.


        :param county: The county of this IVendorParty.  # noqa: E501
        :type: str
        """

        self._county = county

    @property
    def district(self):
        """Gets the district of this IVendorParty.  # noqa: E501


        :return: The district of this IVendorParty.  # noqa: E501
        :rtype: str
        """
        return self._district

    @district.setter
    def district(self, district):
        """Sets the district of this IVendorParty.


        :param district: The district of this IVendorParty.  # noqa: E501
        :type: str
        """

        self._district = district

    @property
    def state_or_region(self):
        """Gets the state_or_region of this IVendorParty.  # noqa: E501


        :return: The state_or_region of this IVendorParty.  # noqa: E501
        :rtype: str
        """
        return self._state_or_region

    @state_or_region.setter
    def state_or_region(self, state_or_region):
        """Sets the state_or_region of this IVendorParty.


        :param state_or_region: The state_or_region of this IVendorParty.  # noqa: E501
        :type: str
        """

        self._state_or_region = state_or_region

    @property
    def postal_code(self):
        """Gets the postal_code of this IVendorParty.  # noqa: E501


        :return: The postal_code of this IVendorParty.  # noqa: E501
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this IVendorParty.


        :param postal_code: The postal_code of this IVendorParty.  # noqa: E501
        :type: str
        """

        self._postal_code = postal_code

    @property
    def country_code(self):
        """Gets the country_code of this IVendorParty.  # noqa: E501


        :return: The country_code of this IVendorParty.  # noqa: E501
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this IVendorParty.


        :param country_code: The country_code of this IVendorParty.  # noqa: E501
        :type: str
        """

        self._country_code = country_code

    @property
    def phone(self):
        """Gets the phone of this IVendorParty.  # noqa: E501


        :return: The phone of this IVendorParty.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this IVendorParty.


        :param phone: The phone of this IVendorParty.  # noqa: E501
        :type: str
        """

        self._phone = phone

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
        if issubclass(IVendorParty, dict):
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
        if not isinstance(other, IVendorParty):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other