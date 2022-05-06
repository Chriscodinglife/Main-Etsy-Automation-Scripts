#! python

import os
import shutil
from datetime import datetime


'''

 ______     __  __     ______     __     ______    
/\  ___\   /\ \_\ \   /\  == \   /\ \   /\  ___\   
\ \ \____  \ \  __ \  \ \  __<   \ \ \  \ \___  \  
 \ \_____\  \ \_\ \_\  \ \_\ \_\  \ \_\  \/\_____\ 
  \/_____/   \/_/\/_/   \/_/ /_/   \/_/   \/_____/ 
                                                   
This script is designed to create the initial project folder for the Etsy Stream Package.

By default this project folder will be saved to the Desktop.

April 2022


'''


def create_project_folder():

    '''This function will handle creating the actual project folder and sub folders needed to get started'''
    
    current_directory = os.path.dirname(__file__)
    project_name = input("Enter the name of the project: ")
    home_folder = os.path.expanduser("~")
    desktop_location = os.path.join(home_folder, "Desktop")
    project_path = os.path.join(desktop_location, project_name)

    ae_folder = os.path.join(project_path, "After Effects")
    fonts_folder = os.path.join(project_path, "Fonts")
    images_folder = os.path.join(project_path, "Images")
    ads_folder = os.path.join(project_path, "Advertising")
    renders_for_ads_folder = os.path.join(project_path, "Renders for Ads")
    renders_for_package_folder = os.path.join(project_path, "Renders For Package")

    icons_folder = "Icons"
    icons_folder_path = os.path.join(current_directory, icons_folder)
    images_icons_folder = os.path.join(images_folder, icons_folder)

    # Create the parent project folder
    if os.path.isdir(project_path):
        print("Project already exists...")
        exit()
    else:
        print(f"Creating the {project_name} folder")
        os.mkdir(project_path)

    # Create Folders
    os.mkdir(ae_folder)
    os.mkdir(fonts_folder)
    os.mkdir(images_folder)
    os.mkdir(ads_folder)
    os.mkdir(renders_for_ads_folder)
    os.mkdir(renders_for_package_folder)

    if os.path.isdir(icons_folder_path):
        shutil.copytree(icons_folder_path, images_icons_folder)
    else:
        print("Icons folder is missing.")

    status_file = "status.txt"
    status_location = os.path.join(project_path, status_file)

    date = datetime.now()
    print("Creating a new status file...")
    with open(status_location, "w") as status:
        status.write("Created project on " + date.strftime("%b %a %Y"))

    return project_path


create_project_folder()