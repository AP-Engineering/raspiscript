#!/usr/bin/env python3

# Written to delete the contents of a specific directory; addressing an issue with
#      8Move_video script (original issue in '8' script needs to be addressed
# written by Cliff Laver, P.Eng on Nov 1, 2020

####################################
### NZBGET POST-PROCESSING SCRIPT

# Import library's for cmds
import os
import shutil
import sys
 

#Variables for program
DelFolderP = "/disks/USBMedia/shares/SABNzbd/completed" #delete folder path
ParentDir = "/disks/USBMedia/shares/SABNzbd" #parent directory of one to be deleted
DelFolder = "completed" #folder to be deleted and recreated

#change current working folder to the one to check
os.chdir(DelFolderP)

#if DelFolder is not empty, change to parent dir
# then delete the DelFolder; after deletion recreate it

if os.listdir() != []: # checks if DelFolder is empty
    os.chdir(ParentDir) # change to the parent directory
    shutil.rmtree(DelFolder) #Delete the contents of the DelFolder
    os.mkdir(DelFolder) #recreate the folder

##########################################################################
# nzbget exit code
sys.exit(93)    

    
