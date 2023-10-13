## Python-Scripting-in-DigSILENT-PowerFactory

### Introduction

This project is dedicated to developing Python scripts for conducting studies and analysis in  DigSilent PowerFactory, a software application used for industrial grade power system simulation and analysis.

Python Scripting enables the automation of tasks and workflows in DigSilent PowerFactory, while also simplifying the manipulation and processing of power system data for in-depth analysis.

### PowerFactory Version

Scripts developed here were executed in an older version - PowerFactory 15.1  - Official Release notes can be found [here](https://www.digsilent.me/dme/filedata/fetch?id=712)

### Environment setup 
 
Scripts were written on Visual Studio Code and the python script file uploaded directly to PowerFactory. Scripting was done in an isolated virtual environment away from the  main python environment. 

- Run this in the cmd terminal window in vs code
  
 - Ensure that in the termianl you are in the folder you intend to store the scripts
```python
py -3  -m venv venv
```
- This creates an isolated environment that you can run your scripts

### Uploading script file to PowerFactory

- After writing your scripts you will need to upload it to PowerFactory and execute the scripts there. Below are imagees showing how Python Scripts can be uploaded. 
  
![image](https://github.com/koechkiplangat/Python-Scripting-in-DigSILENT-PowerFactory/assets/37098206/032e6af3-f946-4aab-a89f-d082f1e42e1d)

- On the toolbars, click on Data then Scripts. A Projects Folder, Library/Scripts opens up as shown below

![tempsnip](https://github.com/koechkiplangat/Python-Scripting-in-DigSILENT-PowerFactory/assets/37098206/82edc1b7-7082-46f1-a5f3-bacf0d411031)

- Select New Object (Circled in Red). The Element selection panel will pop up, choose PythonScripts (ComPython). Upload the script file from its  folder and  execute it.

This will execute the script in PowerFactory

###Test Grid

The Brazillian Seven bus equivalent system is used as the test grid for this project. A digsilent file of this project is available the code section as a .dz file
More information regarding this grid can be found in these two references.

- https://icseg.iti.illinois.edu/brazilian-7-bus-system/#:~:text=This%207%2Dbus%2C%205%2D,small%2Dsignal%20stability%20related%20works.
- https://www.youtube.com/watch?v=ZC355wCnD5w



