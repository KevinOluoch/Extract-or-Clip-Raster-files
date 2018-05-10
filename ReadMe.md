
# Extract by Mask

A python script to clip multiple raster files to extends defined by feature classes (vector files). The program makes use of  **arcpy** module that is available in python 2 installed as part of  **ArcGIS**

## Program workflow

```mermaid
graph LR
A[Raster Files ]  --  Iterate  --> C{Extract}
B[Feature Classes] -- Iterate --> C
C --> D((Convert to .flt))
D --> E[Clipped Raster Files]
``` 
##### NB 
###### Change the input paths before running the program
