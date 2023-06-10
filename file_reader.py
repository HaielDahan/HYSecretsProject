import os

def file_read(path):
    with open(path, "r") as file:
        file_contents = file.read()
    return file_contents

def remove_files_in_folder(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)
            #print(f"Removed file: {file_path}")