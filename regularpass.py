import re

def val_pass(p):
    if (len(p)<6 or len(p)>16):
        print("Not Valid Password")
    elif not re.search("[a-z]",p):
        print("Not Valid Password due to absence of [a-z]")
    elif not re.search("[0-9]",p):
        print("Not Valid Password")
    elif not re.search("[A-Z]",p):
        print("Not Valid Password")
    elif not re.search("[$#@]",p):
        print("Not Valid Password")
    else:
        print("Valid Password")

passwd=raw_input("Enter the password : ");
val_pass(passwd);
    
