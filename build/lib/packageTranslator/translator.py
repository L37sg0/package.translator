""" 
+---------------------------------------------------------------------------------------------------+
|       Translator for language packs or other dictionary files sorted in multiple directories,     |
|   that need to be half-translated fast. Uses googletrans library as translating engine.           |
+---------------------------------------------------------------------------------------------------+
|   Workflow:                                                                                       |
|       1. Define source and target directories.                                                    |
|       2. Define regex string if used.                                                             |
|       3. Define in what language to be translated target file, source language is auto-detected.  |
|       4. Read source file and store matched regex strings into json dictionary.                   |
|       5. Chunk json dictionary into pieces and translate it chunk by chunk.                       |
|       6. Store translated json into new json file.                                                |
|       7. Read source file line by line.                                                           |
|       8. Match regexes and replace them with translated values.                                   |
|       9. Store the newly generated file into target.                                              |
+---------------------------------------------------------------------------------------------------+
"""

from googletrans import Translator                          # Import translator engine object
from os import listdir, mkdir                               # Needed for work with directories
import re                                                   # Needed for work with regex strings
import random                                               # Needed for random choice of google domains
import json                                                 # Needed for work with json files, that are
                                                            # used as temporary and failure storage
class PackageTranslator:
    def __init__(self):
        self.translator = Translator()                                  # Define new Translator engine
        self.dest = "bg"                                                # Define the end translation language
        self.sourcedir = "/home/reghack/Desktop/vtesource/vtenext19ce/modules" 
                                                                        # Define global source directory
        self.targetdir = "/home/reghack/Desktop/package.translator/modules"
                                                                        # Define global target directory
        self.list_of_dirs = listdir(self.sourcedir)                     # Define list of all subdirectories in source directory.

        self.regex = "=>\'(.+?)\',"                                     # Define "regex" to search with.

        self.target_counter = len(listdir(self.targetdir))              # "target_counter" is used to count progress in target directory
                                                                        # in o.w. count how much subdirectories are created

        #self.service_urls = self.get_from_json("service_urls.json")     # Get list of googletrans domains
""" 
    def target_directory(dirpath):                              # Method for creating target directory.
        try:
            mkdir("modules")                                    # Create global target directory if doen's exists.
        except:
            print("Directory already created.")
        try:
            mkdir("modules/"+dirpath)                           # Create target subdirectory if doen's exists.
        except:
            print("Directory already created.")
        dirpath = "modules/"+dirpath
        try:
            mkdir("modules/"+dirpath+"/language")               # Create target sub-subdirectory if doen's exists.
        except:
            print("Directory already created.")
        dirpath = dirpath+"/language/bg_bg.lang.php"            # Define path to target file.
        return(dirpath)                                         # Return path to target file.


    def write_new_line(line, dirpath):                          # Method for writing new line to target file.

        dirpath = target_directory(dirpath)
        print("Writing to: "+dirpath)

        with open("modules/"+dirpath+"/language/bg_bg.lang.php","a") as wf:
            wf.write(line)

        print("Done.")

    def chunker(data,number):                                   # Method for chunking lists on given number
        data = [data[x:x+number] for x in range(0, len(data), number)]
        return(data)

    def read_and_match(filepath, regex):                        # Method for reading file from source directory
                                                                # and matching regexes.
        with open(filepath,"r") as fp:
            line = fp.readline()
            words = []                                          # Empty list that stores all matched words.
            while line:
                match_word = re.search(regex, line)             # Matching words in line sorted by regex.
                if match_word:
                    words.append(match_word.group(1))           # Appending mathched word into storage.
                line = fp.readline()                            # Read next line.
            return(words)                                       # Return storage as list.
            
    def write_translated(source, regex, dirpath, jsonfile):     # Method that reads source and translated json, matches regex,
                                                                # replaces regex with its translated value and writes
                                                                # end result to target file.
        translated = get_from_json(jsonfile)                    # Convert given json file to list of lists with translated words.
        translated = [item for sublist in translated for item in sublist]
                                                                # Convert list of lists to list
        i = 0                                                   # Iterator to loop on translated words.
        with open(source,"r") as source:                        # Read source file.
            line = source.readline()                            # line by line.
            while line:
                match_word = re.search(regex, line)             # Match regex in source.
                if match_word:
                    line = line.replace(match_word, translated[i])
                                                                # Replace matched word with translated value.
                    write_new_line(line, dirpath)               # Write new translated line to target.
                    i += 1                                      # Load next translated value.
                else:                                           # If no match word.
                    write_new_line(line, dirpath)               # copy line from source to target.
                line = source.readline()                        # Read next line.

    def store_as_json(data,filename):                           # Meself.thod for storing data as a json file.
        data = json.dumps(data)
        with open(filename, "w") as fn:
            fn.write(data)

    def get_from_json(self,filename):                          # Method for retrieving data from json file.
        with open(filename, "r") as fn:
            data = fn.read()
            data = json.loads(data)
        return(data)

    def translate_data(chunks):                                 # Method for translating chunks(list of lists) data.
        translated_chunks = []                                  # Storage for the translated chunks.
        for chunk in chunks:
            try:
                translated_chunk = translator.translate(chunk, dest)
                                                                # Translate single chunk of data(100 words or phrases).
            except:                                             # If error occurres -> change translator-engine domain provider.
                new_service_url = random.choice(service_urls)
                translator.service_urls = new_service_url
                print("Error occurred. Search domain changed to: ", new_service_url)
                translated_chunk = translator.translate(chunk, dest)

            translated_chunks.append(translated_chunk)          # Append translated chunk into storage.
        return(translated_chunks)                               # Return translated storage of data.


    def iterate_over_directories(sourcedir, list_of_dirs):      # Method for iterating over source directories and create targets.
        for directory in list_of_dirs[target_counter-1:target_counter]:
            filepath = sourcedir+"/"+directory + "/language/en_us.lang.php"
            dirpath = directory

            #print("Translating from: "+filepath)
            newtext = read_file(filepath,dirpath)
            #print("Done.")

            #print("Writing to: modules/"+dirpath+"/language/bg_bg.lang.php")
            #write_new_file(newtext, dirpath)
            #print("Done.")


#iterate_over_directories(sourcedir, list_of_dirs) """
print(PackageTranslator().list_of_dirs)