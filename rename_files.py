#!/usr/local/bin/python

import os

path = input('In which folder do you want change files. ')

os.chdir(path)

def current_format():
    for file in os.listdir(path):
        print(file)

def new_format():
    for file in os.listdir(path):
        f_name, f_ext = os.path.splitext(file)
        f_title = " ".join(f_name.split('-')[-2:])
        f_course = "".join(f_name.split('-')[:-4]).strip()
        new_name = '{}-{}{}'.format(f_title, f_course, f_ext)
        os.rename(file, new_name)

if __name__ == "__main__":
    print("Current filename format: ")
    current_format()
    ans = input('''
    Do you want rename files 
     ''')
    if ans.lower() == 'y':
        new_format()
    else:
        pass
    print('''-----
        New format
        -----''')
    current_format()















