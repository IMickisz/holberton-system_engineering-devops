# 0x00. Shell, basics

## Learning Objectives

### General

* What does RTFM mean?
* What is a Shebang
* What is the Shell
* What is the shell
* What is the difference between a terminal and a shell
* What is the shell prompt
* How to use the history (the basics)

### Navigation

* What do the commands or built-ins cd, pwd, ls do
* How to navigate the filesystem
* What are the . and .. directories
* What is the working directory, how to print it and how to change it
* What is the root directory
* What is the home directory, and how to go there
* What is the difference between the root directory and the home directory of the user root
* What are the characteristics of hidden files and how to list them
* What does the command cd - do

### Looking Around

* What do the commands ls, less, file do
* How do you use options and arguments with commands
* Understand the ls long format and how to display it

### A Guided Tour

* What does the ln command do
* What do you find in the most common/important directories
* What is a symbolic link
* What is a hard link
* What is the difference between a hard link and a symbolic link

### Manipulating Files

* What do the commands cp, mv, rm, mkdir do
* What are wildcards and how do they work
* How to use wildcards

### Working with Commands

* What do type, which, help, man commands do
* What are the different kinds of commands
* What is an alias
* When do you use the command help instead of man

### Reading Man Pages

* How to read a man page
* What are man page sections
* What are the section numbers for User commands, System calls and Library functions
* Keyboard Shortcuts for Bash
* Common shortcuts for Bash

### LTS

* What does LTS mean?

## Requirements

### General

* Allowed editors: vi, vim, emacs
* All your scripts will be tested on Ubuntu 20.04 LTS
* All your scripts should be exactly two lines long ($ wc -l file should print 2)
* All your files should end with a new line (why?)
* The first line of all your files should be exactly #!/bin/bash
* A README.md file at the root of the repo, containing a description of the repository
* A README.md file, at the root of the folder of this project, describing what each script is doing
* You are not allowed to use backticks, &&, || or ;
* All your scripts must be executable. To make your file executable, use the chmod command: **chmod u+x _file_**. Later, we’ll learn more about how to utilize this command.

# Tasks

## Mandatory tasks

* [Task 0](https://github.com/IMickisz/holberton-system_engineering-devops/blob/main/0x00-shell_basics/0-current_working_directory) : Write a script that prints the absolute path name of the current working directory.
* [Task 1](https://github.com/IMickisz/holberton-system_engineering-devops/blob/main/0x00-shell_basics/1-listit) : Display the contents list of your current directory.
* [Task 2](https://github.com/IMickisz/holberton-system_engineering-devops/blob/main/0x00-shell_basics/2-bring_me_home) : Write a script that changes the working directory to the user’s home directory (without shell variables).
* [Task 3](https://github.com/IMickisz/holberton-system_engineering-devops/blob/main/0x00-shell_basics/3-listfiles) : Display current directory contents in a long format.
* [Task 4](https://github.com/IMickisz/holberton-system_engineering-devops/blob/main/0x00-shell_basics/4-listmorefiles) : Display current directory contents, including hidden files (starting with .). Use the long format.
* [Task 5](https://github.com/IMickisz/holberton-system_engineering-devops/blob/main/0x00-shell_basics/5-listfilesdigitonly) : Display current directory contents (long format, with user and group IDs displayed numerically and hidden files (starting with .)).
* [Task 6](https://github.com/IMickisz/holberton-system_engineering-devops/blob/main/0x00-shell_basics/6-firstdirectory) : Create a script that creates a directory named *my_first_directory* in the */tmp/* directory.
* [Task 7](https://github.com/IMickisz/holberton-system_engineering-devops/blob/main/0x00-shell_basics/7-movethatfile) : Move the file *betty* from */tmp/* to */tmp/my_first_directory*.
* [Task 8](https://github.com/IMickisz/holberton-system_engineering-devops/blob/main/0x00-shell_basics/8-firstdelete) : Delete the file *betty* in */tmp/my_first_directory*.
* [Task 9](https://github.com/IMickisz/holberton-system_engineering-devops/blob/main/0x00-shell_basics/9-firstdirdeletion) : Delete the directory *my_first_directory* that is in the */tmp* directory.
* [Task 10](https://github.com/IMickisz/holberton-system_engineering-devops/blob/main/0x00-shell_basics/10-back) : Write a script that changes the working directory to the previous one.
* [Task 11](https://github.com/IMickisz/holberton-system_engineering-devops/blob/main/0x00-shell_basics/11-lists) : Write a script that lists all files (even ones with names beginning with a period character, which are normally hidden) in the current directory and the parent of the working directory and the */boot* directory (in this order), in long format.
* [Task 12](https://github.com/IMickisz/holberton-system_engineering-devops/blob/main/0x00-shell_basics/12-file_type) : Write a script that prints the type of the file named *iamafile*. The file *iamafile* will be in the */tmp* directory when we will run your script.
* [Task 13](https://github.com/IMickisz/holberton-system_engineering-devops/blob/main/0x00-shell_basics/13-symbolic_link) : Create a symbolic link to */bin/ls*, named *\__ls__*. The symbolic link should be created in the current working directory.
* [Task 14](https://github.com/IMickisz/holberton-system_engineering-devops/blob/main/0x00-shell_basics/14-copy_html) : Create a script that copies all the HTML files from the current working directory to the parent of the working directory, but only copy files that did not exist in the parent of the working directory or were newer than the versions in the parent of the working directory (You can consider that all HTML files have the extension .html).

## Advanced tasks

* [Task 15](https://github.com/IMickisz/holberton-system_engineering-devops/blob/main/0x00-shell_basics/100-lets_move) : Create a script that moves all files beginning with an uppercase letter to the directory */tmp/u*.
* [Task 16](https://github.com/IMickisz/holberton-system_engineering-devops/blob/main/0x00-shell_basics/101-clean_emacs) : Create a script that deletes all files in the current working directory that end with the character *~*.
* [Task 17](https://github.com/IMickisz/holberton-system_engineering-devops/blob/main/0x00-shell_basics/102-tree) : Create a script that creates the directories *welcome/*, *welcome/to/* and *welcome/to/school* in the current directory.
* [Task 18](https://github.com/IMickisz/holberton-system_engineering-devops/blob/main/0x00-shell_basics/103-commas) : Write a command that lists all the files and directories of the current directory, separated by commas (,).
 * Directory names should end with a slash (/)
 * Files and directories starting with a dot (.) should be listed
 * The listing should be alpha ordered, except for the directories . and .. which should be listed at the very beginning
 * Only digits and letters are used to sort; Digits should come first
 * You can assume that all the files we will test with will have at least one letter or one digit
 * The listing should end with a new line
* [Task 19](https://github.com/IMickisz/holberton-system_engineering-devops/blob/main/0x00-shell_basics/school.mgc) : Create a magic file *school.mgc* that can be used with the command file to detect *School* data files. *School* data files always contain the string *SCHOOL* at offset 0.
