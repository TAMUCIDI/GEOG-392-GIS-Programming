# -*- coding: utf-8 -*-

import arcpy
import os
import time

class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Lab6_Toolbox"
        self.alias = "Lab6_Toolbox"

        # List of tool classes associated with this toolbox
        self.tools = [Lab6_Tool]


class Lab6_Tool(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Lab6_Tool"
        self.description = ""
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        param_proj_path = arcpy.Parameter(
            ***
        )
        param_layer_name = arcpy.Parameter(
            ***
        )
        # other optional parameters

        params = [
            param_proj_path, 
            param_layer_name, 
            '''
            If you have other optional parameters, put them here.
            '''
            ]
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        
        # setup the progressor
        # 3s should be enough for you to take screenshots for submission
        readTime = 3
        start = 0
        max = 100
        step = 25
        # >>>>>>>>>>
        arcpy.SetProgressor(***)
        # <<<<<<<<<<
        # Add message to the results pane
        arcpy.AddMessage("Init tool...")

        # Accept user input from toolbox interface
        aprxFilePath = parameters[0]
        layerName = ***
        # other params are oprional
        outputPath = ***

        # fetch the project
        project = arcpy.mp.ArcGISProject(aprxFilePath)
        """
            Fetch the list of layers
            the data structure is:
            project 
            >   map list(name is 'Map')
                >    map (id is 0)
                     >    layer list
        """
        layers = project.listMaps('Map')[0].listLayers()
        
        for layer in layers:
            if layer.isFeatureLayer:
                symbology = layer.symbology
                # Advance the progressor here
                arcpy.SetProgressorPosition(***)
                arcpy.SetProgressorLabel(***)
                arcpy.AddMessage("Finding the layers...")
                time.sleep(readTime)
                # End of advancing progessor
                if hasattr(symbology, 'renderer') and layer.name == 'Structures':
                    # re-render the 'structures' layer into 'UniqueValueRenderer'
                    # >>>>>>>>>>

                    # <<<<<<<<<<
                    # Advance the progressor here
                    arcpy.SetProgressorPosition(***)
                    arcpy.SetProgressorLabel(***)
                    arcpy.AddMessage("Re-rendering...")
                    time.sleep(readTime)
                elif hasattr(symbology, 'renderer') and layer.name == 'trees':
                    # re-render the 'trees' layer into 'GraduateColorsRenderer'
                    # >>>>>>>>>>

                    # <<<<<<<<<<
                    # Advance the progressor here
                    arcpy.SetProgressorPosition(***)
                    arcpy.SetProgressorLabel(***)
                    arcpy.AddMessage("Re-rendering...")
                    time.sleep(readTime)
                else:
                        # Error message
        
        # Save the updated project into a new copy.
        project.saveACopy(***)
        # Advance the progressor here
        arcpy.SetProgressorPosition(***)
        arcpy.SetProgressorLabel(***)
        arcpy.AddMessage("Saving the project...")
        time.sleep(readTime)

        return
