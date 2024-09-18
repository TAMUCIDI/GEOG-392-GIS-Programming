import arcpy
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

### >>>>>> Add your code here
INPUT_DB_PATH = 
CSV_PATH = 
OUTPUT_DB_PATH = 
### <<<<<< End of your code here

arcpy.env.workspace = INPUT_DB_PATH

# Layers need to be kept
layers_to_keep = ["GaragePoints", "LandUse", "Structures", "Trees"]

# list all feature clases
feature_classes = arcpy.ListFeatureClasses()

# delete other classes
for fc in feature_classes:
    if fc not in layers_to_keep:
        arcpy.management.Delete(fc)

# create GDB management
if not os.path.exists(OUTPUT_DB_PATH):
    ### >>>>>> Add your code here
    
    ### <<<<<< End of your code here

# Load .csv file to input GDB
### >>>>>> Add your code here
    
### <<<<<< End of your code here

# Print spatial references before re-projection
print(f"Before Re-Projection...")
print(f"garages layer spatial reference: {arcpy.Describe('XXX').spatialReference.name}.")
print(f"Structures layer spatial reference: {arcpy.Describe('XXX').spatialReference.name}.")

# Re-project
## >>>>>>>>> change the codes below
target_ref = arcpy.SpatialReference("***")
arcpy.management.Project(
   "******",
   "******",
   target_ref
)
## <<<<<<<< End of your code here
# print spatial references after re-projection
print(f"After Re-Projection...")
print(f"garages layer spatial reference: {arcpy.Describe('XXX').spatialReference.name}.")
print(f"re-projected Structures layer spatial reference: {arcpy.Describe('XXX').spatialReference.name}")

### >>>>>> Add your code here
# Buffer analysis
radiumStr = "150 meter"

# Intersect analysis

# Output features to the created GDB
    
### <<<<<< End of your code here
