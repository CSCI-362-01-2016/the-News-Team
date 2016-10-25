#!/usr/bin/env python
from project.youtube_dl import utils
print(utils.sanitize_filename("this is a file name       to sanitize?}{[]\|#'$'",True,False))
