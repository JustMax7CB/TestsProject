from tkinter import *
from tkinter import ttk
from tkinter.messagebox import askquestion

import Main


def DiagnosisWindow():
    DiagnoseWindow = Tk()
    DiagnoseWindow.title("Diagnosis window")
    DiagnoseWindow.geometry("1280x768")
    DiagnoseWindow.resizable(width=False, height=False)

    DiagnoseWindow.grid_rowconfigure(15)
    DiagnoseWindow.grid_columnconfigure(8)

    def Smoking():
        Smoker = askquestion(title='Smoking?', message='Do you smoke?')

    def Disconnect(window):
        window.destroy()
        Main.main()

    ######## Menu Bar ##################
    MenuBar = Menu(DiagnoseWindow)

    FileMenu = Menu(MenuBar, tearoff=0)
    FileMenu.add_separator()
    FileMenu.add_command(label="New")
    FileMenu.add_command(label="Exit", command=quit)
    MenuBar.add_cascade(label="File", menu=FileMenu)

    LoginMenu = Menu(MenuBar, tearoff=0)
    LoginMenu.add_separator()
    LoginMenu.add_command(label="Disconnect", command=lambda: Disconnect(DiagnoseWindow))
    MenuBar.add_cascade(label="Login", menu=LoginMenu)
    #####################################

    DiagnoseWindow.config(menu=MenuBar)

    ############# Variables ####################
    FilePath = r'C:\Users\Sman9\Desktop\TestsProject'
    PatientName = StringVar()
    PatientAge = IntVar()
    PatientGender = StringVar()
    WBC = IntVar()
    Neut = IntVar()
    Lymph = IntVar()
    RBC = DoubleVar()
    HCT = IntVar()
    Urea = IntVar()
    Hb = IntVar()
    CHNO = IntVar()
    Iron = IntVar()
    HDL = IntVar()
    AlkalinePhosphatase = IntVar()
    Smoker = BooleanVar()

    Labelsfont = ("Lato", 13)

    ############################################

    def GenerateTextFile(name):
        if Smoker:
            Smoking_ = "Yes"
        else:
            Smoking_ = "No"
        PatientName = name
        DiagnosisFile = open(FilePath, "Patients", PatientName + ".txt", 'w+')
        DiagnosisFile.write("Patient Name: " + PatientName + "\n")
        DiagnosisFile.write("Smoking : " + Smoking_ + "\n")
        DiagnosisFile.write("White Blood Cells : " + str(WBC.get()) + "\n")
        DiagnosisFile.write("Neutrophil: " + str(Neut.get()) + "\n")
        DiagnosisFile.write("Lymphocytes : " + str(Lymph.get()) + "\n")
        DiagnosisFile.write("Red Blood Cells : " + str(RBC.get()) + "\n")
        DiagnosisFile.write("HCT : " + str(HCT.get()) + "\n")
        DiagnosisFile.write("Urea : " + str(Urea.get()) + "\n")
        DiagnosisFile.write("Hemoglobin : " + str(Hb.get()) + "\n")
        DiagnosisFile.write("CHNO : " + str(CHNO.get()) + "\n")
        DiagnosisFile.write("Iron : " + str(Iron.get()) + "\n")
        DiagnosisFile.write("High Density Lipoprotein : " + str(HDL.get()) + "\n")
        DiagnosisFile.write("Alkline Phosphatase : " + str(AlkalinePhosphatase.get()) + "\n")
        DiagnosisFile.close()

    ############## Buttons #####################

    ConfirmSelection = Button(DiagnoseWindow, text="Confirm", width=20, height=1, background="sienna2",
                              font=Labelsfont, relief=GROOVE, command=lambda: GenerateTextFile(PatientName.get())).grid(
        row=11, column=5)

    #############################################

    Patient_Name_Label = ttk.Label(DiagnoseWindow, width=30, text="Name:", font=Labelsfont).grid(row=1,
                                                                                                 column=1,
                                                                                                 sticky=W)
    Patient_Name_TextBox = ttk.Entry(DiagnoseWindow, width=30, textvariable=PatientName)
    Patient_Name_TextBox.grid(row=1, column=2, sticky=W)
    Patient_Name_TextBox.focus()

    Patient_Age_Label = ttk.Label(DiagnoseWindow, width=20, text="Age:", font=Labelsfont).grid(row=2, column=1,
                                                                                               sticky=W)
    Patient_Age_Combobox = ttk.Combobox(DiagnoseWindow, width=20, values=tuple(range(121)),
                                        textvariable=PatientAge).grid(row=2, column=2, sticky=W)

    Patient_Gender_Label = ttk.Label(DiagnoseWindow, width=20, text="Gender:", font=Labelsfont).grid(row=3, column=1,
                                                                                                     sticky=W)
    Patient_Gender_Combobox = ttk.Combobox(DiagnoseWindow, width=10, values=("Male", "Female"),
                                           textvariable=PatientGender).grid(row=3, column=2, sticky=W)
    WBC_Label = ttk.Label(DiagnoseWindow, width=30, text="White Blood Cells", font=Labelsfont).grid(row=4,
                                                                                                    column=1,
                                                                                                    sticky=W)
    WBC_Scale = Scale(DiagnoseWindow, from_=4000, to=12000, length=600, tickinterval=550,
                      orient=HORIZONTAL, variable=WBC, background="floralwhite").grid(row=4, column=2, sticky=W)

    Neut_Label = ttk.Label(DiagnoseWindow, width=30, text="Neutrophil (in %)", font=Labelsfont).grid(row=5,
                                                                                                     column=1,
                                                                                                     sticky=W)
    Neut_Scale = Scale(DiagnoseWindow, from_=0, to=100, length=400, tickinterval=5, orient=HORIZONTAL, variable=Neut,
                       background="bisque").grid(row=5, column=2, sticky=W)

    Lymph_Label = ttk.Label(DiagnoseWindow, width=30, text="Lymphocytes (in %)", font=Labelsfont).grid(row=6, column=1,
                                                                                                       sticky=W)
    Lymph_Scale = Scale(DiagnoseWindow, from_=0, to=100, length=400, tickinterval=5, orient=HORIZONTAL, variable=Lymph,
                        background="navajo white").grid(row=6, column=2, sticky=W)

    RBC_Label = ttk.Label(DiagnoseWindow, width=30, text="Red Blood Cells", font=Labelsfont).grid(row=7,
                                                                                                  column=1,
                                                                                                  sticky=W)
    RBC_Scale = Scale(DiagnoseWindow, from_=2.0, to=8.5, digits=2, length=400, resolution=0.3, tickinterval=0.5,
                      orient=HORIZONTAL, variable=RBC,
                      background="salmon").grid(row=7, column=2, sticky=W)

    HCT_Label = ttk.Label(DiagnoseWindow, width=30, text="HCT (in %)", font=Labelsfont).grid(row=8,
                                                                                             column=1,
                                                                                             sticky=W)
    HCT_Scale = Scale(DiagnoseWindow, from_=0, to=100, length=400, tickinterval=5, orient=HORIZONTAL, variable=HCT,
                      background="light coral").grid(row=8, column=2, sticky=W)

    Urea_Label = ttk.Label(DiagnoseWindow, width=30, text="Urea (mg)", font=Labelsfont).grid(row=9,
                                                                                             column=1,
                                                                                             sticky=W)
    Urea_Scale = Scale(DiagnoseWindow, from_=10, to=50, length=300, tickinterval=5, orient=HORIZONTAL, variable=Urea,
                       background="indian red").grid(row=9, column=2, sticky=W)

    Hb_Label = ttk.Label(DiagnoseWindow, width=30, text="Hemoglobin (mg)", font=Labelsfont).grid(row=10,
                                                                                                 column=1,
                                                                                                 sticky=W)
    Hb_Scale = Scale(DiagnoseWindow, from_=10.0, to=18.0, length=450, digits=3, resolution=0.5, tickinterval=0.5,
                     orient=HORIZONTAL, variable=Hb,
                     background="rosy brown").grid(row=10, column=2, sticky=W)

    CHNO_Label = ttk.Label(DiagnoseWindow, width=30, text="Creatinine", font=Labelsfont).grid(row=11,
                                                                                              column=1,
                                                                                              sticky=W)
    CHNO_Scale = Scale(DiagnoseWindow, from_=0, to=1.5, length=450, digits=2, resolution=0.1, tickinterval=0.1,
                       orient=HORIZONTAL, variable=CHNO,
                       background="sandy brown").grid(row=11, column=2, sticky=W)

    Iron_Label = ttk.Label(DiagnoseWindow, width=30, text="Iron", font=Labelsfont).grid(row=12,
                                                                                        column=1,
                                                                                        sticky=W)
    Iron_Scale = Scale(DiagnoseWindow, from_=50, to=200, length=450, tickinterval=20, orient=HORIZONTAL, variable=Iron,
                       background="seashell4").grid(row=12, column=2, sticky=W)

    HDL_Label = ttk.Label(DiagnoseWindow, width=30, text="High Density Lipoprotein (mg)", font=Labelsfont).grid(row=13,
                                                                                                                column=1,
                                                                                                                sticky=W)
    HDL_Scale = Scale(DiagnoseWindow, from_=20, to=100, length=450, tickinterval=12, orient=HORIZONTAL, variable=HDL,
                      background="goldenrod").grid(row=13, column=2, sticky=W)

    AlkalinePhosphatase_Label = ttk.Label(DiagnoseWindow, width=30, text="Alkaline Phosphatase (units)",
                                          font=Labelsfont).grid(row=14,
                                                                column=1,
                                                                sticky=W)
    AlkalinePhosphatase_Scale = Scale(DiagnoseWindow, from_=50, to=150, length=450, tickinterval=15, orient=HORIZONTAL,
                                      variable=AlkalinePhosphatase,
                                      background="dark salmon").grid(row=14, column=2, sticky=W)

    def Diagnose():
        DiagnosisFile = open(FilePath, "Patients", PatientName.get() + ".txt", 'a')

    DiagnoseWindow.mainloop()
