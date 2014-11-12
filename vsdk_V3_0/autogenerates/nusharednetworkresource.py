# -*- coding: utf-8 -*-
"""

NUSharedNetworkResource
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

from ..fetchers import NUAddressRangesFetcher
from ..fetchers import NUDHCPOptionsFetcher
from ..fetchers import NUVPNConnectsFetcher
from ..fetchers import NUStaticRoutesFetcher


class NUSharedNetworkResource(NURESTObject):
    """ Represents a SharedNetworkResource object in Nuage VSD solution
        IMPORTANT: Do not override this object.
    """

    def __init__(self, **kwargs):
        """ Initialize a NUSharedNetworkResource instance """

        super(NUSharedNetworkResource, self).__init__()

        # Read/Write Attributes
        self.address = None  #  Address configured on the shared resource - int
        self.description = None  #  Description of the shared resource - int
        self.dhcp_managed = None  #  true if DHCP is enabled else it is false. This value is always true for network resource of type PUBLIC or FLOATING. - int
        self.shared_resource_parent_id = None  #  Parent ID of the floating IP subnet to which this FIP subnet must be attached. If empty it will be created in a new domain. - int
        self.gateway = None  #  Gatemask configured on the shared resource - int
        self.name = None  #  Name of the shared resource. Valid characters are alphabets, numbers, space and hyphen( - ). - int
        self.netmask = None  #  Netmask configured on the shared resource - int
        self.domain_route_distinguisher = None  #  Route distinguisher configured on the shared resource - int
        self.domain_route_target = None  #  Route target configured on the shared resource - int
        self.type = None  #  Type of the shared resource. This is an enum with possible values PUBLIC/FLOATING/L2DOMAIN/UPLINK_SUBNET - int
        self.uplink_interface_ip = None  #  IP address of the host interface - int
        self.uplink_interface_mac = None  #  MAC address of the host interface - int
        self.uplink_v_port_name = None  #  Name of the uplink vport - int
        self.uplink_gw_vlan_attachment_id = None  #  VLAN ID to which this vport must be attached - int
        self.vn_id = None  #  VNID of the Shared Resource - long
        
        self.expose_attribute(local_name=u"address", remote_name=u"address", attribute_type=int)
        self.expose_attribute(local_name=u"description", remote_name=u"description", attribute_type=int)
        self.expose_attribute(local_name=u"dhcp_managed", remote_name=u"DHCPManaged", attribute_type=int)
        self.expose_attribute(local_name=u"shared_resource_parent_id", remote_name=u"sharedResourceParentID", attribute_type=int)
        self.expose_attribute(local_name=u"gateway", remote_name=u"gateway", attribute_type=int)
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=int)
        self.expose_attribute(local_name=u"netmask", remote_name=u"netmask", attribute_type=int)
        self.expose_attribute(local_name=u"domain_route_distinguisher", remote_name=u"domainRouteDistinguisher", attribute_type=int)
        self.expose_attribute(local_name=u"domain_route_target", remote_name=u"domainRouteTarget", attribute_type=int)
        self.expose_attribute(local_name=u"type", remote_name=u"type", attribute_type=int)
        self.expose_attribute(local_name=u"uplink_interface_ip", remote_name=u"uplinkInterfaceIP", attribute_type=int)
        self.expose_attribute(local_name=u"uplink_interface_mac", remote_name=u"uplinkInterfaceMAC", attribute_type=int)
        self.expose_attribute(local_name=u"uplink_v_port_name", remote_name=u"uplinkVPortName", attribute_type=int)
        self.expose_attribute(local_name=u"uplink_gw_vlan_attachment_id", remote_name=u"uplinkGWVlanAttachmentID", attribute_type=int)
        self.expose_attribute(local_name=u"vn_id", remote_name=u"vnID", attribute_type=long)
        
        # Fetchers
        self.address_ranges = []
        self.address_ranges_fetcher = NUAddressRangesFetcher.fetcher_with_object(nurest_object=self, local_name=u"address_ranges")
        self.dhcp_options = []
        self.dhcp_options_fetcher = NUDHCPOptionsFetcher.fetcher_with_object(nurest_object=self, local_name=u"dhcp_options")
        self.vpn_connects = []
        self.vpn_connects_fetcher = NUVPNConnectsFetcher.fetcher_with_object(nurest_object=self, local_name=u"vpn_connects")
        self.static_routes = []
        self.static_routes_fetcher = NUStaticRoutesFetcher.fetcher_with_object(nurest_object=self, local_name=u"static_routes")
        for key, value in kwargs.iteritems():
            if hasattr(self, key):
                setattr(self, key, value)



    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"sharednetworkresource"


