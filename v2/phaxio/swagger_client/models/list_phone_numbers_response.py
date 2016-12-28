# coding: utf-8

"""
    Phaxio API

    API Definition for Phaxio

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ListPhoneNumbersResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, success=None, message=None, data=None):
        """
        ListPhoneNumbersResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'success': 'bool',
            'message': 'str',
            'data': 'list[PhoneNumber]'
        }

        self.attribute_map = {
            'success': 'success',
            'message': 'message',
            'data': 'data'
        }

        self._success = success
        self._message = message
        self._data = data

    @property
    def success(self):
        """
        Gets the success of this ListPhoneNumbersResponse.

        :return: The success of this ListPhoneNumbersResponse.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """
        Sets the success of this ListPhoneNumbersResponse.

        :param success: The success of this ListPhoneNumbersResponse.
        :type: bool
        """

        self._success = success

    @property
    def message(self):
        """
        Gets the message of this ListPhoneNumbersResponse.

        :return: The message of this ListPhoneNumbersResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this ListPhoneNumbersResponse.

        :param message: The message of this ListPhoneNumbersResponse.
        :type: str
        """

        self._message = message

    @property
    def data(self):
        """
        Gets the data of this ListPhoneNumbersResponse.

        :return: The data of this ListPhoneNumbersResponse.
        :rtype: list[PhoneNumber]
        """
        return self._data

    @data.setter
    def data(self, data):
        """
        Sets the data of this ListPhoneNumbersResponse.

        :param data: The data of this ListPhoneNumbersResponse.
        :type: list[PhoneNumber]
        """

        self._data = data

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
