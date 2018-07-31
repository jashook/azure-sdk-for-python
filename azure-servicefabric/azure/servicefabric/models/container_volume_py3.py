# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ContainerVolume(Model):
    """Describes how a volume is attached to a container.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. Name of the volume.
    :type name: str
    :param read_only: The flag indicating whether the volume is read only.
     Default is 'false'.
    :type read_only: bool
    :param destination_path: Required. The path within the container at which
     the volume should be mounted. Only valid path characters are allowed.
    :type destination_path: str
    """

    _validation = {
        'name': {'required': True},
        'destination_path': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'read_only': {'key': 'readOnly', 'type': 'bool'},
        'destination_path': {'key': 'destinationPath', 'type': 'str'},
    }

    def __init__(self, *, name: str, destination_path: str, read_only: bool=None, **kwargs) -> None:
        super(ContainerVolume, self).__init__(**kwargs)
        self.name = name
        self.read_only = read_only
        self.destination_path = destination_path
