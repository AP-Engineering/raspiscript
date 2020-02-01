#!/usr/bin/env python

####################################
### NZBGET POST-PROCESSING SCRIPT


# this is my first script
# ensure that only the temporary folders in the copy directory are deleted: meaning that only delete the
#  folders that start with the day, and not the folders that are the names of TV shows

# Written to move newly downloaded video files to a folder of todays date

# -----------------------------------------------------------------------
# ------- Main Program --------------------------------------------------

# ----- Declare Variables -----------------------------------------------
# Adjust the variables in this section only
import time, os, shutil, fnmatch, subprocess
from subprocess import Popen, PIPE

DeleteAfterDays = 30 # after this many days the old files will be deleted on the external USB drive
MainVideoCopyTo = "/disks/USBMedia/shares/TV"
MainVideoCopyFrom ="/disks/USBMedia/shares/SABNzbd/completed"
video1 = ".mkv" #video file extensions
video2 = ".avi" #video files extensions
video3 = ".mp4" #video files extensions
rar1 = ".rar" #zip file extensions
rar2 = ".z01" # zip file extensions
rar3 = ".x01" #zip file extensions
rar4 = ".rar" #zip file extension
count = 1 #count of unrar files to determine if the all unsucceful
# The below DelFolders are the ones that will be deleted from the copy destination after DeleteAferDays
#  is up, All other folders will be ignored. The folders to delete will START with the values listed. Tied
#  to the format of the today folder.
DelSt1 = "0"
DelSt2 = "1"
DelSt3 = "3"
# ----- END Declare Variables -------------------------------------------
### NZBGET POST-PROCESSING SCRIPT ###


# create a folder with todays date on the external USB if it does not already exist
today = time.strftime("%d_%m_%Y")# formating for new folder
NewFolderToday = MainVideoCopyTo+"/"+today # new folder location
if not os.path.exists(NewFolderToday):
    os.makedirs(NewFolderToday)

# find the video files before moving them
MVC = os.listdir(MainVideoCopyFrom)#list all files and directories in the main folder
unrarDir = [] #initialize array of directory to be unrared
unrarFile = [] # intialize array for file to unrar
newpath = [] #intialize array for the multiple directory structure
c = 0 #ensure that we start with no multiple directories
for a in range(0,len(MVC)): #cycle through all directories
    path = MainVideoCopyFrom+"/"+MVC[a]
    delpath = path
    for root,dirs,files in os.walk(path):
        b = 0 # used for checking to see if dir has been added to extracted folder
        # used for multiple folders inside directories when extracted
        if len(dirs) > 0:
            #directories inside of directories, deal with this
            for b in range(0,len(dirs)):
                newpath = MVC[a]+"_"+dirs[b]
                c = 1
        for file in files:
            #if there is no video file, but there is a rar file, extract the video, move it then delet the rar files
            if file.endswith(video1) or file.endswith(video2) or file.endswith(video3):
                print(" File: %s " % file)
                print("path: %s " %path)
                print("B: %s " %b)
                print("mvc[b]: %s " %MVC[b]) # BUG: changes to display correct directory 013120 NZBGET
                #delete sample files that are smaller than 100MB
                if b == 0:
                    if os.path.getsize(root+"/"+file) < 100000000:
                        print("too small delete")
                        os.remove(root+"/"+file)
                        b = -1
                if b >= 1:
                    if os.path.getsize(newpath+"/"+file) < 100000000:
                        print("too small inside loop, delete sample file")
                        os.remove(newpath+"/"+file)
                        b = -1
                #shutil.move(root+"/"+file,NewFolderToday+"/"+MVC[a]+".mkv")
                #shutil.rmtree(path)
                b = 1+b
                print(" more b: %s" %b)
                print(" more c: %s" %c)
                if b >= 1:
                    if c == 1:
                        #the integer
                        shutil.move(root+"/"+file,NewFolderToday+"/"+newpath+str(b)+".mkv")
                    else:
                        shutil.move(root+"/"+file,NewFolderToday+"/"+MVC[a]+str(b)+".mkv")
                        shutil.rmtree(path)

            else:
                if b != 1 and (file.endswith(rar1) or file.endswith(rar2) or file.endswith(rar3) or file.endswith(rar4)):
                    unrarDir.append(root)
                    unrarFile.append(file)#record file to unrar
                    #print("move the file: %s" %file)
        if b >= 1:
            print("path after move outside for loop is: %s" %delpath)

            #shutil.rmtree(delpath)
