import os
import glob
import sys
import functools
import jsonpickle
from collections import OrderedDict
from Orange.widgets import widget, gui, settings
import Orange.data
from Orange.data.io import FileFormat
from DockerClient import DockerClient
from BwBase import OWBwBWidget, ConnectionDict, BwbGuiElements, getIconName, getJsonName
from PyQt5 import QtWidgets, QtGui

class OWFile(OWBwBWidget):
    name = "File"
    description = "exomiser distroless"
    priority = 1
    icon = getIconName(__file__,"file.png")
    want_main_area = False
    docker_image_name = "carlokroll/exomiser-cli"
    docker_image_tag = "NEW-distroless-13.2.0"
    outputs = [("results",str)]
    pset=functools.partial(settings.Setting,schema_only=True)
    runMode=pset(0)
    exportGraphics=pset(False)
    runTriggers=pset([])
    triggerReady=pset({})
    inputConnectionsStore=pset({})
    optionsChecked=pset({})
    analysis=pset("/data/ExomiserDocker/exomiser-cli-13.2.0/test-analysis-exome.yml")
    springconfig=pset("/data/ExomiserDocker/exomiser-cli-13.2.0/application.properties")
    results=pset(None)
    exodata=pset("/data/exomiser-cli-13-1-0/exomiser-data/")
    pvcf=pset("/data/ExomiserDocker/exomiser-cli-13.2.0/Pfeiffer.vcf")
    def __init__(self):
        super().__init__(self.docker_image_name, self.docker_image_tag)
        with open(getJsonName(__file__,"File")) as f:
            self.data=jsonpickle.decode(f.read())
            f.close()
        self.initVolumes()
        self.inputConnections = ConnectionDict(self.inputConnectionsStore)
        self.drawGUI()
    def handleOutputs(self):
        outputValue="/data/ExomiserDocker/exomiser-cli-13.2.0/results/"
        if hasattr(self,"results"):
            outputValue=getattr(self,"results")
        self.send("results", outputValue)
