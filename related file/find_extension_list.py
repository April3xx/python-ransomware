import os
from os.path import expanduser

class filelist():

    def __init__(self,rewrite = False,dest=None,encoding='utf-8'):
        """
        parameters:
            encoding : file encoding scheme default utf-8
            dest: path to write file if not specify an absolute path it will create filename at running directory
            rewrite: if true rewrite the given destination file if destination file is not given create "dirlist.txt" in running directory
        """
        self.filecount = 0
        if not rewrite:
            self.rewrite = False
        else:
            self.rewrite = True

        self.dest = dest
        self.encoding = encoding
    
    def generatedirlist(self):
        """
        generate a to z and call findext every loop from a to z
        using drives parameter
        """
        for i in range(65,65+26):
            self.findext(chr(i)+":\\")

        
    def findext(self,drives):
        """

        """
        print(drives)
        if self.dest is None:
            with open("dirlist.txt",'w',encoding=self.encoding) as f:
                if self.rewrite == True:
                    f.seek(0)
                    f.truncate()
                for root,_,files in os.walk(drives):
                    for name in files:
                            path = os.path.join(root,name)
                            f.write(path+"\n")
                            self.filecount += 1
                f.write(str(self.filecount))
        else:
            with open(self.dest,'w',encoding=self.encoding) as f:
                if self.rewrite == True:
                    f.seek(0)
                    f.truncate()
                for root,_,files in os.walk(drives):
                    for name in files:
                            path = os.path.join(root,name)
                            f.write(path+"\n")
                            self.filecount += 1
                f.write(str(self.filecount))
            

    def extest(self):
        with open("test.txt",'w') as f:
            f.seek(0)
            f.truncate()
            for i in range(100):
                f.writelines(str(i)+"\n")

    def test(self):
        linecount=0
        with open("testnum",'w') as f:
            for i in range(489067):
                f.write(str(i)+'\n')
                linecount+=1
            f.write(str(linecount))

attk = filelist()
attk.generatedirlist()
#test()
#findext()