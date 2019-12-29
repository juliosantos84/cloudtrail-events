# coding: utf-8
import pprint
import re  # noqa: F401

import six
from enum import Enum
from schema.aws.kms.awsapicallviacloudtrail.EncryptionContext import EncryptionContext  # noqa: F401,E501

class RequestParameters(object):


    _types = {
        'encryptionContext': 'EncryptionContext',
        'keyId': 'str',
        'keySpec': 'str'
    }

    _attribute_map = {
        'encryptionContext': 'encryptionContext',
        'keyId': 'keyId',
        'keySpec': 'keySpec'
    }

    def __init__(self, encryptionContext=None, keyId=None, keySpec=None):  # noqa: E501
        self._encryptionContext = None
        self._keyId = None
        self._keySpec = None
        self.discriminator = None
        self.encryptionContext = encryptionContext
        self.keyId = keyId
        self.keySpec = keySpec


    @property
    def encryptionContext(self):

        return self._encryptionContext

    @encryptionContext.setter
    def encryptionContext(self, encryptionContext):


        self._encryptionContext = encryptionContext


    @property
    def keyId(self):

        return self._keyId

    @keyId.setter
    def keyId(self, keyId):


        self._keyId = keyId


    @property
    def keySpec(self):

        return self._keySpec

    @keySpec.setter
    def keySpec(self, keySpec):


        self._keySpec = keySpec

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
        if issubclass(RequestParameters, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, RequestParameters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

