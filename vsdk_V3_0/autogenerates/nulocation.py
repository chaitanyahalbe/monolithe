# -*- coding: utf-8 -*-

"""
NULocation
Gateway location details

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


class NULocation(NURESTObject):
    """ Represents a Location object

        IMPORTANT: This file has been autogenerated. Do not override it !

    """

    def __init__(self, **kwargs):
        """ Initializes a Location instance

        """
        super(NULocation, self).__init__()

        # Read/Write Attributes
        
        self._time_zone_id = str()
        self._locality = str()
        self._country = str()
        self._longitude = float()
        self._state = str()
        self._address = str()
        self._latitude = float()
        
        self.expose_attribute(local_name=u"time_zone_id", remote_name=u"timeZoneID", attribute_type=str)
        self.expose_attribute(local_name=u"locality", remote_name=u"locality", attribute_type=str)
        self.expose_attribute(local_name=u"country", remote_name=u"country", attribute_type=str)
        self.expose_attribute(local_name=u"longitude", remote_name=u"longitude", attribute_type=float)
        self.expose_attribute(local_name=u"state", remote_name=u"state", attribute_type=str)
        self.expose_attribute(local_name=u"address", remote_name=u"address", attribute_type=str)
        self.expose_attribute(local_name=u"latitude", remote_name=u"latitude", attribute_type=float)
        
        for key, value in kwargs.iteritems():
            if hasattr(self, key):
                setattr(self, key, value)

    # Properties
    
    def _get_time_zone_id(self):
        """ Get attribute time_zone_id

            Time zone in which the Gateway is located.  This can be in the form of a UTC/GMT offset, continent/city location, or country/region.  The available time zones can be found in /usr/share/zoneinfo on a Linux machine or retrieved with TimeZone.getAvailableIDs() in Java.  Refer to the IANA (Internet Assigned Numbers Authority) for a list of time zones.  URL :  http://www.iana.org/time-zones  Default value is UTC (translating to Etc/Zulu)

        """
        return self._time_zone_id

    def _set_time_zone_id(self, value):
        """ Set attribute time_zone_id

            Time zone in which the Gateway is located.  This can be in the form of a UTC/GMT offset, continent/city location, or country/region.  The available time zones can be found in /usr/share/zoneinfo on a Linux machine or retrieved with TimeZone.getAvailableIDs() in Java.  Refer to the IANA (Internet Assigned Numbers Authority) for a list of time zones.  URL :  http://www.iana.org/time-zones  Default value is UTC (translating to Etc/Zulu)

        """
        self._time_zone_id = value

    time_zone_id = property(_get_time_zone_id, _set_time_zone_id)
    
    def _get_locality(self):
        """ Get attribute locality

            Locality/City/County

        """
        return self._locality

    def _set_locality(self, value):
        """ Set attribute locality

            Locality/City/County

        """
        self._locality = value

    locality = property(_get_locality, _set_locality)
    
    def _get_country(self):
        """ Get attribute country

            Country

        """
        return self._country

    def _set_country(self, value):
        """ Set attribute country

            Country

        """
        self._country = value

    country = property(_get_country, _set_country)
    
    def _get_longitude(self):
        """ Get attribute longitude

            Longitude in decimal format.

        """
        return self._longitude

    def _set_longitude(self, value):
        """ Set attribute longitude

            Longitude in decimal format.

        """
        self._longitude = value

    longitude = property(_get_longitude, _set_longitude)
    
    def _get_state(self):
        """ Get attribute state

            State/Province/Region

        """
        return self._state

    def _set_state(self, value):
        """ Set attribute state

            State/Province/Region

        """
        self._state = value

    state = property(_get_state, _set_state)
    
    def _get_address(self):
        """ Get attribute address

            Formatted address including property number, street name, suite or office number, ...

        """
        return self._address

    def _set_address(self, value):
        """ Set attribute address

            Formatted address including property number, street name, suite or office number, ...

        """
        self._address = value

    address = property(_get_address, _set_address)
    
    def _get_latitude(self):
        """ Get attribute latitude

            Latitude in decimal format.

        """
        return self._latitude

    def _set_latitude(self, value):
        """ Set attribute latitude

            Latitude in decimal format.

        """
        self._latitude = value

    latitude = property(_get_latitude, _set_latitude)
    
    # Methods

    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI

        """
        return u"location"
