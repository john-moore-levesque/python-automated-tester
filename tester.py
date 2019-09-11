"""
This class should never be used directly - always use testSuite.py
"""
from collections import OrderedDict
from pagecheck import PageCheck


class Tester():
    """
    Tester class
    name = name of the test (should be the name of the site)
    pages = pages on the site to test
    """
    def __init__(self, name, pages):
        self.name = name
        self.results = OrderedDict()
        for key, val in pages.items():
            _testPage = PageCheck(address=val['address'], ssl=val['ssl'], testString=val['testString'])
            self.results[key] = _testPage

    def outputTestResults(self):
        for test, result in self.results.items():
            print("%s (%s): %s" %(test, result.address, result.testStatus))
