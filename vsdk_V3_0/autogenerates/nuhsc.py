# -*- coding: utf-8 -*-

"""
NUHSC
System Monitoring details for hardware service controllers

This file has been autogenerated and should not be modified.
Author Christophe Serafin <christophe.serafin@alcatel-lucent.com>

This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 3.0 of the License, or (at your option) any later version.

This library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public
License along with this library; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA

"""

from ..fetchers import NUPortStatussFetcher
from ..fetchers import NUJobsFetcher
from ..fetchers import NUBGPPeersFetcher
from ..fetchers import NUVRSsFetcher
from ..fetchers import NUAlarmsFetcher
from bambou import NURESTObject


class NUHSC(NURESTObject):
    """ Represents a HSC object

        IMPORTANT: This file has been autogenerated. Do not override it !

    """

    def __init__(self, **kwargs):
        """ Initializes a HSC instance

        """
        super(NUHSC, self).__init__()

        # Read/Write Attributes
        
        self._last_state_change = str()
        self._status = str()
        self._disks = str()
        self._description = str()
        self._already_marked_for_unavailable = bool()
        self._management_ip = str()
        self._current_cpu_usage = float()
        self._messages = str()
        self._vsds = str()
        self._peak_memory_usage = float()
        self._name = str()
        self._current_memory_usage = float()
        self._unavailable_timestamp = str()
        self._product_version = str()
        self._peak_cpu_usage = float()
        self._address = str()
        self._average_cpu_usage = float()
        self._model = str()
        self._average_memory_usage = float()
        self._type = str()
        self._location = str()
        
        self.expose_attribute(local_name=u"last_state_change", remote_name=u"lastStateChange", attribute_type=str)
        self.expose_attribute(local_name=u"status", remote_name=u"status", attribute_type=str, choices=[u'DEGRADED', u'DOWN', u'UP', u'ADMIN_DOWN'])
        self.expose_attribute(local_name=u"disks", remote_name=u"disks", attribute_type=str)
        self.expose_attribute(local_name=u"description", remote_name=u"description", attribute_type=str)
        self.expose_attribute(local_name=u"already_marked_for_unavailable", remote_name=u"alreadyMarkedForUnavailable", attribute_type=bool)
        self.expose_attribute(local_name=u"management_ip", remote_name=u"managementIP", attribute_type=str)
        self.expose_attribute(local_name=u"current_cpu_usage", remote_name=u"currentCPUUsage", attribute_type=float)
        self.expose_attribute(local_name=u"messages", remote_name=u"messages", attribute_type=str)
        self.expose_attribute(local_name=u"vsds", remote_name=u"vsds", attribute_type=str)
        self.expose_attribute(local_name=u"peak_memory_usage", remote_name=u"peakMemoryUsage", attribute_type=float)
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=str)
        self.expose_attribute(local_name=u"current_memory_usage", remote_name=u"currentMemoryUsage", attribute_type=float)
        self.expose_attribute(local_name=u"unavailable_timestamp", remote_name=u"unavailableTimestamp", attribute_type=str)
        self.expose_attribute(local_name=u"product_version", remote_name=u"productVersion", attribute_type=str)
        self.expose_attribute(local_name=u"peak_cpu_usage", remote_name=u"peakCPUUsage", attribute_type=float)
        self.expose_attribute(local_name=u"address", remote_name=u"address", attribute_type=str)
        self.expose_attribute(local_name=u"average_cpu_usage", remote_name=u"averageCPUUsage", attribute_type=float)
        self.expose_attribute(local_name=u"model", remote_name=u"model", attribute_type=str)
        self.expose_attribute(local_name=u"average_memory_usage", remote_name=u"averageMemoryUsage", attribute_type=float)
        self.expose_attribute(local_name=u"type", remote_name=u"type", attribute_type=str, choices=[u'DC7X50', u'VSG', u'VSA', u'NONE'])
        self.expose_attribute(local_name=u"location", remote_name=u"location", attribute_type=str)
        
        # Fetchers
        
        self.monitoringports = []
        self.monitoringports_fetcher = NUPortStatussFetcher.fetcher_with_entity(entity=self, local_name=u"monitoringports")
        
        self.jobs = []
        self.jobs_fetcher = NUJobsFetcher.fetcher_with_entity(entity=self, local_name=u"jobs")
        
        self.bgppeers = []
        self.bgppeers_fetcher = NUBGPPeersFetcher.fetcher_with_entity(entity=self, local_name=u"bgppeers")
        
        self.vrss = []
        self.vrss_fetcher = NUVRSsFetcher.fetcher_with_entity(entity=self, local_name=u"vrss")
        
        self.alarms = []
        self.alarms_fetcher = NUAlarmsFetcher.fetcher_with_entity(entity=self, local_name=u"alarms")
        
        for key, value in kwargs.iteritems():
            if hasattr(self, key):
                setattr(self, key, value)

    # Properties
    
    def _get_last_state_change(self):
        """ Get attribute last_state_change

            Last state change timestamp (in millis).

        """
        return self._last_state_change

    def _set_last_state_change(self, value):
        """ Set attribute last_state_change

            Last state change timestamp (in millis).

        """
        self._last_state_change = value

    last_state_change = property(_get_last_state_change, _set_last_state_change)
    
    def _get_status(self):
        """ Get attribute status

            Computed status of the entity. Possible values are UP, DOWN, ADMIN_DOWN, DEGRADED, .

        """
        return self._status

    def _set_status(self, value):
        """ Set attribute status

            Computed status of the entity. Possible values are UP, DOWN, ADMIN_DOWN, DEGRADED, .

        """
        self._status = value

    status = property(_get_status, _set_status)
    
    def _get_disks(self):
        """ Get attribute disks

            Set of disk usage details.

        """
        return self._disks

    def _set_disks(self, value):
        """ Set attribute disks

            Set of disk usage details.

        """
        self._disks = value

    disks = property(_get_disks, _set_disks)
    
    def _get_description(self):
        """ Get attribute description

            Description of the entity.

        """
        return self._description

    def _set_description(self, value):
        """ Set attribute description

            Description of the entity.

        """
        self._description = value

    description = property(_get_description, _set_description)
    
    def _get_already_marked_for_unavailable(self):
        """ Get attribute already_marked_for_unavailable

            Flag to indicate that it is already marked a unavailable.

        """
        return self._already_marked_for_unavailable

    def _set_already_marked_for_unavailable(self, value):
        """ Set attribute already_marked_for_unavailable

            Flag to indicate that it is already marked a unavailable.

        """
        self._already_marked_for_unavailable = value

    already_marked_for_unavailable = property(_get_already_marked_for_unavailable, _set_already_marked_for_unavailable)
    
    def _get_management_ip(self):
        """ Get attribute management_ip

            The management IP of the VSC/HSC entity

        """
        return self._management_ip

    def _set_management_ip(self, value):
        """ Set attribute management_ip

            The management IP of the VSC/HSC entity

        """
        self._management_ip = value

    management_ip = property(_get_management_ip, _set_management_ip)
    
    def _get_current_cpu_usage(self):
        """ Get attribute current_cpu_usage

            Current CPU usage percentage.

        """
        return self._current_cpu_usage

    def _set_current_cpu_usage(self, value):
        """ Set attribute current_cpu_usage

            Current CPU usage percentage.

        """
        self._current_cpu_usage = value

    current_cpu_usage = property(_get_current_cpu_usage, _set_current_cpu_usage)
    
    def _get_messages(self):
        """ Get attribute messages

            An array of degraded messages.

        """
        return self._messages

    def _set_messages(self, value):
        """ Set attribute messages

            An array of degraded messages.

        """
        self._messages = value

    messages = property(_get_messages, _set_messages)
    
    def _get_vsds(self):
        """ Get attribute vsds

            A collection of VSD id(s) which are identified by this controller.

        """
        return self._vsds

    def _set_vsds(self, value):
        """ Set attribute vsds

            A collection of VSD id(s) which are identified by this controller.

        """
        self._vsds = value

    vsds = property(_get_vsds, _set_vsds)
    
    def _get_peak_memory_usage(self):
        """ Get attribute peak_memory_usage

            Peek memory usage percentage.

        """
        return self._peak_memory_usage

    def _set_peak_memory_usage(self, value):
        """ Set attribute peak_memory_usage

            Peek memory usage percentage.

        """
        self._peak_memory_usage = value

    peak_memory_usage = property(_get_peak_memory_usage, _set_peak_memory_usage)
    
    def _get_name(self):
        """ Get attribute name

            Identifies the entity with a name.

        """
        return self._name

    def _set_name(self, value):
        """ Set attribute name

            Identifies the entity with a name.

        """
        self._name = value

    name = property(_get_name, _set_name)
    
    def _get_current_memory_usage(self):
        """ Get attribute current_memory_usage

            Current memory usage percentage.

        """
        return self._current_memory_usage

    def _set_current_memory_usage(self, value):
        """ Set attribute current_memory_usage

            Current memory usage percentage.

        """
        self._current_memory_usage = value

    current_memory_usage = property(_get_current_memory_usage, _set_current_memory_usage)
    
    def _get_unavailable_timestamp(self):
        """ Get attribute unavailable_timestamp

            The duration the controller is unavailable (in millis).

        """
        return self._unavailable_timestamp

    def _set_unavailable_timestamp(self, value):
        """ Set attribute unavailable_timestamp

            The duration the controller is unavailable (in millis).

        """
        self._unavailable_timestamp = value

    unavailable_timestamp = property(_get_unavailable_timestamp, _set_unavailable_timestamp)
    
    def _get_product_version(self):
        """ Get attribute product_version

            Product version supported by this entity.

        """
        return self._product_version

    def _set_product_version(self, value):
        """ Set attribute product_version

            Product version supported by this entity.

        """
        self._product_version = value

    product_version = property(_get_product_version, _set_product_version)
    
    def _get_peak_cpu_usage(self):
        """ Get attribute peak_cpu_usage

            Peek CPU usage percentage.

        """
        return self._peak_cpu_usage

    def _set_peak_cpu_usage(self, value):
        """ Set attribute peak_cpu_usage

            Peek CPU usage percentage.

        """
        self._peak_cpu_usage = value

    peak_cpu_usage = property(_get_peak_cpu_usage, _set_peak_cpu_usage)
    
    def _get_address(self):
        """ Get attribute address

            The IP of the VRS entity

        """
        return self._address

    def _set_address(self, value):
        """ Set attribute address

            The IP of the VRS entity

        """
        self._address = value

    address = property(_get_address, _set_address)
    
    def _get_average_cpu_usage(self):
        """ Get attribute average_cpu_usage

            Average CPU usage percentage.

        """
        return self._average_cpu_usage

    def _set_average_cpu_usage(self, value):
        """ Set attribute average_cpu_usage

            Average CPU usage percentage.

        """
        self._average_cpu_usage = value

    average_cpu_usage = property(_get_average_cpu_usage, _set_average_cpu_usage)
    
    def _get_model(self):
        """ Get attribute model

            The model of the hardware service controller

        """
        return self._model

    def _set_model(self, value):
        """ Set attribute model

            The model of the hardware service controller

        """
        self._model = value

    model = property(_get_model, _set_model)
    
    def _get_average_memory_usage(self):
        """ Get attribute average_memory_usage

            Average memory usage percentage.

        """
        return self._average_memory_usage

    def _set_average_memory_usage(self, value):
        """ Set attribute average_memory_usage

            Average memory usage percentage.

        """
        self._average_memory_usage = value

    average_memory_usage = property(_get_average_memory_usage, _set_average_memory_usage)
    
    def _get_type(self):
        """ Get attribute type

            The type of the hardware service controller Possible values are VSA, VSG, DC7X50, NONE, .

        """
        return self._type

    def _set_type(self, value):
        """ Set attribute type

            The type of the hardware service controller Possible values are VSA, VSG, DC7X50, NONE, .

        """
        self._type = value

    type = property(_get_type, _set_type)
    
    def _get_location(self):
        """ Get attribute location

            Identifies the entity to be associated with a location.

        """
        return self._location

    def _set_location(self, value):
        """ Set attribute location

            Identifies the entity to be associated with a location.

        """
        self._location = value

    location = property(_get_location, _set_location)
    
    # Methods

    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI

        """
        return u"hsc"
