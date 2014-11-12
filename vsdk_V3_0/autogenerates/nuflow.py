# -*- coding: utf-8 -*-
"""

NUFlow
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

from ..fetchers import NUFlowSecurityPoliciesFetcher
from ..fetchers import NUFlowForwardingPoliciesFetcher


class NUFlow(NURESTObject):
    """ Represents a Flow object in Nuage VSD solution
        IMPORTANT: Do not override this object.
    """

    def __init__(self, **kwargs):
        """ Initialize a NUFlow instance """

        super(NUFlow, self).__init__()

        # Read/Write Attributes
        self.description = None  #  Description of the flow. - int
        self.destination_tier_id = None  #  Flow destination tier id. - int
        self.metadata = None  #  Metadata field to store flow related data. - int
        self.name = None  #  Name of the flow. - int
        self.origin_tier_id = None  #  Flow origin tier id. - int
        
        self.expose_attribute(local_name=u"description", remote_name=u"description", attribute_type=int)
        self.expose_attribute(local_name=u"destination_tier_id", remote_name=u"destinationTierID", attribute_type=int)
        self.expose_attribute(local_name=u"metadata", remote_name=u"metadata", attribute_type=int)
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=int)
        self.expose_attribute(local_name=u"origin_tier_id", remote_name=u"originTierID", attribute_type=int)
        
        # Fetchers
        self.flow_security_policies = []
        self.flow_security_policies_fetcher = NUFlowSecurityPoliciesFetcher.fetcher_with_object(nurest_object=self, local_name=u"flow_security_policies")
        self.flow_forwarding_policies = []
        self.flow_forwarding_policies_fetcher = NUFlowForwardingPoliciesFetcher.fetcher_with_object(nurest_object=self, local_name=u"flow_forwarding_policies")
        for key, value in kwargs.iteritems():
            if hasattr(self, key):
                setattr(self, key, value)



    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"flow"


