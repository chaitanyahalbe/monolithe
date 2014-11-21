# -*- coding: utf-8 -*-

"""
NUVPortMirror
VPort Mirror Object represents the relationship between a vport and a mirror destination.

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

from bambou import NURESTObject


class NUVPortMirror(NURESTObject):
    """ Represents a VPortMirror object

        IMPORTANT: This file has been autogenerated. Do not override it !

    """

    def __init__(self, **kwargs):
        """ Initializes a VPortMirror instance

        """
        super(NUVPortMirror, self).__init__()

        # Read/Write Attributes
        
        self._v_port_name = str()
        self._domain_name = str()
        self._mirror_direction = str()
        self._mirror_destination_name = str()
        self._attached_network_type = str()
        self._mirror_destination_id = str()
        self._enterpise_name = str()
        self._network_name = str()
        self._vport_id = str()
        
        self.expose_attribute(local_name=u"v_port_name", remote_name=u"VPortName", attribute_type=str)
        self.expose_attribute(local_name=u"domain_name", remote_name=u"domainName", attribute_type=str)
        self.expose_attribute(local_name=u"mirror_direction", remote_name=u"mirrorDirection", attribute_type=str, choices=[u'BOTH', u'EGRESS', u'INGRESS'])
        self.expose_attribute(local_name=u"mirror_destination_name", remote_name=u"mirrorDestinationName", attribute_type=str)
        self.expose_attribute(local_name=u"attached_network_type", remote_name=u"attachedNetworkType", attribute_type=str)
        self.expose_attribute(local_name=u"mirror_destination_id", remote_name=u"mirrorDestinationID", attribute_type=str)
        self.expose_attribute(local_name=u"enterpise_name", remote_name=u"enterpiseName", attribute_type=str)
        self.expose_attribute(local_name=u"network_name", remote_name=u"networkName", attribute_type=str)
        self.expose_attribute(local_name=u"vport_id", remote_name=u"vportId", attribute_type=str)
        
        for key, value in kwargs.iteritems():
            if hasattr(self, key):
                setattr(self, key, value)

    # Properties
    
    def _get_v_port_name(self):
        """ Get attribute v_port_name

            Name of the vport to which the mirror destination is associated with.

        """
        return self._v_port_name

    def _set_v_port_name(self, value):
        """ Set attribute v_port_name

            Name of the vport to which the mirror destination is associated with.

        """
        self._v_port_name = value

    v_port_name = property(_get_v_port_name, _set_v_port_name)
    
    def _get_domain_name(self):
        """ Get attribute domain_name

            Domain name of the vport associated with the mirror destination

        """
        return self._domain_name

    def _set_domain_name(self, value):
        """ Set attribute domain_name

            Domain name of the vport associated with the mirror destination

        """
        self._domain_name = value

    domain_name = property(_get_domain_name, _set_domain_name)
    
    def _get_mirror_direction(self):
        """ Get attribute mirror_direction

            Describes what type of traffic needs to be mirrors - ingress/egress/both Possible values are BOTH, INGRESS, EGRESS, .

        """
        return self._mirror_direction

    def _set_mirror_direction(self, value):
        """ Set attribute mirror_direction

            Describes what type of traffic needs to be mirrors - ingress/egress/both Possible values are BOTH, INGRESS, EGRESS, .

        """
        self._mirror_direction = value

    mirror_direction = property(_get_mirror_direction, _set_mirror_direction)
    
    def _get_mirror_destination_name(self):
        """ Get attribute mirror_destination_name

            Name of the mirror destination

        """
        return self._mirror_destination_name

    def _set_mirror_destination_name(self, value):
        """ Set attribute mirror_destination_name

            Name of the mirror destination

        """
        self._mirror_destination_name = value

    mirror_destination_name = property(_get_mirror_destination_name, _set_mirror_destination_name)
    
    def _get_attached_network_type(self):
        """ Get attribute attached_network_type

            Type of the network attached - L2/L3

        """
        return self._attached_network_type

    def _set_attached_network_type(self, value):
        """ Set attribute attached_network_type

            Type of the network attached - L2/L3

        """
        self._attached_network_type = value

    attached_network_type = property(_get_attached_network_type, _set_attached_network_type)
    
    def _get_mirror_destination_id(self):
        """ Get attribute mirror_destination_id

            Destination ID of the mirror destination object.

        """
        return self._mirror_destination_id

    def _set_mirror_destination_id(self, value):
        """ Set attribute mirror_destination_id

            Destination ID of the mirror destination object.

        """
        self._mirror_destination_id = value

    mirror_destination_id = property(_get_mirror_destination_id, _set_mirror_destination_id)
    
    def _get_enterpise_name(self):
        """ Get attribute enterpise_name

            Enterprise to which the vport associated with the mirror destination belongs to.

        """
        return self._enterpise_name

    def _set_enterpise_name(self, value):
        """ Set attribute enterpise_name

            Enterprise to which the vport associated with the mirror destination belongs to.

        """
        self._enterpise_name = value

    enterpise_name = property(_get_enterpise_name, _set_enterpise_name)
    
    def _get_network_name(self):
        """ Get attribute network_name

            Name of the network to which the vport belongs to

        """
        return self._network_name

    def _set_network_name(self, value):
        """ Set attribute network_name

            Name of the network to which the vport belongs to

        """
        self._network_name = value

    network_name = property(_get_network_name, _set_network_name)
    
    def _get_vport_id(self):
        """ Get attribute vport_id

            Id of the vport to which the mirror destination is associated with.

        """
        return self._vport_id

    def _set_vport_id(self, value):
        """ Set attribute vport_id

            Id of the vport to which the mirror destination is associated with.

        """
        self._vport_id = value

    vport_id = property(_get_vport_id, _set_vport_id)
    
    # Methods

    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI

        """
        return u"vportmirror"
