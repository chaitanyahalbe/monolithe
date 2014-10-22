# -*- coding: utf-8 -*-

from bambou import NURESTFetcher


class NUVirtualMachinesFetcher(NURESTFetcher):
    """ VirtualMachine fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUVirtualMachine
        return NUVirtualMachine