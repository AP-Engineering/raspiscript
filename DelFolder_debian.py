#!/usr/bin/env /usr/bin/python3

# Written to delete the contents of a specific directory; addressing an issue with
#      8Move_video script (original issue in '8' script needs to be addressed
# written by Cliff Laver, P.Eng on Nov 1, 2020
#
# date sept 26, 2021
# issue: script will no longer run in NZBGet on bullseye
# correction: had to update the full path of python3 in the shebang line as a link to python is remove in OS

####################################
### NZBGET POST-PROCESSING SCRIPT

# Import library's for cmds
import os
import shutil
import sys

#Variables for program
DelFolderP = "/media/USBdisk/laver/nzbget/completed" #directory of delfolder
ParentDir = "/media/USBdisk/laver/nzbget" #parent directory of DelFolderP to be deleted
DelFolder = "completed" #folder to be deleted and recreated

#change current working folder to the one to check
#os.chdir(DelFolderP)

#if DelFolder is not empty, change to parent dir
# then delete the DelFolder; after deletion recreate it

if os.listdir(DelFolderP) != []: # checks if DelFolder directory is empty
    os.chdir(ParentDir) # change to the parent directory
    shutil.rmtree(DelFolder) #Delete the contents of the DelFolder
    os.mkdir(DelFolder) #recreate the folder
    sys.exit(93) #nzbget exit code - all is good

##########################################################################
# nzbget exit code
sys.exit(93) # all is good for nzbget
#os._exit(93)
