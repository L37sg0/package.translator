from googletrans import Translator
from os import listdir, mkdir
import re
#import json

translator = Translator()
dest = "bg"
basedir = "/home/reghack/Desktop/vtesource/vtenext19ce/modules"
targetdir = "/home/reghack/Desktop/package.translator/modules"
n = listdir(targetdir)
list_of_dirs = listdir(basedir)

regex = "=>\'(.+?)\',"

def translate_line(regex, line, dest):
    m = re.search(regex, line)
    if m:
        phrase = translator.translate(m.group(1), dest)
        phrase = phrase.text.capitalize()
        newline = line.replace(m.group(0),"=>'"+phrase+"',")
        return(newline)

def write_new_file(file_text, dirpath):
    try:
        mkdir("modules")
    except:
        print("Directory already created.")
    try:
        mkdir("modules/"+dirpath)
    except:
        print("Directory already created.")
    try:
        mkdir("modules/"+dirpath+"/language")
    except:
        print("Directory already created.")

    with open("modules/"+dirpath+"/language/bg_bg.lang.php","w") as wf:
        wf.write(file_text)


def write_new_line(line, dirpath):
    try:
        mkdir("modules")
    except:
        print("Directory already created.")
    try:
        mkdir("modules/"+dirpath)
    except:
        print("Directory already created.")
    try:
        mkdir("modules/"+dirpath+"/language")
    except:
        print("Directory already created.")

    print("Writing to: modules/"+dirpath+"/language/bg_bg.lang.php")

    with open("modules/"+dirpath+"/language/bg_bg.lang.php","a") as wf:
        wf.write(line)

    print("Done.")


def read_file(filepath,dirpath):
    with open(filepath,"r") as fp:
        line = fp.readline()
        newtext = ""
        cnt = 0
        while line:
            #translator = Translator()
            translated_line = translate_line(regex, line, dest)
            if translated_line:
                #print(translated_line)
                write_new_line(translated_line, dirpath)
                #newtext = newtext + translated_line
            else:
                #print(line)
                write_new_line(line, dirpath)
                #newtext = newtext + line
            cnt += 1
            line = fp.readline()
        #return(newtext)

def iterate_over_directories(basedir, list_of_dirs):
    for directory in list_of_dirs[len(n)-1:]:
        filepath = basedir+"/"+directory + "/language/en_us.lang.php"
        dirpath = directory #+ "/language"
        #print(filepath)

        print("Translating from: "+filepath)
        newtext = read_file(filepath,dirpath)
        print("Done.")

        """ print("Writing to: modules/"+dirpath+"/language/bg_bg.lang.php")
        #write_new_file(newtext, dirpath)
        print("Done.") """

#read_file(filepath)

#print(list_of_dirs)
iterate_over_directories(basedir, list_of_dirs)
#print(len(n)-1)