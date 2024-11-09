Restricted Folder Copy-Paste Monitor

This project monitors a specified "root" folder to prevent users from copying and pasting files or content from this folder to unauthorized locations, including external drives or cloud storage. By intercepting clipboard actions and monitoring file modifications in the root folder, this tool restricts the movement of sensitive data.

Features

    1. Clipboard Monitoring: Clears clipboard content if it contains files from the specified root folder, preventing unauthorized paste actions.

    2. File System Monitoring: Watches for modifications within the root folder and triggers clipboard checks as needed.

    3. Cross-Platform: Primarily designed for Windows due to clipboard handling via pywin32, but adaptable to other systems with modifications.

Prerequisites

    1. Python 3.6+: Ensure Python is installed on your system.

    2. Dependencies: Install the required dependencies from the requirements.txt file.

Installation

    1. Clone the repository to your local machine:
        git clone https://github.com/Victorjaglen/Restricted-Folder-Copy-Paste-Monitor.git

    2. Create a Virtual Environment:
        python -m venv venv

    3. Activate the Virtual Environment:
        Windows : venv\Scripts\activate
        MAC : source venv/bin/activate


    4. Install Dependencies: 
        pip install -r requirements.txt

    5. Edit the Root Directory Path: 
        In copy_paste_restriction.py, set the root   directory you want to monitor by updating the   ROOT_DIRECTORY variable:
        ROOT_DIRECTORY = 'C:/restricted_root'
        Replace 'C:/restricted_root' with the path to the folder you want to restrict.

    6. Run the Script: 
        python app.py

        The script will now monitor the specified root folder and intercept any unauthorized copy-paste actions involving files from this folder.