# Downloads Organizer

## Introduction
The Downloads Organizer is a helpful utility designed to automatically manage and organize files in your Downloads folder based on their file types. It ensures that your Downloads folder stays clean and organized by moving files into their respective folders. Additionally, the script handles edge cases where files may be actively downloading or in a temporary state and ensures that duplicate files are properly renamed.

## Features
- Automatic organization of downloaded files into respective folders.
- Handling of ongoing downloads and temporary files.
- Proper renaming of duplicate files.
- Easy setup and usage.

## Getting Started

### Prerequisites
- Python 3.x or later

### Installation
1. Clone or download this repository to your local machine.

### Usage

#### Initial Setup
1. Run the `initialorganizer.py` script through your terminal to set up the folder structure for organizing your downloads. This script creates appropriate folders and prepares your system for automation.

#### Running in the Background
1. Open Task Scheduler on your Windows machine.
2. Click on "Create Task" on the right-hand panel.
3. In the General tab, set the name of the task according to your preferences.
4. In the Triggers tab, click on "New." Then, select "At startup" for the "Begin the task:" option and click OK.
5. In the Actions tab, under the "Program/script" heading, provide the path to your `pythonw.exe`. 
   - For the "Add arguments (optional):" section, enter "downloadautomation.pyw".
   - For the "Start in (optional):" section, specify the directory where `downloadautomation.pyw` is located (enclosed in quotes).
   - Click OK to save the settings.
6. In the Settings tab, check the following checkboxes:
   - Allow the task to be run on demand.
   - Run the task as soon as possible after a scheduled start is missed.
   - If the running task does not end when requested, force it to stop.
7. Click OK to create the task.

The `downloadautomation.pyw` script will now run in the background, automatically organizing your downloaded files.