#unrar files that did not already extract(through sabnzbd program) and then move them to the correct folder
process = 100; #value to determine not run through yet
for a in range(0,len(unrarDir)):#join the path and filename to be extracted together and extract
    if process == 0:
        break; #break out of the loop as extraction was sucessfull
    extract = unrarDir[a]+"/"+unrarFile[a]
    cmdSt = "%s" %extract
    os.chdir(unrarDir[a])# change to the folder that where the extraction will take place
    test = subprocess.call(['unrar','t', cmdSt],stdout=PIPE, stderr=PIPE)#test to make sure that we have the right rar file
    if test == 0:
        process = subprocess.call(['unrar','e', cmdSt],stdout=PIPE, stderr=PIPE) #test was successful, extract the file
        if process != 0 and process !=100:#100 is initialization of the variable
            #create a file with extension .mkv and move it into the todayfolder to inform user extraction did not work
            fileToExtract = "Manually extract file in dir: "+unrarDir[a]
            f = open(fileToExtract, "w+")#create file in the NewFolderToday folder
            f.close()
            print("needs a manual extraction and deletion, dir: %s" %unrarDir[a])
        else:
            print("successful extration, remove the directory: %s" %unrarDir[a])
            #shutil.rmtree(unrarDir[a])
            # move the mkv file and rename it
            for root,dirs,files in os.walk(path):
                for file in files:
                    if file.endswith(video1) or file.endswith(video2) or file.endswith(video3):
                        #if os.path.getsize(file) >
                        shutil.move(root+"/"+file,NewFolderToday+"/"+str(MVC)+".mkv")
                        break
            print("del after break and file move")
            os.chdir(MainVideoCopyFrom) #change to the main folder
            shutil.rmtree(path) #after the mkv file move del the folfer
            a = len(unrarDir)#go to the last place in the loop and stop iteratrions
            break #end main for loop, file has been extracted
    else:
        print("test on file: %s/%s unsuccessful" %(unrarDir[a],unrarFile[a]))
        # Delete the folders after move or unextraction was unsuccessful
           #remove the path now that the video files have been copied
        count = count + 1; #count the amount times through this lop
        #print( "count: %s" %count)
        if (count == len(files)): #all unrar failed, delete dir
            print( "No working rar files deleting dir: %s " %unrarDir[a])
            shutil.rmtree(unrarDir[a])
        #print("delete directory: %s" %delpath)
# Delete the folders and remaining files from the Source folder
# Folders and subfolders are created when a file is copied, therefore delete its contents after set time
DeleteHalfDaysSeconds = 60*60*24*5
DelSource = time.time() - DeleteHalfDaysSeconds#time in seconds
MVC = os.listdir(MainVideoCopyFrom)#check again, as some dirs may have been deleted
for a in range(0,len(MVC)):
    path = MainVideoCopyFrom+"/"+MVC[a] #path of source directories
    st = os.stat(path)
    mtime = st.st_mtime
    if mtime < DelSource:
        print('remove %s' % MVC[a])
        shutil.rmtree(path)

# Delete any folders that are older than X-days defined in the variables section
DeleteDestSeconds = 60*60*24*DeleteAfterDays
DelDestination = time.time() - DeleteDestSeconds #time in seconds
MVCT = os.listdir(MainVideoCopyTo) #path to where the videos are copied too
for a in range(0,len(MVCT)):
    path = MainVideoCopyTo+"/"+MVCT[a] #path of destination directories, all files created on that day are put in the daily directory
    st = os.stat(path)
    mtime = st.st_mtime
    if mtime < DelDestination:
        print('remove destination dir %s' % MVCT[a])
        shutil.rmtree(path)
# ----- END Main Program ------------------------------------------------

##########################################################################
# nzbget exit code
exit /b 93
