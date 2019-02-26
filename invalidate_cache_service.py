
from qgis.server import (QgsConfigCache, QgsService)
from qgis.core import QgsMessageLog


class InvalidateCacheServiceService(QgsService):

    def __init__(self):
        QgsService.__init__(self)

    def name(self):
        return "INVALIDATECACHE"

    def version(self):
        return "0.0.1"

    def allowMethod(method):
        return True

    def executeRequest(self, request, response, project):
        QgsMessageLog.logMessage('Custom service executeRequest')
        QgsConfigCache.instance().removeEntry(project.absoluteFilePath())
        response.setStatusCode(200)
        response.write("Cache cleared for %s" % (project.absoluteFilePath()))


class InvalidateCacheService():

    def __init__(self, serverIface):
        self.serv = InvalidateCacheServiceService()
        serverIface.serviceRegistry().registerService(
            InvalidateCacheServiceService())
