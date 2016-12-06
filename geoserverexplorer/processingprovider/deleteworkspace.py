# -*- coding: utf-8 -*-
#
# (c) 2016 Boundless, http://boundlessgeo.com
# This code is licensed under the GPL 2.0 license.
#
from processing.core.parameters import ParameterString
from geoserverexplorer.processingprovider.geoserveralgorithm import GeoServerAlgorithm


class DeleteWorkspace(GeoServerAlgorithm):

    WORKSPACE = 'WORKSPACE'

    def processAlgorithm(self, progress):
        self.createCatalog()
        workspaceName = self.getParameterValue(self.WORKSPACE)
        ws = self.catalog.get_workspace(workspaceName)
        self.catalog.delete(ws)

    def defineCharacteristics(self):
        self.addBaseParameters()
        self.name = 'Delete workspace'
        self.group = 'GeoServer tools'
        self.addParameter(ParameterString(self.WORKSPACE, 'Workspace'))
