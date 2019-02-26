from qgis.server import (QgsConfigCache, QgsService)
from qgis.core import QgsMessageLog, Qgis


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

        QgsMessageLog.logMessage('INVALIDATECACHE service executeRequest',
                                 'Server', Qgis.Info)
        map = request.parameters()['MAP']
        QgsConfigCache.instance().removeEntry(map)
        msg = "Cache cleared for %s" % (map)
        QgsMessageLog.logMessage(msg,'Server', Qgis.Info)
        response.setStatusCode(200)
        response.write('success - cache cleared')


class InvalidateCacheService():

    def __init__(self, serverIface):
        self.serv = InvalidateCacheServiceService()
        serverIface.serviceRegistry().registerService(
            InvalidateCacheServiceService())
