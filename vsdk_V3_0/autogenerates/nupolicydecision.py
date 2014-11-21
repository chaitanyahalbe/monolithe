# -*- coding: utf-8 -*-

"""
NUPolicyDecision
This object is a read only object that provides the policy decisions for a particular VM interface

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

from ..fetchers import NUQosPrimitivesFetcher
from bambou import NURESTObject


class NUPolicyDecision(NURESTObject):
    """ Represents a PolicyDecision object

        IMPORTANT: This file has been autogenerated. Do not override it !

    """

    def __init__(self, **kwargs):
        """ Initializes a PolicyDecision instance

        """
        super(NUPolicyDecision, self).__init__()

        # Read/Write Attributes
        
        self._stats = str()
        self._ingress_adv_fwd = str()
        self._egress_ac_ls = str()
        self._egress_qos = str()
        self._qos = str()
        self._ingress_ac_ls = str()
        
        self.expose_attribute(local_name=u"stats", remote_name=u"stats", attribute_type=str)
        self.expose_attribute(local_name=u"ingress_adv_fwd", remote_name=u"ingressAdvFwd", attribute_type=str)
        self.expose_attribute(local_name=u"egress_ac_ls", remote_name=u"egressACLs", attribute_type=str)
        self.expose_attribute(local_name=u"egress_qos", remote_name=u"egressQos", attribute_type=str)
        self.expose_attribute(local_name=u"qos", remote_name=u"qos", attribute_type=str)
        self.expose_attribute(local_name=u"ingress_ac_ls", remote_name=u"ingressACLs", attribute_type=str)
        
        # Fetchers
        
        self.qos = []
        self.qos_fetcher = NUQosPrimitivesFetcher.fetcher_with_entity(entity=self, local_name=u"qos")
        
        for key, value in kwargs.iteritems():
            if hasattr(self, key):
                setattr(self, key, value)

    # Properties
    
    def _get_stats(self):
        """ Get attribute stats

            Stats primitive that was selected based on inheritance policies

        """
        return self._stats

    def _set_stats(self, value):
        """ Set attribute stats

            Stats primitive that was selected based on inheritance policies

        """
        self._stats = value

    stats = property(_get_stats, _set_stats)
    
    def _get_ingress_adv_fwd(self):
        """ Get attribute ingress_adv_fwd

            List of actual Ingress Redirect ACLs that will be applied on the interface of this VM

        """
        return self._ingress_adv_fwd

    def _set_ingress_adv_fwd(self, value):
        """ Set attribute ingress_adv_fwd

            List of actual Ingress Redirect ACLs that will be applied on the interface of this VM

        """
        self._ingress_adv_fwd = value

    ingress_adv_fwd = property(_get_ingress_adv_fwd, _set_ingress_adv_fwd)
    
    def _get_egress_ac_ls(self):
        """ Get attribute egress_ac_ls

            List of actual Egress ACLs that will be applied on the interface of this VM

        """
        return self._egress_ac_ls

    def _set_egress_ac_ls(self, value):
        """ Set attribute egress_ac_ls

            List of actual Egress ACLs that will be applied on the interface of this VM

        """
        self._egress_ac_ls = value

    egress_ac_ls = property(_get_egress_ac_ls, _set_egress_ac_ls)
    
    def _get_egress_qos(self):
        """ Get attribute egress_qos

            Egress QoS primitive that was selected

        """
        return self._egress_qos

    def _set_egress_qos(self, value):
        """ Set attribute egress_qos

            Egress QoS primitive that was selected

        """
        self._egress_qos = value

    egress_qos = property(_get_egress_qos, _set_egress_qos)
    
    def _get_qos(self):
        """ Get attribute qos

            QoS primitive that was selected based on inheritance policies

        """
        return self._qos

    def _set_qos(self, value):
        """ Set attribute qos

            QoS primitive that was selected based on inheritance policies

        """
        self._qos = value

    qos = property(_get_qos, _set_qos)
    
    def _get_ingress_ac_ls(self):
        """ Get attribute ingress_ac_ls

            List of actual Ingress ACLs that will be applied on the interface of this VM

        """
        return self._ingress_ac_ls

    def _set_ingress_ac_ls(self, value):
        """ Set attribute ingress_ac_ls

            List of actual Ingress ACLs that will be applied on the interface of this VM

        """
        self._ingress_ac_ls = value

    ingress_ac_ls = property(_get_ingress_ac_ls, _set_ingress_ac_ls)
    
    # Methods

    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI

        """
        return u"policydecision"
