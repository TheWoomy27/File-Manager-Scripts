import os

def create_subfolders(directory, subfolder_names):
    # Ensure the given directory exists
    if not os.path.exists(directory):
        print(f"The directory {directory} does not exist.")
        return
    
    # Loop through all items in the directory
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        
        # Check if the current path is a folder
        if os.path.isdir(item_path):
            # Create subfolders inside the current folder
            for subfolder_name in subfolder_names:
                subfolder_path = os.path.join(item_path, subfolder_name)
                
                if not os.path.exists(subfolder_path):
                    os.makedirs(subfolder_path)
                    print(f"Created subfolder: {subfolder_path}")
                else:
                    print(f"Subfolder already exists: {subfolder_path}")

### Usage
# directory =                   # Directory where folders are
# subfolder_names = ["", ""]    # New subfolders to create
# create_subfolders(directory, subfolder_names)
