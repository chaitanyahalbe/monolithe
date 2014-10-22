# -*- coding: utf-8 -*-

from bambou import NURESTFetcher


class NUIngressAdvancedForwardingEntriesFetcher(NURESTFetcher):
    """ IngressAdvancedForwardingEntry fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUIngressAdvancedForwardingEntry
        return NUIngressAdvancedForwardingEntry