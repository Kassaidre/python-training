import string
import random
from model.contact import Contact
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 2
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a



def random_string(prefix, maxlen):
        symbols = string.ascii_letters + " "*10
        return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_string_digits(prefix, maxlen):
        symbols = string.digits
        return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname="", lastname="")] + [
        Contact(firstname=random_string("firstname", 5), lastname=random_string("lastname", 5),
                home=random_string_digits("", 10), work=random_string_digits("", 10), mobile=random_string_digits("", 10))
        for i in range(2)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))