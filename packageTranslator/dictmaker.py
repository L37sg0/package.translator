import re
import json
from os import listdir, mkdir


class DictionaryMaker:
    def __init__(self):
        self.sourcedir = "/home/reghack/Desktop/abc.work/apps/vtesource/vtenext19ce/modules" 
        #self.source_file = "/home/reghack/Desktop/abc.work/apps/vtesource/vtenext19ce/include/language/en_us.lang.php" 
        self.dictionary = "/home/reghack/Desktop/package.translator/tests/dictionary-worked/bigdic7.json"
        self.targetdir = "/home/reghack/Desktop/bg/"
        #self.target_file = "/home/reghack/Desktop/bg/include/language/bg_bg.lang.php"
        self.regex = "=>\'(.+?)\',"
        self.regex_key = "\'(.+?)\'=>\'"

    def read_and_match(self, filename):                         # Read file match regex and return list of all matches
        with open(filename,"r") as fn:
            line = fn.readline()
            #words = []     
            pair = {}                                     # Empty dict that stores all matched words.
            while line:
                match_key = re.search(self.regex_key, line)
                match_word = re.search(self.regex, line)             # Matching words in line sorted by regex.
                if match_word:
                    pair[match_key.group(1)] = match_word.group(1)
                    #words.append(match_key.group(1))           # Appending mathched word into storage.
                line = fn.readline()                          # Read next line.
            #return(words) 
            return(pair)   

    def store_as_json(self,data,filename):                      # Method for storing data as a json file.
            data = json.dumps(data)
            with open(filename, "w") as fn:
                fn.write(data)

    def get_from_json(self,filename):                           # Method for retrieving data from json file.
        with open(filename, "r") as fn:
            data = fn.read()
            data = json.loads(data)
        return(data)

    def iterate_over_dirs(self):                                    # Iterate over targetdir 
                                                                    # and add all matches in subdictionary
        sourcelist = listdir(self.sourcedir)
        data = set()
        for directory in sourcelist:
            filename = self.sourcedir+"/"+directory+"/language/en_us.lang.php"
            try:
                result = set(self.read_and_match(filename))
                data = data.union(result)
            except EnvironmentError as error:
                print(error)
        data = list(data)
        self.store_as_json(data, self.dictionary)

    def write_translated(self,source, regex, target, dictionary):# Method that reads source and dictionary, matches regex,
                                                                # replaces regex with its translated value and writes
                                                                # end result to target file.
        dictionary = self.get_from_json(dictionary)             
        with open(source,"r") as source:                        # Read source file.
            line = source.readline()                            # line by line.
            while line:
                match_word = re.search(regex, line)             # Match regex in source.
                if match_word:
                    key = match_word.group(1)
                    line = line.replace(match_word.group(0), "=>'"+dictionary[key]+"',")
                                                                # Replace matched word with translated value.
                    self.write_new_line(line, target)          # Write new translated line to target.
                else:                                           # If no match word.
                    self.write_new_line(line, target)          # copy line from source to target.
                line = source.readline()                        # Read next line.
# Tested
    def write_new_line(self,line, target):                     # Method for writing new line to target file.

        print("Writing to: "+target)

        with open(target,"a") as target:
            target.write(line)

        print("Done.")
# Tested

    def create_target_directory(self, dirpath):
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
        filepath = "modules/"+dirpath+"/language/bg_bg.lang.php"            # Define path to target file.
        return(filepath)                                         # Return path to target file.
    # Tested

    def iterate_and_translate(self):
        dictionary = self.dictionary
        sourcelist = listdir(self.sourcedir)
        for directory in sourcelist:
            source_file = self.sourcedir+"/"+directory+"/language/en_us.lang.php"
            target_file = self.create_target_directory(directory)
            print(target_file)
            try:
                self.write_translated(source_file, self.regex, target_file, dictionary)
            except EnvironmentError as error:
                print(error)


    def translate_dictionary(self):                                 # Open source, target and
                                                                    # translate dictionary
        #sourcelist = listdir(self.sourcedir)
        targetlist = listdir(self.targetdir)
        #data = set()
        source_result = {}
        target_result = {}
        dictionary = []
        for target in targetlist:
            source_file = self.sourcedir+"/"+target+"/language/en_us.lang.php"
            target_file = self.targetdir+"/"+target+"/language/bg_bg.lang.php"
            try:
                source_result.update(self.read_and_match(source_file))
                target_result.update(self.read_and_match(target_file))
            except EnvironmentError as error:
                print(error)
        #source_result = [item for sublist in source_result for item in sublist]
        #target_result = [item for sublist in target_result for item in sublist]
        #result = set(zip(source_result, target_result))
        #result = list(result)

        #result = zip(source_result, target_result)
        #for (s, t) in result:
        for item in source_result:
            #key = item.keys()
            data = {}
            try:
                data["en"] = source_result[item]
                data["bg"] = target_result[item]
                dictionary.append(data)
            except EnvironmentError as error:
                print(error)
        #dictionary = list(set(dictionary))
        self.store_as_json(dictionary, self.dictionary)



test = DictionaryMaker()
#source_file = test.source_file
#regex = test.regex
#target_file = test.target_file
#dictionary = test.dictionary
#test.write_translated(source_file, regex, target_file, dictionary)
test.iterate_and_translate()
#test.iterate_over_dirs()
#test.translate_dictionary()
#filename = "/home/reghack/Desktop/vtesource/vtenext19ce/modules/Accounts/language/en_us.lang.php"
#res = test.read_and_match(filename)
#print(res)





