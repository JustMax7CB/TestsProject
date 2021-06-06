import os
from tkinter import *
from tkinter import ttk, messagebox

import Database
import Diagnosis


def main():
    MainWindow = Tk()
    MainWindow.title("Diagnosis App")
    MainWindow.geometry("400x150")
    MainWindow.resizable(width=False, height=False)
    MainWindow.iconbitmap(os.getcwd() + "\RobotDoctor.ico")

    MainWindow.grid_columnconfigure(3)
    MainWindow.grid_rowconfigure(5)

    UsernameEntry = StringVar()
    PasswordEntry = StringVar()
    IDEntry = IntVar()

    UsernameLabel = Label(MainWindow, text="Username", font=("Lato", 11)).grid(row=1, column=1, padx=5, pady=5)
    UsernameTextBox = ttk.Entry(MainWindow, width=30, textvariable=UsernameEntry)
    UsernameTextBox.grid(row=1, column=2, padx=2, pady=2)
    UsernameTextBox.focus()

    PasswordLabel = Label(MainWindow, text="Password", font=("Lato", 11)).grid(row=2, column=1, padx=5, pady=5)
    PasswordTextBox = ttk.Entry(MainWindow, width=30, textvariable=PasswordEntry, show="*")
    PasswordTextBox.grid(row=2, column=2, padx=2, pady=2)

    IDLabel = Label(MainWindow, text="ID", font=("Lato", 11)).grid(row=3, column=1, padx=5, pady=5)
    IDTextBox = ttk.Entry(MainWindow, width=30, textvariable=IDEntry)
    IDTextBox.grid(row=3, column=2, padx=2, pady=2)

    ShowPassword = ttk.Button(MainWindow, text="Show", width=5,
                              command=lambda: PasswordTextBox.configure(show="")).grid(row=2, column=3)
    HidePassword = ttk.Button(MainWindow, text="Hide", width=5,
                              command=lambda: PasswordTextBox.configure(show="*")).grid(row=2, column=4)
    ExitButton = Button(MainWindow, text="Exit", font=('Lato', 11), width=8, command=MainWindow.destroy) \
        .grid(row=5, column=2, padx=5, pady=5)
    LoginButton = Button(MainWindow, text="Login", font=('Lato', 11), width=8,
                         command=lambda: Login(UsernameEntry.get(), PasswordEntry.get(), IDEntry.get(), MainWindow))\
        .grid(row=5, column=1, padx=5, pady=5)
    MainWindow.mainloop()


def Login(username, password, id, window):
    UserNames = list()
    Passwords = list()
    IDs = list()
    UsersSheet = Database.MainSheet
    index = 2
    while UsersSheet.cell(row=index, column=1).value is not None:
        UserNames.append(UsersSheet.cell(row=index, column=1).value)
        Passwords.append(UsersSheet.cell(row=index, column=2).value)
        IDs.append(UsersSheet.cell(row=index, column=3).value)
        index += 1

    if (8 >= len(username)) and (10 >= len(password) >= 8):
        User = list(username)
        NumCount = 0
        for letter in range(0, len(User)):
            if '9' >= User[letter] > '0':
                NumCount += 1
        if NumCount <= 2:
            Special = ("#", "!", "$", "&", "*", "^", "@", "%")
            NumCount = 0
            CharCount = 0
            SpecialCount = 0
            Pass = list(password)
            for number in range(0, len(Pass)):
                if '9' >= Pass[number] > '0':
                    NumCount += 1
                if 'z' >= Pass[number] > 'A':
                    CharCount += 1
                for specialChar in range(0, len(Special)):
                    if Pass[number] == Special[specialChar]:
                        SpecialCount += 1
            result = (NumCount >= 1) and (CharCount >= 1) and (SpecialCount >= 1)
            if not result:
                messagebox.showerror("invalid login attempt", "username or password is incorrect!")
            else:
                if username in UserNames and password in Passwords and id in IDs:
                    messagebox.showinfo("Success!", "Login Successful!")
                    Diagnosis.DiagnosisWindow(window)

                else:
                    messagebox.showerror("invalid login attempt", "username or password is incorrect!")
        else:
            messagebox.showerror("invalid login attempt", "username or password is incorrect!")
    else:
        messagebox.showerror("invalid login attempt", "username or password is incorrect!")


if __name__ == "__main__":
    main()
