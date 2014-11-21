# -*- coding: utf-8 -*-

"""
NUInfrastructureConfig
Represents Infrastructure Config

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


class NUInfrastructureConfig(NURESTObject):
    """ Represents a InfrastructureConfig object

        IMPORTANT: This file has been autogenerated. Do not override it !

    """

    def __init__(self, **kwargs):
        """ Initializes a InfrastructureConfig instance

        """
        super(NUInfrastructureConfig, self).__init__()

        # Read/Write Attributes
        
        self._config = str()
        
        self.expose_attribute(local_name=u"config", remote_name=u"config", attribute_type=str)
        
        for key, value in kwargs.iteritems():
            if hasattr(self, key):
                setattr(self, key, value)

    # Properties
    
    def _get_config(self):
        """ Get attribute config

            Infrastructure Config

        """
        return self._config

    def _set_config(self, value):
        """ Set attribute config

            Infrastructure Config

        """
        self._config = value

    config = property(_get_config, _set_config)
    
    # Methods

    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI

        """
        return u"infraconfi"
