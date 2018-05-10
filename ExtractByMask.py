#-------------------------------------------------------------------------------
# Name:        Extract by mask
# Purpose:     To clip multiple raster files using several feature classes and converting the
#              clipped raster into float format
#
# Author:      Kevin O. Oluoch
#
# Created:     07/02/2018
# Copyright:   (c) @Kevinzekyongare 2018
# Licence:     N/A
#-------------------------------------------------------------------------------

import arcpy, arcinfo, os, sys, string, errno
from arcpy import env
from arcpy.sa import *
#################################################
# THE INPUT FILE AND THE OUTPUT PATHS


# Specify the rasters Base Directory
rasterBaseDir = r"" # Add the path to a directory containing raster 
                    # files to be cliped

# Specify the mask (feature class)
masks = []
for rt, dirts, fils in os.walk(r""): # Add path to the directory with 
                                     # feature classes covering the 
                                     # areas to be clipped
    for fil in fils:
        if fil.endswith('.shp'):
            print os.path.join(rt, fil)
            masks.append(os.path.join(rt, fil))
       

# Specify an output directory
outputWorkspace = r"" #Add path to the output directory


#####################################################
# A loop that clips a raster using polygons feature class

# load the Spatial extention
arcpy.CheckOutExtension("spatial")
# make raster base directory the workspace
arcpy.env.workspace = rasterBaseDir

# Loop through input rasters, and clip using the mask files
i = 0
j = 0
for root, dirs, rasters in os.walk(rasterBaseDir):
    for rasterName in rasters:
        if rasterName.endswith(".tif"):
            raster = os.path.join(root, rasterName)
            print "Processing raster file {}".format(raster)
            print
            print
            for mask in masks :
                # Create path to the output raster of masked data
                maskPath, maskName = os.path.split(mask)
                newRasterPath = "{2}\Clipped_{3}\{1}_{0}.flt".format(
                rasterName[:-4], maskName[:3], root, maskName[:-4])

                newRasterPath = newRasterPath.replace(rasterBaseDir,
                outputWorkspace  )

                newRasterPath = newRasterPath.replace( " ", "_")
                print "########################################################"
                print "Masking using {}..... ".format(maskName)

                filePath, baseName = os.path.split(newRasterPath)
                print

               # Create output folder if it does not exist
                try:
                    os.makedirs(filePath)
                except OSError as e:
                    if e.errno != errno.EEXIST:
                        raise

                # Enable overwrite
                arcpy.env.workspace = root
                arcpy.env.overwriteOutput = True
                j += 1

                # Skip raster masking if an output exists
                if os.path.isfile(newRasterPath):
                    print "Skipped {}".format(newRasterPath)
                    continue

                # Create path to temporary files
                Output_rasterPath = r"{}\tempfiles\tf{}".format(rasterBaseDir, i)
                try:
                    os.makedirs(Output_rasterPath)
                except OSError as e:
                    if e.errno != errno.EEXIST:
                        raise
                Output_raster = r"{0}\t{1}".format(Output_rasterPath, j)

                # Process: Extract by Mask
                arcpy.gp.ExtractByMask_sa(raster, mask, Output_raster)

                # Process: Raster to Float
                arcpy.RasterToFloat_conversion(Output_raster, newRasterPath)

                # Delete the temporary files
                arcpy.Delete_management( Output_raster )


                print "Completed Masking {}".format(maskName)
                print "Masked raster exported to {}".format(newRasterPath)
                print
                print
            i += 1
            print "Masked output .flt file count = {}".format(j)
            print "Masked raster file count = {}".format(i)
            print
            print
            print
            print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
            print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
            print



print "THE END"
print " MASKING COMPLETED"

