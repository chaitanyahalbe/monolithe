# -*- coding: utf-8 -*-
"""

NUZone
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

from ..fetchers import NUStatisticssFetcher
from ..fetchers import NUSubNetworksFetcher
from ..fetchers import NUDHCPOptionsFetcher
from ..fetchers import NUVMInterfacesFetcher
from ..fetchers import NUPermittedActionsFetcher
from ..fetchers import NUQosPrimitivesFetcher
from ..fetchers import NUTCAsFetcher
from ..fetchers import NUStatisticsPoliciesFetcher
from ..fetchers import NUEventLogsFetcher
from ..fetchers import NUVirtualMachinesFetcher
from ..fetchers import NUGroupsFetcher


class NUZone(NURESTObject):
    """ Represents a Zone object in Nuage VSD solution
        IMPORTANT: Do not override this object.
    """

    def __init__(self, **kwargs):
        """ Initialize a NUZone instance """

        super(NUZone, self).__init__()

        # Read/Write Attributes
        self.address = None  #  IP address of the subnet defined. In case of zone, this is an optional field for and allows users to allocate an IP address range to a zone. The VSD will auto-assign IP addresses to subnets from this range if a specific IP address is not defined for the subnet - int
        self.associated_application_id = None  #  The associated application ID. - int
        self.associated_application_object_id = None  #  The associated application object ID. - int
        self.associated_application_object_type = None  #  The associated application object type. - int
        self.template_id = None  #  The ID of the template that this zone was derived from - int
        self.description = None  #  A description of the zone - int
        self.ip_type = None  #  IPv4 or IPv6(only IPv4 is supported in R1.0) - int
        self.maintenance_mode = None  #  maintenanceMode is an enum that indicates if the Zone is accepting VM activation requests. Possible values are DISABLED, ENABLED and ENABLED_INHERITED - int
        self.name = None  #  Name of the current entity(Zone or zone template or subnet etc..) Valid characters are alphabets, numbers, space and hyphen( - ). - int
        self.netmask = None  #  Netmask of the subnet defined - int
        self.number_of_hosts_in_subnets = None  #  Number of hosts in each of the subnets that can be created under a zone and are auto-assigned IP addresses - int
        self.public_zone = None  #  If a zone is marked as public, then it is lined to the public network associated with this data center - int
        self.multicast = None  #  multicast is enum that indicates multicast policy on zone/zone template. Possible values are ENABLED ,DISABLED  and INHERITED - int
        self.associated_multicast_channel_map_id = None  #  The ID of the Multi Cast Channel Map  this zone/zone template is associated with. This has to be set when  enableMultiCast is set to ENABLED - int
        
        self.expose_attribute(local_name=u"address", remote_name=u"address", attribute_type=int)
        self.expose_attribute(local_name=u"associated_application_id", remote_name=u"associatedApplicationID", attribute_type=int)
        self.expose_attribute(local_name=u"associated_application_object_id", remote_name=u"associatedApplicationObjectID", attribute_type=int)
        self.expose_attribute(local_name=u"associated_application_object_type", remote_name=u"associatedApplicationObjectType", attribute_type=int)
        self.expose_attribute(local_name=u"template_id", remote_name=u"templateID", attribute_type=int)
        self.expose_attribute(local_name=u"description", remote_name=u"description", attribute_type=int)
        self.expose_attribute(local_name=u"ip_type", remote_name=u"IPType", attribute_type=int)
        self.expose_attribute(local_name=u"maintenance_mode", remote_name=u"maintenanceMode", attribute_type=int)
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=int)
        self.expose_attribute(local_name=u"netmask", remote_name=u"netmask", attribute_type=int)
        self.expose_attribute(local_name=u"number_of_hosts_in_subnets", remote_name=u"numberOfHostsInSubnets", attribute_type=int)
        self.expose_attribute(local_name=u"public_zone", remote_name=u"publicZone", attribute_type=int)
        self.expose_attribute(local_name=u"multicast", remote_name=u"multicast", attribute_type=int)
        self.expose_attribute(local_name=u"associated_multicast_channel_map_id", remote_name=u"associatedMulticastChannelMapID", attribute_type=int)
        
        # Fetchers
        self.statisticss = []
        self.statisticss_fetcher = NUStatisticssFetcher.fetcher_with_object(nurest_object=self, local_name=u"statisticss")
        self.sub_networks = []
        self.sub_networks_fetcher = NUSubNetworksFetcher.fetcher_with_object(nurest_object=self, local_name=u"sub_networks")
        self.dhcp_options = []
        self.dhcp_options_fetcher = NUDHCPOptionsFetcher.fetcher_with_object(nurest_object=self, local_name=u"dhcp_options")
        self.vm_interfaces = []
        self.vm_interfaces_fetcher = NUVMInterfacesFetcher.fetcher_with_object(nurest_object=self, local_name=u"vm_interfaces")
        self.permitted_actions = []
        self.permitted_actions_fetcher = NUPermittedActionsFetcher.fetcher_with_object(nurest_object=self, local_name=u"permitted_actions")
        self.qos_primitives = []
        self.qos_primitives_fetcher = NUQosPrimitivesFetcher.fetcher_with_object(nurest_object=self, local_name=u"qos_primitives")
        self.tcas = []
        self.tcas_fetcher = NUTCAsFetcher.fetcher_with_object(nurest_object=self, local_name=u"tcas")
        self.statistics_policies = []
        self.statistics_policies_fetcher = NUStatisticsPoliciesFetcher.fetcher_with_object(nurest_object=self, local_name=u"statistics_policies")
        self.event_logs = []
        self.event_logs_fetcher = NUEventLogsFetcher.fetcher_with_object(nurest_object=self, local_name=u"event_logs")
        self.virtual_machines = []
        self.virtual_machines_fetcher = NUVirtualMachinesFetcher.fetcher_with_object(nurest_object=self, local_name=u"virtual_machines")
        self.groups = []
        self.groups_fetcher = NUGroupsFetcher.fetcher_with_object(nurest_object=self, local_name=u"groups")
        for key, value in kwargs.iteritems():
            if hasattr(self, key):
                setattr(self, key, value)



    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"zone"


