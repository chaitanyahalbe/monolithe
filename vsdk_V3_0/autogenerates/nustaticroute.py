# -*- coding: utf-8 -*-
"""

NUStaticRoute
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

from ..fetchers import NUEventLogsFetcher


class NUStaticRoute(NURESTObject):
    """ Represents a StaticRoute object in Nuage VSD solution
        IMPORTANT: Do not override this object.
    """

    def __init__(self, **kwargs):
        """ Initialize a NUStaticRoute instance """

        super(NUStaticRoute, self).__init__()

        # Read/Write Attributes
        self.address = None  #  IP address of the route - int
        self.ip_type = None  #  IPv4 or IPv6 (only IPv4 supported in R1.0) - int
        self.netmask = None  #  Netmask associated with the route - int
        self.next_hop_ip = None  #  IP address of the next hop. This must be a VM attached to the dVRS - int
        
        self.expose_attribute(local_name=u"address", remote_name=u"address", attribute_type=int)
        self.expose_attribute(local_name=u"ip_type", remote_name=u"IPType", attribute_type=int)
        self.expose_attribute(local_name=u"netmask", remote_name=u"netmask", attribute_type=int)
        self.expose_attribute(local_name=u"next_hop_ip", remote_name=u"nextHopIp", attribute_type=int)
        
        # Fetchers
        self.event_logs = []
        self.event_logs_fetcher = NUEventLogsFetcher.fetcher_with_object(nurest_object=self, local_name=u"event_logs")
        for key, value in kwargs.iteritems():
            if hasattr(self, key):
                setattr(self, key, value)



    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"staticroute"


