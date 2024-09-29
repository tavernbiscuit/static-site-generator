import shutil
import os

def copy_files_recursive(source_path, dest_path):
    if not os.path.exists(dest_path):
        os.mkdir(dest_path)
    
    for item in os.listdir(source_path):
        from_path = os.path.join(source_path, item)
        to_path = os.path.join(dest_path, item)
        
        if os.path.isfile(from_path):
            shutil.copy(from_path, to_path)
        else:
            copy_files_recursive(from_path, to_path)


 