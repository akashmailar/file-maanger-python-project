import os
import shutil

def manage_folders(folder):
    file_types = {
        'Images' : ['.png', '.jpg', '.jpeg', '.gif'],
        'Documents' : ['.pdf', '.docx', '.xlsx', '.csv'],
        'Music' : ['.mp3'],
        'Videos' : ['.mp4'],
        'Zipfiles' : ['.zip'],
        'PythonFiles' : ['.py']
    }

    for filename in os.listdir(folder):
        filepath = os.path.join(folder, filename)
        
        if os.path.isfile(filepath):
            for directory, extensions in file_types.items():
                if filename.endswith(tuple(extensions)):
                    folder_path = os.path.join(folder, directory)
                    
                    if os.path.exists(folder_path) == False:
                        os.makedirs(folder_path)

                    shutil.move(filepath, os.path.join(folder_path, filename))
                    print(f"{filename} moved to {directory}")
                    break


manage_folders(r"pathName")