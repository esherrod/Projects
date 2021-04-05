import os
import shutil
from hurry.filesize import size

from os.path import expanduser
home = expanduser("~/Desktop")
os.chdir(home)

from datetime import datetime
now = datetime.now()

date = now.strftime("%d.%m.%Y")

backup_folder = home + "/" + date
os.mkdir(backup_folder)