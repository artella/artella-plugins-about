#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains Artella About plugin implementation
"""

from __future__ import print_function, division, absolute_import

from artella.core import plugin


class AboutPlugin(plugin.ArtellaPlugin, object):

    ID = 'artella-plugins-about'
    INDEX = 6

    def __init__(self, config_dict=None, manager=None):
        super(AboutPlugin, self).__init__(config_dict=config_dict, manager=manager)

    def about(self):
        """
        Shows an about window that shows information about current installed Artella plugin
        """

        print('Showing About Info ...')
