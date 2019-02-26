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

 This script initializes the plugin, making it known to QGIS and QGIS Server.
"""


def serverClassFactory(serverIface):  # pylint: disable=invalid-name
    """Load InvalidateCacheServer class from file invalidate_cache_server.

    :param iface: A QGIS Server interface instance.
    :type iface: QgsServerInterface
    """
    #
    from .invalidate_cache_service import InvalidateCacheService
    return InvalidateCacheService(serverIface)
