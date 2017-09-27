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


class GifImages(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, fixed_height=None, fixed_height_still=None, fixed_height_downsampled=None, fixed_width=None, fixed_width_still=None, fixed_width_downsampled=None, fixed_height_small=None, fixed_height_small_still=None, fixed_width_small=None, fixed_width_small_still=None, downsized=None, downsized_still=None, downsized_large=None, downsized_medium=None, downsized_small=None, original=None, original_still=None, looping=None, preview=None, preview_gif=None):
        """
        GifImages - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'fixed_height': 'GifImagesFixedHeight',
            'fixed_height_still': 'GifImagesFixedHeightStill',
            'fixed_height_downsampled': 'GifImagesFixedHeightDownsampled',
            'fixed_width': 'GifImagesFixedWidth',
            'fixed_width_still': 'GifImagesFixedWidthStill',
            'fixed_width_downsampled': 'GifImagesFixedWidthDownsampled',
            'fixed_height_small': 'GifImagesFixedHeightSmall',
            'fixed_height_small_still': 'GifImagesFixedHeightSmallStill',
            'fixed_width_small': 'GifImagesFixedWidthSmall',
            'fixed_width_small_still': 'GifImagesFixedWidthSmallStill',
            'downsized': 'GifImagesDownsized',
            'downsized_still': 'GifImagesDownsizedStill',
            'downsized_large': 'GifImagesDownsizedLarge',
            'downsized_medium': 'GifImagesDownsizedMedium',
            'downsized_small': 'GifImagesDownsizedSmall',
            'original': 'GifImagesOriginal',
            'original_still': 'GifImagesOriginalStill',
            'looping': 'GifImagesLooping',
            'preview': 'GifImagesPreview',
            'preview_gif': 'GifImagesPreviewGif'
        }

        self.attribute_map = {
            'fixed_height': 'fixed_height',
            'fixed_height_still': 'fixed_height_still',
            'fixed_height_downsampled': 'fixed_height_downsampled',
            'fixed_width': 'fixed_width',
            'fixed_width_still': 'fixed_width_still',
            'fixed_width_downsampled': 'fixed_width_downsampled',
            'fixed_height_small': 'fixed_height_small',
            'fixed_height_small_still': 'fixed_height_small_still',
            'fixed_width_small': 'fixed_width_small',
            'fixed_width_small_still': 'fixed_width_small_still',
            'downsized': 'downsized',
            'downsized_still': 'downsized_still',
            'downsized_large': 'downsized_large',
            'downsized_medium': 'downsized_medium',
            'downsized_small': 'downsized_small',
            'original': 'original',
            'original_still': 'original_still',
            'looping': 'looping',
            'preview': 'preview',
            'preview_gif': 'preview_gif'
        }

        self._fixed_height = fixed_height
        self._fixed_height_still = fixed_height_still
        self._fixed_height_downsampled = fixed_height_downsampled
        self._fixed_width = fixed_width
        self._fixed_width_still = fixed_width_still
        self._fixed_width_downsampled = fixed_width_downsampled
        self._fixed_height_small = fixed_height_small
        self._fixed_height_small_still = fixed_height_small_still
        self._fixed_width_small = fixed_width_small
        self._fixed_width_small_still = fixed_width_small_still
        self._downsized = downsized
        self._downsized_still = downsized_still
        self._downsized_large = downsized_large
        self._downsized_medium = downsized_medium
        self._downsized_small = downsized_small
        self._original = original
        self._original_still = original_still
        self._looping = looping
        self._preview = preview
        self._preview_gif = preview_gif

    @property
    def fixed_height(self):
        """
        Gets the fixed_height of this GifImages.

        :return: The fixed_height of this GifImages.
        :rtype: GifImagesFixedHeight
        """
        return self._fixed_height

    @fixed_height.setter
    def fixed_height(self, fixed_height):
        """
        Sets the fixed_height of this GifImages.

        :param fixed_height: The fixed_height of this GifImages.
        :type: GifImagesFixedHeight
        """

        self._fixed_height = fixed_height

    @property
    def fixed_height_still(self):
        """
        Gets the fixed_height_still of this GifImages.

        :return: The fixed_height_still of this GifImages.
        :rtype: GifImagesFixedHeightStill
        """
        return self._fixed_height_still

    @fixed_height_still.setter
    def fixed_height_still(self, fixed_height_still):
        """
        Sets the fixed_height_still of this GifImages.

        :param fixed_height_still: The fixed_height_still of this GifImages.
        :type: GifImagesFixedHeightStill
        """

        self._fixed_height_still = fixed_height_still

    @property
    def fixed_height_downsampled(self):
        """
        Gets the fixed_height_downsampled of this GifImages.

        :return: The fixed_height_downsampled of this GifImages.
        :rtype: GifImagesFixedHeightDownsampled
        """
        return self._fixed_height_downsampled

    @fixed_height_downsampled.setter
    def fixed_height_downsampled(self, fixed_height_downsampled):
        """
        Sets the fixed_height_downsampled of this GifImages.

        :param fixed_height_downsampled: The fixed_height_downsampled of this GifImages.
        :type: GifImagesFixedHeightDownsampled
        """

        self._fixed_height_downsampled = fixed_height_downsampled

    @property
    def fixed_width(self):
        """
        Gets the fixed_width of this GifImages.

        :return: The fixed_width of this GifImages.
        :rtype: GifImagesFixedWidth
        """
        return self._fixed_width

    @fixed_width.setter
    def fixed_width(self, fixed_width):
        """
        Sets the fixed_width of this GifImages.

        :param fixed_width: The fixed_width of this GifImages.
        :type: GifImagesFixedWidth
        """

        self._fixed_width = fixed_width

    @property
    def fixed_width_still(self):
        """
        Gets the fixed_width_still of this GifImages.

        :return: The fixed_width_still of this GifImages.
        :rtype: GifImagesFixedWidthStill
        """
        return self._fixed_width_still

    @fixed_width_still.setter
    def fixed_width_still(self, fixed_width_still):
        """
        Sets the fixed_width_still of this GifImages.

        :param fixed_width_still: The fixed_width_still of this GifImages.
        :type: GifImagesFixedWidthStill
        """

        self._fixed_width_still = fixed_width_still

    @property
    def fixed_width_downsampled(self):
        """
        Gets the fixed_width_downsampled of this GifImages.

        :return: The fixed_width_downsampled of this GifImages.
        :rtype: GifImagesFixedWidthDownsampled
        """
        return self._fixed_width_downsampled

    @fixed_width_downsampled.setter
    def fixed_width_downsampled(self, fixed_width_downsampled):
        """
        Sets the fixed_width_downsampled of this GifImages.

        :param fixed_width_downsampled: The fixed_width_downsampled of this GifImages.
        :type: GifImagesFixedWidthDownsampled
        """

        self._fixed_width_downsampled = fixed_width_downsampled

    @property
    def fixed_height_small(self):
        """
        Gets the fixed_height_small of this GifImages.

        :return: The fixed_height_small of this GifImages.
        :rtype: GifImagesFixedHeightSmall
        """
        return self._fixed_height_small

    @fixed_height_small.setter
    def fixed_height_small(self, fixed_height_small):
        """
        Sets the fixed_height_small of this GifImages.

        :param fixed_height_small: The fixed_height_small of this GifImages.
        :type: GifImagesFixedHeightSmall
        """

        self._fixed_height_small = fixed_height_small

    @property
    def fixed_height_small_still(self):
        """
        Gets the fixed_height_small_still of this GifImages.

        :return: The fixed_height_small_still of this GifImages.
        :rtype: GifImagesFixedHeightSmallStill
        """
        return self._fixed_height_small_still

    @fixed_height_small_still.setter
    def fixed_height_small_still(self, fixed_height_small_still):
        """
        Sets the fixed_height_small_still of this GifImages.

        :param fixed_height_small_still: The fixed_height_small_still of this GifImages.
        :type: GifImagesFixedHeightSmallStill
        """

        self._fixed_height_small_still = fixed_height_small_still

    @property
    def fixed_width_small(self):
        """
        Gets the fixed_width_small of this GifImages.

        :return: The fixed_width_small of this GifImages.
        :rtype: GifImagesFixedWidthSmall
        """
        return self._fixed_width_small

    @fixed_width_small.setter
    def fixed_width_small(self, fixed_width_small):
        """
        Sets the fixed_width_small of this GifImages.

        :param fixed_width_small: The fixed_width_small of this GifImages.
        :type: GifImagesFixedWidthSmall
        """

        self._fixed_width_small = fixed_width_small

    @property
    def fixed_width_small_still(self):
        """
        Gets the fixed_width_small_still of this GifImages.

        :return: The fixed_width_small_still of this GifImages.
        :rtype: GifImagesFixedWidthSmallStill
        """
        return self._fixed_width_small_still

    @fixed_width_small_still.setter
    def fixed_width_small_still(self, fixed_width_small_still):
        """
        Sets the fixed_width_small_still of this GifImages.

        :param fixed_width_small_still: The fixed_width_small_still of this GifImages.
        :type: GifImagesFixedWidthSmallStill
        """

        self._fixed_width_small_still = fixed_width_small_still

    @property
    def downsized(self):
        """
        Gets the downsized of this GifImages.

        :return: The downsized of this GifImages.
        :rtype: GifImagesDownsized
        """
        return self._downsized

    @downsized.setter
    def downsized(self, downsized):
        """
        Sets the downsized of this GifImages.

        :param downsized: The downsized of this GifImages.
        :type: GifImagesDownsized
        """

        self._downsized = downsized

    @property
    def downsized_still(self):
        """
        Gets the downsized_still of this GifImages.

        :return: The downsized_still of this GifImages.
        :rtype: GifImagesDownsizedStill
        """
        return self._downsized_still

    @downsized_still.setter
    def downsized_still(self, downsized_still):
        """
        Sets the downsized_still of this GifImages.

        :param downsized_still: The downsized_still of this GifImages.
        :type: GifImagesDownsizedStill
        """

        self._downsized_still = downsized_still

    @property
    def downsized_large(self):
        """
        Gets the downsized_large of this GifImages.

        :return: The downsized_large of this GifImages.
        :rtype: GifImagesDownsizedLarge
        """
        return self._downsized_large

    @downsized_large.setter
    def downsized_large(self, downsized_large):
        """
        Sets the downsized_large of this GifImages.

        :param downsized_large: The downsized_large of this GifImages.
        :type: GifImagesDownsizedLarge
        """

        self._downsized_large = downsized_large

    @property
    def downsized_medium(self):
        """
        Gets the downsized_medium of this GifImages.

        :return: The downsized_medium of this GifImages.
        :rtype: GifImagesDownsizedMedium
        """
        return self._downsized_medium

    @downsized_medium.setter
    def downsized_medium(self, downsized_medium):
        """
        Sets the downsized_medium of this GifImages.

        :param downsized_medium: The downsized_medium of this GifImages.
        :type: GifImagesDownsizedMedium
        """

        self._downsized_medium = downsized_medium

    @property
    def downsized_small(self):
        """
        Gets the downsized_small of this GifImages.

        :return: The downsized_small of this GifImages.
        :rtype: GifImagesDownsizedSmall
        """
        return self._downsized_small

    @downsized_small.setter
    def downsized_small(self, downsized_small):
        """
        Sets the downsized_small of this GifImages.

        :param downsized_small: The downsized_small of this GifImages.
        :type: GifImagesDownsizedSmall
        """

        self._downsized_small = downsized_small

    @property
    def original(self):
        """
        Gets the original of this GifImages.

        :return: The original of this GifImages.
        :rtype: GifImagesOriginal
        """
        return self._original

    @original.setter
    def original(self, original):
        """
        Sets the original of this GifImages.

        :param original: The original of this GifImages.
        :type: GifImagesOriginal
        """

        self._original = original

    @property
    def original_still(self):
        """
        Gets the original_still of this GifImages.

        :return: The original_still of this GifImages.
        :rtype: GifImagesOriginalStill
        """
        return self._original_still

    @original_still.setter
    def original_still(self, original_still):
        """
        Sets the original_still of this GifImages.

        :param original_still: The original_still of this GifImages.
        :type: GifImagesOriginalStill
        """

        self._original_still = original_still

    @property
    def looping(self):
        """
        Gets the looping of this GifImages.

        :return: The looping of this GifImages.
        :rtype: GifImagesLooping
        """
        return self._looping

    @looping.setter
    def looping(self, looping):
        """
        Sets the looping of this GifImages.

        :param looping: The looping of this GifImages.
        :type: GifImagesLooping
        """

        self._looping = looping

    @property
    def preview(self):
        """
        Gets the preview of this GifImages.

        :return: The preview of this GifImages.
        :rtype: GifImagesPreview
        """
        return self._preview

    @preview.setter
    def preview(self, preview):
        """
        Sets the preview of this GifImages.

        :param preview: The preview of this GifImages.
        :type: GifImagesPreview
        """

        self._preview = preview

    @property
    def preview_gif(self):
        """
        Gets the preview_gif of this GifImages.

        :return: The preview_gif of this GifImages.
        :rtype: GifImagesPreviewGif
        """
        return self._preview_gif

    @preview_gif.setter
    def preview_gif(self, preview_gif):
        """
        Sets the preview_gif of this GifImages.

        :param preview_gif: The preview_gif of this GifImages.
        :type: GifImagesPreviewGif
        """

        self._preview_gif = preview_gif

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
        if not isinstance(other, GifImages):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
