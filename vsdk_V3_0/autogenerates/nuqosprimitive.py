# -*- coding: utf-8 -*-

"""
NUQosPrimitive
The object manipulates the QoS parameters attached to a domain, zone, or subnet

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

from ..fetchers import NUVirtualMachinesFetcher
from bambou import NURESTObject


class NUQosPrimitive(NURESTObject):
    """ Represents a QosPrimitive object

        IMPORTANT: This file has been autogenerated. Do not override it !

    """

    def __init__(self, **kwargs):
        """ Initializes a QosPrimitive instance

        """
        super(NUQosPrimitive, self).__init__()

        # Read/Write Attributes
        
        self._rewrite_forwarding_class = bool()
        self._committed_information_rate = str()
        self._associated_dscp_forwarding_class_table_id = str()
        self._description = str()
        self._bum_peak_burst_size = str()
        self._burst = str()
        self._committed_burst_size = str()
        self._bum_rate_limiting_active = bool()
        self._service_class = str()
        self._bum_committed_burst_size = str()
        self._bum_peak_information_rate = str()
        self._bum_committed_information_rate = str()
        self._peak = str()
        self._trusted_forwarding_class = bool()
        self._rate_limiting_active = bool()
        self._active = bool()
        self._assoc_qos_id = str()
        self._associated_dscp_forwarding_class_table_name = str()
        self._name = str()
        
        self.expose_attribute(local_name=u"rewrite_forwarding_class", remote_name=u"rewriteForwardingClass", attribute_type=bool)
        self.expose_attribute(local_name=u"committed_information_rate", remote_name=u"committedInformationRate", attribute_type=str)
        self.expose_attribute(local_name=u"associated_dscp_forwarding_class_table_id", remote_name=u"associatedDSCPForwardingClassTableID", attribute_type=str)
        self.expose_attribute(local_name=u"description", remote_name=u"description", attribute_type=str)
        self.expose_attribute(local_name=u"bum_peak_burst_size", remote_name=u"BUMPeakBurstSize", attribute_type=str)
        self.expose_attribute(local_name=u"burst", remote_name=u"burst", attribute_type=str)
        self.expose_attribute(local_name=u"committed_burst_size", remote_name=u"committedBurstSize", attribute_type=str)
        self.expose_attribute(local_name=u"bum_rate_limiting_active", remote_name=u"BUMRateLimitingActive", attribute_type=bool)
        self.expose_attribute(local_name=u"service_class", remote_name=u"serviceClass", attribute_type=str, choices=[u'D', u'E', u'F', u'G', u'A', u'B', u'C', u'H', u'NONE'])
        self.expose_attribute(local_name=u"bum_committed_burst_size", remote_name=u"BUMCommittedBurstSize", attribute_type=str)
        self.expose_attribute(local_name=u"bum_peak_information_rate", remote_name=u"BUMPeakInformationRate", attribute_type=str)
        self.expose_attribute(local_name=u"bum_committed_information_rate", remote_name=u"BUMCommittedInformationRate", attribute_type=str)
        self.expose_attribute(local_name=u"peak", remote_name=u"peak", attribute_type=str)
        self.expose_attribute(local_name=u"trusted_forwarding_class", remote_name=u"trustedForwardingClass", attribute_type=bool)
        self.expose_attribute(local_name=u"rate_limiting_active", remote_name=u"rateLimitingActive", attribute_type=bool)
        self.expose_attribute(local_name=u"active", remote_name=u"active", attribute_type=bool)
        self.expose_attribute(local_name=u"assoc_qos_id", remote_name=u"assocQosId", attribute_type=str)
        self.expose_attribute(local_name=u"associated_dscp_forwarding_class_table_name", remote_name=u"associatedDSCPForwardingClassTableName", attribute_type=str)
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=str)
        
        # Fetchers
        
        self.vms = []
        self.vms_fetcher = NUVirtualMachinesFetcher.fetcher_with_entity(entity=self, local_name=u"vms")
        
        for key, value in kwargs.iteritems():
            if hasattr(self, key):
                setattr(self, key, value)

    # Properties
    
    def _get_rewrite_forwarding_class(self):
        """ Get attribute rewrite_forwarding_class

            Specifies if the rewrite flag is set for the QoS policy / template

        """
        return self._rewrite_forwarding_class

    def _set_rewrite_forwarding_class(self, value):
        """ Set attribute rewrite_forwarding_class

            Specifies if the rewrite flag is set for the QoS policy / template

        """
        self._rewrite_forwarding_class = value

    rewrite_forwarding_class = property(_get_rewrite_forwarding_class, _set_rewrite_forwarding_class)
    
    def _get_committed_information_rate(self):
        """ Get attribute committed_information_rate

            Committed bandwidth that is allowed from each VM

        """
        return self._committed_information_rate

    def _set_committed_information_rate(self, value):
        """ Set attribute committed_information_rate

            Committed bandwidth that is allowed from each VM

        """
        self._committed_information_rate = value

    committed_information_rate = property(_get_committed_information_rate, _set_committed_information_rate)
    
    def _get_associated_dscp_forwarding_class_table_id(self):
        """ Get attribute associated_dscp_forwarding_class_table_id

            ID of the DSCP->Forwarding Class used by this Qos Policy

        """
        return self._associated_dscp_forwarding_class_table_id

    def _set_associated_dscp_forwarding_class_table_id(self, value):
        """ Set attribute associated_dscp_forwarding_class_table_id

            ID of the DSCP->Forwarding Class used by this Qos Policy

        """
        self._associated_dscp_forwarding_class_table_id = value

    associated_dscp_forwarding_class_table_id = property(_get_associated_dscp_forwarding_class_table_id, _set_associated_dscp_forwarding_class_table_id)
    
    def _get_description(self):
        """ Get attribute description

            A description of the QoS object

        """
        return self._description

    def _set_description(self, value):
        """ Set attribute description

            A description of the QoS object

        """
        self._description = value

    description = property(_get_description, _set_description)
    
    def _get_bum_peak_burst_size(self):
        """ Get attribute bum_peak_burst_size

            Peak burst size setting for Broadcast/Multicast rate limiting

        """
        return self._bum_peak_burst_size

    def _set_bum_peak_burst_size(self, value):
        """ Set attribute bum_peak_burst_size

            Peak burst size setting for Broadcast/Multicast rate limiting

        """
        self._bum_peak_burst_size = value

    bum_peak_burst_size = property(_get_bum_peak_burst_size, _set_bum_peak_burst_size)
    
    def _get_burst(self):
        """ Get attribute burst

            The maximum burst size associated with the rate limiter

        """
        return self._burst

    def _set_burst(self, value):
        """ Set attribute burst

            The maximum burst size associated with the rate limiter

        """
        self._burst = value

    burst = property(_get_burst, _set_burst)
    
    def _get_committed_burst_size(self):
        """ Get attribute committed_burst_size

            Committed burst size associated with the rate limiter

        """
        return self._committed_burst_size

    def _set_committed_burst_size(self, value):
        """ Set attribute committed_burst_size

            Committed burst size associated with the rate limiter

        """
        self._committed_burst_size = value

    committed_burst_size = property(_get_committed_burst_size, _set_committed_burst_size)
    
    def _get_bum_rate_limiting_active(self):
        """ Get attribute bum_rate_limiting_active

            Flag the indicates whether Broadcast/Multicast rate limiting is enabled or disabled

        """
        return self._bum_rate_limiting_active

    def _set_bum_rate_limiting_active(self, value):
        """ Set attribute bum_rate_limiting_active

            Flag the indicates whether Broadcast/Multicast rate limiting is enabled or disabled

        """
        self._bum_rate_limiting_active = value

    bum_rate_limiting_active = property(_get_bum_rate_limiting_active, _set_bum_rate_limiting_active)
    
    def _get_service_class(self):
        """ Get attribute service_class

            Class of service to be used. Service classes in order of priority are A (1), B (2), C(3), D(4), E(5), F(6), G(7) and H(8) Possible values are NONE, A, B, C, D, E, F, G, H, .

        """
        return self._service_class

    def _set_service_class(self, value):
        """ Set attribute service_class

            Class of service to be used. Service classes in order of priority are A (1), B (2), C(3), D(4), E(5), F(6), G(7) and H(8) Possible values are NONE, A, B, C, D, E, F, G, H, .

        """
        self._service_class = value

    service_class = property(_get_service_class, _set_service_class)
    
    def _get_bum_committed_burst_size(self):
        """ Get attribute bum_committed_burst_size

            Committed burst size setting for BUM Shaper

        """
        return self._bum_committed_burst_size

    def _set_bum_committed_burst_size(self, value):
        """ Set attribute bum_committed_burst_size

            Committed burst size setting for BUM Shaper

        """
        self._bum_committed_burst_size = value

    bum_committed_burst_size = property(_get_bum_committed_burst_size, _set_bum_committed_burst_size)
    
    def _get_bum_peak_information_rate(self):
        """ Get attribute bum_peak_information_rate

            Peak rate setting for Broadcast/Multicast rate limiting

        """
        return self._bum_peak_information_rate

    def _set_bum_peak_information_rate(self, value):
        """ Set attribute bum_peak_information_rate

            Peak rate setting for Broadcast/Multicast rate limiting

        """
        self._bum_peak_information_rate = value

    bum_peak_information_rate = property(_get_bum_peak_information_rate, _set_bum_peak_information_rate)
    
    def _get_bum_committed_information_rate(self):
        """ Get attribute bum_committed_information_rate

            Committed information rate setting for BUM Shaper

        """
        return self._bum_committed_information_rate

    def _set_bum_committed_information_rate(self, value):
        """ Set attribute bum_committed_information_rate

            Committed information rate setting for BUM Shaper

        """
        self._bum_committed_information_rate = value

    bum_committed_information_rate = property(_get_bum_committed_information_rate, _set_bum_committed_information_rate)
    
    def _get_peak(self):
        """ Get attribute peak

            Peak bandwidth that is allowed from each VM

        """
        return self._peak

    def _set_peak(self, value):
        """ Set attribute peak

            Peak bandwidth that is allowed from each VM

        """
        self._peak = value

    peak = property(_get_peak, _set_peak)
    
    def _get_trusted_forwarding_class(self):
        """ Get attribute trusted_forwarding_class

            Specifies if the trusted flag is set for the QoS policy / template

        """
        return self._trusted_forwarding_class

    def _set_trusted_forwarding_class(self, value):
        """ Set attribute trusted_forwarding_class

            Specifies if the trusted flag is set for the QoS policy / template

        """
        self._trusted_forwarding_class = value

    trusted_forwarding_class = property(_get_trusted_forwarding_class, _set_trusted_forwarding_class)
    
    def _get_rate_limiting_active(self):
        """ Get attribute rate_limiting_active

            Identifies if rate limiting must be implemented

        """
        return self._rate_limiting_active

    def _set_rate_limiting_active(self, value):
        """ Set attribute rate_limiting_active

            Identifies if rate limiting must be implemented

        """
        self._rate_limiting_active = value

    rate_limiting_active = property(_get_rate_limiting_active, _set_rate_limiting_active)
    
    def _get_active(self):
        """ Get attribute active

            If enabled, it means that this ACL or QOS entry is active

        """
        return self._active

    def _set_active(self, value):
        """ Set attribute active

            If enabled, it means that this ACL or QOS entry is active

        """
        self._active = value

    active = property(_get_active, _set_active)
    
    def _get_assoc_qos_id(self):
        """ Get attribute assoc_qos_id

            ID of object associated with this QoS object

        """
        return self._assoc_qos_id

    def _set_assoc_qos_id(self, value):
        """ Set attribute assoc_qos_id

            ID of object associated with this QoS object

        """
        self._assoc_qos_id = value

    assoc_qos_id = property(_get_assoc_qos_id, _set_assoc_qos_id)
    
    def _get_associated_dscp_forwarding_class_table_name(self):
        """ Get attribute associated_dscp_forwarding_class_table_name

            Name of the DSCP->Forwarding Class used by this Qos Policy

        """
        return self._associated_dscp_forwarding_class_table_name

    def _set_associated_dscp_forwarding_class_table_name(self, value):
        """ Set attribute associated_dscp_forwarding_class_table_name

            Name of the DSCP->Forwarding Class used by this Qos Policy

        """
        self._associated_dscp_forwarding_class_table_name = value

    associated_dscp_forwarding_class_table_name = property(_get_associated_dscp_forwarding_class_table_name, _set_associated_dscp_forwarding_class_table_name)
    
    def _get_name(self):
        """ Get attribute name

            A unique name of the QoS object

        """
        return self._name

    def _set_name(self, value):
        """ Set attribute name

            A unique name of the QoS object

        """
        self._name = value

    name = property(_get_name, _set_name)
    
    # Methods

    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI

        """
        return u"qo"
