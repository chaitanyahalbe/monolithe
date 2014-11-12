# -*- coding: utf-8 -*-
"""

NUBGPPeer
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



class NUBGPPeer(NURESTObject):
    """ Represents a BGPPeer object in Nuage VSD solution
        IMPORTANT: Do not override this object.
    """

    def __init__(self, **kwargs):
        """ Initialize a NUBGPPeer instance """

        super(NUBGPPeer, self).__init__()

        # Read/Write Attributes
        self.address = None  #  IP of the BGP peer. - int
        self.last_state_change = None  #  Last state change timestamp. - long
        self.status = None  #  Current connection status of the BGP peer. - int
        
        self.expose_attribute(local_name=u"address", remote_name=u"address", attribute_type=int)
        self.expose_attribute(local_name=u"last_state_change", remote_name=u"lastStateChange", attribute_type=long)
        self.expose_attribute(local_name=u"status", remote_name=u"status", attribute_type=int)
        
        # Fetchers
        for key, value in kwargs.iteritems():
            if hasattr(self, key):
                setattr(self, key, value)



    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"bgppeer"


