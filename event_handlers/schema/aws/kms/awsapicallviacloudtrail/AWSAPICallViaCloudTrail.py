# coding: utf-8
import pprint
import re  # noqa: F401

import six
from enum import Enum
from schema.aws.kms.awsapicallviacloudtrail.AWSAPICallViaCloudTrailItem import AWSAPICallViaCloudTrailItem  # noqa: F401,E501
from schema.aws.kms.awsapicallviacloudtrail.Object import Object  # noqa: F401,E501
from schema.aws.kms.awsapicallviacloudtrail.RequestParameters import RequestParameters  # noqa: F401,E501
from schema.aws.kms.awsapicallviacloudtrail.UserIdentity import UserIdentity  # noqa: F401,E501

class AWSAPICallViaCloudTrail(object):


    _types = {
        'requestParameters': 'RequestParameters',
        'userIdentity': 'UserIdentity',
        'eventID': 'str',
        'awsRegion': 'str',
        'eventVersion': 'str',
        'responseElements': 'Object',
        'sourceIPAddress': 'str',
        'eventSource': 'str',
        'resources': 'list[AWSAPICallViaCloudTrailItem]',
        'userAgent': 'str',
        'readOnly': 'bool',
        'eventType': 'str',
        'requestID': 'str',
        'eventTime': 'datetime',
        'eventName': 'str'
    }

    _attribute_map = {
        'requestParameters': 'requestParameters',
        'userIdentity': 'userIdentity',
        'eventID': 'eventID',
        'awsRegion': 'awsRegion',
        'eventVersion': 'eventVersion',
        'responseElements': 'responseElements',
        'sourceIPAddress': 'sourceIPAddress',
        'eventSource': 'eventSource',
        'resources': 'resources',
        'userAgent': 'userAgent',
        'readOnly': 'readOnly',
        'eventType': 'eventType',
        'requestID': 'requestID',
        'eventTime': 'eventTime',
        'eventName': 'eventName'
    }

    def __init__(self, requestParameters=None, userIdentity=None, eventID=None, awsRegion=None, eventVersion=None, responseElements=None, sourceIPAddress=None, eventSource=None, resources=None, userAgent=None, readOnly=None, eventType=None, requestID=None, eventTime=None, eventName=None):  # noqa: E501
        self._requestParameters = None
        self._userIdentity = None
        self._eventID = None
        self._awsRegion = None
        self._eventVersion = None
        self._responseElements = None
        self._sourceIPAddress = None
        self._eventSource = None
        self._resources = None
        self._userAgent = None
        self._readOnly = None
        self._eventType = None
        self._requestID = None
        self._eventTime = None
        self._eventName = None
        self.discriminator = None
        self.requestParameters = requestParameters
        self.userIdentity = userIdentity
        self.eventID = eventID
        self.awsRegion = awsRegion
        self.eventVersion = eventVersion
        self.responseElements = responseElements
        self.sourceIPAddress = sourceIPAddress
        self.eventSource = eventSource
        self.resources = resources
        self.userAgent = userAgent
        self.readOnly = readOnly
        self.eventType = eventType
        self.requestID = requestID
        self.eventTime = eventTime
        self.eventName = eventName


    @property
    def requestParameters(self):

        return self._requestParameters

    @requestParameters.setter
    def requestParameters(self, requestParameters):


        self._requestParameters = requestParameters


    @property
    def userIdentity(self):

        return self._userIdentity

    @userIdentity.setter
    def userIdentity(self, userIdentity):


        self._userIdentity = userIdentity


    @property
    def eventID(self):

        return self._eventID

    @eventID.setter
    def eventID(self, eventID):


        self._eventID = eventID


    @property
    def awsRegion(self):

        return self._awsRegion

    @awsRegion.setter
    def awsRegion(self, awsRegion):


        self._awsRegion = awsRegion


    @property
    def eventVersion(self):

        return self._eventVersion

    @eventVersion.setter
    def eventVersion(self, eventVersion):


        self._eventVersion = eventVersion


    @property
    def responseElements(self):

        return self._responseElements

    @responseElements.setter
    def responseElements(self, responseElements):


        self._responseElements = responseElements


    @property
    def sourceIPAddress(self):

        return self._sourceIPAddress

    @sourceIPAddress.setter
    def sourceIPAddress(self, sourceIPAddress):


        self._sourceIPAddress = sourceIPAddress


    @property
    def eventSource(self):

        return self._eventSource

    @eventSource.setter
    def eventSource(self, eventSource):


        self._eventSource = eventSource


    @property
    def resources(self):

        return self._resources

    @resources.setter
    def resources(self, resources):


        self._resources = resources


    @property
    def userAgent(self):

        return self._userAgent

    @userAgent.setter
    def userAgent(self, userAgent):


        self._userAgent = userAgent


    @property
    def readOnly(self):

        return self._readOnly

    @readOnly.setter
    def readOnly(self, readOnly):


        self._readOnly = readOnly


    @property
    def eventType(self):

        return self._eventType

    @eventType.setter
    def eventType(self, eventType):


        self._eventType = eventType


    @property
    def requestID(self):

        return self._requestID

    @requestID.setter
    def requestID(self, requestID):


        self._requestID = requestID


    @property
    def eventTime(self):

        return self._eventTime

    @eventTime.setter
    def eventTime(self, eventTime):


        self._eventTime = eventTime


    @property
    def eventName(self):

        return self._eventName

    @eventName.setter
    def eventName(self, eventName):


        self._eventName = eventName

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
        if issubclass(AWSAPICallViaCloudTrail, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, AWSAPICallViaCloudTrail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

