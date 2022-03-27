"""
In this Python challenge, you need to write a function that accepts an encoded string as a parameter. 
This string will contain a first name, last name, and an id.

Values in the string can be separated by any number of zeros. The id is a numeric value but will contain no zeros. 
The function should parse the string and return a Python dictionary that contains the first name, last name, and id values.

An example input would be "Robert000Smith000123". The function should return the following using that input:

{ "first_name": "Robert", "last_name": "Smith", "id": "123" }
"""

import re

def parse_encoded_string(string):
    d_dict = {}
    res = re.sub(r'[0]+', '/', string).split('/')
    d_dict['first_name'], d_dict['last_name'], d_dict['id'] = res[0], res[1], res[2]
    return d_dict
