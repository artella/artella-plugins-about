#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains Artella About plugin implementation
"""

from __future__ import print_function, division, absolute_import

import artella
from artella.core import plugin, qtutils

if qtutils.QT_AVAILABLE:
    from artella.externals.Qt import QtCore, QtWidgets


class AboutPlugin(plugin.ArtellaPlugin, object):

    ID = 'artella-plugins-about'
    INDEX = 6

    def __init__(self, config_dict=None, manager=None):
        super(AboutPlugin, self).__init__(config_dict=config_dict, manager=manager)

    def about(self):
        """
        Shows an about window that shows information about current installed Artella plugin
        """

        about_dialog = AboutDialog()
        about_dialog.exec_()


class AboutDialog(artella.Dialog, object):
    def __init__(self, parent=None, **kwargs):
        super(AboutDialog, self).__init__(parent, **kwargs)

        self.setWindowTitle('About Artella Plugin')

        self._fill_data()

    def setup_ui(self):
        super(AboutDialog, self).setup_ui()

        artella_frame = QtWidgets.QFrame()
        artella_frame_layout = QtWidgets.QHBoxLayout()
        artella_frame.setLayout(artella_frame_layout)
        artella_frame.setStyleSheet('background: rgb(23, 165, 151)')

        artella_header = QtWidgets.QLabel()
        artella_header_pixmap = artella.ResourcesMgr().pixmap('artella_header')
        artella_header.setPixmap(artella_header_pixmap
                                 )
        artella_frame_layout.addStretch()
        artella_frame_layout.addWidget(artella_header)
        artella_frame_layout.addStretch()

        self._plugins_tree = QtWidgets.QTreeWidget()
        self._plugins_tree.setHeaderLabels(['ID', 'Name', 'Version'])
        self._plugins_tree.setColumnCount(3)
        self._plugins_tree.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        self.main_layout.addWidget(artella_frame)
        self.main_layout.addWidget(self._plugins_tree)

    def _fill_data(self):
        added_packages = dict()

        plugins = artella.PluginsMgr().plugins

        for plugin_id, plugin_data in plugins.items():
            plugin_package = plugin_data.get('package', 'Not Defined')
            package_item = added_packages.get(plugin_package, None)
            if not package_item:
                package_item = QtWidgets.QTreeWidgetItem([plugin_package])
                self._plugins_tree.addTopLevelItem(package_item)
                added_packages[plugin_package] = package_item
            plugin_name = plugin_data['name']
            plugin_item = QtWidgets.QTreeWidgetItem([plugin_id, plugin_name])
            package_item.addChild(plugin_item)

        self._plugins_tree.expandAll()
        self._plugins_tree.resizeColumnToContents(0)
        self._plugins_tree.resizeColumnToContents(1)
        self._plugins_tree.resizeColumnToContents(2)
