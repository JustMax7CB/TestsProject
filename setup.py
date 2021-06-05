import sys, os

from cx_Freeze import setup, Executable

includefiles = ['Doctor.xlsx']
includes = []
excludes = []
packages = ['tkinter', 'openpyxl']
build_exe_options = {'includes': includes, 'packages': packages, 'excludes': excludes, 'include_files': includefiles}

base = None
if sys.platform == 'win64':
    base = 'Win64GUI'
elif sys.platform == 'win32':
    base = 'Win32GUI'

exe = Executable(
    script="Main.py",
    target_name="AutoDoctor",
    base=base,
    icon="C:\\Users\Sman9\Desktop\TestsProject\RobotDoctor.ico",

    )

setup(
    name="AutoDoctor",
    version="0.1",
    description="Program to diagnose blood results and generate a matching treatment.",
    options={'build_exe': build_exe_options},
    executables=[exe]
    )
