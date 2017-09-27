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


class GifImagesFixedHeightSmall(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, url=None, width=None, height=None, size=None, mp4=None, mp4_size=None, webp=None, webp_size=None):
        """
        GifImagesFixedHeightSmall - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'url': 'str',
            'width': 'str',
            'height': 'str',
            'size': 'str',
            'mp4': 'str',
            'mp4_size': 'str',
            'webp': 'str',
            'webp_size': 'str'
        }

        self.attribute_map = {
            'url': 'url',
            'width': 'width',
            'height': 'height',
            'size': 'size',
            'mp4': 'mp4',
            'mp4_size': 'mp4_size',
            'webp': 'webp',
            'webp_size': 'webp_size'
        }

        self._url = url
        self._width = width
        self._height = height
        self._size = size
        self._mp4 = mp4
        self._mp4_size = mp4_size
        self._webp = webp
        self._webp_size = webp_size

    @property
    def url(self):
        """
        Gets the url of this GifImagesFixedHeightSmall.
        The publicly-accessible direct URL for this GIF.

        :return: The url of this GifImagesFixedHeightSmall.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this GifImagesFixedHeightSmall.
        The publicly-accessible direct URL for this GIF.

        :param url: The url of this GifImagesFixedHeightSmall.
        :type: str
        """

        self._url = url

    @property
    def width(self):
        """
        Gets the width of this GifImagesFixedHeightSmall.
        The width of this GIF in pixels.

        :return: The width of this GifImagesFixedHeightSmall.
        :rtype: str
        """
        return self._width

    @width.setter
    def width(self, width):
        """
        Sets the width of this GifImagesFixedHeightSmall.
        The width of this GIF in pixels.

        :param width: The width of this GifImagesFixedHeightSmall.
        :type: str
        """

        self._width = width

    @property
    def height(self):
        """
        Gets the height of this GifImagesFixedHeightSmall.
        The height of this GIF in pixels.

        :return: The height of this GifImagesFixedHeightSmall.
        :rtype: str
        """
        return self._height

    @height.setter
    def height(self, height):
        """
        Sets the height of this GifImagesFixedHeightSmall.
        The height of this GIF in pixels.

        :param height: The height of this GifImagesFixedHeightSmall.
        :type: str
        """

        self._height = height

    @property
    def size(self):
        """
        Gets the size of this GifImagesFixedHeightSmall.
        The size of this GIF in bytes.

        :return: The size of this GifImagesFixedHeightSmall.
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        """
        Sets the size of this GifImagesFixedHeightSmall.
        The size of this GIF in bytes.

        :param size: The size of this GifImagesFixedHeightSmall.
        :type: str
        """

        self._size = size

    @property
    def mp4(self):
        """
        Gets the mp4 of this GifImagesFixedHeightSmall.
        The URL for this GIF in .MP4 format.

        :return: The mp4 of this GifImagesFixedHeightSmall.
        :rtype: str
        """
        return self._mp4

    @mp4.setter
    def mp4(self, mp4):
        """
        Sets the mp4 of this GifImagesFixedHeightSmall.
        The URL for this GIF in .MP4 format.

        :param mp4: The mp4 of this GifImagesFixedHeightSmall.
        :type: str
        """

        self._mp4 = mp4

    @property
    def mp4_size(self):
        """
        Gets the mp4_size of this GifImagesFixedHeightSmall.
        The size in bytes of the .MP4 file corresponding to this GIF.

        :return: The mp4_size of this GifImagesFixedHeightSmall.
        :rtype: str
        """
        return self._mp4_size

    @mp4_size.setter
    def mp4_size(self, mp4_size):
        """
        Sets the mp4_size of this GifImagesFixedHeightSmall.
        The size in bytes of the .MP4 file corresponding to this GIF.

        :param mp4_size: The mp4_size of this GifImagesFixedHeightSmall.
        :type: str
        """

        self._mp4_size = mp4_size

    @property
    def webp(self):
        """
        Gets the webp of this GifImagesFixedHeightSmall.
        The URL for this GIF in .webp format.

        :return: The webp of this GifImagesFixedHeightSmall.
        :rtype: str
        """
        return self._webp

    @webp.setter
    def webp(self, webp):
        """
        Sets the webp of this GifImagesFixedHeightSmall.
        The URL for this GIF in .webp format.

        :param webp: The webp of this GifImagesFixedHeightSmall.
        :type: str
        """

        self._webp = webp

    @property
    def webp_size(self):
        """
        Gets the webp_size of this GifImagesFixedHeightSmall.
        The size in bytes of the .webp file corresponding to this GIF.

        :return: The webp_size of this GifImagesFixedHeightSmall.
        :rtype: str
        """
        return self._webp_size

    @webp_size.setter
    def webp_size(self, webp_size):
        """
        Sets the webp_size of this GifImagesFixedHeightSmall.
        The size in bytes of the .webp file corresponding to this GIF.

        :param webp_size: The webp_size of this GifImagesFixedHeightSmall.
        :type: str
        """

        self._webp_size = webp_size

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
        if not isinstance(other, GifImagesFixedHeightSmall):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
