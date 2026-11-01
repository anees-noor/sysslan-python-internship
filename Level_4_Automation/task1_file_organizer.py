import os
import shutil

folder = input("Enter folder path to organize: ")

for filename in os.listdir(folder):

    file_path = os.path.join(folder, filename)

    if os.path.isfile(file_path):

        extension = filename.split(".")[-1].lower()

        if extension in ["jpg", "png", "jpeg"]:
            folder_name = "Images"

        elif extension in ["pdf", "docx", "txt"]:
            folder_name = "Documents"

        elif extension in ["mp3", "wav"]:
            folder_name = "Audio"

        elif extension in ["mp4", "mkv"]:
            folder_name = "Videos"

        else:
            folder_name = "Others"

        destination = os.path.join(folder, folder_name)

        os.makedirs(destination, exist_ok=True)

        shutil.move(
            file_path,
            os.path.join(destination, filename)
        )

print("Files organized successfully!")