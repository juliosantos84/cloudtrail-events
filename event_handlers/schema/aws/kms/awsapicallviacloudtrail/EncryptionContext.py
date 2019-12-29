# coding: utf-8
import pprint
import re  # noqa: F401

import six
from enum import Enum

class EncryptionContext(object):


    _types = {
        'aws_s3_arn': 'str'
    }

    _attribute_map = {
        'aws_s3_arn': 'aws:s3:arn'
    }

    def __init__(self, aws_s3_arn=None):  # noqa: E501
        self._aws_s3_arn = None
        self.discriminator = None
        self.aws_s3_arn = aws_s3_arn


    @property
    def aws_s3_arn(self):

        return self._aws_s3_arn

    @aws_s3_arn.setter
    def aws_s3_arn(self, aws_s3_arn):


        self._aws_s3_arn = aws_s3_arn

    def to_dict(self):
        result = {}

        for attr, _ in six.iteritems(self._types):
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
        if issubclass(EncryptionContext, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, EncryptionContext):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

