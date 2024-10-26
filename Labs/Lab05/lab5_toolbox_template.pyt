# -*- coding: utf-8 -*-

import arcpy
import os

class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Lab5_Toolbox"
        self.alias = "Lab5_Toolbox"

        # List of tool classes associated with this toolbox
        self.tools = [Lab5_Tool]


class Lab5_Tool(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Lab5_Tool"
        self.description = ""
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        param_GDB_folder = arcpy.Parameter(
            displayName="GDB Folder",
            name="gdbfolder",
            datatype="GPString",
            parameterType="Required",
            direction="Input"
        )
        param_GDB_Name = arcpy.Parameter(
            displayName="GDB Name",
            name="gdbname",
            datatype="GPString",
            parameterType="Required",
            direction="Input"
        )
        ...
        params = [
            param_GDB_folder, 
            param_GDB_Name, 
            ...
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
        #query user input
        GDB_Folder = parameters[0].valueAsText
        GDB_Name = parameters[1].valueAsText
        Garage_CSV_File = 
        Garage_Layer_Name = 
        Campus_GDB = 
        Selected_Garage_Name = 
        Buffer_Radius =

        print("User Input:")
        print("GDBFolder:" + GDB_Folder)
        print("GDB_Name: " + GDB_Name)
        print("Garage_CSV_File" + Garage_CSV_File)
        print("Garage_layer_Name: " + Garage_Layer_Name)
        print("Campus_GDB: " + Campus_GDB)
        print("Selected_Garage_Name: " + Selected_Garage_Name)
        print("Buffer_Radius: " + Buffer_Radius)

        #create gdb
        arcpy.management.CreateFileGDB(***)
        GDB_Full_Path = 

        #import garage csv
        garages = arcpy.management.MakeXYEventLayer(***)
        arcpy.FeatureClassToGeodatabase_conversion(***)

        #search surcor
        structures = Campus_GDB + "/Structures"
        where_clause = "BldgName = '%s'" % Selected_Garage_Name
        cursor = arcpy.da.SearchCursor(***)

        shouldProceed = False

        for row in cursor:
            if row.getValue("BldgName") == Selected_Garage_Name:
                shouldProceed = True

        if shouldProceed == True:
            #select garage as feature layer
            selected_garage_layer_name = ***
            garage_feature = arcpy.analysis.Select(***)

            # Buffer the selected building
            garage_buff_name = "/building_buffed"
            arcpy.analysis.Buffer(***)

            #clip
            arcpy.analysis.Clip(***)
            print("success")
        else:
            print("error")

        return
