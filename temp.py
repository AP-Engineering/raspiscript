#!/usr/bin/env python
#
# Logger post-processing script for NZBGet
#
# Copyright (C) 2013-2016 Andrey Prygunkov <hugbug@users.sourceforge.net>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#


##############################################################################
### NZBGET POST-PROCESSING SCRIPT                                          ###

# Save nzb log into a file.
#
# This script saves the download and post-processing log of nzb-file
# into file _nzblog.txt in the destination directory.
#
# NOTE: This script requires Python to be installed on your system.

### NZBGET POST-PROCESSING SCRIPT                                          ###
##############################################################################


import os
import sys
import datetime

try:
	from xmlrpclib import ServerProxy # python 2
	from urllib2 import quote
except ImportError:
	from xmlrpc.client import ServerProxy # python 3
	from urllib.parse import quote

# Exit codes used by NZBGet
POSTPROCESS_SUCCESS=93
POSTPROCESS_NONE=95
POSTPROCESS_ERROR=94

# Check if the script is called from nzbget 15.0 or later
if not 'NZBOP_NZBLOG' in os.environ:
	print('*** NZBGet post-processing script ***')
	print('This script is supposed to be called from nzbget (15.0 or later).')
	sys.exit(POSTPROCESS_ERROR)
if 'NZBOP_NZBLOG' in os.environ:
	print('************* NZB success *************')
	sys.exit(POSTPROCESS_SUCCESS)
