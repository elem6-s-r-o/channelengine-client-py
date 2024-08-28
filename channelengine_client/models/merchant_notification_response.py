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

class MerchantNotificationResponse(object):
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
        'read': 'bool',
        'created_at': 'datetime',
        'message': 'str',
        'subject': 'str',
        'count': 'int',
        'type': 'NotificationType'
    }

    attribute_map = {
        'id': 'Id',
        'read': 'Read',
        'created_at': 'CreatedAt',
        'message': 'Message',
        'subject': 'Subject',
        'count': 'Count',
        'type': 'Type'
    }

    def __init__(self, id=None, read=None, created_at=None, message=None, subject=None, count=None, type=None):  # noqa: E501
        """MerchantNotificationResponse - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._read = None
        self._created_at = None
        self._message = None
        self._subject = None
        self._count = None
        self._type = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if read is not None:
            self.read = read
        if created_at is not None:
            self.created_at = created_at
        if message is not None:
            self.message = message
        if subject is not None:
            self.subject = subject
        if count is not None:
            self.count = count
        if type is not None:
            self.type = type

    @property
    def id(self):
        """Gets the id of this MerchantNotificationResponse.  # noqa: E501

        Unique identifier used by ChannelEngine.  # noqa: E501

        :return: The id of this MerchantNotificationResponse.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MerchantNotificationResponse.

        Unique identifier used by ChannelEngine.  # noqa: E501

        :param id: The id of this MerchantNotificationResponse.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def read(self):
        """Gets the read of this MerchantNotificationResponse.  # noqa: E501

        Indicating whether the notification is already read using the backoffice.  # noqa: E501

        :return: The read of this MerchantNotificationResponse.  # noqa: E501
        :rtype: bool
        """
        return self._read

    @read.setter
    def read(self, read):
        """Sets the read of this MerchantNotificationResponse.

        Indicating whether the notification is already read using the backoffice.  # noqa: E501

        :param read: The read of this MerchantNotificationResponse.  # noqa: E501
        :type: bool
        """

        self._read = read

    @property
    def created_at(self):
        """Gets the created_at of this MerchantNotificationResponse.  # noqa: E501

        Get the created date time.  # noqa: E501

        :return: The created_at of this MerchantNotificationResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this MerchantNotificationResponse.

        Get the created date time.  # noqa: E501

        :param created_at: The created_at of this MerchantNotificationResponse.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def message(self):
        """Gets the message of this MerchantNotificationResponse.  # noqa: E501


        :return: The message of this MerchantNotificationResponse.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this MerchantNotificationResponse.


        :param message: The message of this MerchantNotificationResponse.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def subject(self):
        """Gets the subject of this MerchantNotificationResponse.  # noqa: E501


        :return: The subject of this MerchantNotificationResponse.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this MerchantNotificationResponse.


        :param subject: The subject of this MerchantNotificationResponse.  # noqa: E501
        :type: str
        """

        self._subject = subject

    @property
    def count(self):
        """Gets the count of this MerchantNotificationResponse.  # noqa: E501


        :return: The count of this MerchantNotificationResponse.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this MerchantNotificationResponse.


        :param count: The count of this MerchantNotificationResponse.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def type(self):
        """Gets the type of this MerchantNotificationResponse.  # noqa: E501


        :return: The type of this MerchantNotificationResponse.  # noqa: E501
        :rtype: NotificationType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this MerchantNotificationResponse.


        :param type: The type of this MerchantNotificationResponse.  # noqa: E501
        :type: NotificationType
        """

        self._type = type

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
        if issubclass(MerchantNotificationResponse, dict):
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
        if not isinstance(other, MerchantNotificationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
