import requests
from bs4 import BeautifulSoup
import hashlib
import sys
import os
######################### Getting users passworlist > encode to md5 and add to p_list[] #########################
def pass_encode():
    p_list = []
    my_dir = os.getcwd()
    with open(my_dir + "/pass_list.txt", "w") as out:
        for d in soup:
            out.write(str(d))
    out.close()

    with open(my_dir + "/pass_list.txt", "r") as out:
        for x in out:
            h = x.replace("\r", "").replace("\n", "")
            r = hashlib.md5(h.encode())
            p_list.append(r.hexdigest()+" -> "+x)
    out.close()
    return list(p_list)
######################### user input #########################
try:
    URL = sys.argv[1]
except:
    print("Wrong passwords file")
    URL = str(input("Type here URL for passwords file "))
   
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html.parser')
hashes_list = pass_encode()
######################### cracking md5 hash or string #########################
user_input = str(input("""Please type here your md5 hash or string that you want to crack
Type "s" if you want to exit.
Type your choice :   """))
print("Your choice is -> " + user_input + "\n\r")
if user_input == "s":
    print("Thanks for using md5_rainbow_v2")
else:
    for p in hashes_list:
        if user_input in p:
            print(p)







