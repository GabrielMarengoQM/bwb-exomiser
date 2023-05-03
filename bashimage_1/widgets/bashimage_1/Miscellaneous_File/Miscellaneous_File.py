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

class OWMiscellaneous_File(OWBwBWidget):
    name = "Miscellaneous_File"
    description = "Enter and output a file"
    priority = 10
    icon = getIconName(__file__,"exomiser.png")
    want_main_area = False
    docker_image_name = "exomiser/exomiser-cli"
    docker_image_tag = "13.2.0"
    pset=functools.partial(settings.Setting,schema_only=True)
    runMode=pset(0)
    exportGraphics=pset(False)
    runTriggers=pset([])
    triggerReady=pset({})
    inputConnectionsStore=pset({})
    optionsChecked=pset({})
    exodata=pset("/data/exomiser-cli-13-1-0/exomiser-data")
    exoconfig=pset("/data/exomiser-cli-13.2.0/examples")
    exoresults=pset(None)
    def __init__(self):
        super().__init__(self.docker_image_name, self.docker_image_tag)
        with open(getJsonName(__file__,"Miscellaneous_File")) as f:
            self.data=jsonpickle.decode(f.read())
            f.close()
        self.initVolumes()
        self.inputConnections = ConnectionDict(self.inputConnectionsStore)
        self.drawGUI()
