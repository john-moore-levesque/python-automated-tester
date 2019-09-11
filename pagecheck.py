"""
This class should never be used directly - always use testSuite.py
"""
import bs4
import httplib2


class PageCheck():
    """
    PageCheck class
    address = address to check
    ssl = True (if SSL is enabled; this is the default - used to add "http"
        or "https" to address if necessary)
    testString = string to search for in the page text
    """
    def __init__(self, address, ssl=True, testString=None):

        self.address = address.strip()
        if "http" not in self.address:
            if ssl:
                self.address = "https://%s" %(self.address)
            else:
                self.address = "http://%s" %(self.address)
        self.http = httplib2.Http()
        self.testString = testString
        self.testStatus = None
        try:
            """
            If self.status and self.response, go ahead and get the "body" part
                of the page and do runCheck
            """
            self.status, self.response = self.http.request(self.address,
                                                            redirections=0)
            self.page = bs4.BeautifulSoup(self.response,
                                            parse_only=bs4.SoupStrainer("body"),
                                            features="html.parser").text
        except TimeoutError:
            """
            If there's a timeout error, indicate that in the response and
                testStatus
            We want to do this instead of just setting self.testStatus to False
                because we can't even run the test to see if the string is
                on the page
            """
            self.status, self.response, self.page, self.testStatus = False, "Timeout Error", False, "Timeout Error"

        self.runCheck()


    def runCheck(self):
        """
        If self.page is a bool, then there was a timeout error
        Otherwise, set self.testStatus to True/False, depending on whether
        or not testString appears in the page text
        """
        if type(self.page) is bool:
            self.testStatus = "Timeout Error"
        elif self.testString in self.page:
            self.testStatus = True
        else:
            self.testStatus = False
