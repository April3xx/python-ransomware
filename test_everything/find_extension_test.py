import os

class filelist():

    def __init__(self,encoding='utf-8'):
        """
        parameters:
            encoding : file encoding scheme default utf-8
            dest: path to write file if not specify an absolute path it will create filename at running directory
            rewrite: if true rewrite the given destination file if destination file is not given create "dirlist.txt" in running directory
        """
        self.filecount = 0
        self.encoding = encoding
    
    def generatedirlist(self):
        """
        generate a to z and call findext every loop from a to z
        using drives parameter
        """
        for i in range(65,65+26):
            self.findext(chr(i)+":")
        
    def findext(self,drives):
        """

        """
        print(drives)

        with open("dirlist.txt",'w',encoding=self.encoding) as f:
            for _,_,files in os.walk(drives):
                for name in files:
                    if '.' in name:
                        name = name[name.rfind('.'):]
                        f.write(name+"\n")
                        self.filecount +=1
                    else:
                        f.write(name+'\n')
                        self.filecount += 1
            f.write(str(self.filecount))

if __name__ == "__main__":
    attk = filelist()
    attk.findext('C:\\')
#test()
#findext()