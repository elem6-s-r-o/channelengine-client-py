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

class MerchantSingleOrderReturnResponse(object):
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
        'merchant_order_no': 'str',
        'lines': 'list[MerchantSingleOrderReturnLineResponse]',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'merchant_return_no': 'str',
        'channel_return_no': 'str',
        'channel_id': 'int',
        'global_channel_id': 'int',
        'global_channel_name': 'str',
        'status': 'ReturnStatus',
        'id': 'int',
        'reason': 'ReturnReason',
        'customer_comment': 'str',
        'merchant_comment': 'str',
        'refund_incl_vat': 'float',
        'refund_excl_vat': 'float',
        'return_date': 'datetime',
        'extra_data': 'dict(str, str)'
    }

    attribute_map = {
        'merchant_order_no': 'MerchantOrderNo',
        'lines': 'Lines',
        'created_at': 'CreatedAt',
        'updated_at': 'UpdatedAt',
        'merchant_return_no': 'MerchantReturnNo',
        'channel_return_no': 'ChannelReturnNo',
        'channel_id': 'ChannelId',
        'global_channel_id': 'GlobalChannelId',
        'global_channel_name': 'GlobalChannelName',
        'status': 'Status',
        'id': 'Id',
        'reason': 'Reason',
        'customer_comment': 'CustomerComment',
        'merchant_comment': 'MerchantComment',
        'refund_incl_vat': 'RefundInclVat',
        'refund_excl_vat': 'RefundExclVat',
        'return_date': 'ReturnDate',
        'extra_data': 'ExtraData'
    }

    def __init__(self, merchant_order_no=None, lines=None, created_at=None, updated_at=None, merchant_return_no=None, channel_return_no=None, channel_id=None, global_channel_id=None, global_channel_name=None, status=None, id=None, reason=None, customer_comment=None, merchant_comment=None, refund_incl_vat=None, refund_excl_vat=None, return_date=None, extra_data=None):  # noqa: E501
        """MerchantSingleOrderReturnResponse - a model defined in Swagger"""  # noqa: E501
        self._merchant_order_no = None
        self._lines = None
        self._created_at = None
        self._updated_at = None
        self._merchant_return_no = None
        self._channel_return_no = None
        self._channel_id = None
        self._global_channel_id = None
        self._global_channel_name = None
        self._status = None
        self._id = None
        self._reason = None
        self._customer_comment = None
        self._merchant_comment = None
        self._refund_incl_vat = None
        self._refund_excl_vat = None
        self._return_date = None
        self._extra_data = None
        self.discriminator = None
        if merchant_order_no is not None:
            self.merchant_order_no = merchant_order_no
        if lines is not None:
            self.lines = lines
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if merchant_return_no is not None:
            self.merchant_return_no = merchant_return_no
        if channel_return_no is not None:
            self.channel_return_no = channel_return_no
        if channel_id is not None:
            self.channel_id = channel_id
        if global_channel_id is not None:
            self.global_channel_id = global_channel_id
        if global_channel_name is not None:
            self.global_channel_name = global_channel_name
        if status is not None:
            self.status = status
        if id is not None:
            self.id = id
        if reason is not None:
            self.reason = reason
        if customer_comment is not None:
            self.customer_comment = customer_comment
        if merchant_comment is not None:
            self.merchant_comment = merchant_comment
        if refund_incl_vat is not None:
            self.refund_incl_vat = refund_incl_vat
        if refund_excl_vat is not None:
            self.refund_excl_vat = refund_excl_vat
        if return_date is not None:
            self.return_date = return_date
        if extra_data is not None:
            self.extra_data = extra_data

    @property
    def merchant_order_no(self):
        """Gets the merchant_order_no of this MerchantSingleOrderReturnResponse.  # noqa: E501

        The unique order reference used by the Merchant.  # noqa: E501

        :return: The merchant_order_no of this MerchantSingleOrderReturnResponse.  # noqa: E501
        :rtype: str
        """
        return self._merchant_order_no

    @merchant_order_no.setter
    def merchant_order_no(self, merchant_order_no):
        """Sets the merchant_order_no of this MerchantSingleOrderReturnResponse.

        The unique order reference used by the Merchant.  # noqa: E501

        :param merchant_order_no: The merchant_order_no of this MerchantSingleOrderReturnResponse.  # noqa: E501
        :type: str
        """

        self._merchant_order_no = merchant_order_no

    @property
    def lines(self):
        """Gets the lines of this MerchantSingleOrderReturnResponse.  # noqa: E501


        :return: The lines of this MerchantSingleOrderReturnResponse.  # noqa: E501
        :rtype: list[MerchantSingleOrderReturnLineResponse]
        """
        return self._lines

    @lines.setter
    def lines(self, lines):
        """Sets the lines of this MerchantSingleOrderReturnResponse.


        :param lines: The lines of this MerchantSingleOrderReturnResponse.  # noqa: E501
        :type: list[MerchantSingleOrderReturnLineResponse]
        """

        self._lines = lines

    @property
    def created_at(self):
        """Gets the created_at of this MerchantSingleOrderReturnResponse.  # noqa: E501

        The date at which the return was created in ChannelEngine.  # noqa: E501

        :return: The created_at of this MerchantSingleOrderReturnResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this MerchantSingleOrderReturnResponse.

        The date at which the return was created in ChannelEngine.  # noqa: E501

        :param created_at: The created_at of this MerchantSingleOrderReturnResponse.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this MerchantSingleOrderReturnResponse.  # noqa: E501

        The date at which the return was last modified in ChannelEngine.  # noqa: E501

        :return: The updated_at of this MerchantSingleOrderReturnResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this MerchantSingleOrderReturnResponse.

        The date at which the return was last modified in ChannelEngine.  # noqa: E501

        :param updated_at: The updated_at of this MerchantSingleOrderReturnResponse.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def merchant_return_no(self):
        """Gets the merchant_return_no of this MerchantSingleOrderReturnResponse.  # noqa: E501

        The unique return reference used by the Merchant, will be empty in case of a channel or unacknowledged return.  # noqa: E501

        :return: The merchant_return_no of this MerchantSingleOrderReturnResponse.  # noqa: E501
        :rtype: str
        """
        return self._merchant_return_no

    @merchant_return_no.setter
    def merchant_return_no(self, merchant_return_no):
        """Sets the merchant_return_no of this MerchantSingleOrderReturnResponse.

        The unique return reference used by the Merchant, will be empty in case of a channel or unacknowledged return.  # noqa: E501

        :param merchant_return_no: The merchant_return_no of this MerchantSingleOrderReturnResponse.  # noqa: E501
        :type: str
        """

        self._merchant_return_no = merchant_return_no

    @property
    def channel_return_no(self):
        """Gets the channel_return_no of this MerchantSingleOrderReturnResponse.  # noqa: E501

        The unique return reference used by the Channel, will be empty in case of a merchant return.  # noqa: E501

        :return: The channel_return_no of this MerchantSingleOrderReturnResponse.  # noqa: E501
        :rtype: str
        """
        return self._channel_return_no

    @channel_return_no.setter
    def channel_return_no(self, channel_return_no):
        """Sets the channel_return_no of this MerchantSingleOrderReturnResponse.

        The unique return reference used by the Channel, will be empty in case of a merchant return.  # noqa: E501

        :param channel_return_no: The channel_return_no of this MerchantSingleOrderReturnResponse.  # noqa: E501
        :type: str
        """

        self._channel_return_no = channel_return_no

    @property
    def channel_id(self):
        """Gets the channel_id of this MerchantSingleOrderReturnResponse.  # noqa: E501

        The id of the channel.  # noqa: E501

        :return: The channel_id of this MerchantSingleOrderReturnResponse.  # noqa: E501
        :rtype: int
        """
        return self._channel_id

    @channel_id.setter
    def channel_id(self, channel_id):
        """Sets the channel_id of this MerchantSingleOrderReturnResponse.

        The id of the channel.  # noqa: E501

        :param channel_id: The channel_id of this MerchantSingleOrderReturnResponse.  # noqa: E501
        :type: int
        """

        self._channel_id = channel_id

    @property
    def global_channel_id(self):
        """Gets the global_channel_id of this MerchantSingleOrderReturnResponse.  # noqa: E501

        The id of the Global Channel.  # noqa: E501

        :return: The global_channel_id of this MerchantSingleOrderReturnResponse.  # noqa: E501
        :rtype: int
        """
        return self._global_channel_id

    @global_channel_id.setter
    def global_channel_id(self, global_channel_id):
        """Sets the global_channel_id of this MerchantSingleOrderReturnResponse.

        The id of the Global Channel.  # noqa: E501

        :param global_channel_id: The global_channel_id of this MerchantSingleOrderReturnResponse.  # noqa: E501
        :type: int
        """

        self._global_channel_id = global_channel_id

    @property
    def global_channel_name(self):
        """Gets the global_channel_name of this MerchantSingleOrderReturnResponse.  # noqa: E501

        The name of the Global Channel.  # noqa: E501

        :return: The global_channel_name of this MerchantSingleOrderReturnResponse.  # noqa: E501
        :rtype: str
        """
        return self._global_channel_name

    @global_channel_name.setter
    def global_channel_name(self, global_channel_name):
        """Sets the global_channel_name of this MerchantSingleOrderReturnResponse.

        The name of the Global Channel.  # noqa: E501

        :param global_channel_name: The global_channel_name of this MerchantSingleOrderReturnResponse.  # noqa: E501
        :type: str
        """

        self._global_channel_name = global_channel_name

    @property
    def status(self):
        """Gets the status of this MerchantSingleOrderReturnResponse.  # noqa: E501


        :return: The status of this MerchantSingleOrderReturnResponse.  # noqa: E501
        :rtype: ReturnStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this MerchantSingleOrderReturnResponse.


        :param status: The status of this MerchantSingleOrderReturnResponse.  # noqa: E501
        :type: ReturnStatus
        """

        self._status = status

    @property
    def id(self):
        """Gets the id of this MerchantSingleOrderReturnResponse.  # noqa: E501

        The unique return reference used by ChannelEngine.  # noqa: E501

        :return: The id of this MerchantSingleOrderReturnResponse.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MerchantSingleOrderReturnResponse.

        The unique return reference used by ChannelEngine.  # noqa: E501

        :param id: The id of this MerchantSingleOrderReturnResponse.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def reason(self):
        """Gets the reason of this MerchantSingleOrderReturnResponse.  # noqa: E501


        :return: The reason of this MerchantSingleOrderReturnResponse.  # noqa: E501
        :rtype: ReturnReason
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this MerchantSingleOrderReturnResponse.


        :param reason: The reason of this MerchantSingleOrderReturnResponse.  # noqa: E501
        :type: ReturnReason
        """

        self._reason = reason

    @property
    def customer_comment(self):
        """Gets the customer_comment of this MerchantSingleOrderReturnResponse.  # noqa: E501

        Optional. Comment of customer on the (reason of) the return.  # noqa: E501

        :return: The customer_comment of this MerchantSingleOrderReturnResponse.  # noqa: E501
        :rtype: str
        """
        return self._customer_comment

    @customer_comment.setter
    def customer_comment(self, customer_comment):
        """Sets the customer_comment of this MerchantSingleOrderReturnResponse.

        Optional. Comment of customer on the (reason of) the return.  # noqa: E501

        :param customer_comment: The customer_comment of this MerchantSingleOrderReturnResponse.  # noqa: E501
        :type: str
        """

        self._customer_comment = customer_comment

    @property
    def merchant_comment(self):
        """Gets the merchant_comment of this MerchantSingleOrderReturnResponse.  # noqa: E501

        Optional. Comment of merchant on the return.  # noqa: E501

        :return: The merchant_comment of this MerchantSingleOrderReturnResponse.  # noqa: E501
        :rtype: str
        """
        return self._merchant_comment

    @merchant_comment.setter
    def merchant_comment(self, merchant_comment):
        """Sets the merchant_comment of this MerchantSingleOrderReturnResponse.

        Optional. Comment of merchant on the return.  # noqa: E501

        :param merchant_comment: The merchant_comment of this MerchantSingleOrderReturnResponse.  # noqa: E501
        :type: str
        """

        self._merchant_comment = merchant_comment

    @property
    def refund_incl_vat(self):
        """Gets the refund_incl_vat of this MerchantSingleOrderReturnResponse.  # noqa: E501

        Refund amount incl. VAT.  # noqa: E501

        :return: The refund_incl_vat of this MerchantSingleOrderReturnResponse.  # noqa: E501
        :rtype: float
        """
        return self._refund_incl_vat

    @refund_incl_vat.setter
    def refund_incl_vat(self, refund_incl_vat):
        """Sets the refund_incl_vat of this MerchantSingleOrderReturnResponse.

        Refund amount incl. VAT.  # noqa: E501

        :param refund_incl_vat: The refund_incl_vat of this MerchantSingleOrderReturnResponse.  # noqa: E501
        :type: float
        """

        self._refund_incl_vat = refund_incl_vat

    @property
    def refund_excl_vat(self):
        """Gets the refund_excl_vat of this MerchantSingleOrderReturnResponse.  # noqa: E501

        Refund amount excl. VAT.  # noqa: E501

        :return: The refund_excl_vat of this MerchantSingleOrderReturnResponse.  # noqa: E501
        :rtype: float
        """
        return self._refund_excl_vat

    @refund_excl_vat.setter
    def refund_excl_vat(self, refund_excl_vat):
        """Sets the refund_excl_vat of this MerchantSingleOrderReturnResponse.

        Refund amount excl. VAT.  # noqa: E501

        :param refund_excl_vat: The refund_excl_vat of this MerchantSingleOrderReturnResponse.  # noqa: E501
        :type: float
        """

        self._refund_excl_vat = refund_excl_vat

    @property
    def return_date(self):
        """Gets the return_date of this MerchantSingleOrderReturnResponse.  # noqa: E501

        The date at which the return was originally created in the source system (if available).  # noqa: E501

        :return: The return_date of this MerchantSingleOrderReturnResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._return_date

    @return_date.setter
    def return_date(self, return_date):
        """Sets the return_date of this MerchantSingleOrderReturnResponse.

        The date at which the return was originally created in the source system (if available).  # noqa: E501

        :param return_date: The return_date of this MerchantSingleOrderReturnResponse.  # noqa: E501
        :type: datetime
        """

        self._return_date = return_date

    @property
    def extra_data(self):
        """Gets the extra_data of this MerchantSingleOrderReturnResponse.  # noqa: E501

        Extra data on the return. Each item must have an unqiue key  # noqa: E501

        :return: The extra_data of this MerchantSingleOrderReturnResponse.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._extra_data

    @extra_data.setter
    def extra_data(self, extra_data):
        """Sets the extra_data of this MerchantSingleOrderReturnResponse.

        Extra data on the return. Each item must have an unqiue key  # noqa: E501

        :param extra_data: The extra_data of this MerchantSingleOrderReturnResponse.  # noqa: E501
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
        if issubclass(MerchantSingleOrderReturnResponse, dict):
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
        if not isinstance(other, MerchantSingleOrderReturnResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
