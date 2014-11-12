# -*- coding: utf-8 -*-
"""

NUAlarm
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



class NUAlarm(NURESTObject):
    """ Represents a Alarm object in Nuage VSD solution
        IMPORTANT: Do not override this object.
    """

    def __init__(self, **kwargs):
        """ Initialize a NUAlarm instance """

        super(NUAlarm, self).__init__()

        # Read/Write Attributes
        self.acknowledged = None  #  Flag to indicate that is already acknowledge or not - int
        self.target_object = None  #  Identifies affected Entity.  Example: Alarm generated by TCA for Domain domain1(Packets towards a VM, Breach) - int
        self.timestamp = None  #  Indicates the time that the alarm was triggered - long
        self.description = None  #  Description of the alarm - int
        self.enterprise_id = None  #  Enterprise that this alarm belongs to - int
        self.error_condition = None  #  Identifies the error condition - int
        self.name = None  #  The alarm name.  Each type of alarm will generate its own name - int
        self.number_of_occurances = None  #  Number of times that the alarm was triggered - int
        self.reason = None  #  Provides a description of the alarm - int
        self.severity = None  #  Severity of the alarm. - MAJOR, MINOR, CRITICAL, INFO, WARNING. - int
        
        self.expose_attribute(local_name=u"acknowledged", remote_name=u"acknowledged", attribute_type=int)
        self.expose_attribute(local_name=u"target_object", remote_name=u"targetObject", attribute_type=int)
        self.expose_attribute(local_name=u"timestamp", remote_name=u"timestamp", attribute_type=long)
        self.expose_attribute(local_name=u"description", remote_name=u"description", attribute_type=int)
        self.expose_attribute(local_name=u"enterprise_id", remote_name=u"enterpriseID", attribute_type=int)
        self.expose_attribute(local_name=u"error_condition", remote_name=u"errorCondition", attribute_type=int)
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=int)
        self.expose_attribute(local_name=u"number_of_occurances", remote_name=u"numberOfOccurances", attribute_type=int)
        self.expose_attribute(local_name=u"reason", remote_name=u"reason", attribute_type=int)
        self.expose_attribute(local_name=u"severity", remote_name=u"severity", attribute_type=int)
        
        # Fetchers
        for key, value in kwargs.iteritems():
            if hasattr(self, key):
                setattr(self, key, value)



    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"alarm"


