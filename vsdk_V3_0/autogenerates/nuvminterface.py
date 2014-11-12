# -*- coding: utf-8 -*-
"""

NUVMInterface
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
from ..fetchers import NUDHCPOptionsFetcher
from ..fetchers import NURedirectionTargetsFetcher
from ..fetchers import NUTCAsFetcher
from ..fetchers import NUPolicyDecisionsFetcher
from ..fetchers import NUPolicyGroupsFetcher
from ..fetchers import NUEventLogsFetcher
from ..fetchers import NUStaticRoutesFetcher
from ..fetchers import NUMultiCastChannelMapsFetcher


class NUVMInterface(NURESTObject):
    """ Represents a VMInterface object in Nuage VSD solution
        IMPORTANT: Do not override this object.
    """

    def __init__(self, **kwargs):
        """ Initialize a NUVMInterface instance """

        super(NUVMInterface, self).__init__()

        # Read/Write Attributes
        self.ip_address = None  #  IP address of the  interface - int
        self.mac = None  #  MAC address of the  interface - int
        self.multi_nicv_port_name = None  #  Name of the Multi NIC VPort associated with this VM Interface - int
        self.name = None  #  Device name associated with this interface - int
        self.vmuuid = None  #  UUID of the associated virtual machine - int
        self.associated_floating_ip_address = None  #  Floating Ip Address of this network interface eg: 10.1.2.1 - int
        self.attached_network_id = None  #  ID of the l2 domain or Subnet that the VM is attached to - int
        self.attached_network_type = None  #  l2 domain or Subnet that the interface is attached to - int
        self.domain_id = None  #  ID of the domain that the VM is attached to - int
        self.domain_name = None  #  Name of the domain that the VM is attached to - int
        self.gateway = None  #  Gateway of the subnet that the VM is connected to - int
        self.netmask = None  #  Netmask of the subnet that the VM is attached to - int
        self.network_name = None  #  Name of the network that the VM is attached to - int
        self.policy_decision_id = None  #  The policy decision ID for this particular  interface - int
        self.tier_id = None  #  ID of the tier that the interface is attached to. - int
        self.v_port_id = None  #  ID of the vport that the interface is attached to - int
        self.v_port_name = None  #  Name of the vport that the VM is attached to - int
        self.zone_id = None  #  ID of the zone that the interface is attached to - int
        self.zone_name = None  #  Name of the zone that the VM is attached to - int
        
        self.expose_attribute(local_name=u"ip_address", remote_name=u"IPAddress", attribute_type=int)
        self.expose_attribute(local_name=u"mac", remote_name=u"MAC", attribute_type=int)
        self.expose_attribute(local_name=u"multi_nicv_port_name", remote_name=u"multiNICVPortName", attribute_type=int)
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=int)
        self.expose_attribute(local_name=u"vmuuid", remote_name=u"VMUUID", attribute_type=int)
        self.expose_attribute(local_name=u"associated_floating_ip_address", remote_name=u"associatedFloatingIPAddress", attribute_type=int)
        self.expose_attribute(local_name=u"attached_network_id", remote_name=u"attachedNetworkID", attribute_type=int)
        self.expose_attribute(local_name=u"attached_network_type", remote_name=u"attachedNetworkType", attribute_type=int)
        self.expose_attribute(local_name=u"domain_id", remote_name=u"domainID", attribute_type=int)
        self.expose_attribute(local_name=u"domain_name", remote_name=u"domainName", attribute_type=int)
        self.expose_attribute(local_name=u"gateway", remote_name=u"gateway", attribute_type=int)
        self.expose_attribute(local_name=u"netmask", remote_name=u"netmask", attribute_type=int)
        self.expose_attribute(local_name=u"network_name", remote_name=u"networkName", attribute_type=int)
        self.expose_attribute(local_name=u"policy_decision_id", remote_name=u"policyDecisionID", attribute_type=int)
        self.expose_attribute(local_name=u"tier_id", remote_name=u"tierID", attribute_type=int)
        self.expose_attribute(local_name=u"v_port_id", remote_name=u"VPortID", attribute_type=int)
        self.expose_attribute(local_name=u"v_port_name", remote_name=u"VPortName", attribute_type=int)
        self.expose_attribute(local_name=u"zone_id", remote_name=u"zoneID", attribute_type=int)
        self.expose_attribute(local_name=u"zone_name", remote_name=u"zoneName", attribute_type=int)
        
        # Fetchers
        self.statisticss = []
        self.statisticss_fetcher = NUStatisticssFetcher.fetcher_with_object(nurest_object=self, local_name=u"statisticss")
        self.dhcp_options = []
        self.dhcp_options_fetcher = NUDHCPOptionsFetcher.fetcher_with_object(nurest_object=self, local_name=u"dhcp_options")
        self.redirection_targets = []
        self.redirection_targets_fetcher = NURedirectionTargetsFetcher.fetcher_with_object(nurest_object=self, local_name=u"redirection_targets")
        self.tcas = []
        self.tcas_fetcher = NUTCAsFetcher.fetcher_with_object(nurest_object=self, local_name=u"tcas")
        self.policy_decisions = []
        self.policy_decisions_fetcher = NUPolicyDecisionsFetcher.fetcher_with_object(nurest_object=self, local_name=u"policy_decisions")
        self.policy_groups = []
        self.policy_groups_fetcher = NUPolicyGroupsFetcher.fetcher_with_object(nurest_object=self, local_name=u"policy_groups")
        self.event_logs = []
        self.event_logs_fetcher = NUEventLogsFetcher.fetcher_with_object(nurest_object=self, local_name=u"event_logs")
        self.static_routes = []
        self.static_routes_fetcher = NUStaticRoutesFetcher.fetcher_with_object(nurest_object=self, local_name=u"static_routes")
        self.multi_cast_channel_maps = []
        self.multi_cast_channel_maps_fetcher = NUMultiCastChannelMapsFetcher.fetcher_with_object(nurest_object=self, local_name=u"multi_cast_channel_maps")
        for key, value in kwargs.iteritems():
            if hasattr(self, key):
                setattr(self, key, value)



    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"vminterface"


