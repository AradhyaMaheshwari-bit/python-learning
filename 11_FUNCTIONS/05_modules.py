# Built in Module
# List of all built in modules: https://docs.python.org/3/py-modindex.html
import math
print(math.sqrt(16))


# External Modules
# User Defined and Third Party modules
'''
User Defined: user creates on its convenience
Third Party: user imports someone else's code
'''

import os
os.abort

import mymodule
mymodule.hello()

import requests
r = requests.get("https://www.google.com")
print(r.text)
