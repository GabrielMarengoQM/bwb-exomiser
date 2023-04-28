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

class OWMiscellaneous_File_1(OWBwBWidget):
    name = "Miscellaneous_File_1"
    description = "Enter and output a file"
    priority = 10
    icon = getIconName(__file__,"file.png")
    want_main_area = False
    docker_image_name = "gabrielmarengoqm/bashimages"
    docker_image_tag = "exomiser_files_edit"
    pset=functools.partial(settings.Setting,schema_only=True)
    runMode=pset(0)
    exportGraphics=pset(False)
    runTriggers=pset([])
    triggerReady=pset({})
    inputConnectionsStore=pset({})
    optionsChecked=pset({})
    datadir=pset("/exomiser-data")
    assemblytype=pset(None)
    assemblydataver=pset(None)
    phenotypedataver=pset(None)
    apdir=pset("application.properties")
    mapping=pset("/data/bashimage2")
    def __init__(self):
        super().__init__(self.docker_image_name, self.docker_image_tag)
        with open(getJsonName(__file__,"Miscellaneous_File_1")) as f:
            self.data=jsonpickle.decode(f.read())
            f.close()
        self.initVolumes()
        self.inputConnections = ConnectionDict(self.inputConnectionsStore)
        self.drawGUI()
