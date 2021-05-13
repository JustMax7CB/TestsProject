from tkinter import *
from tkinter import ttk, messagebox

import Database
import Diagnosis


def main():
    MainWindow = Tk()
    MainWindow.title("Diagnosis App")
    MainWindow.geometry("400x130")
    MainWindow.resizable(width=False, height=False)

    MainWindow.grid_columnconfigure(3)
    MainWindow.grid_rowconfigure(5)

    UsernameEntry = StringVar()
    PasswordEntry = StringVar()

    UsernameLabel = Label(MainWindow, text="Username", font=("Lato", 11)).grid(row=1, column=1, padx=5, pady=5)
    UsernameTextBox = ttk.Entry(MainWindow, width=30, textvariable=UsernameEntry)
    UsernameTextBox.grid(row=1, column=2, padx=5, pady=5)

    PasswordLabel = Label(MainWindow, text="Password", font=("Lato", 11)).grid(row=2, column=1, padx=5, pady=5)
    PasswordTextBox = ttk.Entry(MainWindow, width=30, textvariable=PasswordEntry, show="*")
    PasswordTextBox.grid(row=2, column=2, padx=5, pady=5)

    ShowPassword = ttk.Button(MainWindow, text="Show", width=5,
                              command=lambda: PasswordTextBox.configure(show="")).grid(row=2, column=3)
    HidePassword = ttk.Button(MainWindow, text="Hide", width=5,
                              command=lambda: PasswordTextBox.configure(show="*")).grid(row=2, column=4)
    ExitButton = Button(MainWindow, text="Exit", font=('Lato', 11), width=8, command=quit) \
        .grid(row=5, column=2, padx=5, pady=5)
    LoginButton = Button(MainWindow, text="Login", font=('Lato', 11), width=8,
                         command=lambda: Login(UsernameEntry.get(), PasswordEntry.get(), MainWindow))\
        .grid(row=5, column=1, padx=5, pady=5)
    MainWindow.mainloop()


def Login(username, password, window):
    UserNames = list()
    Passwords = list()
    UsersSheet = Database.MainSheet
    index = 2
    while UsersSheet.cell(row=index, column=1).value is not None:
        UserNames.append(UsersSheet.cell(row=index, column=1).value)
        Passwords.append(UsersSheet.cell(row=index, column=2).value)
        index += 1

    if (8 >= len(username) >= 6 and username in UserNames) and (10 >= len(password) >= 8 and password in Passwords):
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
                messagebox.showinfo("Success!", "Login Successful!")
                window.destroy()
                Diagnosis.DiagnosisWindow()
        else:
            messagebox.showerror("invalid login attempt", "username or password is incorrect!")
    else:
        messagebox.showerror("invalid login attempt", "username or password is incorrect!")


if __name__ == "__main__":
    main()
