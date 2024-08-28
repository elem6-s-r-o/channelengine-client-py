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

class MerchantGetReportStatusResponse(object):
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
        'status': 'ReportStatus',
        'resource_url': 'str'
    }

    attribute_map = {
        'status': 'Status',
        'resource_url': 'ResourceUrl'
    }

    def __init__(self, status=None, resource_url=None):  # noqa: E501
        """MerchantGetReportStatusResponse - a model defined in Swagger"""  # noqa: E501
        self._status = None
        self._resource_url = None
        self.discriminator = None
        if status is not None:
            self.status = status
        if resource_url is not None:
            self.resource_url = resource_url

    @property
    def status(self):
        """Gets the status of this MerchantGetReportStatusResponse.  # noqa: E501


        :return: The status of this MerchantGetReportStatusResponse.  # noqa: E501
        :rtype: ReportStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this MerchantGetReportStatusResponse.


        :param status: The status of this MerchantGetReportStatusResponse.  # noqa: E501
        :type: ReportStatus
        """

        self._status = status

    @property
    def resource_url(self):
        """Gets the resource_url of this MerchantGetReportStatusResponse.  # noqa: E501


        :return: The resource_url of this MerchantGetReportStatusResponse.  # noqa: E501
        :rtype: str
        """
        return self._resource_url

    @resource_url.setter
    def resource_url(self, resource_url):
        """Sets the resource_url of this MerchantGetReportStatusResponse.


        :param resource_url: The resource_url of this MerchantGetReportStatusResponse.  # noqa: E501
        :type: str
        """

        self._resource_url = resource_url

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
        if issubclass(MerchantGetReportStatusResponse, dict):
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
        if not isinstance(other, MerchantGetReportStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other