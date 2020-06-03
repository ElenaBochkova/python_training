import random
import string
import os
import getopt
import sys
import jsonpickle
from model.contact import Contact

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    print(err)
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix+"".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_number(maxlen):
    symbols = string.digits + "(" + ")" + "+" + "-" + " "
    return "".join([random.choice(symbols) for i in range (random.randrange(maxlen))])

def random_email(prefix, maxlen1, maxlen2):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    first = "".join([random.choice(symbols) for i in range(random.randrange(maxlen1))])
    second = "".join([random.choice(symbols) for i in range(random.randrange(maxlen2))])
    return prefix + first + "@" + second

testdata = [Contact(
    firstname=random_string("firstname", 10),
    lastname=random_string("lastname", 10),
    nickname=random_string("nickname", 10),
    home_phone=random_number(10),
    mobile_phone=random_number(10),
    work_phone=random_number(10),
    secondary_phone=random_number(10),
    email1=random_email("email1", 10,5),
    email2=random_email("email2", 10,5),
    email3=random_email("email3", 10,5),
    address=random_string("address", 20))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)
with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))