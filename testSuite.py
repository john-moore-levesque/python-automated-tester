from tester import Tester
from json import load
from argparse import ArgumentParser


def createTester(name, jpages):
    """
    Create a single Tester
    """
    def _validatePage(page):
        """
        Confirm that each item in the JSON dictionary is of the correct format
            for creating a PageCheck object
        """
        if type(page) is not dict:
            print("Wrong type")
            return False
        if len(page) is not 3:
            print("Wrong length")
            return False
        if 'address' not in page.keys():
            print("No key address")
            return False
        if 'ssl' not in page.keys():
            print("No key ssl")
            return False
        if 'testString' not in page.keys():
            print("No key test string")
            return False

        address = page['address']
        ssl = page['ssl']
        testString = page['testString']
        if type(address) is not str:
            print("Address is not string")
            return False
        if type(ssl) is not bool:
            print("SSL is not bool")
            return False
        if type(testString) is not str:
            print("testString is not string")
            return False
        return True

    pages = {}
    for key, val in jpages.items():
        if _validatePage(val):
            pages[key] = val

    return Tester(name, pages)


def createTesters(infile):
    """
    Create a list of Testers from an input file
    The assumption is that the input file is:
    - A JSON file
    - The primary key is the name of a group of tests (e.g., the name of a site)
    - Each sub-element consists of correctly formatted entries for creating a
        PageCheck object
    """
    testers = []
    with open(infile, 'r') as jfile:
        jdata = load(jfile)
        for testName, testData in jdata.items():
            testers.append(createTester(testName, testData))
    return testers


def displayTestResults(testers):
    """
    Display the test results from a list of testers
    """
    if type(testers) is not list:
        return False
    if not len(testers):
        return False
    for tester in testers:
        if type(tester) is not Tester:
            return False
        else:
            print("/-------------/")
            print("%s" %(tester.name))
            tester.outputTestResults()
            print("\n")


def interface(**args):
    """
    Simple user interface
    """
    parser = ArgumentParser(description="Test web pages for a specific string")
    parser.add_argument("--files", "-f", metavar="files", nargs="+",
                        help="Space-separated list of files")
    args = parser.parse_args()
    if args.files:
        for file in args.files:
            testers = createTesters(file)
            for tester in testers:
                print("%s" %(tester.name))
                tester.outputTestResults()
                print("\n")
    else:
        return False


if __name__ == "__main__":
    interface()
