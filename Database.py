from openpyxl import *

DoctorDB = load_workbook(filename='Doctor.xlsx', data_only=True) # Doctors Database with username and passwords
MainSheet = DoctorDB['Users']
