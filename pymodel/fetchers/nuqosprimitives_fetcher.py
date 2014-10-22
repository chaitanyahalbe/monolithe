# -*- coding: utf-8 -*-

from bambou import NURESTFetcher


class NUQosPrimitivesFetcher(NURESTFetcher):
    """ QosPrimitive fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUQosPrimitive
        return NUQosPrimitive