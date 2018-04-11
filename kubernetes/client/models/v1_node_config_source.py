# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.10.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1NodeConfigSource(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'api_version': 'str',
        'config_map_ref': 'V1ObjectReference',
        'kind': 'str'
    }

    attribute_map = {
        'api_version': 'apiVersion',
        'config_map_ref': 'configMapRef',
        'kind': 'kind'
    }

    def __init__(self, api_version=None, config_map_ref=None, kind=None):
        """
        V1NodeConfigSource - a model defined in Swagger
        """

        self._api_version = None
        self._config_map_ref = None
        self._kind = None
        self.discriminator = None

        if api_version is not None:
          self.api_version = api_version
        if config_map_ref is not None:
          self.config_map_ref = config_map_ref
        if kind is not None:
          self.kind = kind

    @property
    def api_version(self):
        """
        Gets the api_version of this V1NodeConfigSource.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

        :return: The api_version of this V1NodeConfigSource.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """
        Sets the api_version of this V1NodeConfigSource.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

        :param api_version: The api_version of this V1NodeConfigSource.
        :type: str
        """

        self._api_version = api_version

    @property
    def config_map_ref(self):
        """
        Gets the config_map_ref of this V1NodeConfigSource.

        :return: The config_map_ref of this V1NodeConfigSource.
        :rtype: V1ObjectReference
        """
        return self._config_map_ref

    @config_map_ref.setter
    def config_map_ref(self, config_map_ref):
        """
        Sets the config_map_ref of this V1NodeConfigSource.

        :param config_map_ref: The config_map_ref of this V1NodeConfigSource.
        :type: V1ObjectReference
        """

        self._config_map_ref = config_map_ref

    @property
    def kind(self):
        """
        Gets the kind of this V1NodeConfigSource.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

        :return: The kind of this V1NodeConfigSource.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """
        Sets the kind of this V1NodeConfigSource.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

        :param kind: The kind of this V1NodeConfigSource.
        :type: str
        """

        self._kind = kind

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
        if not isinstance(other, V1NodeConfigSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
