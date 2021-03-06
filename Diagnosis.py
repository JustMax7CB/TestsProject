import os
from tkinter import *
from tkinter import ttk, messagebox, filedialog
from tkinter.messagebox import askquestion
import Main


def DiagnosisWindow(topLevel):
    MainFolder = os.getcwd()
    topLevel.destroy()
    DiagnoseWindow = Tk()
    DiagnoseWindow.title("Diagnosis window")
    DiagnoseWindow.geometry("1640x786")
    DiagnoseWindow.resizable(width=False, height=False)
    DiagnoseWindow.iconbitmap(MainFolder + "\RobotDoctor.ico")

    DiagnoseWindow.grid_rowconfigure(15)
    DiagnoseWindow.grid_columnconfigure(8)

    def Smoking():
        Smoker = askquestion(title='Smoking?', message='Does the Patient Smoking?')
        return Smoker.upper()

    def Disconnect(window):
        window.destroy()
        Main.main()

    def New():
        DiagnosisWindow(DiagnoseWindow)

    ######## Menu Bar ##################
    MenuBar = Menu(DiagnoseWindow)

    FileMenu = Menu(MenuBar, tearoff=0)
    FileMenu.add_separator()
    FileMenu.add_command(label="New", command=New)
    FileMenu.add_command(label="Exit", command=DiagnoseWindow.destroy)
    MenuBar.add_cascade(label="File", menu=FileMenu)

    LoginMenu = Menu(MenuBar, tearoff=0)
    LoginMenu.add_separator()
    LoginMenu.add_command(label="Disconnect", command=lambda: Disconnect(DiagnoseWindow))
    MenuBar.add_cascade(label="Login", menu=LoginMenu)
    #####################################

    DiagnoseWindow.config(menu=MenuBar)

    ############# Variables ####################
    PatientName = StringVar()
    PatientAge = IntVar()
    PatientGender = StringVar()
    WBC = IntVar()
    Neut = IntVar()
    Lymph = IntVar()
    RBC = DoubleVar()
    HCT = IntVar()
    Urea = IntVar()
    Hb = DoubleVar()
    CHNO = DoubleVar()
    Iron = IntVar()
    HDL = IntVar()
    AlkalinePhosphatase = IntVar()

    Labelsfont = ("Lato", 13)

    ############################################
    PatientsFolder = os.getcwd()

    def EditFile():
        TextFileDisplay.configure(state=NORMAL)

    def SaveFile():
        nonlocal PatientsFolder
        File = None
        try:
            File = open(PatientsFolder + PatientName.get() + ".txt", 'w')
        except:
            messagebox.showerror(title="Error", message="Failed to open the file\n")
        if File:
            data = TextFileDisplay.get(1.0, END)
            File.write(data)
            File.close()
            TextFileDisplay.configure(state=DISABLED)

    def OpenDiagnoseFile(name):
        TextFileDisplay.configure(state=NORMAL)
        File = None
        try:
            File = open(PatientsFolder + name + ".txt", 'r+')
        except:
            messagebox.showerror(title="Error", message="Failed to open the file\n")
        if File:
            TextFileDisplay.insert(1.0, File.read())
            File.close()
            TextFileDisplay.configure(state=DISABLED)

    def GenerateTextFile(name):
        nonlocal PatientsFolder
        if not os.path.isdir(os.getcwd() + "\\build\Patients\\"):
            os.makedirs(os.getcwd() + "\\build\Patients\\")
        PatientsFolder = os.getcwd() + "\\build\Patients\\"
        TextFileDisplay.configure(state=DISABLED)
        Smoker = Smoking()
        PatientName = name
        DiagnosisFile = open(PatientsFolder + "\\" + PatientName + ".txt", 'w+')
        DiagnosisFile.write("Patient Name: " + PatientName + "\n")
        DiagnosisFile.write("Smoking : " + Smoker + "\n")
        DiagnosisFile.write("White Blood Cells : " + str(WBC.get()) + " units\n")
        DiagnosisFile.write("Neutrophil: " + str(Neut.get()) + "%\n")
        DiagnosisFile.write("Lymphocytes : " + str(Lymph.get()) + "%\n")
        DiagnosisFile.write("Red Blood Cells : " + str(RBC.get()) + " units\n")
        DiagnosisFile.write("Hematocrit : " + str(HCT.get()) + "%\n")
        DiagnosisFile.write("Urea : " + str(Urea.get()) + " mg\n")
        DiagnosisFile.write("Hemoglobin : " + str(Hb.get()) + " mg\n")
        DiagnosisFile.write("CHNO : " + str(CHNO.get()) + " units\n")
        DiagnosisFile.write("Iron : " + str(Iron.get()) + " units\n")
        DiagnosisFile.write("High Density Lipoprotein : " + str(HDL.get()) + " mg\n")
        DiagnosisFile.write("Alkline Phosphatase : " + str(AlkalinePhosphatase.get()) + " units\n")
        DiagnosisFile.close()
        Diagnose()

    ############## Buttons #####################

    ConfirmSelection = Button(DiagnoseWindow, text="Confirm", width=20, height=1, background="sienna2",
                              font=Labelsfont, relief=GROOVE, command=lambda: GenerateTextFile(PatientName.get()))
    ConfirmSelection.place(x=850, y=707, width=110, height=37)

    ExitButton = Button(DiagnoseWindow, text="Exit", width=10, height=1, background="sienna2",
                        font=Labelsfont, relief=GROOVE, command=DiagnoseWindow.destroy)
    ExitButton.place(x=1550, y=707, width=70, height=37)

    EditButton = Button(DiagnoseWindow, text="Edit", width=20, height=1, background="light blue",
                        font=Labelsfont, relief=GROOVE, command=EditFile)
    EditButton.place(x=1120, y=635, width=70, height=37)

    SaveButton = Button(DiagnoseWindow, text="Save", width=20, height=1, background="light blue",
                        font=Labelsfont, relief=GROOVE, command=SaveFile)
    SaveButton.place(x=1200, y=635, width=70, height=37)
    #############################################

    TextFileDisplay = Text(DiagnoseWindow, width=10, height=10, font=Labelsfont, state=DISABLED)
    TextFileDisplay.place(x=1120, y=50, width=500, height=570)

    TextFileScrollBar = Scrollbar(DiagnoseWindow, orient=VERTICAL)
    TextFileDisplay.configure(yscrollcommand=TextFileScrollBar.set)
    TextFileScrollBar.configure(command=TextFileDisplay.yview)
    TextFileScrollBar.place(x=1615, y=50, height=570)

    Patient_Name_Label = ttk.Label(DiagnoseWindow, width=30, text="Name:", font=Labelsfont).grid(row=1,
                                                                                                 column=1,
                                                                                                 sticky=W)
    Patient_Name_TextBox = ttk.Entry(DiagnoseWindow, width=30, textvariable=PatientName)
    Patient_Name_TextBox.grid(row=1, column=2, sticky=W)
    Patient_Name_TextBox.focus_set()

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
    WBC_Scale = Scale(DiagnoseWindow, from_=4000, to=20000, length=800, tickinterval=800,
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

    HCT_Label = ttk.Label(DiagnoseWindow, width=30, text="Hematocrit (in %)", font=Labelsfont).grid(row=8,
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

    HDL_Label = ttk.Label(DiagnoseWindow, width=30, text="High Density Lipoprotein", font=Labelsfont).grid(row=13,
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
        nonlocal PatientGender
        nonlocal PatientsFolder
        DiagnosisFile = None
        try:
            DiagnosisFile = open(PatientsFolder + "\\" + PatientName.get() + ".txt", 'a')
        except:
            messagebox.showerror(title="Error", message="Failed to open the file\n")
        if DiagnosisFile:
            DiagnosisFile.write("\nDiagnosis:\n\n")
            Patient_age = PatientAge.get()
            PatientGender = PatientGender.get()
            wbc = WBC.get()
            neut = Neut.get()
            lymph = Lymph.get()
            rbc = float(RBC.get())
            hct = HCT.get()
            urea = Urea.get()
            hb = float(Hb.get())
            chno = float(CHNO.get())
            iron = Iron.get()
            hdl = HDL.get()
            alkaline = AlkalinePhosphatase.get()
            ################### Age 0-3  START ##################
            if 0 <= Patient_age <= 3:
                if wbc > 17500:
                    DiagnosisFile.write("High WBC(White blood cells):\n"
                                        "Usually indicated that there is an infection if there is a fever.\n"
                                        "In other rare cases, very high WBC count may indicate about blood disease or "
                                        "cancer.\n "
                                        "Recommended treatment:\n"
                                        "for infection: Specific antibiotic.\n"
                                        "for blood disease a combination of cyclophospamide and corticosurides.\n"
                                        "for cancer: Entrectinib.\n\n")
                elif wbc < 6000:
                    DiagnosisFile.write("Low WBC(White blood cells):\n"
                                        "Indicate viral disease, failure of the immune system and in extremely rare "
                                        "cases "
                                        "- cancer.\n"
                                        "Recommended treatment:\n"
                                        "for viral disease: Rest at home.\n"
                                        "for cancer: Entrectinib.\n\n")

                if neut > 54:
                    DiagnosisFile.write("High Neut(Neutrophil):\n"
                                        "Indicate usually on bacterial infection\n"
                                        "Recommended treatment:\n"
                                        "for bacterial infection: Specific antibiotic.\n")
                elif neut < 28:
                    DiagnosisFile.write("Low Neut(Neutrophil):\n"
                                        "Indicate a disturbance in blood production, tendency to infections from \n"
                                        "bacteria and in rare cases - a cancerous process.\n"
                                        "Recommended treatment:\n"
                                        "for blood production: 1 10mg pill of vitamin B12 once a day for a month and"
                                        "1 5mg pill of Folic acid once a day for a month.\n"
                                        "for infections: Specific antibiotic.\n"
                                        "for cancer: Entrectinib\n\n")

                if lymph > 52:
                    DiagnosisFile.write("High Lymph(Lymphocytes):\n"
                                        "Indicates about a problem in creating blood cells.\n"
                                        "Recommended treatment:\n"
                                        "for blood production: 1 10mg pill of vitamin B12 once a day for a month and"
                                        "1 5mg pill of Folic acid once a day for a month.\n\n")
                elif lymph < 36:
                    DiagnosisFile.write("Low Lymph(Lymphocytes):\n"
                                        "May indicate on prolonged bacterial infection, or about lymphoma cancer.\n"
                                        "Recommended treatment:\n"
                                        "for bacterial infection: Specific antibiotic.\n"
                                        "for lymphoma cancer: Entrectinib.\n\n")

                if rbc > 6:
                    DiagnosisFile.write("High RBC(Red blood cells):\n"
                                        "Could indicate on disturbance in the blood production system,\n"
                                        "high levels were also observed in smokers and in lung disease patients.\n"
                                        "Recommended treatment:\n"
                                        "for blood production: 1 10mg pill of vitamin B12 once a day for a month and"
                                        "1 5mg pill of Folic acid once a day for a month.\n\n")
                elif rbc < 4.5:
                    DiagnosisFile.write("Low RBC(Red blood cells):\n"
                                        "Could indicate on anemia or heavy bleeding.\n"
                                        "Recommended treatment:\n"
                                        "for anemia: 2 pills 10 mg each, of Vitamin B12 a day, for a month.\n"
                                        "for bleeding: Urgently evacuate to a hospital.\n\n")

                if PatientGender == "Male":
                    if hct > 54:
                        DiagnosisFile.write("High HCT(Hematocrit):\n"
                                            "Usually found in smokers.\n"
                                            "Recommended treatment:\n"
                                            "for smokers: Stop smoking.\n\n")
                    elif hct < 37:
                        DiagnosisFile.write("Low HCT(Hematocrit):\n"
                                            "Indicate mostly about bleeding or anemia.\n"
                                            "Recommended treatment:\n"
                                            "for bleeding : Urgently evacuate to a hospital.\n"
                                            "for anemia: 2 pills 10 mg each of Vitamin B12 a day, for a month.\n\n")
                elif PatientGender == "Female":
                    if hct > 47:
                        DiagnosisFile.write("High HCT(Hematocrit):\n"
                                            "Usually found in smokers.\n"
                                            "Recommended treatment:\n"
                                            "for smoking: Stop smoking.\n\n")
                    elif hct < 33:
                        DiagnosisFile.write("Low HCT(Hematocrit):\n"
                                            "Indicate mostly about bleeding or anemia.\n"
                                            "Recommended treatment:\n"
                                            "for bleeding : Urgently evacuate to a hospital.\n"
                                            "for anemia: 2 pills 10 mg each of Vitamin B12 a day, for a month.\n\n")

                if urea > 43:
                    DiagnosisFile.write("High Urea:\n"
                                        "Could indicate on kidney disease, dehydration or\n"
                                        "a high-protein diet.\n"
                                        "Recommended treatment:\n"
                                        "for kidney disease: balance sugar levels in blood.\n"
                                        "for dehydration: Complete rest lying down and returning fluids by drinking\n"
                                        "for a high-protein diet: Arrange an appointment with a nutritionist.\n\n")
                elif urea < 17:
                    DiagnosisFile.write("Low Urea:\n"
                                        "Malnutrition , a low protein diet or liver disease.\n"
                                        "It should be noted that in pregnancy the level of the infiltrator(Urea) "
                                        "decreases.\n"
                                        "Recommended treatment:\n"
                                        "for Malnutrition: Arrange an appointment with a nutritionist.\n"
                                        "for a low protein diet: Arrange an appointment with a nutritionist.\n"
                                        "for a liver disease: Referral to a specific diagnosis for the purpose of "
                                        "determining treatment.\n\n")

                if hb < 11.5:
                    DiagnosisFile.write("Low Hb(Hemoglobin):\n"
                                        "Indicative of anemia.\n"
                                        "This could be due to hematological disorder from iron deficiency and "
                                        "bleeding.\n "
                                        "Recommended treatment:\n"
                                        "for hematological disorder: Injection of a hormone to encourage red blood "
                                        "cell "
                                        "production.\n "
                                        "for bleeding: Urgently evacuate to a hospital.\n\n")

                if 0 <= Patient_age <= 2:
                    if chno > 0.5:
                        DiagnosisFile.write("High CHNO(Creatinine):\n"
                                            "May indicate a kidney problem and in severe cases kidney failure.\n"
                                            "High values can also be found during diarrhea and vomiting\n"
                                            "(Causes of increased muscle breakdown and high values of creatinine),\n"
                                            "muscle disease and increased consumption of meat.\n"
                                            "Recommended treatment:\n"
                                            "for kidney problem: balance sugar levels in blood.\n"
                                            "for muscle disease: 2 pills of 5mg each of Altman's Turmeric c3 a day, "
                                            "for a month.\n"
                                            "for increased consumption of meat: Arrange an appointment with a "
                                            "nutritionist.\n\n")
                    if chno < 0.2:
                        DiagnosisFile.write("Low CHNO(Creatinine):\n"
                                            "Most often seen in patients with very poor muscle mass and malnourished\n"
                                            "people who do not consume enough protein.\n"
                                            "Recommended treatment:\n"
                                            "for malnourished: Arrange an appointment with a nutritionist.\n"
                                            "for not enough protein: Arrange an appointment with a nutritionist.\n\n")
                elif Patient_age > 2:
                    if chno > 1:
                        DiagnosisFile.write("High CHNO(Creatinine):\n"
                                            "May indicate a kidney problem and in severe cases kidney failure.\n"
                                            "High values can also be found during diarrhea and vomiting\n"
                                            "(Causes of increased muscle breakdown and high values of creatinine),\n"
                                            "muscle disease and increased consumption of meat.\n"
                                            "Recommended treatment:\n"
                                            "for kidney problem: balance sugar levels in blood.\n"
                                            "for muscle disease: 2 pills of 5mg each of Altman's Turmeric c3 a day, "
                                            "for a month.\n"
                                            "for increased consumption of meat: Arrange an appointment with a "
                                            "nutritionist.\n\n")
                    if chno < 0.5:
                        DiagnosisFile.write("Low CHNO(Creatinine):\n"
                                            "Most often seen in patients with very poor muscle mass and malnourished\n"
                                            "people who do not consume enough protein.\n"
                                            "Recommended treatment:\n"
                                            "for malnourished: Arrange an appointment with a nutritionist.\n"
                                            "for not enough protein: Arrange an appointment with a nutritionist.\n\n")

                if PatientGender == "Male":
                    if iron > 160:
                        DiagnosisFile.write("High Iron:\n"
                                            "Could indicate iron poisoning.\n"
                                            "Recommended treatment:\n"
                                            "for iron poisoning: Evacuate to a hospital.\n\n")
                    elif iron < 60:
                        DiagnosisFile.write("Low Iron:\n"
                                            "Usually attests to an inadequate diet or an increase in iron requirement\n"
                                            "(For example, at pregnancy) or about blood loss due to bleeding.\n"
                                            "Recommended treatment:\n"
                                            "for increase in iron requirement: 2 10mg pills of Vitamin B12 for a "
                                            "month.\n "
                                            "for blood loss: Urgently evacuate to a hospital.\n\n")
                if PatientGender == "Female":
                    if iron > 160 * 0.8:
                        DiagnosisFile.write("High Iron:\n"
                                            "Could indicate iron poisoning.\n"
                                            "Recommended treatment:\n"
                                            "for iron poisoning: Evacuate to a hospital.\n\n")
                    elif iron < 60 * 0.8:
                        DiagnosisFile.write("Low Iron:\n"
                                            "Usually attests to an inadequate diet or\nan increase in iron requirement"
                                            "(For example, at pregnancy) or about blood loss due to bleeding.\n"
                                            "Recommended treatment:\n"
                                            "for increase in iron requirement: 2 10mg pills of Vitamin B12 for a "
                                            "month.\n "
                                            "for blood loss: Urgently evacuate to a hospital.\n\n")

                if PatientGender == "Male":
                    if hdl > 62:
                        DiagnosisFile.write("High HDL(High density lipoprotein):\n"
                                            "Usually harmless. Physical activity raises ""good"" cholesterol levels.\n\n")
                        #  Harmless, doesn't need treatment.
                    elif hdl < 29:
                        DiagnosisFile.write("Low HDL(High density lipoprotein):\n"
                                            "May indicate risk of heart disease, about hyperlipidemia(Hypertension in "
                                            "the "
                                            "blood) or about adult diabetes.\n"
                                            "Recommended treatment:\n"
                                            "for heart disease: Arrange an appointment with a nutritionist.\n"
                                            "for hyperlipidemia: Arrange an appointment with a nutritionist,\n"
                                            "1 5mg pill of Simovil a day for a week.\n"
                                            "for adult diabetes: Insulin adjustment for the patient.\n\n")
                elif PatientGender == "Female":
                    if hdl > 82:
                        DiagnosisFile.write("High HDL(High density lipoprotein):\n"
                                            "Usually harmless. Physical activity raises ""good"" cholesterol levels.\n")
                        #  Harmless, doesn't need treatment.
                    elif hdl < 34:
                        DiagnosisFile.write("Low HDL(High density lipoprotein):\n"
                                            "May indicate risk of heart disease, about hyperlipidemia(Hypertension in "
                                            "the "
                                            "blood) or about adult diabetes.\n"
                                            "Recommended treatment:\n"
                                            "for heart disease: Arrange an appointment with a nutritionist.\n"
                                            "for hyperlipidemia: Arrange an appointment with a nutritionist,\n"
                                            "1 5mg pill of Simovil a day for a week.\n"
                                            "for adult diabetes: Insulin adjustment for the patient.\n\n")

                if alkaline > 120:
                    DiagnosisFile.write("High Alkaline Phosphatase:\n"
                                        "Could indicate about liver disease, biliary diseases, pregnancy, "
                                        "Hyperthyroidism "
                                        "(Hyperactivity of thyroid gland) or use of various medications.\n"
                                        "Recommended treatment:\n"
                                        "for liver disease: Referral to a specific diagnosis for the purpose of "
                                        "determining treatment.\n"
                                        "for biliary diseases: Referral for surgical treatment.\n"
                                        "for Hyperthyroidism: Propylthiouracil To decrease thyroid activity.\n"
                                        "for use of various medications: Referral to the family doctor for a match "
                                        "test "
                                        "between the medications.\n\n")
                if alkaline < 60:
                    DiagnosisFile.write("Low Alkaline Phosphatase:\n"
                                        "May indicate a poor diet that lacks proteins.\n"
                                        "lack in vitamins like B12, C, B6 and folic acid.\n"
                                        "Recommended treatment:\n"
                                        "for poor diet: Arrange an appointment with a nutritionist.\n"
                                        "for lack in vitamins: Referral for a blood test to identify the missing "
                                        "vitamins.\n\n")

                ################### Age 0-3  END ##################

                ################### Age 4-17  START ##################

            elif 4 <= PatientAge.get() <= 17:
                if wbc > 15500:
                    DiagnosisFile.write("High WBC(White blood cells):\n"
                                        "Usually indicated that there is an infection if there is a fever.\n"
                                        "In other rare cases, very high WBC count may indicate about blood disease or "
                                        "cancer.\n"
                                        "Recommended treatment:\n"
                                        "for infection: Specific antibiotic.\n"
                                        "for blood disease a combination of cyclophospamide and corticosurides.\n"
                                        "for cancer: Entrectinib.\n\n")
                elif wbc < 5500:
                    DiagnosisFile.write("Low WBC(White blood cells):\n"
                                        "Indicate viral disease, failure of the immune system and in extremely rare "
                                        "cases "
                                        "- cancer.\n"
                                        "Recommended treatment:\n"
                                        "for viral disease: Rest at home.\n"
                                        "for cancer: Entrectinib.\n\n")

                if neut > 54:
                    DiagnosisFile.write("High Neut(Neutrophil):\n"
                                        "Indicate viral disease, failure of the immune system and in extremely rare "
                                        "cases "
                                        "- cancer.\n"
                                        "Recommended treatment:\n"
                                        "for bacterial infection: Specific antibiotic.\n\n")
                elif neut < 28:
                    DiagnosisFile.write("Low Neut(Neutrophil):\n"
                                        "Indicate a disturbance in blood formation of a tendency to infections from \n"
                                        "bacteria and in rare cases - a cancerous process.\n"
                                        "Recommended treatment:\n"
                                        "for blood production: 1 10mg pill of vitamin B12 once a day for a month and"
                                        "1 5mg pill of Folic acid once a day for a month.\n"
                                        "for infections: Specific antibiotic.\n"
                                        "for cancer: Entrectinib\n\n")

                if lymph > 52:
                    DiagnosisFile.write("High Lymph(Lymphocytes):\n"
                                        "Indicates about a problem in creating blood cells.\n"
                                        "Recommended treatment:\n"
                                        "for blood production: 1 10mg pill of vitamin B12 once a day for a month and"
                                        "1 5mg pill of Folic acid once a day for a month.\n\n")
                elif lymph < 36:
                    DiagnosisFile.write("Low Lymph(Lymphocytes):\n"
                                        "May indicate on prolonged bacterial infection, or about lymphoma cancer.\n"
                                        "Recommended treatment:\n"
                                        "for bacterial infection: Specific antibiotic.\n"
                                        "for lymphoma cancer: Entrectinib.\n\n")

                if rbc > 6:
                    DiagnosisFile.write("High RBC(Red blood cells):\n"
                                        "Could indicate on disturbance in the blood production system,\n"
                                        "high levels were also observed in smokers and in lung disease patients.\n"
                                        "Recommended treatment:\n"
                                        "for blood production: 1 10mg pill of vitamin B12 once a day for a month and"
                                        "1 5mg pill of Folic acid once a day for a month.\n\n")
                elif rbc < 4.5:
                    DiagnosisFile.write("Low RBC(Red blood cells):\n"
                                        "Could indicate on anemia or heavy bleeding.\n"
                                        "Recommended treatment:\n"
                                        "for anemia: 2 pills 10 mg each, of Vitamin B12 a day, for a month.\n"
                                        "for bleeding: Urgently evacuate to a hospital.\n\n")

                if PatientGender == "Male":
                    if hct > 54:
                        DiagnosisFile.write("High HCT(Hematocrit):\n"
                                            "Usually found in smokers.\n"
                                            "Recommended treatment:\n"
                                            "for smoking: Stop smoking.\n\n")
                    elif hct < 37:
                        DiagnosisFile.write("Low HCT(Hematocrit):\n"
                                            "Indicate mostly about bleeding or anemia.\n"
                                            "Recommended treatment:\n"
                                            "for bleeding : Urgently evacuate to a hospital.\n"
                                            "for anemia: 2 pills 10 mg each of Vitamin B12 a day, for a month.\n\n")
                elif PatientGender == "Female":
                    if hct > 47:
                        DiagnosisFile.write("High HCT(Hematocrit):\n"
                                            "Usually found in smokers.\n"
                                            "Recommended treatment:\n"
                                            "for smoking: Stop smoking.\n\n")
                    elif hct < 33:
                        DiagnosisFile.write("Low HCT(Hematocrit):\n"
                                            "Indicate mostly about bleeding or anemia.\n"
                                            "Recommended treatment:\n"
                                            "for bleeding : Urgently evacuate to a hospital.\n"
                                            "for anemia: 2 pills 10 mg each of Vitamin B12 a day, for a month.\n\n")

                if urea > 43:
                    DiagnosisFile.write("High Urea:\n"
                                        "Could indicate on kidney disease, dehydration or\n"
                                        "a high-protein diet.\n"
                                        "Recommended treatment:\n"
                                        "for kidney disease: balance sugar levels in blood.\n"
                                        "for dehydration: Complete rest lying down and returning fluids by drinking\n"
                                        "for a high-protein diet: Arrange an appointment with a nutritionist.\n\n")
                elif urea < 17:
                    DiagnosisFile.write("Low Urea:\n"
                                        "Malnutrition , a low protein diet or liver disease.\n"
                                        "It should be noted that in pregnancy the level of the infiltrator(Urea) "
                                        "decreases.\n"
                                        "Recommended treatment:\n"
                                        "for Malnutrition: Arrange an appointment with a nutritionist.\n"
                                        "for a low protein diet: Arrange an appointment with a nutritionist.\n"
                                        "for a liver disease: Referral to a specific diagnosis for the purpose of "
                                        "determining treatment.\n\n")

                if hb < 11.5:
                    DiagnosisFile.write("Low Hb(Hemoglobin):\n"
                                        "Indicative of anemia.\n"
                                        "This could be due to hematological disorder from iron deficiency and "
                                        "bleeding.\n"
                                        "Recommended treatment:\n"
                                        "for hematological disorder: Injection of a hormone to encourage red blood "
                                        "cell "
                                        "production.\n "
                                        "for bleeding: Urgently evacuate to a hospital.\n\n")

                if chno > 1:
                    DiagnosisFile.write("High CHNO(Creatinine):\n"
                                        "May indicate a kidney problem and in severe cases kidney failure.\n"
                                        "High values can also be found during diarrhea and vomiting\n"
                                        "(Causes of increased muscle breakdown and high values of creatinine),\n"
                                        "muscle disease and increased consumption of meat.\n"
                                        "Recommended treatment:\n"
                                        "for kidney problem: balance sugar levels in blood.\n"
                                        "for muscle disease: 2 pills of 5mg each of Altman's Turmeric c3 a day, "
                                        "for a month.\n"
                                        "for increased consumption of meat: Arrange an appointment with a "
                                        "nutritionist.\n\n")
                if chno < 0.5:
                    DiagnosisFile.write("Low CHNO(Creatinine):\n"
                                        "Most often seen in patients with very poor muscle mass and malnourished\n"
                                        "people who do not consume enough protein.\n"
                                        "Recommended treatment:\n"
                                        "for malnourished: Arrange an appointment with a nutritionist.\n"
                                        "for not enough protein: Arrange an appointment with a nutritionist.\n\n")

                if PatientGender == "Male":
                    if iron > 160:
                        DiagnosisFile.write("High Iron:\n"
                                            "Could indicate iron poisoning.\n"
                                            "Recommended treatment:\n"
                                            "for iron poisoning: Evacuate to a hospital.\n\n")
                    elif iron < 60:
                        DiagnosisFile.write("Low Iron:\n"
                                            "Usually attests to an inadequate diet or\nan increase in iron requirement"
                                            "(For example, at pregnancy) or about blood loss due to bleeding.\n"
                                            "Recommended treatment:\n"
                                            "for increase in iron requirement: 2 10mg pills of Vitamin B12 for a "
                                            "month.\n "
                                            "for blood loss: Urgently evacuate to a hospital.\n\n")
                elif PatientGender == "Female":
                    if iron > 160 * 0.8:
                        DiagnosisFile.write("High Iron:\n"
                                            "Could indicate iron poisoning.\n"
                                            "Recommended treatment:\n"
                                            "for iron poisoning: Evacuate to a hospital.\n\n")
                    elif iron < 60 * 0.8:
                        DiagnosisFile.write("Low Iron:\n"
                                            "Usually attests to an inadequate diet or\nan increase in iron requirement"
                                            "(For example, at pregnancy) or about blood loss due to bleeding.\n"
                                            "Recommended treatment:\n"
                                            "for increase in iron requirement: 2 10mg pills of Vitamin B12 for a "
                                            "month.\n "
                                            "for blood loss: Urgently evacuate to a hospital.\n\n")

                if PatientGender == "Male":
                    if hdl > 62:
                        DiagnosisFile.write("High HDL(High density lipoprotein):\n"
                                            "Usually harmless. Physical activity raises ""good"" cholesterol levels.\n\n")
                        #  Harmless, doesn't need treatment.
                    elif hdl < 29:
                        DiagnosisFile.write("Low HDL(High density lipoprotein):\n"
                                            "May indicate risk of heart disease, about hyperlipidemia(Hypertension in "
                                            "the "
                                            "blood) or about adult diabetes.\n"
                                            "Recommended treatment:\n"
                                            "for heart disease: Arrange an appointment with a nutritionist.\n"
                                            "for hyperlipidemia: Arrange an appointment with a nutritionist,\n"
                                            "1 5mg pill of Simovil a day for a week.\n"
                                            "for adult diabetes: Insulin adjustment for the patient.\n\n")
                elif PatientGender == "Female":
                    if hdl > 82:
                        DiagnosisFile.write("High HDL(High density lipoprotein):\n"
                                            "Usually harmless. Physical activity raises ""good"" cholesterol levels.\n\n")
                        #  Harmless, doesn't need treatment.
                    elif hdl < 34:
                        DiagnosisFile.write("Low HDL(High density lipoprotein):\n"
                                            "May indicate risk of heart disease, about hyperlipidemia(Hypertension in "
                                            "the "
                                            "blood) or about adult diabetes.\n"
                                            "Recommended treatment:\n"
                                            "for heart disease: Arrange an appointment with a nutritionist.\n"
                                            "for hyperlipidemia: Arrange an appointment with a nutritionist,\n"
                                            "1 5mg pill of Simovil a day for a week.\n"
                                            "for adult diabetes: Insulin adjustment for the patient.\n\n")

                if alkaline > 120:
                    DiagnosisFile.write("High Alkaline Phosphatase:\n"
                                        "Could indicate about liver disease, biliary diseases, pregnancy, "
                                        "Hyperthyroidism "
                                        "(Hyperactivity of thyroid gland) or use of various medications.\n"
                                        "Recommended treatment:\n"
                                        "for liver disease: Referral to a specific diagnosis for the purpose of "
                                        "determining treatment.\n"
                                        "for biliary diseases: Referral for surgical treatment.\n"
                                        "for Hyperthyroidism: Propylthiouracil To decrease thyroid activity.\n"
                                        "for use of various medications: Referral to the family doctor for a match "
                                        "test "
                                        "between the medications.\n\n")
                elif alkaline < 60:
                    DiagnosisFile.write("Low Alkaline Phosphatase:\n"
                                        "May indicate a poor diet that lacks proteins.\n"
                                        "lack in vitamins like B12, C, B6 and folic acid.\n"
                                        "Recommended treatment:\n"
                                        "for poor diet: Arrange an appointment with a nutritionist.\n"
                                        "for lack in vitamins: Referral for a blood test to identify the missing "
                                        "vitamins.\n\n")

                    ################### Age 4-17  END ##################

                    ################### Age 18+  START ##################

            if PatientAge.get() >= 18:
                if wbc > 11000:
                    DiagnosisFile.write("High WBC(White blood cells):\n"
                                        "Usually indicated that there is an infection if there is a fever.\n"
                                        "In other rare cases, very high WBC count may indicate about blood disease or "
                                        "cancer.\n"
                                        "Recommended treatment:\n"
                                        "for infection: Specific antibiotic.\n"
                                        "for blood disease a combination of cyclophospamide and corticosurides.\n"
                                        "for cancer: Entrectinib.\n\n")
                elif wbc < 4500:
                    DiagnosisFile.write("Low WBC(White blood cells):\n"
                                        "Indicate viral disease, failure of the immune system and in extremely rare "
                                        "cases "
                                        "- cancer.\n"
                                        "Recommended treatment:\n"
                                        "for viral disease: Rest at home.\n"
                                        "for cancer: Entrectinib.\n\n")

                if neut > 54:
                    DiagnosisFile.write("High Neut(Neutrophil):\n"
                                        "Indicate viral disease, failure of the immune system and in extremely rare "
                                        "cases "
                                        "- cancer.\n"
                                        "Recommended treatment:\n"
                                        "for bacterial infection: Specific antibiotic.\n\n")
                elif neut < 28:
                    DiagnosisFile.write("Low Neut(Neutrophil):\n"
                                        "Indicate a disturbance in blood formation of a tendency to infections from \n"
                                        "bacteria and in rare cases - a cancerous process.\n"
                                        "Recommended treatment:\n"
                                        "for blood production: 1 10mg pill of vitamin B12 once a day for a month and"
                                        "1 5mg pill of Folic acid once a day for a month.\n"
                                        "for infections: Specific antibiotic.\n"
                                        "for cancer: Entrectinib\n\n")

                if lymph > 52:
                    DiagnosisFile.write("High Lymph(Lymphocytes):\n"
                                        "Indicates about a problem in creating blood cells.\n"
                                        "Recommended treatment:\n"
                                        "for blood production: 1 10mg pill of vitamin B12 once a day for a month and"
                                        "1 5mg pill of Folic acid once a day for a month.\n\n")
                elif lymph < 36:
                    DiagnosisFile.write("Low Lymph(Lymphocytes):\n"
                                        "May indicate on prolonged bacterial infection, or about lymphoma cancer.\n"
                                        "Recommended treatment:\n"
                                        "for bacterial infection: Specific antibiotic.\n"
                                        "for lymphoma cancer: Entrectinib.\n\n")

                if rbc > 6:
                    DiagnosisFile.write("High RBC(Red blood cells):\n"
                                        "Could indicate on disturbance in the blood production system,\n"
                                        "high levels were also observed in smokers and in lung disease patients.\n"
                                        "Recommended treatment:\n"
                                        "for blood production: 1 10mg pill of vitamin B12 once a day for a month and"
                                        "1 5mg pill of Folic acid once a day for a month.\n\n")
                elif rbc < 4.5:
                    DiagnosisFile.write("Low RBC(Red blood cells):\n"
                                        "Could indicate on anemia or heavy bleeding.\n"
                                        "Recommended treatment:\n"
                                        "for anemia: 2 pills 10 mg each, of Vitamin B12 a day, for a month.\n"
                                        "for bleeding: Urgently evacuate to a hospital.\n\n")

                if PatientGender == "Male":
                    if hct > 54:
                        DiagnosisFile.write("High HCT(Hematocrit):\n"
                                            "Usually found in smokers.\n"
                                            "Recommended treatment:\n"
                                            "for smoking: Stop smoking.\n\n")
                    elif hct < 37:
                        DiagnosisFile.write("Low HCT(Hematocrit):\n"
                                            "Indicate mostly about bleeding or anemia.\n"
                                            "Recommended treatment:\n"
                                            "for bleeding : Urgently evacuate to a hospital.\n"
                                            "for anemia: 2 pills 10 mg each of Vitamin B12 a day, for a month.\n\n")
                elif PatientGender == "Female":
                    if hct > 47:
                        DiagnosisFile.write("High HCT(Hematocrit):\n"
                                            "Usually found in smokers.\n"
                                            "Recommended treatment:\n"
                                            "for smoking: Stop smoking.\n\n")
                    elif hct < 33:
                        DiagnosisFile.write("Low HCT(Hematocrit):\n"
                                            "Indicate mostly about bleeding or anemia.\n"
                                            "Recommended treatment:\n"
                                            "for bleeding : Urgently evacuate to a hospital.\n"
                                            "for anemia: 2 pills 10 mg each of Vitamin B12 a day, for a month.\n\n")

                if urea > 43:
                    DiagnosisFile.write("High Urea:\n"
                                        "Could indicate on kidney disease, dehydration or\n"
                                        "a high-protein diet.\n"
                                        "Recommended treatment:\n"
                                        "for kidney disease: balance sugar levels in blood.\n"
                                        "for dehydration: Complete rest lying down and returning fluids by drinking\n"
                                        "for a high-protein diet: Arrange an appointment with a nutritionist.\n\n")
                elif urea < 17:
                    DiagnosisFile.write("Low Urea:\n"
                                        "Malnutrition , a low protein diet or liver disease.\n"
                                        "It should be noted that in pregnancy the level of the infiltrator(Urea) "
                                        "decreases.\n"
                                        "Recommended treatment:\n"
                                        "for Malnutrition: Arrange an appointment with a nutritionist.\n"
                                        "for a low protein diet: Arrange an appointment with a nutritionist.\n"
                                        "for a liver disease: Referral to a specific diagnosis for the purpose of "
                                        "determining treatment.\n\n")

                if PatientGender == "Male":
                    if hb < 12:
                        DiagnosisFile.write("Low Hb(Hemoglobin):\n"
                                            "Indicative of anemia.\n"
                                            "This could be due to hematological disorder from iron deficiency and "
                                            "bleeding.\n"
                                            "Recommended treatment:\n"
                                            "for hematological disorder: Injection of a hormone to encourage red blood "
                                            "cell production.\n "
                                            "for bleeding: Urgently evacuate to a hospital.\n\n")
                elif PatientGender == "Female":
                    if hb < 12:
                        DiagnosisFile.write("Low Hb(Hemoglobin):\n"
                                            "Indicative of anemia.\n"
                                            "This could be due to hematological disorder from iron deficiency and "
                                            "bleeding.\n"
                                            "Recommended treatment:\n"
                                            "for hematological disorder: Injection of a hormone to encourage red blood "
                                            "cell production.\n"
                                            "for bleeding: Urgently evacuate to a hospital.\n\n")

                if 18 <= PatientAge.get() <= 59:
                    if chno > 1:
                        DiagnosisFile.write("High CHNO(Creatinine):\n"
                                            "May indicate a kidney problem and in severe cases kidney failure.\n"
                                            "High values can also be found during diarrhea and vomiting\n"
                                            "(Causes of increased muscle breakdown and high values of "
                                            "creatinine),\n "
                                            "muscle disease and increased consumption of meat.\n"
                                            "Recommended treatment:\n"
                                            "for kidney problem: balance sugar levels in blood.\n"
                                            "for muscle disease: 2 pills of 5mg each of Altman's Turmeric c3 a day, "
                                            "for a month.\n"
                                            "for increased consumption of meat: Arrange an appointment with a "
                                            "nutritionist.\n\n")
                    if chno < 0.6:
                        DiagnosisFile.write("Low CHNO(Creatinine):\n"
                                            "Most often seen in patients with very poor muscle mass and "
                                            "malnourished\n"
                                            "people who do not consume enough protein.\n"
                                            "Recommended treatment:\n"
                                            "for malnourished: Arrange an appointment with a nutritionist.\n"
                                            "for not enough protein: Arrange an appointment with a nutritionist.\n\n")
                elif PatientAge.get() >= 60:
                    if chno > 1.2:
                        DiagnosisFile.write("High CHNO(Creatinine):\n"
                                            "May indicate a kidney problem and in severe cases kidney failure.\n"
                                            "High values can also be found during diarrhea and vomiting\n"
                                            "(Causes of increased muscle breakdown and high values of creatinine),\n"
                                            "muscle disease and increased consumption of meat.\n"
                                            "Recommended treatment:\n"
                                            "for kidney problem: balance sugar levels in blood.\n"
                                            "for muscle disease: 2 pills of 5mg each of Altman's Turmeric c3 a day, "
                                            "for a month.\n"
                                            "for increased consumption of meat: Arrange an appointment with a "
                                            "nutritionist.\n\n")
                    if chno < 0.6:
                        DiagnosisFile.write("Low CHNO(Creatinine):\n"
                                            "Most often seen in patients with very poor muscle mass and malnourished\n"
                                            "people who do not consume enough protein.\n"
                                            "Recommended treatment:\n"
                                            "for malnourished: Arrange an appointment with a nutritionist.\n"
                                            "for not enough protein: Arrange an appointment with a nutritionist.\n\n")

                if PatientGender == "Male":
                    if iron > 160:
                        DiagnosisFile.write("High Iron:\n"
                                            "Could indicate iron poisoning.\n"
                                            "Recommended treatment:\n"
                                            "for iron poisoning: Evacuate to a hospital.\n\n")
                    elif iron < 60:
                        DiagnosisFile.write("Low Iron:\n"
                                            "Usually attests to an inadequate diet or an increase in iron requirement"
                                            "(For example, at pregnancy) or about blood loss due to bleeding.\n"
                                            "Recommended treatment:\n"
                                            "for increase in iron requirement: 2 10mg pills of Vitamin B12 for a "
                                            "month.\n "
                                            "for blood loss: Urgently evacuate to a hospital.\n\n")
                elif PatientGender == "Female":
                    if iron > 160 * 0.8:
                        DiagnosisFile.write("High Iron:\n"
                                            "Could indicate iron poisoning.\n"
                                            "Recommended treatment:\n"
                                            "for iron poisoning: Evacuate to a hospital.\n\n")
                    elif iron < 60 * 0.8:
                        DiagnosisFile.write("Low Iron:\n"
                                            "Usually attests to an inadequate diet or an increase in iron requirement"
                                            "(For example, at pregnancy) or about blood loss due to bleeding.\n"
                                            "Recommended treatment:\n"
                                            "for increase in iron requirement: 2 10mg pills of Vitamin B12 for a "
                                            "month.\n "
                                            "for blood loss: Urgently evacuate to a hospital.\n\n")

                if PatientGender == "Male":
                    if hdl > 62:
                        DiagnosisFile.write("High HDL(High density lipoprotein):\n"
                                            "Usually harmless. Physical activity raises ""good"" cholesterol levels.\n\n")
                    elif hdl < 29:
                        DiagnosisFile.write("Low HDL(High density lipoprotein):\n"
                                            "May indicate risk of heart disease, about hyperlipidemia(Hypertension in "
                                            "the "
                                            "blood) or about adult diabetes.\n"
                                            "Recommended treatment:\n"
                                            "for heart disease: Arrange an appointment with a nutritionist.\n"
                                            "for hyperlipidemia: Arrange an appointment with a nutritionist,\n"
                                            "1 5mg pill of Simovil a day for a week.\n"
                                            "for adult diabetes: Insulin adjustment for the patient.\n\n")
                elif PatientGender == "Female":
                    if hdl > 82:
                        DiagnosisFile.write("High HDL(High density lipoprotein):\n"
                                            "Usually harmless. Physical activity raises 'good' cholesterol "
                                            "levels.\n\n")
                        #  Harmless, doesn't need treatment.
                    elif hdl < 34:

                        DiagnosisFile.write("Low HDL(High density lipoprotein):\n"
                                            "May indicate risk of heart disease, about hyperlipidemia(Hypertension in "
                                            "the "
                                            "blood) or about adult diabetes.\n"
                                            "Recommended treatment:\n"
                                            "for heart disease: Arrange an appointment with a nutritionist.\n"
                                            "for hyperlipidemia: Arrange an appointment with a nutritionist,\n"
                                            "1 5mg pill of Simovil a day for a week.\n"
                                            "for adult diabetes: Insulin adjustment for the patient.\n\n")

                if alkaline > 120:
                    DiagnosisFile.write("High Alkaline Phosphatase:\n"
                                        "Could indicate about liver disease, biliary diseases, pregnancy, "
                                        "Hyperthyroidism "
                                        "(Hyperactivity of thyroid gland) or use of various medications.\n"
                                        "Recommended treatment:\n"
                                        "for liver disease: Referral to a specific diagnosis for the purpose of "
                                        "determining treatment.\n"
                                        "for biliary diseases: Referral for surgical treatment.\n"
                                        "for Hyperthyroidism: Propylthiouracil To decrease thyroid activity.\n"
                                        "for use of various medications: Referral to the family doctor for a match "
                                        "test "
                                        "between the medications.\n\n")
                elif alkaline < 60:
                    DiagnosisFile.write("Low Alkaline Phosphatase:\n"
                                        "May indicate a poor diet that lacks proteins.\n"
                                        "lack in vitamins like B12, C, B6 and folic acid.\n"
                                        "Recommended treatment:\n"
                                        "for poor diet: Arrange an appointment with a nutritionist.\n"
                                        "for lack in vitamins: Referral for a blood test to identify the missing "
                                        "vitamins.\n\n")

            DiagnosisFile.close()
            messagebox.showinfo("Diagnose Done!", "Diagnose Done!\n File created!")
            OpenDiagnoseFile(PatientName.get())

    DiagnoseWindow.mainloop()
