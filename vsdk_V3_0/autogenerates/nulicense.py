# -*- coding: utf-8 -*-
"""

NULicense
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

from ..fetchers import NUEventLogsFetcher


class NULicense(NURESTObject):
    """ Represents a License object in Nuage VSD solution
        IMPORTANT: Do not override this object.
    """

    def __init__(self, **kwargs):
        """ Initialize a NULicense instance """

        super(NULicense, self).__init__()

        # Read/Write Attributes
        self.allowed_cpes_count = None  #  Maximum number of CPEs enabled with this license. A value of -1 indicates an unlimited number of CPEs - long
        self.allowed_nics_count = None  #  Maximum number of NICs allowed. A value of -1 indicates unlimited number of NICs - long
        self.allowed_vms_count = None  #  Maximum number of VMs enabled with this license. A value of -1 indicates an unlimited number of VMs - long
        self.allowed_vrsgs_count = None  #  Maximum number of VRSGs enabled with this license. A value of -1 indicates an unlimited number of VRSGs - long
        self.allowed_vrss_count = None  #  Maximum number of VRSs enabled with this license. A value of -1 indicates an unlimited number of VRSs - long
        self.city = None  #  City of the owner associated with the license file - int
        self.company = None  #  Company of the owner associated with the license file - int
        self.country = None  #  Country of the owner associated with the license file - int
        self.customer_key = None  #  Customer key associated with the licese - int
        self.email = None  #  Email of the owner associated with the license file - int
        self.expiration_date = None  #  Expiration date of this license - int
        self.is_cluster_license = None  #  Indicates if the license is associated with standlone or cluster setup of VSD - int
        self.license = None  #  Base 64 value of the license - int
        self.license_id = None  #  Unique identifier of the license file - int
        self.license_type = None  #   - int
        self.major_release = None  #  Major software release associated with this license - int
        self.minor_release = None  #  Minor software release for which this license has been issued - int
        self.phone = None  #  Phone number of the owner associated with the license file - int
        self.product_version = None  #  Version of the product that this license applies to - int
        self.provider = None  #  Provider of the license file - int
        self.state = None  #  State of the owner associated with the license file - int
        self.street = None  #  Address of the owner associated with the license file - int
        self.user_name = None  #  The name of the user associated with the license - int
        self.zip = None  #  Zipcode of the owner associated with the license file - int
        
        self.expose_attribute(local_name=u"allowed_cpes_count", remote_name=u"allowedCPEsCount", attribute_type=long)
        self.expose_attribute(local_name=u"allowed_nics_count", remote_name=u"allowedNICsCount", attribute_type=long)
        self.expose_attribute(local_name=u"allowed_vms_count", remote_name=u"allowedVMsCount", attribute_type=long)
        self.expose_attribute(local_name=u"allowed_vrsgs_count", remote_name=u"allowedVRSGsCount", attribute_type=long)
        self.expose_attribute(local_name=u"allowed_vrss_count", remote_name=u"allowedVRSsCount", attribute_type=long)
        self.expose_attribute(local_name=u"city", remote_name=u"city", attribute_type=int)
        self.expose_attribute(local_name=u"company", remote_name=u"company", attribute_type=int)
        self.expose_attribute(local_name=u"country", remote_name=u"country", attribute_type=int)
        self.expose_attribute(local_name=u"customer_key", remote_name=u"customerKey", attribute_type=int)
        self.expose_attribute(local_name=u"email", remote_name=u"email", attribute_type=int)
        self.expose_attribute(local_name=u"expiration_date", remote_name=u"expirationDate", attribute_type=int)
        self.expose_attribute(local_name=u"is_cluster_license", remote_name=u"isClusterLicense", attribute_type=int)
        self.expose_attribute(local_name=u"license", remote_name=u"license", attribute_type=int)
        self.expose_attribute(local_name=u"license_id", remote_name=u"licenseID", attribute_type=int)
        self.expose_attribute(local_name=u"license_type", remote_name=u"licenseType", attribute_type=int)
        self.expose_attribute(local_name=u"major_release", remote_name=u"majorRelease", attribute_type=int)
        self.expose_attribute(local_name=u"minor_release", remote_name=u"minorRelease", attribute_type=int)
        self.expose_attribute(local_name=u"phone", remote_name=u"phone", attribute_type=int)
        self.expose_attribute(local_name=u"product_version", remote_name=u"productVersion", attribute_type=int)
        self.expose_attribute(local_name=u"provider", remote_name=u"provider", attribute_type=int)
        self.expose_attribute(local_name=u"state", remote_name=u"state", attribute_type=int)
        self.expose_attribute(local_name=u"street", remote_name=u"street", attribute_type=int)
        self.expose_attribute(local_name=u"user_name", remote_name=u"userName", attribute_type=int)
        self.expose_attribute(local_name=u"zip", remote_name=u"zip", attribute_type=int)
        
        # Fetchers
        self.event_logs = []
        self.event_logs_fetcher = NUEventLogsFetcher.fetcher_with_object(nurest_object=self, local_name=u"event_logs")
        for key, value in kwargs.iteritems():
            if hasattr(self, key):
                setattr(self, key, value)



    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"license"


