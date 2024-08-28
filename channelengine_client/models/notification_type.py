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

class NotificationType(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    CHANNEL_ORDER_ANONYMIZED_BY_REQUEST = "CHANNEL_ORDER_ANONYMIZED_BY_REQUEST"
    CHANNEL_ORDER_ANONYMIZED_AUTOMATICALLY = "CHANNEL_ORDER_ANONYMIZED_AUTOMATICALLY"
    CHANNEL_ORDER_CANCELLATION_REQUEST_NEW = "CHANNEL_ORDER_CANCELLATION_REQUEST_NEW"
    CHANNEL_ORDER_CORRECTION_NEEDED = "CHANNEL_ORDER_CORRECTION_NEEDED"
    CHANNEL_ORDER_DUPLICATE_LINE = "CHANNEL_ORDER_DUPLICATE_LINE"
    CHANNEL_ORDER_INVOICE_SEND_FAILED = "CHANNEL_ORDER_INVOICE_SEND_FAILED"
    CHANNEL_ORDER_IMPORT_FAILED = "CHANNEL_ORDER_IMPORT_FAILED"
    CHANNEL_ORDER_NEW = "CHANNEL_ORDER_NEW"
    CHANNEL_ORDER_OVERDUE = "CHANNEL_ORDER_OVERDUE"
    CHANNEL_PRODUCT_DATA_EXPORT_FAILED = "CHANNEL_PRODUCT_DATA_EXPORT_FAILED"
    CHANNEL_PRODUCT_DATA_IMPORT_FAILED = "CHANNEL_PRODUCT_DATA_IMPORT_FAILED"
    CHANNEL_RETURN_EXPORT_FAILED = "CHANNEL_RETURN_EXPORT_FAILED"
    CHANNEL_RETURN_IMPORT_FAILED = "CHANNEL_RETURN_IMPORT_FAILED"
    CHANNEL_RETURN_NEW = "CHANNEL_RETURN_NEW"
    CHANNEL_RETURN_OVERDUE = "CHANNEL_RETURN_OVERDUE"
    CHANNEL_REFUND_EXPORT_FAILED = "CHANNEL_REFUND_EXPORT_FAILED"
    CHANNEL_SHIPMENT_IMPORT_FAILED = "CHANNEL_SHIPMENT_IMPORT_FAILED"
    CHANNEL_SHIPMENT_IMPORT_STATUS_FAILED = "CHANNEL_SHIPMENT_IMPORT_STATUS_FAILED"
    CHANNEL_SHIPMENT_EXPORT_FAILED = "CHANNEL_SHIPMENT_EXPORT_FAILED"
    CHANNEL_SHIPMENT_IMPORT_MISSING_LINE_FAILED = "CHANNEL_SHIPMENT_IMPORT_MISSING_LINE_FAILED"
    CHANNEL_FULFILLMENT_SHIPMENT_IMPORT_STATUS_FAILED = "CHANNEL_FULFILLMENT_SHIPMENT_IMPORT_STATUS_FAILED"
    CHANNEL_FULFILLMENT_SHIPMENT_EXPORT_FAILED = "CHANNEL_FULFILLMENT_SHIPMENT_EXPORT_FAILED"
    CHANNEL_FULFILLMENT_SHIPMENT_EXPORT_SUCCEEDED = "CHANNEL_FULFILLMENT_SHIPMENT_EXPORT_SUCCEEDED"
    CHANNEL_FULFILLMENT_SHIPMENT_LINE_FOR_CLOSED_ORDER = "CHANNEL_FULFILLMENT_SHIPMENT_LINE_FOR_CLOSED_ORDER"
    CHANNELENGINE_SUPPORT_NOTIFICATION = "CHANNELENGINE_SUPPORT_NOTIFICATION"
    CHANNELENGINE_WEBHOOK_RQUEST_FAILED = "CHANNELENGINE_WEBHOOK_RQUEST_FAILED"
    FEED_NO_PRODUCTS_FAILED = "FEED_NO_PRODUCTS_FAILED"
    FEED_IMPORT_FAILED = "FEED_IMPORT_FAILED"
    GLOBAL_MESSAGE = "GLOBAL_MESSAGE"
    MERCHANT_ORDER_EXPORT_FAILED = "MERCHANT_ORDER_EXPORT_FAILED"
    PLUGIN_INVALID_SETTING = "PLUGIN_INVALID_SETTING"
    PLUGIN_DEACTIVATED = "PLUGIN_DEACTIVATED"
    PRODUCT_BUNDLE_IMPORT_FAILED = "PRODUCT_BUNDLE_IMPORT_FAILED"
    CHANNEL_REFUND_LINE_ITEMS_ERROR = "CHANNEL_REFUND_LINE_ITEMS_ERROR"
    CHANNEL_CANCELLATION_EXPORT_FAILED = "CHANNEL_CANCELLATION_EXPORT_FAILED"
    MERCHANT_ORDER_EXPORT_LINES_CANCELLED = "MERCHANT_ORDER_EXPORT_LINES_CANCELLED"
    OAUTH_REFRESH_TOKEN_ABOUT_TO_EXPIRE = "OAUTH_REFRESH_TOKEN_ABOUT_TO_EXPIRE"
    MERCHANT_CANCELLATION_IMPORT_FAILED = "MERCHANT_CANCELLATION_IMPORT_FAILED"
    CHANNEL_ORDER_TOO_LONG_ON_NEW = "CHANNEL_ORDER_TOO_LONG_ON_NEW"
    MERCHANT_STOCK_UPDATE_FAILED = "MERCHANT_STOCK_UPDATE_FAILED"
    FEED_INVALID_PRODUCTS_OCCURED = "FEED_INVALID_PRODUCTS_OCCURED"
    CHANNEL_SHIPMENT_EXPORT_INVALID_MERCHANTSHIPMENTNO = "CHANNEL_SHIPMENT_EXPORT_INVALID_MERCHANTSHIPMENTNO"
    CHANNEL_PRODUCT_OFFER_EXPORT_FAILED = "CHANNEL_PRODUCT_OFFER_EXPORT_FAILED"
    TRANSLATION_IMAGE_TAGS_BROKEN = "TRANSLATION_IMAGE_TAGS_BROKEN"
    CHANNEL_RETURN_DELETED = "CHANNEL_RETURN_DELETED"
    TAX_PROVIDER_NOT_ACTIVATED = "TAX_PROVIDER_NOT_ACTIVATED"
    STOCK_LOCATION_NOT_FOUND = "STOCK_LOCATION_NOT_FOUND"
    CUSTOM_VAT_RATE_OVERLAPPING_RATES = "CUSTOM_VAT_RATE_OVERLAPPING_RATES"
    TRANSLATION_FAILED = "TRANSLATION_FAILED"
    ORDER_FALLBACK_TO_DEFAULT_STOCKLOCATION = "ORDER_FALLBACK_TO_DEFAULT_STOCKLOCATION"
    CHANNEL_FULFILLMENT_SHIPMENT_RECEIVED = "CHANNEL_FULFILLMENT_SHIPMENT_RECEIVED"
    TRANSLATION_RETRY = "TRANSLATION_RETRY"
    PLUGIN_SALES_CHANNEL_DEACTIVATED = "PLUGIN_SALES_CHANNEL_DEACTIVATED"
    PLUGIN_CATEGORIES_CHANGED = "PLUGIN_CATEGORIES_CHANGED"
    PLUGIN_ATTRIBUTES_CHANGED = "PLUGIN_ATTRIBUTES_CHANGED"
    ORDER_WITH_BACKORDER_STATUS = "ORDER_WITH_BACKORDER_STATUS"
    ORDER_WITH_BACKORDER_STATUS_FULFILLED = "ORDER_WITH_BACKORDER_STATUS_FULFILLED"
    ORDERS_GOT_REJECTED_BY_MCF = "ORDERS_GOT_REJECTED_BY_MCF"
    PLUGIN_VALIDATION_FAILED = "PLUGIN_VALIDATION_FAILED"
    UPDATE_STOCK_SWITCHED_OFF_FOR_PLUGIN = "UPDATE_STOCK_SWITCHED_OFF_FOR_PLUGIN"
    CHANNEL_RETURN_REQUIRED_ATTENTION = "CHANNEL_RETURN_REQUIRED_ATTENTION"
    CHANNEL_PURCHASE_ORDER_NEW = "CHANNEL_PURCHASE_ORDER_NEW"
    CHANNEL_PURCHASE_ORDER_LINE_CHANGED = "CHANNEL_PURCHASE_ORDER_LINE_CHANGED"
    CHANNEL_PURCHASE_ORDER_LINE_CANCELLED = "CHANNEL_PURCHASE_ORDER_LINE_CANCELLED"
    CHANNEL_PURCHASE_ORDER_ACKNOWLEDGEMENT_FAILED = "CHANNEL_PURCHASE_ORDER_ACKNOWLEDGEMENT_FAILED"
    CHANNEL_PURCHASE_ORDER_SHIPMENT_EXPORT_FAILED = "CHANNEL_PURCHASE_ORDER_SHIPMENT_EXPORT_FAILED"
    CHANNEL_PURCHASE_ORDER_INVOICE_CREATION_FAILED = "CHANNEL_PURCHASE_ORDER_INVOICE_CREATION_FAILED"
    CHANNEL_KPI_TARGET_MISSED = "CHANNEL_KPI_TARGET_MISSED"
    LATE_UNSHIPPED_ORDERS = "LATE_UNSHIPPED_ORDERS"
    FEED_ENABLED = "FEED_ENABLED"
    FEED_DISABLED = "FEED_DISABLED"
    PRODUCT_IMPORT_FEEDS_SUCCESS = "PRODUCT_IMPORT_FEEDS_SUCCESS"
    SETTLEMENT_EXPORT_FAILED = "SETTLEMENT_EXPORT_FAILED"
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
    }

    attribute_map = {
    }

    def __init__(self):  # noqa: E501
        """NotificationType - a model defined in Swagger"""  # noqa: E501
        self.discriminator = None

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
        if issubclass(NotificationType, dict):
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
        if not isinstance(other, NotificationType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
