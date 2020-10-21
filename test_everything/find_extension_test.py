import os

class filelist():

    def __init__(self,ext,opfile,encoding,overwrite):
        """
        parameters:
            encoding:   file encoding scheme default utf-8
            opfile:     path to write output-file
                        default: create "dirlist.txt" at running directory
            ext:        list extension or fullpath? 
                        default: extension
        """

        self.filecount = 0
        self.encoding = encoding
        self.opfile = opfile
        if ext is None:
            self.ext = False
        else:
            self.ext = ext
        if opfile is None:
            self.opfile = "dirlist.txt"
        else:
            self.opfile = opfile
        if encoding is None:
            self.encoding = "utf-8"
        else:
            self.encoding = encoding
        if overwrite is None:
            self.overwrite = True
        else: overwrite = False

    def run(self):
        self.generatedrivelist()

    def generatedrivelist(self):
        """
        generate a to z and call extlist every loop from a to z
        using drives parameter
        """
        for i in range(65,65+26):
            try:
                if(self.ext):
                    self.extlist(chr(i)+":\\",self.opfile)
                else: self.fullfilepathlist(chr(i)+":",self.opfile) 
            except Exception as exception:
                print(exception)
                break
            
        
    def extlist(self,drives,opfile):
        """

        list just extensions

        """
        print("listing Drives :" + drives)

        if self.overwrite == False:
            if os.path.exists(opfile):
                append_write = 'a'
            else:
                append_write = 'w'
        else:
            append_write='w'

        with open(opfile,append_write,encoding=self.encoding) as f:
            print("\n")
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

            

    def fullfilepathlist(self,drives,opfile):
        """
        list a full file path
        """
        print("listing "+ drives)

        if self.overwrite == False:
            if os.path.exists(opfile):
                append_write = 'a'
            else:
                append_write = 'w'
        else:
            append_write='w'

        with open(opfile,append_write,encoding=self.encoding) as f:
            print("\n")
            for root,_,files in os.walk(drives):
                for name in files:
                    filepath = os.path.join(root,name)
                    f.write(filepath+'\n')
                    self.filecount+=1
                f.write(str(self.filecount))


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--ext")
    parser.add_argument("--opfile")
    parser.add_argument("--encoding")
    parser.add_argument("--overwrite")
    args = parser.parse_args()
    ext = args.ext
    opfile = args.opfile
    encoding = args.encoding
    overwrite = args.overwrite

    boo = filelist(ext=ext,encoding=encoding,opfile=opfile,overwrite=overwrite)
    boo.run()
    #bugs when choose to overwrite files, files in Drive's loop overwrite itself