import os
import shutil
from datetime import datetime

source_folder = input("Enter folder path to backup: ")

if os.path.exists(source_folder):

    backup_name = "Backup_" + datetime.now().strftime("%Y%m%d_%H%M%S")

    backup_folder = os.path.join(
        os.path.dirname(source_folder),
        backup_name
    )

    shutil.copytree(source_folder, backup_folder)

    print("Backup created successfully!")
    print("Backup location:", backup_folder)

else:
    print("Source folder does not exist.")