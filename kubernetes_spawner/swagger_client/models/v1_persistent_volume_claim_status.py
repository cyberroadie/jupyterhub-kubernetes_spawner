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


class V1PersistentVolumeClaimStatus(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, phase=None, access_modes=None, capacity=None):
        """
        V1PersistentVolumeClaimStatus - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'phase': 'str',
            'access_modes': 'list[V1PersistentVolumeAccessMode]',
            'capacity': 'Any'
        }

        self.attribute_map = {
            'phase': 'phase',
            'access_modes': 'accessModes',
            'capacity': 'capacity'
        }

        self._phase = phase
        self._access_modes = access_modes
        self._capacity = capacity

    @property
    def phase(self):
        """
        Gets the phase of this V1PersistentVolumeClaimStatus.
        Phase represents the current phase of PersistentVolumeClaim.

        :return: The phase of this V1PersistentVolumeClaimStatus.
        :rtype: str
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        """
        Sets the phase of this V1PersistentVolumeClaimStatus.
        Phase represents the current phase of PersistentVolumeClaim.

        :param phase: The phase of this V1PersistentVolumeClaimStatus.
        :type: str
        """

        self._phase = phase

    @property
    def access_modes(self):
        """
        Gets the access_modes of this V1PersistentVolumeClaimStatus.
        AccessModes contains the actual access modes the volume backing the PVC has. More info: http://releases.k8s.io/release-1.2/docs/user-guide/persistent-volumes.md#access-modes-1

        :return: The access_modes of this V1PersistentVolumeClaimStatus.
        :rtype: list[V1PersistentVolumeAccessMode]
        """
        return self._access_modes

    @access_modes.setter
    def access_modes(self, access_modes):
        """
        Sets the access_modes of this V1PersistentVolumeClaimStatus.
        AccessModes contains the actual access modes the volume backing the PVC has. More info: http://releases.k8s.io/release-1.2/docs/user-guide/persistent-volumes.md#access-modes-1

        :param access_modes: The access_modes of this V1PersistentVolumeClaimStatus.
        :type: list[V1PersistentVolumeAccessMode]
        """

        self._access_modes = access_modes

    @property
    def capacity(self):
        """
        Gets the capacity of this V1PersistentVolumeClaimStatus.
        Represents the actual resources of the underlying volume.

        :return: The capacity of this V1PersistentVolumeClaimStatus.
        :rtype: Any
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """
        Sets the capacity of this V1PersistentVolumeClaimStatus.
        Represents the actual resources of the underlying volume.

        :param capacity: The capacity of this V1PersistentVolumeClaimStatus.
        :type: Any
        """

        self._capacity = capacity

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
