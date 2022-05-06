import pyperclip
import csv
import os

'''
 ______     __  __     ______     __     ______    
/\  ___\   /\ \_\ \   /\  == \   /\ \   /\  ___\   
\ \ \____  \ \  __ \  \ \  __<   \ \ \  \ \___  \  
 \ \_____\  \ \_\ \_\  \ \_\ \_\  \ \_\  \/\_____\ 
  \/_____/   \/_/\/_/   \/_/ /_/   \/_/   \/_____/ 
                                                   

Get Description For Post

This script is designed to output a basic text file that will contain a generic description for posts made on Social Media (e.g. Youtube and Etsy etc)


April 2022
'''

def create_description():
    
    # Start with a blank string variable that will be populated throughout this script
    list_of_file_descriptions = ""
    # Import the CSV file that was the template file for the corresponding project
    csv_file = input("Enter the csv template file for this project: ")
    stripped_file = csv_file.replace('"', "")

    # Read out all the data of the csv file into a list to use later
    csv_data = []
    with open(stripped_file, newline='') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row in reader:
            csv_data.append(row)
    
    project_folder_location = input("Please enter the project path: ").replace('"', "")
    project_folder_path = os.path.normpath(project_folder_location)
    if os.path.isdir(project_folder_location):
        project_name = os.path.basename(project_folder_path)
    else:
        print("The Project path was not properly specified...Exiting")
        exit()

    list_of_file_descriptions += f"{project_name}\n\n"
    list_of_file_descriptions += "-------------------------------------\n\n"
    package_details = input("Please enter some initial details for your package:(What the package is about, how it was designed) ")
    list_of_file_descriptions += f"{package_details}\n\n"
    list_of_file_descriptions += "-------------------------------------\n\n"
    list_of_file_descriptions += "---Disclaimer for your Download---\n\n"
    list_of_file_descriptions += "Please read the following regarding purchasing this Downloadable Package\n\n"
    list_of_file_descriptions += "This is a digital package that you can download from us. When you purchase this product you will be given a PDF with a download link that you can use to download the full package from us. Please do not share this link.\n\n"
    manual_link = input("Please input the URL for this project's manual here: ")
    list_of_file_descriptions += f"For instructions on how to setup your stream with our package visit this link: {manual_link}\n\n"
    list_of_file_descriptions += "This package has been optimized for OBS and StreamLabs OBS and comes with quick installer files for both programs to help you quickly setup your stream.\n\n"
    list_of_file_descriptions += "-------------------------------------\n\n"
    list_of_file_descriptions += "This package utilizes free fonts available online and are required for your stream to work correctly."
    list_of_file_descriptions += "These fonts are not included inside this package but links will be provided to you to where you can download them:\n"
    print("Please input fonts that you will need for this description.")

    while True:
        font_name = input("Enter the name of the font: ")
        font_url = input(f"Enter in the URL for the font {font_name}: ")
        list_of_file_descriptions += f"{font_name}: {font_url}\n"
        ask_user = input("Do you have any more fonts to add? [yes/no]: ")
        if ask_user == "yes" or ask_user == "y":
            continue
        else:
            break
    list_of_file_descriptions += "\n"
    list_of_file_descriptions += "-------------------------------------\n\n"
    list_of_file_descriptions += "This animated streaming package comes with an assortment of Animated 60FPS .webm files and Static .png files as listed below.\n\n"
    list_of_file_descriptions += "What you will receive with this package:\n\n"


    # Go through the csv_data list and append all the available data to the file description variable
    i = 0
    for row in csv_data:
        this_csv_row = csv_data[i]

        file_element = this_csv_row[0]
        file_width = this_csv_row[1]
        file_height = this_csv_row[2]
        file_type = this_csv_row[3]
        if file_type == "None":
            list_of_file_descriptions += f"1 {file_element} \n"
            list_of_file_descriptions += f"- 1 {file_element} {file_width}x{file_height} file\n"
        else: 
            file_type = file_type.replace("[", "")
            file_type = file_type.replace("]", "")
            these_types = file_type.split("|")
            number_of_items = len(these_types)
            if number_of_items > 1: 
                list_of_file_descriptions += f"{str(number_of_items)} {file_element}s\n"
            else: 
                list_of_file_descriptions += f"{str(number_of_items)} {file_element} file\n"
            for this_type in these_types:
                list_of_file_descriptions += f"- 1 {this_type} {file_element} {file_width}x{file_height} file\n"
        list_of_file_descriptions += "\n"

        i += 1

    # final
    list_of_file_descriptions += "Extra Items\n"
    list_of_file_descriptions += "- A thank you note\n"
    list_of_file_descriptions += "- A shortcut link to our store\n"
    list_of_file_descriptions += "- A Quick OBS Installer File\n"
    list_of_file_descriptions += "- A Quick StreamLabs Installer File\n"
    list_of_file_descriptions += "- An Official Stream Guide For Setting Up Your Stream\n"
    list_of_file_descriptions += "-------------------------------------\n\n"
    list_of_file_descriptions += "Thank you for stopping by our store and we hope you found something that you like!\n\n"
    list_of_file_descriptions += "Contact us even for custom stream overlays you need, or if you have any trouble setting up your purchase from our store. We would be glad to help you out!\n\n"
    list_of_file_descriptions += "-------------------------------------\n\n"
    list_of_file_descriptions += "Who We Are:\n\n"
    list_of_file_descriptions += "We are MBP and we try to make sick twitch overlays and share them for sell online for OBS and Streamlabs! Hope to see you streaming soon!\n\n"
    list_of_file_descriptions += "Check us out on Youtube here!: https://www.youtube.com/channel/UCGpXLFJZBIQcJDLKT6NjSeg\n\n"

    
    pyperclip.copy(list_of_file_descriptions)

    # Finally output a file in the project folder so that we can have a description file to work with.
    description_file = "description_for_post.txt"
    description_file_location = os.path.join(project_folder_path, description_file)

    with open(description_file_location, "w") as file:
        file.writelines(list_of_file_descriptions)
        file.close()

    print("Check out the project folder for the description for the post. We also added the description to your clipboard ;]. Exiting...")


create_description()