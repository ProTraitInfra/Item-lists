# Version control of data element lists
Here you will find the installation/set-up guide for the version control of the **ProTrait** data element lists

## 1. Install software
- Install [GitHub Desktop](https://desktop.github.com/)
- Download & install [Python](python.org) and PIP. [Check this tutorial to find out how](https://matthewhorne.me/how-to-install-python-and-pip-on-windows-10/).

## 2. Set up this repository in GitHub Desktop
- Open GitHub Desktop
- Click File --> Clone repository
- Select tab "URL"
- Paste "https://github.com/ProTraitInfra/Item-lists.git" in text field under "Repository URL or GitHub username and repository
- Set "local path". This will be the folder in which all documents are stored on your computer.
- Click "Clone"
- If asked login with your Git**Lab** username and password.

## 3. Convert files to CSV
- Open repository in your file explorer. For example: C:\Users\John Doe\Documents\data-element-lists 
- Put data element files (.xlsx) in folder "lists". **Note: please do not use spaces and long names for these files. If you do, it will not work** 
- Execute (double-click) file "convertXlsToCsv.bat". This program will convert all your xlsx files to CSV files. This is needed since it is not possible to track document changes in xlsx

## 4. Upload files
- Open GitHub Desktop
- Set this repository as your Current repository
- Select all changed files in the left vertical bar
- Add a description of the changes made
- Click "commit to Master"


