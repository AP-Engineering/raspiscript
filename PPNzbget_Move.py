#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
###########################################################################
### NZBGET POST-PROCESSING SCRIPT
### ABOUT
# used to move files to the correct location, delete files after x days to
# save on storage space.

### OPTIONS
# Enable debugging mode (yes, no).
#
# Logging will be much more verbose, but if you are experiencing issues,
# developers and support staff will only be able to help you much easier
# if they have this extra bit of detail in your logging output
#Debug=yes

#NZBOP_UNPACK


### NZBGET POST-PROCESSING SCRIPT
###########################################################################

# variable declaration ---------------------------------------#
# END variable declaration -----------------------------------#

if $NZBOP_UNPACK != "no":
	print("[ERROR] Please enable option \"Unpack\" in nzbget configuration file")
