import os
import csv
import re
import shutil

'''

 ______     __  __     ______     __     ______    
/\  ___\   /\ \_\ \   /\  == \   /\ \   /\  ___\   
\ \ \____  \ \  __ \  \ \  __<   \ \ \  \ \___  \  
 \ \_____\  \ \_\ \_\  \ \_\ \_\  \ \_\  \/\_____\ 
  \/_____/   \/_/\/_/   \/_/ /_/   \/_/   \/_____/ 
                                                   

Create Twitch Package Folder

This script is designed to make the the Twitch folder that will be compressed and uploaded to Google Drive

This will save in the project folder

April 2022


'''

current_directory = os.path.dirname(__file__)


# Check if a folder currently exists that gets passed through to this function
# Then if it doesn't exist, create it
def check_folder_exists_then_create(folder):

    '''This will check if the folder being passed was already created in order to be safe not to overwrite it.'''

    if os.path.isdir(folder):
        print(f"The folder: {folder} already exists.")
    else:
        # Create folder
        print(f"Creating folder: {folder}")
        os.makedirs(folder)


def remove_xmp_files(folder):

    '''There are some annoying xmp files that are created with .webm files. This will get rid of all of them.'''

    files_in_directory = os.listdir(folder)

    filtered_files = [file for file in files_in_directory if file.endswith(".xmp")]

    for file in filtered_files:
        path_to_file = os.path.join(folder, file)
        os.remove(path_to_file)


def fix_png_filenames(folder):

    '''Fix the png files that have a wierd ending to it due to AE file output.'''

    files_in_directory = os.listdir(folder)

    filtered_files = [file for file in files_in_directory if file.endswith(".png")]

    for file in filtered_files:

        space_count = 0
        for a in file:
            if (a.isspace()) is True:
                space_count += 1
        
        if space_count == 1:
            # path_to_file = os.path.join(folder, file)
            # Do regex to grab the portion of the file name that we want
            x = re.split("\s", file, 1)
            file_extension = ".png"
            file_name = x[0]
            new_file_name = file_name + file_extension

            # Rename png files
            source = f"{folder}/{file}"
            destination = f"{folder}/{new_file_name}"
            os.rename(source, destination)
        elif space_count == 0:
            print(f"No need to rename {file}. Passing...")


def copy_thank_you(folder):

    '''Copy the Thank you PNG file over to the specified folder path.'''

    thanks_image = "Thank_You.png"
    thanks_image_path = os.path.join(current_directory, thanks_image)
    shutil.copy(thanks_image_path, folder)


def create_etsy_shortcut(folder):

    '''Create a shortcut to the Etsy Store in the specified folder.'''

    target_url = "https://www.etsy.com/shop/MoreBackgrounds"
    link_name = "Visit Our Etsy Store.url"
    link_path = os.path.join(folder, link_name)

    with open(link_path, 'w') as shortcut:
        shortcut.write('[InternetShortcut]\n')
        shortcut.write('URL=' + target_url)


def copy_lua_script(folder):

    '''Copy over the Lua template into the Twitch folder.'''

    lua_script = "Quick OBS Installer Template.lua"
    script_path = os.path.join(current_directory, lua_script)

    script_new_name = "Quick OBS Installer.lua"
    new_script_path = os.path.join(folder, script_new_name)

    shutil.copy(script_path, new_script_path)


# Using csv library, iterate through the stream template csv and create 
# a series of folders for the final rendered products
def create_twitch_folders():

    '''Create the Twitch folder where all the final rendered items will go into and organize into all the folders.'''

    csv_file = input("Please enter csv template file path for project: ")
    stripped_csv_file = csv_file.replace('"', "")
    
    project_folder_location = input("Please enter the project path: ").replace('"', "")
    project_folder_path = os.path.normpath(project_folder_location)
    if os.path.isdir(project_folder_location):
        project_name = os.path.basename(project_folder_path)
    else:
        print("The Project path was not properly specified...Exiting")
        exit()
    
    new_parent_dir = os.path.join(project_folder_path, project_name)

    renders_for_package_folder = "Renders For Package"
    renders_path = os.path.join(project_folder_path, renders_for_package_folder)

    # Remvoe the XMP Files and fix the PNG Rendered files' names
    remove_xmp_files(renders_path)
    fix_png_filenames(renders_path)
    
    # Create the Twitch Package Folder
    check_folder_exists_then_create(new_parent_dir)

    csv_data = []
    with open(stripped_csv_file, newline='') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row in reader:
            csv_data.append(row)

    # Get a list of all the files inside the renders folder
    files_in_rendered_folder = os.listdir(renders_path)

    i = 0
    for row in csv_data:
        this_csv_row = csv_data[i]

        folder_name = this_csv_row[0]
        folder_path = os.path.join(new_parent_dir, folder_name)
        print(folder_path)
        check_folder_exists_then_create(folder_path)

        print("Moving file")
        file_element = this_csv_row[0]
        file_width = this_csv_row[1]
        file_height = this_csv_row[2]
        file_type = this_csv_row[3]
        if file_type == "None":
            expected_file_name = file_element + "_" + file_width + "_" + file_height
            
            for file in files_in_rendered_folder:
                actual_file_name = os.path.splitext(file)[0]
                actual_file_path = os.path.join(renders_path, file)
                if expected_file_name == actual_file_name:
                    shutil.copy(actual_file_path, folder_path)

        else:
            file_type = file_type.replace("[", "")
            file_type = file_type.replace("]", "")
            these_types = file_type.split("|")
            for this_type in these_types:
                expected_file_name = this_type + "_" + file_element + "_" + file_width + "_" + file_height
                
                for file in files_in_rendered_folder:
                    actual_file_name = os.path.splitext(file)[0]
                    actual_file_path = os.path.join(renders_path, file)
                    if expected_file_name == actual_file_name:
                        shutil.copy(actual_file_path, folder_path)

        i += 1
    
    # Copy over the thanks image
    copy_thank_you(new_parent_dir)

    # Add the shortcut to the Etsy MBP Store
    create_etsy_shortcut(new_parent_dir)

    # Add the lua script
    copy_lua_script(new_parent_dir)

    print("Twitch package has been created...Exiting")


create_twitch_folders()