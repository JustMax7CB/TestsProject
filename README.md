# TestsProject

Recieved an assignment in a course "Quality testing in software engineering" to develop an app to analyze patient's blood test to generate a recommended treatment.

• Doctor.xlsx represents as the database of the doctors who can access the app.
• Database.py consists openPyXl library to connect between the Excel enviroment to Python and save the Excel File/Sheet/Cell as a variable to use in the app.
• Main.py as the main file of the app, opens a log-in window to access the main purpose of the app.
• Diagnosis.py is the file that handles all the analyzing the blood results and generating a recommended treatment, 
also generating a text file for each patient once analyzed and reading the file in a text box, where the active doctor can edit and save the file with any notes.
• DiagnoseTable.xlsx is a Excel table for checking a specific disease to generate a more accurate treatment (yet to be implemented!).
