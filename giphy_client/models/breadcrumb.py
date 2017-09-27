# coding: utf-8
#
# Created by David Hargat.
# Copyright © 2017 Giphy. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""
    giphy-api

    Giphy's public api.

    OpenAPI spec version: 0.9.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Breadcrumb(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, url=None, id=None, name=None):
        """
        Breadcrumb - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'url': 'str',
            'id': 'int',
            'name': 'str'
        }

        self.attribute_map = {
            'url': 'url',
            'id': 'id',
            'name': 'name'
        }

        self._url = url
        self._id = id
        self._name = name

    @property
    def url(self):
        """
        Gets the url of this Breadcrumb.

        :return: The url of this Breadcrumb.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this Breadcrumb.

        :param url: The url of this Breadcrumb.
        :type: str
        """

        self._url = url

    @property
    def id(self):
        """
        Gets the id of this Breadcrumb.

        :return: The id of this Breadcrumb.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Breadcrumb.

        :param id: The id of this Breadcrumb.
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this Breadcrumb.

        :return: The name of this Breadcrumb.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Breadcrumb.

        :param name: The name of this Breadcrumb.
        :type: str
        """

        self._name = name

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
        if not isinstance(other, Breadcrumb):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
