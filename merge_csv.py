#-------------------------------------------------------------------------------
# Name:        Merge CSV
# Purpose:     To Merge multiple csv files to form one Excel workbook (.xlsx file) with 
#              each CSV files as wooksheets
#
# Author:      Kevin O. Oluoch
#
# Created:     21/05/2018
# Copyright:   @Kevinzekyongare 2018
# Licence:     N/A
#
# Python: Python 2.7.x
#-------------------------------------------------------------------------------

'''
  NB
    enter the path to the directory with csv files and the path to the output directory( should be diffrent) before running

'''
import os
import glob
import csv
from xlsxwriter.workbook import Workbook

# The link to the new Xlsx file and csv directory
wb_path ='./Kevinzekyongare.xlsx' # REPLACE

# The link to the new Xlsx file and csv directory
csv_dir _path ='./Kevinzekyongare' # REPLACE

workbook = Workbook(wb_path)

#
for csvfile in glob.glob(os.path.join(csv_dir_path, '*.csv')):
    print os.path.basename(csvfile)
    worksheet = workbook.add_worksheet(os.path.splitext(os.path.basename(csvfile))[0]) #worksheet name equals csv file name
    with open(csvfile, 'rb') as f:
        print "current csv: " ,
        print csvfile
        reader = csv.reader(f)
        for r, row in enumerate(reader):
            print "row: {} columns".format(r)
            for c, col in enumerate(row):
                print "col: {}".format(c),
                print col,
                worksheet.write(r, c, col) #write the csv file content into it
            print
    print
    print "##################################"
workbook.close()
