# -*- coding: utf-8 -*-
"""

NUL2Domain
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

from ..fetchers import NUBridgeInterfacesFetcher
from ..fetchers import NUAddressRangesFetcher
from ..fetchers import NUEgressACLTemplatesFetcher
from ..fetchers import NUVPortsFetcher
from ..fetchers import NUStatisticssFetcher
from ..fetchers import NUDHCPOptionsFetcher
from ..fetchers import NUHostInterfacesFetcher
from ..fetchers import NUPermittedActionsFetcher
from ..fetchers import NURedirectionTargetsFetcher
from ..fetchers import NUPolicyGroupsFetcher
from ..fetchers import NUStatisticsPoliciesFetcher
from ..fetchers import NUVirtualMachinesFetcher
from ..fetchers import NUStaticRoutesFetcher
from ..fetchers import NUGroupsFetcher
from ..fetchers import NUIngressACLTemplatesFetcher
from ..fetchers import NUJobsFetcher
from ..fetchers import NUIngressAdvancedForwardingTemplatesFetcher
from ..fetchers import NUQosPrimitivesFetcher
from ..fetchers import NUMetadatasFetcher
from ..fetchers import NUTCAsFetcher
from ..fetchers import NUVPNConnectsFetcher
from ..fetchers import NUEventLogsFetcher


class NUL2Domain(NURESTObject):
    """ Represents a L2Domain object in Nuage VSD solution
        IMPORTANT: Do not override this object.
    """

    def __init__(self, **kwargs):
        """ Initialize a NUL2Domain instance """

        super(NUL2Domain, self).__init__()

        # Read/Write Attributes
        self.address = None  #  Network address of the L2Domain / L2Domain template defined.  - int
        self.associated_shared_network_resource_id = None  #  The ID of the L2 Domain  that this L2 Domain object is pointing to - int
        self.template_id = None  #  The ID of the L2 Domain template that this L2 Domain object was derived from - int
        self.description = None  #  A description field provided by the user that identifies the L2Domain / L2Domain template. - int
        self.dhcp_managed = None  #  decides whether L2Domain / L2Domain template DHCP is managed by VSD - int
        self.gateway = None  #  The IP address of the gateway of this l2 domain - int
        self.gateway_mac_address = None  #  The MAC address of the Gateway. - int
        self.ip_type = None  #  IPv4 or IPv6(only IPv4 is supported in R2.0) - int
        self.maintenance_mode = None  #  maintenanceMode is an enum that indicates if the L2Domain is accepting VM activation requests. Possible values are DISABLED, ENABLED and ENABLED_INHERITED - int
        self.name = None  #  Name of the L2Domain / L2Domain template,has to be unique within a Enterprise. Valid characters are alphabets, numbers, space and hyphen( - ). - int
        self.netmask = None  #  Netmask of the L2Domain / L2Domain template defined - int
        self.route_distinguisher = None  #  The Route Distinguisher value assigned by VSD for this subnet that is used by the BGP-EVPN protocol in VSC - int
        self.route_target = None  #  The Route Target value assigned by VSD for this subnet that is used by the BGP-EVPN protocol in VSC - int
        self.service_id = None  #  The service ID used by the VSCs to identify this subnet - long
        self.vn_id = None  #  Current Network's  globally unique  VXLAN network identifier generated by VSD - long
        self.multicast = None  #  multicast is enum that indicates multicast policy on L2Domain / L2Domain template. Possible values are ENABLED and DISABLED - int
        self.associated_multicast_channel_map_id = None  #  The ID of the Multi Cast Channel Map this L2Domain / L2Domain template template is associated with. This has to be set when  enableMultiCast is set to ENABLED - int
        
        self.expose_attribute(local_name=u"address", remote_name=u"address", attribute_type=int)
        self.expose_attribute(local_name=u"associated_shared_network_resource_id", remote_name=u"associatedSharedNetworkResourceID", attribute_type=int)
        self.expose_attribute(local_name=u"template_id", remote_name=u"templateID", attribute_type=int)
        self.expose_attribute(local_name=u"description", remote_name=u"description", attribute_type=int)
        self.expose_attribute(local_name=u"dhcp_managed", remote_name=u"DHCPManaged", attribute_type=int)
        self.expose_attribute(local_name=u"gateway", remote_name=u"gateway", attribute_type=int)
        self.expose_attribute(local_name=u"gateway_mac_address", remote_name=u"gatewayMACAddress", attribute_type=int)
        self.expose_attribute(local_name=u"ip_type", remote_name=u"IPType", attribute_type=int)
        self.expose_attribute(local_name=u"maintenance_mode", remote_name=u"maintenanceMode", attribute_type=int)
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=int)
        self.expose_attribute(local_name=u"netmask", remote_name=u"netmask", attribute_type=int)
        self.expose_attribute(local_name=u"route_distinguisher", remote_name=u"routeDistinguisher", attribute_type=int)
        self.expose_attribute(local_name=u"route_target", remote_name=u"routeTarget", attribute_type=int)
        self.expose_attribute(local_name=u"service_id", remote_name=u"serviceID", attribute_type=long)
        self.expose_attribute(local_name=u"vn_id", remote_name=u"vnId", attribute_type=long)
        self.expose_attribute(local_name=u"multicast", remote_name=u"multicast", attribute_type=int)
        self.expose_attribute(local_name=u"associated_multicast_channel_map_id", remote_name=u"associatedMulticastChannelMapID", attribute_type=int)
        
        # Fetchers
        self.bridge_interfaces = []
        self.bridge_interfaces_fetcher = NUBridgeInterfacesFetcher.fetcher_with_object(nurest_object=self, local_name=u"bridge_interfaces")
        self.address_ranges = []
        self.address_ranges_fetcher = NUAddressRangesFetcher.fetcher_with_object(nurest_object=self, local_name=u"address_ranges")
        self.egress_acl_templates = []
        self.egress_acl_templates_fetcher = NUEgressACLTemplatesFetcher.fetcher_with_object(nurest_object=self, local_name=u"egress_acl_templates")
        self.v_ports = []
        self.v_ports_fetcher = NUVPortsFetcher.fetcher_with_object(nurest_object=self, local_name=u"v_ports")
        self.statisticss = []
        self.statisticss_fetcher = NUStatisticssFetcher.fetcher_with_object(nurest_object=self, local_name=u"statisticss")
        self.dhcp_options = []
        self.dhcp_options_fetcher = NUDHCPOptionsFetcher.fetcher_with_object(nurest_object=self, local_name=u"dhcp_options")
        self.host_interfaces = []
        self.host_interfaces_fetcher = NUHostInterfacesFetcher.fetcher_with_object(nurest_object=self, local_name=u"host_interfaces")
        self.permitted_actions = []
        self.permitted_actions_fetcher = NUPermittedActionsFetcher.fetcher_with_object(nurest_object=self, local_name=u"permitted_actions")
        self.redirection_targets = []
        self.redirection_targets_fetcher = NURedirectionTargetsFetcher.fetcher_with_object(nurest_object=self, local_name=u"redirection_targets")
        self.policy_groups = []
        self.policy_groups_fetcher = NUPolicyGroupsFetcher.fetcher_with_object(nurest_object=self, local_name=u"policy_groups")
        self.statistics_policies = []
        self.statistics_policies_fetcher = NUStatisticsPoliciesFetcher.fetcher_with_object(nurest_object=self, local_name=u"statistics_policies")
        self.virtual_machines = []
        self.virtual_machines_fetcher = NUVirtualMachinesFetcher.fetcher_with_object(nurest_object=self, local_name=u"virtual_machines")
        self.static_routes = []
        self.static_routes_fetcher = NUStaticRoutesFetcher.fetcher_with_object(nurest_object=self, local_name=u"static_routes")
        self.groups = []
        self.groups_fetcher = NUGroupsFetcher.fetcher_with_object(nurest_object=self, local_name=u"groups")
        self.ingress_acl_templates = []
        self.ingress_acl_templates_fetcher = NUIngressACLTemplatesFetcher.fetcher_with_object(nurest_object=self, local_name=u"ingress_acl_templates")
        self.jobs = []
        self.jobs_fetcher = NUJobsFetcher.fetcher_with_object(nurest_object=self, local_name=u"jobs")
        self.ingress_advanced_forwarding_templates = []
        self.ingress_advanced_forwarding_templates_fetcher = NUIngressAdvancedForwardingTemplatesFetcher.fetcher_with_object(nurest_object=self, local_name=u"ingress_advanced_forwarding_templates")
        self.qos_primitives = []
        self.qos_primitives_fetcher = NUQosPrimitivesFetcher.fetcher_with_object(nurest_object=self, local_name=u"qos_primitives")
        self.metadatas = []
        self.metadatas_fetcher = NUMetadatasFetcher.fetcher_with_object(nurest_object=self, local_name=u"metadatas")
        self.tcas = []
        self.tcas_fetcher = NUTCAsFetcher.fetcher_with_object(nurest_object=self, local_name=u"tcas")
        self.vpn_connects = []
        self.vpn_connects_fetcher = NUVPNConnectsFetcher.fetcher_with_object(nurest_object=self, local_name=u"vpn_connects")
        self.event_logs = []
        self.event_logs_fetcher = NUEventLogsFetcher.fetcher_with_object(nurest_object=self, local_name=u"event_logs")
        for key, value in kwargs.iteritems():
            if hasattr(self, key):
                setattr(self, key, value)



    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"l2domain"


