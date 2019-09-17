# python-automated-tester
Usage:
```
python testSuite.py [ARGUMENTS]
usage: testSuite.py [-h] [--files files [files...]]
Test web pages for a specific string  
optional arguments:
 -h, --help            show this help message and exit       
 --files files [files ...], -f files [files...]
        Space-separated list of files
```

If no argument is provided, the script just exits.

The tests.json file contains examples for the following cases:

* Testing a site over HTTP
* Testing a site over HTTPS
* Testing a site for a string that doesn't exist
* Testing a non-existent site over HTTP
* Testing a non-existent site over HTTPS
