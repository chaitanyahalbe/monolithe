# -*- coding: utf-8 -*-

from bambou import NURESTFetcher


class NUVMInterfacesFetcher(NURESTFetcher):
    """ VMInterface fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUVMInterface
        return NUVMInterface