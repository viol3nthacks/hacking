# Demonstration of the zipfile function and cracking implimentation
# You will need a dictionary.txt file and zip file to crack
# MULTI THREADED APPLICATION VERSION

import zipfile
from threading import Thread

def extractFile(zFile, password):
    try:
        zFile.extractall(pwd=password)
        print '[+] Password = ' + password + '\n'
    except:
        pass
def main():
    zFile = zipfile.ZipFile('evil.zip')
    passFile = open('dictionary.txt')
    for line in passFile.readlines():
        password = line.strip('\n')
        t = Thread(target=extractFile, args=(zFile, password))
        t.start()
if __name__ == '__main__':
    main()
