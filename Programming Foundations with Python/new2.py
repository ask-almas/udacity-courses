import os
def rename_files():
    file_list = os.listdir(r"D:\Downloads\prank")
    saved_path=os.getcwd()
    print("Current working directory is "+saved_path)
    os.chdir(r"D:\Downloads\prank")
    
    for old_name in file_list:
        new_name = old_name.translate(None, "0123456789")
        print("Old name is "+old_name)
        os.rename(old_name, new_name)
        print("New name is "+new_name)
    os.chdir(saved_path)

rename_files()
