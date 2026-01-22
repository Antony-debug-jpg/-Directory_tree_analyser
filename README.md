Directory Tree Analyzer
Overview

The Directory Tree Analyzer is a Python command-line application that analyzes the structure and contents of a specified directory.
It recursively scans folders to compute statistics such as the number of files and subdirectories, total storage size, file type distribution, and the largest files found.

The project was developed to demonstrate practical understanding of Python basics, file system operations, and exception handling.

Objectives

Understand directory traversal in Python

Apply file handling concepts

Practice dictionary-based data aggregation

Implement robust error handling

Build a functional command-line tool

Features

Recursive directory scanning

Counts total files and directories

Calculates total size of files

Groups files by extension

Displays the largest files

Handles permission and access errors gracefully

Runs via command-line interface (CLI)

Technologies Used

Python 3

Standard libraries:

os

sys

Project Structure
DIRECTORY_TREE_ANALYSER/
│
├── directory_analyser.py
└── README.md

How to Run the Program
Step 1: Navigate to the Project Folder

Open a terminal (PowerShell) and navigate to the project directory:

cd DIRECTORY_TREE_ANALYSER

Step 2: Run the Analyzer

Provide the directory path as a command-line argument:

python directory_analyser.py <directory_path>

Example
python directory_analyser.py C:\Users\Hp\Documents

Output Description

After execution, the program prints a summary report that includes:

Total number of folders

Total number of files

Combined size of all accessible files

File count grouped by extension

Largest files detected in the directory

Zero Output Explanation

If the program outputs zero values for files, folders, or size, this indicates that:

The selected directory is empty, or

Files exist but are inaccessible due to permission restrictions

This behavior is expected and confirms correct handling of such cases.

Error Handling

Invalid paths are detected and reported

Permission-related errors are handled using try-except blocks

The program does not terminate unexpectedly when access is denied

Learning Outcomes

This project demonstrates:

Python syntax and control flow

Recursive directory traversal

File system interaction

Dictionary usage for data organization

Exception handling using try-except

Command-line argument processing

Author

Franklin Tumaini
Computer Science Student

License

This project is intended for educational purposes and is free to use and modify for learning.

