import os
import shutil

### Creates new folders for each file in a directory and moves them into the folder

def create_folders_for_files(source_directory, target_directory):
    # Ensure the source and target directories exist
    if not os.path.exists(source_directory):
        print(f"The source directory {source_directory} does not exist.")
        return
    
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)
        print(f"Created target directory: {target_directory}")
    
    # Loop through all files in the source directory
    for filename in os.listdir(source_directory):
        file_path = os.path.join(source_directory, filename)
        
        # Check if the current path is a file
        if os.path.isfile(file_path):
            # Extract the file name without the extension
            folder_name = os.path.splitext(filename)[0]
            folder_path = os.path.join(target_directory, folder_name)
            
            # Create the new folder in the target directory
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
                print(f"Created folder: {folder_path}")
            else:
                print(f"Folder already exists: {folder_path}")
            
            # Optionally, move or copy the file into the new folder
            shutil.move(file_path, os.path.join(folder_path, filename))
            print(f"Moved file {filename} to folder {folder_name}")

### Usage
# source_directory =        # Directory where all the file are located
# target_directory =        # Directory where all the folders will be created
# create_folders_for_files(source_directory, target_directory)
