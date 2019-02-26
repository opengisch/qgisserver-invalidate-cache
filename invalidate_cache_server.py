# -*- coding: utf-8 -*-
"""
/***************************************************************************
    QGIS Server Plugin Filters: Add a new request to invalidate QGIS server
    cache of a project
    ---------------------
    Date                 : February 2019
    Copyright            : (C) 2019 by Marco Bernasocchi - OPENGIS.ch
    Email                : marco at opengis.ch
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

__author__ = 'Marco Bernasocchi'
__date__ = 'February 2019'
__copyright__ = '(C) 2019, Marco Bernasocchi - OPENGIS.ch'

from qgis.core import QgsMessageLog, QgsLogger


class InvalidateCacheServer:
    """Plugin for QGIS server
    this plugin loads invalidatecache filter"""

    def __init__(self, serverIface):
        # Save reference to the QGIS server interface
        self.serverIface = serverIface
        QgsMessageLog.logMessage("SUCCESS - invalidatecache init",
                                 'plugin',
                                 QgsMessageLog.INFO)

        from .invalidate_cache_filter import InvalidateCacheFilter
        try:
            serverIface.registerFilter(InvalidateCacheFilter(serverIface), 50)
        except Exception as e:
            QgsLogger.debug("invalidatecache - Error loading filter: %s" % e )
