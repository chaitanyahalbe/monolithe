# -*- coding: utf-8 -*-

"""
NUVSP
System Monitoring details for VSP

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

from ..fetchers import NUHSCsFetcher
from ..fetchers import NUVSCsFetcher
from ..fetchers import NUVSDsFetcher
from bambou import NURESTObject


class NUVSP(NURESTObject):
    """ Represents a VSP object

        IMPORTANT: This file has been autogenerated. Do not override it !

    """

    def __init__(self, **kwargs):
        """ Initializes a VSP instance

        """
        super(NUVSP, self).__init__()

        # Read/Write Attributes
        
        self._product_version = str()
        self._description = str()
        self._name = str()
        self._location = str()
        
        self.expose_attribute(local_name=u"product_version", remote_name=u"productVersion", attribute_type=str)
        self.expose_attribute(local_name=u"description", remote_name=u"description", attribute_type=str)
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=str)
        self.expose_attribute(local_name=u"location", remote_name=u"location", attribute_type=str)
        
        # Fetchers
        
        self.hscs = []
        self.hscs_fetcher = NUHSCsFetcher.fetcher_with_entity(entity=self, local_name=u"hscs")
        
        self.vscs = []
        self.vscs_fetcher = NUVSCsFetcher.fetcher_with_entity(entity=self, local_name=u"vscs")
        
        self.vsds = []
        self.vsds_fetcher = NUVSDsFetcher.fetcher_with_entity(entity=self, local_name=u"vsds")
        
        for key, value in kwargs.iteritems():
            if hasattr(self, key):
                setattr(self, key, value)

    # Properties
    
    def _get_product_version(self):
        """ Get attribute product_version

            Product version number for VSP

        """
        return self._product_version

    def _set_product_version(self, value):
        """ Set attribute product_version

            Product version number for VSP

        """
        self._product_version = value

    product_version = property(_get_product_version, _set_product_version)
    
    def _get_description(self):
        """ Get attribute description

            Description of the VSP

        """
        return self._description

    def _set_description(self, value):
        """ Set attribute description

            Description of the VSP

        """
        self._description = value

    description = property(_get_description, _set_description)
    
    def _get_name(self):
        """ Get attribute name

            Name of the VSP

        """
        return self._name

    def _set_name(self, value):
        """ Set attribute name

            Name of the VSP

        """
        self._name = value

    name = property(_get_name, _set_name)
    
    def _get_location(self):
        """ Get attribute location

            Installed location of the VSP product

        """
        return self._location

    def _set_location(self, value):
        """ Set attribute location

            Installed location of the VSP product

        """
        self._location = value

    location = property(_get_location, _set_location)
    
    # Methods

    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI

        """
        return u"vsp"
