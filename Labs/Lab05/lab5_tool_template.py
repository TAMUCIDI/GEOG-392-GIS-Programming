import arcpy
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

"""
You can change the `workspace` path as your wish.
"""
arcpy.env.workspace = BASE_DIR

"""
Here are some hints of what values the following variables should accept.
When running, the following code section will accept user input from terminal
Use `input()` method.

GDB_Folder = "***/Labs/Lab5"
GDB_Name = "Lab5.gdb"
Garage_CSV_File = "***/Labs/Lab5/garages.csv"
Garage_Layer_Name = "garages"
Campus_GDB = "***/Labs/Lab5/Campus.gdb"
Selected_Garage_Name = "Northside Parking Garage"
Buffer_Radius = "150 meter"
"""
### >>>>>> Add your code here
print("Please input the following parameters:\n")
GDB_Folder = 
GDB_Name = 
Garage_CSV_File = 
Garage_Layer_Name = 
Campus_GDB = 
Selected_Garage_Name = 
Buffer_Radius = 
### <<<<<< End of your code here

"""
In this section, you can re-use your codes from Lab4.

"""
### >>>>>> Add your code here
#create gdb
arcpy.management.CreateFileGDB(***)
GDB_Full_Path = 

#import garage csv
garages = arcpy.management.MakeXYEventLayer(***)
arcpy.FeatureClassToGeodatabase_conversion(***)
### <<<<<< End of your code here

"""
Create a searchCursor.
Select the garage with `where` or `SQL` clause using `arcpy.analysis.Select` method.
Apply `Buffer` and `Clip` analysis on the selected feature.
Use `arcpy.analysis.Buffer()` and `arcpy.analysis.Clip()`.
"""
### >>>>>> Add your code here
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
### <<<<<< End of your code here