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

class IRefund(object):
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
        'id': 'int',
        'reason': 'RefundReason',
        'channel_export_status': 'ChannelExportStatus',
        'sub_total_incl_tax': 'float',
        'original_sub_total_incl_tax': 'float',
        'additional_amount_incl_tax': 'float',
        'original_additional_amount_incl_tax': 'float',
        'shipping_cost_incl_tax': 'float',
        'original_shipping_cost_incl_tax': 'float',
        'total_incl_tax': 'float',
        'original_total_incl_tax': 'float',
        'merchant_comment': 'str',
        'merchant_refund_no': 'str',
        'channel_refund_no': 'str',
        'channel_order_no': 'str',
        'created_by_type': 'CreatedByType',
        'refund_date': 'datetime',
        'external_batch_no': 'str',
        'channel_acknowledged_date': 'datetime',
        'merchant_acknowledged_date': 'datetime',
        'order_id': 'int',
        'channel_id': 'int',
        'return_id': 'int',
        'currency': 'IRefundCurrency',
        'lines': 'list[IRefundLine]',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'deleted_at': 'datetime'
    }

    attribute_map = {
        'id': 'Id',
        'reason': 'Reason',
        'channel_export_status': 'ChannelExportStatus',
        'sub_total_incl_tax': 'SubTotalInclTax',
        'original_sub_total_incl_tax': 'OriginalSubTotalInclTax',
        'additional_amount_incl_tax': 'AdditionalAmountInclTax',
        'original_additional_amount_incl_tax': 'OriginalAdditionalAmountInclTax',
        'shipping_cost_incl_tax': 'ShippingCostInclTax',
        'original_shipping_cost_incl_tax': 'OriginalShippingCostInclTax',
        'total_incl_tax': 'TotalInclTax',
        'original_total_incl_tax': 'OriginalTotalInclTax',
        'merchant_comment': 'MerchantComment',
        'merchant_refund_no': 'MerchantRefundNo',
        'channel_refund_no': 'ChannelRefundNo',
        'channel_order_no': 'ChannelOrderNo',
        'created_by_type': 'CreatedByType',
        'refund_date': 'RefundDate',
        'external_batch_no': 'ExternalBatchNo',
        'channel_acknowledged_date': 'ChannelAcknowledgedDate',
        'merchant_acknowledged_date': 'MerchantAcknowledgedDate',
        'order_id': 'OrderId',
        'channel_id': 'ChannelId',
        'return_id': 'ReturnId',
        'currency': 'Currency',
        'lines': 'Lines',
        'created_at': 'CreatedAt',
        'updated_at': 'UpdatedAt',
        'deleted_at': 'DeletedAt'
    }

    def __init__(self, id=None, reason=None, channel_export_status=None, sub_total_incl_tax=None, original_sub_total_incl_tax=None, additional_amount_incl_tax=None, original_additional_amount_incl_tax=None, shipping_cost_incl_tax=None, original_shipping_cost_incl_tax=None, total_incl_tax=None, original_total_incl_tax=None, merchant_comment=None, merchant_refund_no=None, channel_refund_no=None, channel_order_no=None, created_by_type=None, refund_date=None, external_batch_no=None, channel_acknowledged_date=None, merchant_acknowledged_date=None, order_id=None, channel_id=None, return_id=None, currency=None, lines=None, created_at=None, updated_at=None, deleted_at=None):  # noqa: E501
        """IRefund - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._reason = None
        self._channel_export_status = None
        self._sub_total_incl_tax = None
        self._original_sub_total_incl_tax = None
        self._additional_amount_incl_tax = None
        self._original_additional_amount_incl_tax = None
        self._shipping_cost_incl_tax = None
        self._original_shipping_cost_incl_tax = None
        self._total_incl_tax = None
        self._original_total_incl_tax = None
        self._merchant_comment = None
        self._merchant_refund_no = None
        self._channel_refund_no = None
        self._channel_order_no = None
        self._created_by_type = None
        self._refund_date = None
        self._external_batch_no = None
        self._channel_acknowledged_date = None
        self._merchant_acknowledged_date = None
        self._order_id = None
        self._channel_id = None
        self._return_id = None
        self._currency = None
        self._lines = None
        self._created_at = None
        self._updated_at = None
        self._deleted_at = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if reason is not None:
            self.reason = reason
        if channel_export_status is not None:
            self.channel_export_status = channel_export_status
        if sub_total_incl_tax is not None:
            self.sub_total_incl_tax = sub_total_incl_tax
        if original_sub_total_incl_tax is not None:
            self.original_sub_total_incl_tax = original_sub_total_incl_tax
        if additional_amount_incl_tax is not None:
            self.additional_amount_incl_tax = additional_amount_incl_tax
        if original_additional_amount_incl_tax is not None:
            self.original_additional_amount_incl_tax = original_additional_amount_incl_tax
        if shipping_cost_incl_tax is not None:
            self.shipping_cost_incl_tax = shipping_cost_incl_tax
        if original_shipping_cost_incl_tax is not None:
            self.original_shipping_cost_incl_tax = original_shipping_cost_incl_tax
        if total_incl_tax is not None:
            self.total_incl_tax = total_incl_tax
        if original_total_incl_tax is not None:
            self.original_total_incl_tax = original_total_incl_tax
        if merchant_comment is not None:
            self.merchant_comment = merchant_comment
        if merchant_refund_no is not None:
            self.merchant_refund_no = merchant_refund_no
        if channel_refund_no is not None:
            self.channel_refund_no = channel_refund_no
        if channel_order_no is not None:
            self.channel_order_no = channel_order_no
        if created_by_type is not None:
            self.created_by_type = created_by_type
        if refund_date is not None:
            self.refund_date = refund_date
        if external_batch_no is not None:
            self.external_batch_no = external_batch_no
        if channel_acknowledged_date is not None:
            self.channel_acknowledged_date = channel_acknowledged_date
        if merchant_acknowledged_date is not None:
            self.merchant_acknowledged_date = merchant_acknowledged_date
        if order_id is not None:
            self.order_id = order_id
        if channel_id is not None:
            self.channel_id = channel_id
        if return_id is not None:
            self.return_id = return_id
        if currency is not None:
            self.currency = currency
        if lines is not None:
            self.lines = lines
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if deleted_at is not None:
            self.deleted_at = deleted_at

    @property
    def id(self):
        """Gets the id of this IRefund.  # noqa: E501


        :return: The id of this IRefund.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IRefund.


        :param id: The id of this IRefund.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def reason(self):
        """Gets the reason of this IRefund.  # noqa: E501


        :return: The reason of this IRefund.  # noqa: E501
        :rtype: RefundReason
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this IRefund.


        :param reason: The reason of this IRefund.  # noqa: E501
        :type: RefundReason
        """

        self._reason = reason

    @property
    def channel_export_status(self):
        """Gets the channel_export_status of this IRefund.  # noqa: E501


        :return: The channel_export_status of this IRefund.  # noqa: E501
        :rtype: ChannelExportStatus
        """
        return self._channel_export_status

    @channel_export_status.setter
    def channel_export_status(self, channel_export_status):
        """Sets the channel_export_status of this IRefund.


        :param channel_export_status: The channel_export_status of this IRefund.  # noqa: E501
        :type: ChannelExportStatus
        """

        self._channel_export_status = channel_export_status

    @property
    def sub_total_incl_tax(self):
        """Gets the sub_total_incl_tax of this IRefund.  # noqa: E501


        :return: The sub_total_incl_tax of this IRefund.  # noqa: E501
        :rtype: float
        """
        return self._sub_total_incl_tax

    @sub_total_incl_tax.setter
    def sub_total_incl_tax(self, sub_total_incl_tax):
        """Sets the sub_total_incl_tax of this IRefund.


        :param sub_total_incl_tax: The sub_total_incl_tax of this IRefund.  # noqa: E501
        :type: float
        """

        self._sub_total_incl_tax = sub_total_incl_tax

    @property
    def original_sub_total_incl_tax(self):
        """Gets the original_sub_total_incl_tax of this IRefund.  # noqa: E501


        :return: The original_sub_total_incl_tax of this IRefund.  # noqa: E501
        :rtype: float
        """
        return self._original_sub_total_incl_tax

    @original_sub_total_incl_tax.setter
    def original_sub_total_incl_tax(self, original_sub_total_incl_tax):
        """Sets the original_sub_total_incl_tax of this IRefund.


        :param original_sub_total_incl_tax: The original_sub_total_incl_tax of this IRefund.  # noqa: E501
        :type: float
        """

        self._original_sub_total_incl_tax = original_sub_total_incl_tax

    @property
    def additional_amount_incl_tax(self):
        """Gets the additional_amount_incl_tax of this IRefund.  # noqa: E501


        :return: The additional_amount_incl_tax of this IRefund.  # noqa: E501
        :rtype: float
        """
        return self._additional_amount_incl_tax

    @additional_amount_incl_tax.setter
    def additional_amount_incl_tax(self, additional_amount_incl_tax):
        """Sets the additional_amount_incl_tax of this IRefund.


        :param additional_amount_incl_tax: The additional_amount_incl_tax of this IRefund.  # noqa: E501
        :type: float
        """

        self._additional_amount_incl_tax = additional_amount_incl_tax

    @property
    def original_additional_amount_incl_tax(self):
        """Gets the original_additional_amount_incl_tax of this IRefund.  # noqa: E501


        :return: The original_additional_amount_incl_tax of this IRefund.  # noqa: E501
        :rtype: float
        """
        return self._original_additional_amount_incl_tax

    @original_additional_amount_incl_tax.setter
    def original_additional_amount_incl_tax(self, original_additional_amount_incl_tax):
        """Sets the original_additional_amount_incl_tax of this IRefund.


        :param original_additional_amount_incl_tax: The original_additional_amount_incl_tax of this IRefund.  # noqa: E501
        :type: float
        """

        self._original_additional_amount_incl_tax = original_additional_amount_incl_tax

    @property
    def shipping_cost_incl_tax(self):
        """Gets the shipping_cost_incl_tax of this IRefund.  # noqa: E501


        :return: The shipping_cost_incl_tax of this IRefund.  # noqa: E501
        :rtype: float
        """
        return self._shipping_cost_incl_tax

    @shipping_cost_incl_tax.setter
    def shipping_cost_incl_tax(self, shipping_cost_incl_tax):
        """Sets the shipping_cost_incl_tax of this IRefund.


        :param shipping_cost_incl_tax: The shipping_cost_incl_tax of this IRefund.  # noqa: E501
        :type: float
        """

        self._shipping_cost_incl_tax = shipping_cost_incl_tax

    @property
    def original_shipping_cost_incl_tax(self):
        """Gets the original_shipping_cost_incl_tax of this IRefund.  # noqa: E501


        :return: The original_shipping_cost_incl_tax of this IRefund.  # noqa: E501
        :rtype: float
        """
        return self._original_shipping_cost_incl_tax

    @original_shipping_cost_incl_tax.setter
    def original_shipping_cost_incl_tax(self, original_shipping_cost_incl_tax):
        """Sets the original_shipping_cost_incl_tax of this IRefund.


        :param original_shipping_cost_incl_tax: The original_shipping_cost_incl_tax of this IRefund.  # noqa: E501
        :type: float
        """

        self._original_shipping_cost_incl_tax = original_shipping_cost_incl_tax

    @property
    def total_incl_tax(self):
        """Gets the total_incl_tax of this IRefund.  # noqa: E501


        :return: The total_incl_tax of this IRefund.  # noqa: E501
        :rtype: float
        """
        return self._total_incl_tax

    @total_incl_tax.setter
    def total_incl_tax(self, total_incl_tax):
        """Sets the total_incl_tax of this IRefund.


        :param total_incl_tax: The total_incl_tax of this IRefund.  # noqa: E501
        :type: float
        """

        self._total_incl_tax = total_incl_tax

    @property
    def original_total_incl_tax(self):
        """Gets the original_total_incl_tax of this IRefund.  # noqa: E501


        :return: The original_total_incl_tax of this IRefund.  # noqa: E501
        :rtype: float
        """
        return self._original_total_incl_tax

    @original_total_incl_tax.setter
    def original_total_incl_tax(self, original_total_incl_tax):
        """Sets the original_total_incl_tax of this IRefund.


        :param original_total_incl_tax: The original_total_incl_tax of this IRefund.  # noqa: E501
        :type: float
        """

        self._original_total_incl_tax = original_total_incl_tax

    @property
    def merchant_comment(self):
        """Gets the merchant_comment of this IRefund.  # noqa: E501


        :return: The merchant_comment of this IRefund.  # noqa: E501
        :rtype: str
        """
        return self._merchant_comment

    @merchant_comment.setter
    def merchant_comment(self, merchant_comment):
        """Sets the merchant_comment of this IRefund.


        :param merchant_comment: The merchant_comment of this IRefund.  # noqa: E501
        :type: str
        """

        self._merchant_comment = merchant_comment

    @property
    def merchant_refund_no(self):
        """Gets the merchant_refund_no of this IRefund.  # noqa: E501


        :return: The merchant_refund_no of this IRefund.  # noqa: E501
        :rtype: str
        """
        return self._merchant_refund_no

    @merchant_refund_no.setter
    def merchant_refund_no(self, merchant_refund_no):
        """Sets the merchant_refund_no of this IRefund.


        :param merchant_refund_no: The merchant_refund_no of this IRefund.  # noqa: E501
        :type: str
        """

        self._merchant_refund_no = merchant_refund_no

    @property
    def channel_refund_no(self):
        """Gets the channel_refund_no of this IRefund.  # noqa: E501


        :return: The channel_refund_no of this IRefund.  # noqa: E501
        :rtype: str
        """
        return self._channel_refund_no

    @channel_refund_no.setter
    def channel_refund_no(self, channel_refund_no):
        """Sets the channel_refund_no of this IRefund.


        :param channel_refund_no: The channel_refund_no of this IRefund.  # noqa: E501
        :type: str
        """

        self._channel_refund_no = channel_refund_no

    @property
    def channel_order_no(self):
        """Gets the channel_order_no of this IRefund.  # noqa: E501


        :return: The channel_order_no of this IRefund.  # noqa: E501
        :rtype: str
        """
        return self._channel_order_no

    @channel_order_no.setter
    def channel_order_no(self, channel_order_no):
        """Sets the channel_order_no of this IRefund.


        :param channel_order_no: The channel_order_no of this IRefund.  # noqa: E501
        :type: str
        """

        self._channel_order_no = channel_order_no

    @property
    def created_by_type(self):
        """Gets the created_by_type of this IRefund.  # noqa: E501


        :return: The created_by_type of this IRefund.  # noqa: E501
        :rtype: CreatedByType
        """
        return self._created_by_type

    @created_by_type.setter
    def created_by_type(self, created_by_type):
        """Sets the created_by_type of this IRefund.


        :param created_by_type: The created_by_type of this IRefund.  # noqa: E501
        :type: CreatedByType
        """

        self._created_by_type = created_by_type

    @property
    def refund_date(self):
        """Gets the refund_date of this IRefund.  # noqa: E501


        :return: The refund_date of this IRefund.  # noqa: E501
        :rtype: datetime
        """
        return self._refund_date

    @refund_date.setter
    def refund_date(self, refund_date):
        """Sets the refund_date of this IRefund.


        :param refund_date: The refund_date of this IRefund.  # noqa: E501
        :type: datetime
        """

        self._refund_date = refund_date

    @property
    def external_batch_no(self):
        """Gets the external_batch_no of this IRefund.  # noqa: E501


        :return: The external_batch_no of this IRefund.  # noqa: E501
        :rtype: str
        """
        return self._external_batch_no

    @external_batch_no.setter
    def external_batch_no(self, external_batch_no):
        """Sets the external_batch_no of this IRefund.


        :param external_batch_no: The external_batch_no of this IRefund.  # noqa: E501
        :type: str
        """

        self._external_batch_no = external_batch_no

    @property
    def channel_acknowledged_date(self):
        """Gets the channel_acknowledged_date of this IRefund.  # noqa: E501


        :return: The channel_acknowledged_date of this IRefund.  # noqa: E501
        :rtype: datetime
        """
        return self._channel_acknowledged_date

    @channel_acknowledged_date.setter
    def channel_acknowledged_date(self, channel_acknowledged_date):
        """Sets the channel_acknowledged_date of this IRefund.


        :param channel_acknowledged_date: The channel_acknowledged_date of this IRefund.  # noqa: E501
        :type: datetime
        """

        self._channel_acknowledged_date = channel_acknowledged_date

    @property
    def merchant_acknowledged_date(self):
        """Gets the merchant_acknowledged_date of this IRefund.  # noqa: E501


        :return: The merchant_acknowledged_date of this IRefund.  # noqa: E501
        :rtype: datetime
        """
        return self._merchant_acknowledged_date

    @merchant_acknowledged_date.setter
    def merchant_acknowledged_date(self, merchant_acknowledged_date):
        """Sets the merchant_acknowledged_date of this IRefund.


        :param merchant_acknowledged_date: The merchant_acknowledged_date of this IRefund.  # noqa: E501
        :type: datetime
        """

        self._merchant_acknowledged_date = merchant_acknowledged_date

    @property
    def order_id(self):
        """Gets the order_id of this IRefund.  # noqa: E501


        :return: The order_id of this IRefund.  # noqa: E501
        :rtype: int
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this IRefund.


        :param order_id: The order_id of this IRefund.  # noqa: E501
        :type: int
        """

        self._order_id = order_id

    @property
    def channel_id(self):
        """Gets the channel_id of this IRefund.  # noqa: E501


        :return: The channel_id of this IRefund.  # noqa: E501
        :rtype: int
        """
        return self._channel_id

    @channel_id.setter
    def channel_id(self, channel_id):
        """Sets the channel_id of this IRefund.


        :param channel_id: The channel_id of this IRefund.  # noqa: E501
        :type: int
        """

        self._channel_id = channel_id

    @property
    def return_id(self):
        """Gets the return_id of this IRefund.  # noqa: E501


        :return: The return_id of this IRefund.  # noqa: E501
        :rtype: int
        """
        return self._return_id

    @return_id.setter
    def return_id(self, return_id):
        """Sets the return_id of this IRefund.


        :param return_id: The return_id of this IRefund.  # noqa: E501
        :type: int
        """

        self._return_id = return_id

    @property
    def currency(self):
        """Gets the currency of this IRefund.  # noqa: E501


        :return: The currency of this IRefund.  # noqa: E501
        :rtype: IRefundCurrency
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this IRefund.


        :param currency: The currency of this IRefund.  # noqa: E501
        :type: IRefundCurrency
        """

        self._currency = currency

    @property
    def lines(self):
        """Gets the lines of this IRefund.  # noqa: E501


        :return: The lines of this IRefund.  # noqa: E501
        :rtype: list[IRefundLine]
        """
        return self._lines

    @lines.setter
    def lines(self, lines):
        """Sets the lines of this IRefund.


        :param lines: The lines of this IRefund.  # noqa: E501
        :type: list[IRefundLine]
        """

        self._lines = lines

    @property
    def created_at(self):
        """Gets the created_at of this IRefund.  # noqa: E501


        :return: The created_at of this IRefund.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this IRefund.


        :param created_at: The created_at of this IRefund.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this IRefund.  # noqa: E501


        :return: The updated_at of this IRefund.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this IRefund.


        :param updated_at: The updated_at of this IRefund.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def deleted_at(self):
        """Gets the deleted_at of this IRefund.  # noqa: E501


        :return: The deleted_at of this IRefund.  # noqa: E501
        :rtype: datetime
        """
        return self._deleted_at

    @deleted_at.setter
    def deleted_at(self, deleted_at):
        """Sets the deleted_at of this IRefund.


        :param deleted_at: The deleted_at of this IRefund.  # noqa: E501
        :type: datetime
        """

        self._deleted_at = deleted_at

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
        if issubclass(IRefund, dict):
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
        if not isinstance(other, IRefund):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
