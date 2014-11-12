# -*- coding: utf-8 -*-
"""

NUVirtualMachine
This file has been autogenerated by Swagger  and should not be modified.

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

from bambou import NURESTObject

from ..fetchers import NUVMResyncsFetcher
from ..fetchers import NUVMInterfacesFetcher
from ..fetchers import NUVRSsFetcher
from ..fetchers import NUEventLogsFetcher
from ..fetchers import NUAlarmsFetcher


class NUVirtualMachine(NURESTObject):
    """ Represents a VirtualMachine object in Nuage VSD solution
        IMPORTANT: Do not override this object.
    """

    def __init__(self, **kwargs):
        """ Initialize a NUVirtualMachine instance """

        super(NUVirtualMachine, self).__init__()

        # Read/Write Attributes
        self.app_name = None  #  Application name that this VM belongs to - int
        self.domain_i_ds = None  #  Array of IDs of the domain that the VM is connected to - int
        self.enterprise_id = None  #  ID of the enterprise that this VM belongs to - int
        self.enterprise_name = None  #  Name of the enterprise that this VM belongs to - int
        self.hypervisor_ip = None  #  IP address of the hypervisor that this VM is currently running in - int
        self.interfaces = None  #  List of VM interfaces associated with the VM - int
        self.l2_domain_i_ds = None  #  Array of IDs of the l2 domain that the VM is connected to - int
        self.name = None  #  Name of the VM - int
        self.resync_info = None  #  Information of the status of the resync operation of a VM - int
        self.subnet_i_ds = None  #  Array of IDs of the subnets that the VM is connected to - int
        self.user_id = None  #  ID of the user that created this VM - int
        self.user_name = None  #  Username of the user that created this VM - int
        self.uuid = None  #  UUID of the VM - int
        self.status = None  #  Status of the VM - UNKNOWN, NOSTATE, RUNNING, BLOCKED, PAUSED, SHUTDOWN, SHUTOFF, CRASHED, LAST, UNREACHABLE, INIT, DELETE_PENDING - int
        self.reason_type = None  #  Reason of the event associated with the VM - UNKNOWN, NOSTATE_UNKNOWN, NOSTATE_LAST, RUNNING_UNKNOWN, RUNNING_BOOTED, RUNNING_MIGRATED, RUNNING_RESTORED, RUNNING_FROM_SNAPSHOT, RUNNING_UNPAUSED, RUNNING_MIGRATION_CANCELED, RUNNING_SAVE_CANCELED, RUNNING_LAST, BLOCKED_UNKNOWN, BLOCKED_LAST, PAUSED_UNKNOWN, PAUSED_USER, PAUSED_MIGRATION, PAUSED_SAVE, PAUSED_DUMP, PAUSED_IOERROR, PAUSED_WATCHDOG, PAUSED_FROM_SNAPSHOT, PAUSED_SHUTTING_DOWN, PAUSED_LAST, SHUTDOWN_UNKNOWN, SHUTDOWN_USER, SHUTDOWN_LAST, SHUTOFF_UNKNOWN, SHUTOFF_SHUTDOWN, SHUTOFF_DESTROYED, SHUTOFF_CRASHED, SHUTOFF_MIGRATED, SHUTOFF_SAVED, SHUTOFF_FAILED,SHUTOFF_FROM_SNAPSHOT, SHUTOFF_LAST, CRASHED_UNKNOWN, CRASHED_LAST - int
        self.vrsid = None  #  Id of the VRS that this VM is attached to. - int
        self.zone_i_ds = None  #  Array of IDs of the zone that this VM is attached to - int
        
        self.expose_attribute(local_name=u"app_name", remote_name=u"appName", attribute_type=int)
        self.expose_attribute(local_name=u"domain_i_ds", remote_name=u"domainIDs", attribute_type=int)
        self.expose_attribute(local_name=u"enterprise_id", remote_name=u"enterpriseID", attribute_type=int)
        self.expose_attribute(local_name=u"enterprise_name", remote_name=u"enterpriseName", attribute_type=int)
        self.expose_attribute(local_name=u"hypervisor_ip", remote_name=u"hypervisorIP", attribute_type=int)
        self.expose_attribute(local_name=u"interfaces", remote_name=u"interfaces", attribute_type=int)
        self.expose_attribute(local_name=u"l2_domain_i_ds", remote_name=u"l2DomainIDs", attribute_type=int)
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=int)
        self.expose_attribute(local_name=u"resync_info", remote_name=u"resyncInfo", attribute_type=int)
        self.expose_attribute(local_name=u"subnet_i_ds", remote_name=u"subnetIDs", attribute_type=int)
        self.expose_attribute(local_name=u"user_id", remote_name=u"userID", attribute_type=int)
        self.expose_attribute(local_name=u"user_name", remote_name=u"userName", attribute_type=int)
        self.expose_attribute(local_name=u"uuid", remote_name=u"UUID", attribute_type=int)
        self.expose_attribute(local_name=u"status", remote_name=u"status", attribute_type=int)
        self.expose_attribute(local_name=u"reason_type", remote_name=u"reasonType", attribute_type=int)
        self.expose_attribute(local_name=u"vrsid", remote_name=u"VRSID", attribute_type=int)
        self.expose_attribute(local_name=u"zone_i_ds", remote_name=u"zoneIDs", attribute_type=int)
        
        # Fetchers
        self.vm_resyncs = []
        self.vm_resyncs_fetcher = NUVMResyncsFetcher.fetcher_with_object(nurest_object=self, local_name=u"vm_resyncs")
        self.vm_interfaces = []
        self.vm_interfaces_fetcher = NUVMInterfacesFetcher.fetcher_with_object(nurest_object=self, local_name=u"vm_interfaces")
        self.vrss = []
        self.vrss_fetcher = NUVRSsFetcher.fetcher_with_object(nurest_object=self, local_name=u"vrss")
        self.event_logs = []
        self.event_logs_fetcher = NUEventLogsFetcher.fetcher_with_object(nurest_object=self, local_name=u"event_logs")
        self.alarms = []
        self.alarms_fetcher = NUAlarmsFetcher.fetcher_with_object(nurest_object=self, local_name=u"alarms")
        for key, value in kwargs.iteritems():
            if hasattr(self, key):
                setattr(self, key, value)



    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"virtualmachine"


