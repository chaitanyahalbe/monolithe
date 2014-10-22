# -*- coding: utf-8 -*-

from bambou import NURESTFetcher


class NUInfrastructurePortProfilesFetcher(NURESTFetcher):
    """ InfrastructurePortProfile fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUInfrastructurePortProfile
        return NUInfrastructurePortProfile