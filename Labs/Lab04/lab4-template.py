import arcpy
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

### >>>>>> Add your code here
INPUT_DB_PATH = 
CSV_PATH = 
OUTPUT_DB_PATH = 
### <<<<<< End of your code here

arcpy.env.workspace = INPUT_DB_PATH

# create GDB management
if not os.path.exists(OUTPUT_DB_PATH):
    ### >>>>>> Add your code here
    
    ### <<<<<< End of your code here

# Load .csv file to input GDB
### >>>>>> Add your code here
    
### <<<<<< End of your code here

radiumStr = "150 meter"

# Buffer analysis
### >>>>>> Add your code here
    
### <<<<<< End of your code here

# Intersect analysis
### >>>>>> Add your code here
    
### <<<<<< End of your code here

# Output features to the created GDB
### >>>>>> Add your code here
    
### <<<<<< End of your code here
