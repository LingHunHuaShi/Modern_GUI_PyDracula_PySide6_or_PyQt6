import sys
import os
from cx_Freeze import setup, Executable

# ADD FILES
files = ['icon.ico','themes/']

# TARGET
target = Executable(
    script="main.py",
    base="Win32GUI",
    icon="icon.ico"
)

# SETUP CX FREEZE
setup(
    name = "学生个人课表管理系统",
    version = "1.0",
    description = "none",
    author = "zzzzzh",
    options = {'build_exe' : {'include_files' : files}},
    executables = [target]
    
)
