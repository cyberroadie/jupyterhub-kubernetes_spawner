# coding: utf-8

"""

    No descripton provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class V1NFSVolumeSource(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, server=None, path=None, read_only=None):
        """
        V1NFSVolumeSource - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'server': 'str',
            'path': 'str',
            'read_only': 'bool'
        }

        self.attribute_map = {
            'server': 'server',
            'path': 'path',
            'read_only': 'readOnly'
        }

        self._server = server
        self._path = path
        self._read_only = read_only

    @property
    def server(self):
        """
        Gets the server of this V1NFSVolumeSource.
        Server is the hostname or IP address of the NFS server. More info: http://releases.k8s.io/release-1.2/docs/user-guide/volumes.md#nfs

        :return: The server of this V1NFSVolumeSource.
        :rtype: str
        """
        return self._server

    @server.setter
    def server(self, server):
        """
        Sets the server of this V1NFSVolumeSource.
        Server is the hostname or IP address of the NFS server. More info: http://releases.k8s.io/release-1.2/docs/user-guide/volumes.md#nfs

        :param server: The server of this V1NFSVolumeSource.
        :type: str
        """

        self._server = server

    @property
    def path(self):
        """
        Gets the path of this V1NFSVolumeSource.
        Path that is exported by the NFS server. More info: http://releases.k8s.io/release-1.2/docs/user-guide/volumes.md#nfs

        :return: The path of this V1NFSVolumeSource.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this V1NFSVolumeSource.
        Path that is exported by the NFS server. More info: http://releases.k8s.io/release-1.2/docs/user-guide/volumes.md#nfs

        :param path: The path of this V1NFSVolumeSource.
        :type: str
        """

        self._path = path

    @property
    def read_only(self):
        """
        Gets the read_only of this V1NFSVolumeSource.
        ReadOnly here will force the NFS export to be mounted with read-only permissions. Defaults to false. More info: http://releases.k8s.io/release-1.2/docs/user-guide/volumes.md#nfs

        :return: The read_only of this V1NFSVolumeSource.
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """
        Sets the read_only of this V1NFSVolumeSource.
        ReadOnly here will force the NFS export to be mounted with read-only permissions. Defaults to false. More info: http://releases.k8s.io/release-1.2/docs/user-guide/volumes.md#nfs

        :param read_only: The read_only of this V1NFSVolumeSource.
        :type: bool
        """

        self._read_only = read_only

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
