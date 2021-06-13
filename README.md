# TestsProject

Recieved an assignment in a course "Quality testing in software engineering" to develop an app to analyze patient's blood test to generate a recommended treatment.

• Doctor.xlsx represents as the database of the doctors who can access the app.

• Database.py consists openPyXl library to connect between the Excel enviroment to Python and save the Excel File/Sheet/Cell as a variable to use in the app.

• Main.py as the main file of the app, opens a log-in window to access the main purpose of the app.

• Diagnosis.py is the file that handles all the analyzing the blood results and generating a recommended treatment, 
also generating a text file for each patient once analyzed and reading the file in a text box, where the active doctor can edit and save the file with any notes.

• DiagnoseTable.xlsx is a Excel table for checking a specific disease to generate a more accurate treatment (yet to be implemented!).


In order to create an executable file you'll need:
1. Install cx_Freeze using pip:
   1.1. open cmd by CTRL + R and typing 'cmd' and pressing enter
   1.2. type pip install cx_freeze
2. download/pull the files from the "New" branch in a folder
3. open the cmd in the folder(2 options):
   • open the folder which you downloaded the files in and type 'cmd' in the path explorer
   [Capture](https://user-images.githubusercontent.com/83203304/121799726-5584d100-cc36-11eb-944e-1608bd0c142b.JPG)
   • open cmd by CTRL + R and typing 'cmd' and pressing enter
     in the cmd console type cd 'directoryofthefolder'
4. type in the cmd console 'python setup.py build' or 'python3 setup.py build'
5. a folder named 'build' will be created in the currently active folder and inside the 'build' folder there will be a folder named 'exe.win-amd64-3.9'
6. inside 'exe.win-amd64-3.9' folder there will be a executable file named 'AutoDoctor'.
7. In order to start the program just double click on 'AutoDoctor'
