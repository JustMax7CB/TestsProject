import os
from tkinter import *
from tkinter import ttk, messagebox
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
        Smoker = askquestion(title='Smoking?', message='Does the Patient Smoking?')
        return Smoker

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
    FilePath = r"C:\Users\Sman9\Desktop\TestsProject\Patients"
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

    Smoker = Smoking()


    Labelsfont = ("Lato", 13)

    ############################################

    def GenerateTextFile(name):
        PatientName = name
        DiagnosisFile = open(FilePath + "\\" + PatientName + ".txt", 'w')
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
        DiagnosisFile = open(FilePath + "\\" + PatientName.get() + ".txt", 'a')
        DiagnosisFile.write("\nDiagnosis:\n\n")

        ################### Age 0-3  START ##################
        if 0 <= PatientAge.get() <= 3:
            if WBC.get() > 17500:
                DiagnosisFile.write("High WBC(White blood cells):\n"
                                    "Usually indicated that there is an infection if there is a fever.\n"
                                    "In other rare cases, very high WBC count may indicate about blood disease or "
                                    "cancer.\n "
                                    "Recommended treatment:\n"
                                    "for infection: Specific antibiotic.\n"
                                    "for blood disease a combination of cyclophospamide and corticosurides.\n"
                                    "for cancer: Entrectinib.\n\n")
            elif WBC.get() < 6000:
                DiagnosisFile.write("Low WBC(White blood cells):\n"
                                    "Indicate viral disease, failure of the immune system and in extremely rare cases "
                                    "- cancer.\n"
                                    "Recommended treatment:\n"
                                    "for viral disease: Rest at home.\n"
                                    "for cancer: Entrectinib.\n\n")

            if Neut.get() > 54:
                DiagnosisFile.write("High Neut(Neutrophil):\n"
                                    "Indicate usually on bacterial infection\n"
                                    "Recommended treatment:\n"
                                    "for bacterial infection: Specific antibiotic.\n")
            elif Neut.get() < 28:
                DiagnosisFile.write("Low Neut(Neutrophil):\n"
                                    "Indicate a disturbance in blood production, tendency to infections from \n"
                                    "bacteria and in rare cases - a cancerous process.\n"
                                    "Recommended treatment:\n"
                                    "for blood production: 1 10mg pill of vitamin B12 once a day for a month and"
                                    "1 5mg pill of Folic acid once a day for a month.\n"
                                    "for infections: Specific antibiotic.\n"
                                    "for cancer: Entrectinib\n\n")

            if Lymph.get() > 52:
                DiagnosisFile.write("High Lymph(Lymphocytes):\n"
                                    "Indicates about a problem in creating blood cells.\n\n")
            elif Lymph.get() < 36:
                DiagnosisFile.write("Low Lymph(Lymphocytes):\n"
                                    "May indicate on prolonged bacterial infection, or about lymphoma cancer.\n\n")

            if float(RBC.get()) > 6:
                DiagnosisFile.write("High RBC(Red blood cells):\n"
                                    "Could indicate on disturbance in the blood production system,\n"
                                    "high levels were also observed in smokers and in lung disease patients.\n\n")
            elif float(RBC.get()) < 4.5:
                DiagnosisFile.write("Low RBC(Red blood cells):\n"
                                    "Could indicate on anemia or heavy bleeding.\n"
                                    "Recommended treatment:\n"
                                    "for anemia: 2 pills 10 mg each, of Vitamin B12 a day, for a month.\n"
                                    "for bleeding: Urgently evacuate to a hospital.\n\n")

            if PatientGender == "Male":
                if HCT.get() > 54:
                    DiagnosisFile.write("High HCT(Hematocrit):\n"
                                        "Usually found in smokers.\n"
                                        "Recommended treatment:\n"
                                        "for smokers: Stop smoking.")
                elif HCT.get() < 37:
                    DiagnosisFile.write("Low HCT(Hematocrit):\n"
                                        "Indicate mostly about bleeding or anemia.\n\n")
            elif PatientGender == "Female":
                if HCT.get() > 47:
                    DiagnosisFile.write("High HCT(Hematocrit):\n"
                                        "Usually found in smokers.\n\n")
                elif HCT.get() < 33:
                    DiagnosisFile.write("Low HCT(Hematocrit):\n"
                                        "Indicate mostly about bleeding or anemia.\n\n")

            if Urea.get() > 43:
                DiagnosisFile.write("High Urea:\n"
                                    "Could indicate on kidney disease, dehydration or\n"
                                    "a high-protein diet.\n\n")
            elif Urea.get() < 17:
                DiagnosisFile.write("Low Urea:\n"
                                    "Malnutrition , a low protein diet or liver disease.\n"
                                    "It should be noted that in pregnancy the level of the infiltrator(Urea) "
                                    "decreases.\n\n")

            if float(Hb.get()) < 11.5:
                DiagnosisFile.write("Low Hb(Hemoglobin):\n"
                                    "Indicative of anemia.\n"
                                    "This could be due to hematological disorder from iron deficiency and bleeding.\n\n")

            if 0 <= PatientAge.get() <= 2:
                if float(CHNO.get()) > 0.5:
                    DiagnosisFile.write("High CHNO(Creatinine):\n"
                                        "May indicate a kidney problem and in severe cases kidney failure.\n"
                                        "High values can also be found during diarrhea and vomiting\n"
                                        "(Causes of increased muscle breakdown and high values of creatinine),\n"
                                        "muscle disease and increased consumption of meat.\n\n")
                if float(CHNO.get()) < 0.2:
                    DiagnosisFile.write("Low CHNO(Creatinine):\n"
                                        "Most often seen in patients with very poor muscle mass and malnourished\n"
                                        "people who do not consume enough protein.\n\n")
            elif PatientAge.get() > 2:
                if float(CHNO.get()) > 1:
                    DiagnosisFile.write("High CHNO(Creatinine):\n"
                                        "May indicate a kidney problem and in severe cases kidney failure.\n"
                                        "High values can also be found during diarrhea and vomiting\n"
                                        "(Causes of increased muscle breakdown and high values of creatinine),\n"
                                        "muscle disease and increased consumption of meat.\n\n")
                if float(CHNO.get()) < 0.5:
                    DiagnosisFile.write("Low CHNO(Creatinine):\n"
                                        "Most often seen in patients with very poor muscle mass and malnourished\n"
                                        "people who do not consume enough protein.\n\n")

            if PatientGender == "Male":
                if Iron.get() > 160:
                    DiagnosisFile.write("High Iron:\n"
                                        "Could indicate iron poisoning.\n\n")
                elif Iron.get() < 60:
                    DiagnosisFile.write("Low Iron:\n"
                                        "Usually attests to an inadequate diet or\nan increase in iron requirement"
                                        "(For example, at pregnancy) or about blood loss due to bleeding.\n\n")
            if PatientGender == "Female":
                if Iron.get() > 160 * 0.8:
                    DiagnosisFile.write("High Iron:\n"
                                        "Could indicate iron poisoning.\n\n")
                elif Iron.get() < 60 * 0.8:
                    DiagnosisFile.write("Low Iron:\n"
                                        "Usually attests to an inadequate diet or\nan increase in iron requirement"
                                        "(For example, at pregnancy) or about blood loss due to bleeding.\n\n")

            if PatientGender == "Male":
                if HDL.get() > 62:
                    DiagnosisFile.write("High HDL(High density lipoprotein):\n"
                                        "Usually harmless. Physical activity raises ""good"" cholesterol levels.\n\n")
                elif HDL.get() < 29:
                    DiagnosisFile.write("Low HDL(High density lipoprotein):\n"
                                        "May indicate risk of heart disease, about hyperlipidemia(Hypertension in the "
                                        "blood) or about adult diabetes.\n\n")
            elif PatientGender == "Female":
                if HDL.get() > 82:
                    DiagnosisFile.write("High HDL(High density lipoprotein):\n"
                                        "Usually harmless. Physical activity raises ""good"" cholesterol levels.\n")
                elif HDL.get() < 34:
                    DiagnosisFile.write("Low HDL(High density lipoprotein):\n"
                                        "May indicate risk of heart disease, about hyperlipidemia(Hypertension in the "
                                        "blood) or about adult diabetes.\n\n")

            if AlkalinePhosphatase.get() > 120:
                DiagnosisFile.write("High Alkaline Phosphatase:\n"
                                    "Could indicate about liver disease, biliary diseases, pregnancy, Hyperthyroidism"
                                    "(Hyperactivity of thyroid gland) or use of various medications.\n\n")
            if AlkalinePhosphatase.get() < 60:
                DiagnosisFile.write("Low Alkaline Phosphatase:\n"
                                    "May indicate a poor diet that lacks proteins.\n"
                                    "lack in vitamins like B12, C, B6 and folic acid.\n\n")

            ################### Age 0-3  END ##################

            ################### Age 4-17  START ##################

        elif 4 <= PatientAge.get() <= 17:
            if WBC.get() > 15500:
                DiagnosisFile.write("High WBC(White blood cells):\n"
                                    "Usually indicated that there is an infection if there is a fever.\n"
                                    "In other rare cases, very high WBC count may indicate about blood disease or cancer.\n\n")
            elif WBC.get() < 5500:
                DiagnosisFile.write("Low WBC(White blood cells):\n"
                                    "Indicate viral disease, failure of the immune system and in extremely rare cases "
                                    "- cancer.\n\n")

            if Neut.get() > 54:
                DiagnosisFile.write("High Neut(Neutrophil):\n"
                                    "Indicate viral disease, failure of the immune system and in extremely rare cases "
                                    "- cancer.\n\n")
            elif Neut.get() < 28:
                DiagnosisFile.write("Low Neut(Neutrophil):\n"
                                    "Indicate a disturbance in blood formation of a tendency to infections from \n"
                                    "bacteria and in rare cases - a cancerous process.\n\n")

            if Lymph.get() > 52:
                DiagnosisFile.write("High Lymph(Lymphocytes):\n"
                                    "Indicates about a problem in creating blood cells.\n\n")
            elif Lymph.get() < 36:
                DiagnosisFile.write("Low Lymph(Lymphocytes):\n"
                                    "May indicate on prolonged bacterial infection, or about lymphoma cancer.\n\n")

            if float(RBC.get()) > 6:
                DiagnosisFile.write("High RBC(Red blood cells):\n"
                                    "Could indicate on disturbance in the blood production system,\n"
                                    "high levels were also observed in smokers and in lung disease patients.\n\n")
            elif float(RBC.get()) < 4.5:
                DiagnosisFile.write("Low RBC(Red blood cells):\n"
                                    "Could indicate on anemia or heavy bleeding.\n\n")

            if PatientGender == "Male":
                if HCT.get() > 54:
                    DiagnosisFile.write("High HCT(Hematocrit):\n"
                                        "Usually found in smokers.\n\n")
                elif HCT.get() < 37:
                    DiagnosisFile.write("Low HCT(Hematocrit):\n"
                                        "Indicate mostly about bleeding or anemia.\n\n")
            elif PatientGender == "Female":
                if HCT.get() > 47:
                    DiagnosisFile.write("High HCT(Hematocrit):\n"
                                        "Usually found in smokers.\n\n")
                elif HCT.get() < 33:
                    DiagnosisFile.write("Low HCT(Hematocrit):\n"
                                        "Indicate mostly about bleeding or anemia.\n\n")

            if Urea.get() > 43:
                DiagnosisFile.write("High Urea:\n"
                                    "Could indicate on kidney disease, dehydration or\n"
                                    "a high-protein diet.\n\n")
            elif Urea.get() < 17:
                DiagnosisFile.write("Low Urea:\n"
                                    "Malnutrition , alow protein diet or liver disease.\n"
                                    "It should be noted that in pregnancy the level of the infiltrator(Urea) "
                                    "decreases.\n\n")

            if float(Hb.get()) < 11.5:
                DiagnosisFile.write("Low Hb(Hemoglobin):\n"
                                    "Indicative of anemia.\n"
                                    "This could be due to hematological disorder from iron deficiency and "
                                    "bleeding.\n\n")

            if float(CHNO.get()) > 1:
                DiagnosisFile.write("High CHNO(Creatinine):\n"
                                    "May indicate a kidney problem and in severe cases kidney failure.\n"
                                    "High values can also be found during diarrhea and vomiting\n"
                                    "(Causes of increased muscle breakdown and high values of creatinine),\n"
                                    "muscle disease and increased consumption of meat.\n\n")
            if float(CHNO.get()) < 0.5:
                DiagnosisFile.write("Low CHNO(Creatinine):\n"
                                    "Most often seen in patients with very poor muscle mass and malnourished\n"
                                    "people who do not consume enough protein.\n\n")

            if PatientGender == "Male":
                if Iron.get() > 160:
                    DiagnosisFile.write("High Iron:\n"
                                        "Could indicate iron poisoning.\n\n")
                elif Iron.get() < 60:
                    DiagnosisFile.write("Low Iron:\n"
                                        "Usually attests to an inadequate diet or\nan increase in iron requirement"
                                        "(For example, at pregnancy) or about blood loss due to bleeding.\n\n")
            if PatientGender == "Female":
                if Iron.get() > 160 * 0.8:
                    DiagnosisFile.write("High Iron:\n"
                                        "Could indicate iron poisoning.\n\n")
                elif Iron.get() < 60 * 0.8:
                    DiagnosisFile.write("Low Iron:\n"
                                        "Usually attests to an inadequate diet or\nan increase in iron requirement"
                                        "(For example, at pregnancy) or about blood loss due to bleeding.\n\n")

            if PatientGender == "Male":
                if HDL.get() > 62:
                    DiagnosisFile.write("High HDL(High density lipoprotein):\n"
                                        "Usually harmless. Physical activity raises ""good"" cholesterol levels.\n\n")
                elif HDL.get() < 29:
                    DiagnosisFile.write("Low HDL(High density lipoprotein):\n"
                                        "May indicate risk of heart disease, about hyperlipidemia(Hypertension in the "
                                        "blood) or about adult diabetes.\n\n")
            elif PatientGender == "Female":
                if HDL.get() > 82:
                    DiagnosisFile.write("High HDL(High density lipoprotein):\n"
                                        "Usually harmless. Physical activity raises ""good"" cholesterol levels.\n\n")
                elif HDL.get() < 34:
                    DiagnosisFile.write("Low HDL(High density lipoprotein):\n"
                                        "May indicate risk of heart disease, about hyperlipidemia(Hypertension in the "
                                        "blood) or about adult diabetes.\n\n")

            if AlkalinePhosphatase.get() > 120:
                DiagnosisFile.write("High Alkaline Phosphatase:\n"
                                    "Could indicate about liver disease, biliary diseases, pregnancy, Hyperthyroidism"
                                    "(Hyperactivity of thyroid gland) or use of various medications.\n\n")
            if AlkalinePhosphatase.get() < 60:
                DiagnosisFile.write("Low Alkaline Phosphatase:\n"
                                    "May indicate a poor diet that lacks proteins.\n"
                                    "lack in vitamins like B12, C, B6 and folic acid.\n\n")

                ################### Age 4-17  END ##################

                ################### Age 18+  START ##################

        if PatientAge.get() >= 18:
            if WBC.get() > 11000:
                DiagnosisFile.write("High WBC(White blood cells):\n"
                                    "Usually indicated that there is an infection if there is a fever.\n"
                                    "In other rare cases, very high WBC count may indicate about blood disease or cancer.\n\n")
            elif WBC.get() < 4500:
                DiagnosisFile.write("Low WBC(White blood cells):\n"
                                    "Indicate viral disease, failure of the immune system and in extremely rare cases "
                                    "- cancer.\n\n")

            if Neut.get() > 54:
                DiagnosisFile.write("High Neut(Neutrophil):\n"
                                    "Indicate viral disease, failure of the immune system and in extremely rare cases "
                                    "- cancer.\n\n")
            elif Neut.get() < 28:
                DiagnosisFile.write("Low Neut(Neutrophil):\n"
                                    "Indicate a disturbance in blood formation of a tendency to infections from \n"
                                    "bacteria and in rare cases - a cancerous process.\n\n")

            if Lymph.get() > 52:
                DiagnosisFile.write("High Lymph(Lymphocytes):\n"
                                    "Indicates about a problem in creating blood cells.\n\n")
            elif Lymph.get() < 36:
                DiagnosisFile.write("Low Lymph(Lymphocytes):\n"
                                    "May indicate on prolonged bacterial infection, or about lymphoma cancer.\n\n")

            if float(RBC.get()) > 6:
                DiagnosisFile.write("High RBC(Red blood cells):\n"
                                    "Could indicate on disturbance in the blood production system,\n"
                                    "high levels were also observed in smokers and in lung disease patients.\n\n")
            elif float(RBC.get()) < 4.5:
                DiagnosisFile.write("Low RBC(Red blood cells):\n"
                                    "Could indicate on anemia or heavy bleeding.\n\n")

            if PatientGender == "Male":
                if HCT.get() > 54:
                    DiagnosisFile.write("High HCT(Hematocrit):\n"
                                        "Usually found in smokers.\n\n")
                elif HCT.get() < 37:
                    DiagnosisFile.write("Low HCT(Hematocrit):\n"
                                        "Indicate mostly about bleeding or anemia.\n\n")
            elif PatientGender == "Female":
                if HCT.get() > 47:
                    DiagnosisFile.write("High HCT(Hematocrit):\n"
                                        "Usually found in smokers.\n\n")
                elif HCT.get() < 33:
                    DiagnosisFile.write("Low HCT(Hematocrit):\n"
                                        "Indicate mostly about bleeding or anemia.\n\n")

            if Urea.get() > 43:
                DiagnosisFile.write("High Urea:\n"
                                    "Could indicate on kidney disease, dehydration or\n"
                                    "a high-protein diet.\n\n")
            elif Urea.get() < 17:
                DiagnosisFile.write("Low Urea:\n"
                                    "Malnutrition , alow protein diet or liver disease.\n"
                                    "It should be noted that in pregnancy the level of the infiltrator(Urea) "
                                    "decreases.\n\n")

            if PatientGender == "Male":
                if float(Hb.get()) < 12:
                    DiagnosisFile.write("Low Hb(Hemoglobin):\n"
                                        "Indicative of anemia.\n"
                                        "This could be due to hematological disorder from iron deficiency and "
                                        "bleeding.\n\n")
            elif PatientGender == "Female":
                if float(Hb.get()) < 12:
                    DiagnosisFile.write("Low Hb(Hemoglobin):\n"
                                        "Indicative of anemia.\n"
                                        "This could be due to hematological disorder from iron deficiency and "
                                        "bleeding.\n\n")
            if 18 <= PatientAge.get() <= 59:
                if float(CHNO.get()) > 1:
                    DiagnosisFile.write("High CHNO(Creatinine):\n"
                                        "May indicate a kidney problem and in severe cases kidney failure.\n"
                                        "High values can also be found during diarrhea and vomiting\n"
                                        "(Causes of increased muscle breakdown and high values of "
                                        "creatinine),\n "
                                        "muscle disease and increased consumption of meat.\n\n")
                if float(CHNO.get()) < 0.6:
                    DiagnosisFile.write("Low CHNO(Creatinine):\n"
                                        "Most often seen in patients with very poor muscle mass and "
                                        "malnourished\n "
                                        "people who do not consume enough protein.\n\n")
            elif PatientAge.get() >= 60:
                if float(CHNO.get()) > 1.2:
                    DiagnosisFile.write("High CHNO(Creatinine):\n"
                                        "May indicate a kidney problem and in severe cases kidney failure.\n"
                                        "High values can also be found during diarrhea and vomiting\n"
                                        "(Causes of increased muscle breakdown and high values of creatinine),\n"
                                        "muscle disease and increased consumption of meat.\n\n")
                if float(CHNO.get()) < 0.6:
                    DiagnosisFile.write("Low CHNO(Creatinine):\n"
                                        "Most often seen in patients with very poor muscle mass and malnourished\n"
                                        "people who do not consume enough protein.\n\n")

            if PatientGender == "Male":
                if Iron.get() > 160:
                    DiagnosisFile.write("High Iron:\n"
                                        "Could indicate iron poisoning.\n\n")
                elif Iron.get() < 60:
                    DiagnosisFile.write("Low Iron:\n"
                                        "Usually attests to an inadequate diet or\nan increase in iron requirement"
                                        "(For example, at pregnancy) or about blood loss due to bleeding.\n\n")
            if PatientGender == "Female":
                if Iron.get() > 160 * 0.8:
                    DiagnosisFile.write("High Iron:\n"
                                        "Could indicate iron poisoning.\n\n")
                elif Iron.get() < 60 * 0.8:
                    DiagnosisFile.write("Low Iron:\n"
                                        "Usually attests to an inadequate diet or\nan increase in iron requirement"
                                        "(For example, at pregnancy) or about blood loss due to bleeding.\n\n")

            if PatientGender == "Male":
                if HDL.get() > 62:
                    DiagnosisFile.write("High HDL(High density lipoprotein):\n"
                                        "Usually harmless. Physical activity raises ""good"" cholesterol levels.\n\n")
                elif HDL.get() < 29:
                    DiagnosisFile.write("Low HDL(High density lipoprotein):\n"
                                        "May indicate risk of heart disease, about hyperlipidemia(Hypertension in the "
                                        "blood) or about adult diabetes.\\nn")
            elif PatientGender == "Female":
                if HDL.get() > 82:
                    DiagnosisFile.write("High HDL(High density lipoprotein):\n"
                                        "Usually harmless. Physical activity raises ""good"" cholesterol levels.\n\n")
                elif HDL.get() < 34:
                    DiagnosisFile.write("Low HDL(High density lipoprotein):\n"
                                        "May indicate risk of heart disease, about hyperlipidemia(Hypertension in the "
                                        "blood) or about adult diabetes.\n\n")

            if AlkalinePhosphatase.get() > 120:
                DiagnosisFile.write("High Alkaline Phosphatase:\n"
                                    "Could indicate about liver disease, biliary diseases, pregnancy, Hyperthyroidism"
                                    "(Hyperactivity of thyroid gland) or use of various medications.\n\n")
            if AlkalinePhosphatase.get() < 60:
                DiagnosisFile.write("Low Alkaline Phosphatase:\n"
                                    "May indicate a poor diet that lacks proteins.\n"
                                    "lack in vitamins like B12, C, B6 and folic acid.\n\n")

        DiagnosisFile.close()
        messagebox.showinfo("Diagnose Done!", "Diagnose Done!\n File created!")

    DiagnoseWindow.mainloop()
