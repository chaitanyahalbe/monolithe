# -*- coding: utf-8 -*-

"""
NUL2DomainTemplate
L2 Domain in VSD as derived by templates. This object describes the L2 Domain template

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

from ..fetchers import NUEgressACLTemplatesFetcher
from ..fetchers import NUIngressACLTemplatesFetcher
from ..fetchers import NUJobsFetcher
from ..fetchers import NUAddressRangesFetcher
from ..fetchers import NUPolicyGroupTemplatesFetcher
from ..fetchers import NUGroupsFetcher
from ..fetchers import NUL2DomainsFetcher
from ..fetchers import NUIngressAdvancedForwardingTemplatesFetcher
from ..fetchers import NURedirectionTargetTemplatesFetcher
from ..fetchers import NUPermittedActionsFetcher
from ..fetchers import NUQosPrimitivesFetcher
from bambou import NURESTObject


class NUL2DomainTemplate(NURESTObject):
    """ Represents a L2DomainTemplate object

        IMPORTANT: This file has been autogenerated. Do not override it !

    """

    def __init__(self, **kwargs):
        """ Initializes a L2DomainTemplate instance

        """
        super(NUL2DomainTemplate, self).__init__()

        # Read/Write Attributes
        
        self._ip_type = str()
        self._dhcp_managed = bool()
        self._description = str()
        self._associated_multicast_channel_map_id = str()
        self._netmask = str()
        self._multicast = str()
        self._address = str()
        self._gateway = str()
        self._name = str()
        
        self.expose_attribute(local_name=u"ip_type", remote_name=u"IPType", attribute_type=str, choices=[u'IPV6', u'IPV4'])
        self.expose_attribute(local_name=u"dhcp_managed", remote_name=u"DHCPManaged", attribute_type=bool)
        self.expose_attribute(local_name=u"description", remote_name=u"description", attribute_type=str)
        self.expose_attribute(local_name=u"associated_multicast_channel_map_id", remote_name=u"associatedMulticastChannelMapID", attribute_type=str)
        self.expose_attribute(local_name=u"netmask", remote_name=u"netmask", attribute_type=str)
        self.expose_attribute(local_name=u"multicast", remote_name=u"multicast", attribute_type=str, choices=[u'ENABLED', u'INHERITED', u'DISABLED'])
        self.expose_attribute(local_name=u"address", remote_name=u"address", attribute_type=str)
        self.expose_attribute(local_name=u"gateway", remote_name=u"gateway", attribute_type=str)
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=str)
        
        # Fetchers
        
        self.egressacltemplates = []
        self.egressacltemplates_fetcher = NUEgressACLTemplatesFetcher.fetcher_with_entity(entity=self, local_name=u"egressacltemplates")
        
        self.ingressacltemplates = []
        self.ingressacltemplates_fetcher = NUIngressACLTemplatesFetcher.fetcher_with_entity(entity=self, local_name=u"ingressacltemplates")
        
        self.jobs = []
        self.jobs_fetcher = NUJobsFetcher.fetcher_with_entity(entity=self, local_name=u"jobs")
        
        self.addressranges = []
        self.addressranges_fetcher = NUAddressRangesFetcher.fetcher_with_entity(entity=self, local_name=u"addressranges")
        
        self.policygrouptemplates = []
        self.policygrouptemplates_fetcher = NUPolicyGroupTemplatesFetcher.fetcher_with_entity(entity=self, local_name=u"policygrouptemplates")
        
        self.groups = []
        self.groups_fetcher = NUGroupsFetcher.fetcher_with_entity(entity=self, local_name=u"groups")
        
        self.l2domains = []
        self.l2domains_fetcher = NUL2DomainsFetcher.fetcher_with_entity(entity=self, local_name=u"l2domains")
        
        self.ingressadvfwdtemplates = []
        self.ingressadvfwdtemplates_fetcher = NUIngressAdvancedForwardingTemplatesFetcher.fetcher_with_entity(entity=self, local_name=u"ingressadvfwdtemplates")
        
        self.redirectiontargettemplates = []
        self.redirectiontargettemplates_fetcher = NURedirectionTargetTemplatesFetcher.fetcher_with_entity(entity=self, local_name=u"redirectiontargettemplates")
        
        self.permissions = []
        self.permissions_fetcher = NUPermittedActionsFetcher.fetcher_with_entity(entity=self, local_name=u"permissions")
        
        self.qos = []
        self.qos_fetcher = NUQosPrimitivesFetcher.fetcher_with_entity(entity=self, local_name=u"qos")
        
        for key, value in kwargs.iteritems():
            if hasattr(self, key):
                setattr(self, key, value)

    # Properties
    
    def _get_ip_type(self):
        """ Get attribute ip_type

            IPv4 or IPv6(only IPv4 is supported in R2.0) Possible values are IPV4, IPV6, .

        """
        return self._ip_type

    def _set_ip_type(self, value):
        """ Set attribute ip_type

            IPv4 or IPv6(only IPv4 is supported in R2.0) Possible values are IPV4, IPV6, .

        """
        self._ip_type = value

    ip_type = property(_get_ip_type, _set_ip_type)
    
    def _get_dhcp_managed(self):
        """ Get attribute dhcp_managed

            decides whether L2Domain / L2Domain template DHCP is managed by VSD

        """
        return self._dhcp_managed

    def _set_dhcp_managed(self, value):
        """ Set attribute dhcp_managed

            decides whether L2Domain / L2Domain template DHCP is managed by VSD

        """
        self._dhcp_managed = value

    dhcp_managed = property(_get_dhcp_managed, _set_dhcp_managed)
    
    def _get_description(self):
        """ Get attribute description

            A description field provided by the user that identifies the L2Domain / L2Domain template.

        """
        return self._description

    def _set_description(self, value):
        """ Set attribute description

            A description field provided by the user that identifies the L2Domain / L2Domain template.

        """
        self._description = value

    description = property(_get_description, _set_description)
    
    def _get_associated_multicast_channel_map_id(self):
        """ Get attribute associated_multicast_channel_map_id

            The ID of the Multi Cast Channel Map this L2Domain / L2Domain template template is associated with. This has to be set when  enableMultiCast is set to ENABLED

        """
        return self._associated_multicast_channel_map_id

    def _set_associated_multicast_channel_map_id(self, value):
        """ Set attribute associated_multicast_channel_map_id

            The ID of the Multi Cast Channel Map this L2Domain / L2Domain template template is associated with. This has to be set when  enableMultiCast is set to ENABLED

        """
        self._associated_multicast_channel_map_id = value

    associated_multicast_channel_map_id = property(_get_associated_multicast_channel_map_id, _set_associated_multicast_channel_map_id)
    
    def _get_netmask(self):
        """ Get attribute netmask

            Netmask of the L2Domain / L2Domain template defined

        """
        return self._netmask

    def _set_netmask(self, value):
        """ Set attribute netmask

            Netmask of the L2Domain / L2Domain template defined

        """
        self._netmask = value

    netmask = property(_get_netmask, _set_netmask)
    
    def _get_multicast(self):
        """ Get attribute multicast

            multicast is enum that indicates multicast policy on L2Domain / L2Domain template. Possible values are ENABLED and DISABLED Possible values are INHERITED, ENABLED, DISABLED, .

        """
        return self._multicast

    def _set_multicast(self, value):
        """ Set attribute multicast

            multicast is enum that indicates multicast policy on L2Domain / L2Domain template. Possible values are ENABLED and DISABLED Possible values are INHERITED, ENABLED, DISABLED, .

        """
        self._multicast = value

    multicast = property(_get_multicast, _set_multicast)
    
    def _get_address(self):
        """ Get attribute address

            Network address of the L2Domain / L2Domain template defined. 

        """
        return self._address

    def _set_address(self, value):
        """ Set attribute address

            Network address of the L2Domain / L2Domain template defined. 

        """
        self._address = value

    address = property(_get_address, _set_address)
    
    def _get_gateway(self):
        """ Get attribute gateway

            The IP address of the gateway of this l2 domain

        """
        return self._gateway

    def _set_gateway(self, value):
        """ Set attribute gateway

            The IP address of the gateway of this l2 domain

        """
        self._gateway = value

    gateway = property(_get_gateway, _set_gateway)
    
    def _get_name(self):
        """ Get attribute name

            Name of the L2Domain / L2Domain template,has to be unique within a Enterprise. Valid characters are alphabets, numbers, space and hyphen( - ).

        """
        return self._name

    def _set_name(self, value):
        """ Set attribute name

            Name of the L2Domain / L2Domain template,has to be unique within a Enterprise. Valid characters are alphabets, numbers, space and hyphen( - ).

        """
        self._name = value

    name = property(_get_name, _set_name)
    
    # Methods

    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI

        """
        return u"l2domaintemplate"
