#!/usr/local/bin/python

import os

path = input('In which folder do you want change files?>>> ')

os.chdir(path)


def new_format():
    for file in os.listdir(path):
        fprint = []
        f_name, f_ext = os.path.splitext(file)
        f_title = "-".join(f_name.split('-')[-2:])
        f_course = " ".join(f_name.split('-')[:-2]).strip()
        new_name = '{}--{}{}'.format(f_title, f_course, f_ext)
        print(new_name)
        

if __name__ == "__main__":
    new_format()















