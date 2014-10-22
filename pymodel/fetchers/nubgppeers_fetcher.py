# -*- coding: utf-8 -*-

from bambou import NURESTFetcher


class NUBGPPeersFetcher(NURESTFetcher):
    """ BGPPeer fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUBGPPeer
        return NUBGPPeer