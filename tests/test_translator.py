from unittest import TestCase
from nose.tools import assert_list_equal, assert_equal
from packageTranslator.translator import PackageTranslator
from packageTranslator.dictmaker import DictionaryMaker


class TestTargetDirectorCreatory(TestCase):
    """     
    def test_target_directory(self):
        dirpath = "Accounts"
        result = PackageTranslator().target_directory(dirpath)
        assert_equal("modules/Accounts/language/bg_bg.lang.php", result)

    def test_target_counter(self):
        result = PackageTranslator().target_counter
        assert_equal(25, result)

    def test_chunker(self):
        testlist = ["a","b","c","d"]
        result = PackageTranslator().chunker(testlist,2)
        assert_list_equal([["a","b"],["c","d"]], result)

    def test_store_and_get_as_json(self):
        testdata = [["a","b"],["c","d"]]
        testfilename = "tests/test.json"
        PackageTranslator().store_as_json(testdata,testfilename)
        result = PackageTranslator().get_from_json("tests/test.json")
        assert_list_equal(testdata, result)

    def test_read_and_match(self):
        testregex = "=>\'(.+?)\',"
        testfilename = "tests/test.source.php"
        testlist = ['Сметки','Сметки: начало']
        result = PackageTranslator().read_and_match(testfilename, testregex)
        assert_list_equal(testlist, result)

    def test_write_translated_and_write_new_line(self):
        testsource = "tests/test.source.php"
        testregex = "=>\'(.+?)\',"
        testtarget = "tests/test.target.php"
        testjsonfile = "tests/test.translated.json"
        PackageTranslator().write_translated(testsource,testregex,testtarget,testjsonfile)
        result = PackageTranslator().read_and_match(testtarget, testregex)
        testlist = ['Здравей','Свят']
        assert_list_equal(testlist, result) """
    """ 
    def test_translate_data(self):
        testdest = "bg"                                                         # Define dest
        testregex = "=>\'(.+?)\',"                                              # Define regex
        testsource = "/home/reghack/Desktop/vtesource/vtenext19ce/modules/Settings/language/en_us.lang.php"
                                                                                # Define source file
        testtarget = "tests/bg_bg.lang.php"
        testenstore = "tests/en.chunks.json"                                    # Define json store for source
        testbgstore = "tests/bg.chunks.json"                                    # Define json store for target
        #testlist = PackageTranslator().read_and_match(testsource, testregex)    # Read source and match regex
        #testlist = PackageTranslator().chunker(testlist,25)                    # Chunk matched list in sublists of 25
        #PackageTranslator().store_as_json(testlist,testenstore)                 # Store matched list as json
        testlist = PackageTranslator().get_from_json(testenstore)               # Read json store for source    
        #testtranslated = PackageTranslator().translate_data(testlist[0], testdest)
        #PackageTranslator().store_as_json(testtranslated, testbgstore)
        PackageTranslator().translate_chunks(testlist, testdest, testbgstore) """

    def test_dict_maker(self):
        regex = "=>\'(.+?)\',"
        source = "/home/reghack/Desktop/vtesource/vtenext19ce/include/language/en_us.lang.php"
        maker = DictionaryMaker()
        data = maker.read_and_match(source, regex)
        maker.store_as_json(data,"tests/bigdic.json")