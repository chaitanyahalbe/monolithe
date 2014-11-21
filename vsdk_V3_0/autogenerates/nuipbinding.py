# -*- coding: utf-8 -*-

"""
NUIPBinding
This is the definition of a IP Bindings associated with in a Network

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


class NUIPBinding(NURESTObject):
    """ Represents a IPBinding object

        IMPORTANT: This file has been autogenerated. Do not override it !

    """

    def __init__(self, **kwargs):
        """ Initializes a IPBinding instance

        """
        super(NUIPBinding, self).__init__()

        # Read/Write Attributes
        
        self._dynamic_allocation_enabled = bool()
        self._mac = str()
        self._ip_address = str()
        
        self.expose_attribute(local_name=u"dynamic_allocation_enabled", remote_name=u"dynamicAllocationEnabled", attribute_type=bool)
        self.expose_attribute(local_name=u"mac", remote_name=u"MAC", attribute_type=str)
        self.expose_attribute(local_name=u"ip_address", remote_name=u"IPAddress", attribute_type=str)
        
        for key, value in kwargs.iteritems():
            if hasattr(self, key):
                setattr(self, key, value)

    # Properties
    
    def _get_dynamic_allocation_enabled(self):
        """ Get attribute dynamic_allocation_enabled

            Binding is static or dynamic

        """
        return self._dynamic_allocation_enabled

    def _set_dynamic_allocation_enabled(self, value):
        """ Set attribute dynamic_allocation_enabled

            Binding is static or dynamic

        """
        self._dynamic_allocation_enabled = value

    dynamic_allocation_enabled = property(_get_dynamic_allocation_enabled, _set_dynamic_allocation_enabled)
    
    def _get_mac(self):
        """ Get attribute mac

            MAC Address

        """
        return self._mac

    def _set_mac(self, value):
        """ Set attribute mac

            MAC Address

        """
        self._mac = value

    mac = property(_get_mac, _set_mac)
    
    def _get_ip_address(self):
        """ Get attribute ip_address

            Static IP Address

        """
        return self._ip_address

    def _set_ip_address(self, value):
        """ Set attribute ip_address

            Static IP Address

        """
        self._ip_address = value

    ip_address = property(_get_ip_address, _set_ip_address)
    
    # Methods

    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI

        """
        return u"ipreservation"
