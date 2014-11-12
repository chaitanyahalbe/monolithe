# -*- coding: utf-8 -*-
"""

NUSubNetworkTemplate
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
from ..fetchers import NUSubNetworksFetcher
from ..fetchers import NUQosPrimitivesFetcher
from ..fetchers import NUEventLogsFetcher


class NUSubNetworkTemplate(NURESTObject):
    """ Represents a SubNetworkTemplate object in Nuage VSD solution
        IMPORTANT: Do not override this object.
    """

    def __init__(self, **kwargs):
        """ Initialize a NUSubNetworkTemplate instance """

        super(NUSubNetworkTemplate, self).__init__()

        # Read/Write Attributes
        self.address = None  #  IP address of the subnet defined. In case of zone, this is an optional field for and allows users to allocate an IP address range to a zone. The VSD will auto-assign IP addresses to subnets from this range if a specific IP address is not defined for the subnet - int
        self.description = None  #  A description field provided by the user that identifies the subnet - int
        self.gateway = None  #  The IP address of the gateway of this subnet - int
        self.ip_type = None  #  IPv4 or IPv6(only IPv4 is supported in R1.0) - int
        self.name = None  #  Name of the current entity(Zone or zone template or subnet etc..) Valid characters are alphabets, numbers, space and hyphen( - ). - int
        self.netmask = None  #  Netmask of the subnet defined - int
        self.multicast = None  #  multicast is enum that indicates multicast policy on Subnet/Subnet Template. Possible values are ENABLED ,DISABLED  and INHERITED - int
        self.associated_multicast_channel_map_id = None  #  The ID of the Multi Cast Channel Map  this Subnet/Subnet Template is associated with. This has to be set when  enableMultiCast is set to ENABLED - int
        self.proxy_arp = None  #   when set VRS will act as  ARP Proxy - int
        self.split_subnet = None  #  Need to add correct description - int
        
        self.expose_attribute(local_name=u"address", remote_name=u"address", attribute_type=int)
        self.expose_attribute(local_name=u"description", remote_name=u"description", attribute_type=int)
        self.expose_attribute(local_name=u"gateway", remote_name=u"gateway", attribute_type=int)
        self.expose_attribute(local_name=u"ip_type", remote_name=u"IPType", attribute_type=int)
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=int)
        self.expose_attribute(local_name=u"netmask", remote_name=u"netmask", attribute_type=int)
        self.expose_attribute(local_name=u"multicast", remote_name=u"multicast", attribute_type=int)
        self.expose_attribute(local_name=u"associated_multicast_channel_map_id", remote_name=u"associatedMulticastChannelMapID", attribute_type=int)
        self.expose_attribute(local_name=u"proxy_arp", remote_name=u"proxyARP", attribute_type=int)
        self.expose_attribute(local_name=u"split_subnet", remote_name=u"splitSubnet", attribute_type=int)
        
        # Fetchers
        self.address_ranges = []
        self.address_ranges_fetcher = NUAddressRangesFetcher.fetcher_with_object(nurest_object=self, local_name=u"address_ranges")
        self.sub_networks = []
        self.sub_networks_fetcher = NUSubNetworksFetcher.fetcher_with_object(nurest_object=self, local_name=u"sub_networks")
        self.qos_primitives = []
        self.qos_primitives_fetcher = NUQosPrimitivesFetcher.fetcher_with_object(nurest_object=self, local_name=u"qos_primitives")
        self.event_logs = []
        self.event_logs_fetcher = NUEventLogsFetcher.fetcher_with_object(nurest_object=self, local_name=u"event_logs")
        for key, value in kwargs.iteritems():
            if hasattr(self, key):
                setattr(self, key, value)



    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"subnetworktemplate"


