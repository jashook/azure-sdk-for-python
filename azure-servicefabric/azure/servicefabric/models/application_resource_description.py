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


class ApplicationResourceDescription(Model):
    """Describes a service fabric application resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param description: User readable description of the application.
    :type description: str
    :param debug_params: Internal use.
    :type debug_params: str
    :param services: describes the services in the application.
    :type services:
     list[~azure.servicefabric.models.ServiceResourceDescription]
    :ivar health_state: Describes the health state of an application resource.
     Possible values include: 'Invalid', 'Ok', 'Warning', 'Error', 'Unknown'
    :vartype health_state: str or ~azure.servicefabric.models.HealthState
    :ivar unhealthy_evaluation: When the application's health state is not
     'Ok', this additional details from service fabric Health Manager for the
     user to know why the application is marked unhealthy.
    :vartype unhealthy_evaluation: str
    :ivar status: Status of the application resource. Possible values include:
     'Invalid', 'Ready', 'Upgrading', 'Creating', 'Deleting', 'Failed'
    :vartype status: str or
     ~azure.servicefabric.models.ApplicationResourceStatus
    :ivar status_details: Gives additional information about the current
     status of the application deployment.
    :vartype status_details: str
    :ivar service_names: Names of the services in the application.
    :vartype service_names: list[str]
    :param diagnostics: Describes the diagnostics definition and usage for an
     application resource.
    :type diagnostics: ~azure.servicefabric.models.DiagnosticsDescription
    :param name: Required. Application resource name.
    :type name: str
    """

    _validation = {
        'health_state': {'readonly': True},
        'unhealthy_evaluation': {'readonly': True},
        'status': {'readonly': True},
        'status_details': {'readonly': True},
        'service_names': {'readonly': True},
        'name': {'required': True},
    }

    _attribute_map = {
        'description': {'key': 'properties.description', 'type': 'str'},
        'debug_params': {'key': 'properties.debugParams', 'type': 'str'},
        'services': {'key': 'properties.services', 'type': '[ServiceResourceDescription]'},
        'health_state': {'key': 'properties.healthState', 'type': 'str'},
        'unhealthy_evaluation': {'key': 'properties.unhealthyEvaluation', 'type': 'str'},
        'status': {'key': 'properties.status', 'type': 'str'},
        'status_details': {'key': 'properties.statusDetails', 'type': 'str'},
        'service_names': {'key': 'properties.serviceNames', 'type': '[str]'},
        'diagnostics': {'key': 'properties.diagnostics', 'type': 'DiagnosticsDescription'},
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ApplicationResourceDescription, self).__init__(**kwargs)
        self.description = kwargs.get('description', None)
        self.debug_params = kwargs.get('debug_params', None)
        self.services = kwargs.get('services', None)
        self.health_state = None
        self.unhealthy_evaluation = None
        self.status = None
        self.status_details = None
        self.service_names = None
        self.diagnostics = kwargs.get('diagnostics', None)
        self.name = kwargs.get('name', None)
