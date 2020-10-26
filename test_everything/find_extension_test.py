import os

class filelist():

    def __init__(self,overwrite,ext,opfile=None,encoding=None):
        """
        parameters:
            encoding:   file encoding scheme default utf-8
            opfile:     path to write output-file
                        default: create "dirlist.txt" at running directory
            ext:        list extension or fullpath?
                        default: extension
        """
        self.ext = ext
        if self.ext =='true':
            self.ext = True
        else: self.ext = False

        if opfile is None:
            self.opfile = "dirlist.txt"
        else:
            self.opfile = opfile
        if encoding is None:
            self.encoding = "utf-8"
        else:
            self.encoding = encoding

        self.overwrite = overwrite
        if self.overwrite == 'false':
            self.overwrite = False
        else: self.overwrite = True

        self.filecount = 0

    def run(self):
        self.generatedrivelist()

    def generatedrivelist(self):
        """
        generate a to z and call extlist every loop from a to z
        using drives parameter
        """
        for i in range(65,65+26):
            try:
                drivestring = chr(i)+":\\"
                print(drivestring)
                if self.ext:
                    self.extlist(drivestring,self.opfile)
                else: self.fullfilepathlist(drivestring,self.opfile)

            except Exception as exception:
                print(exception)
                break
            
    def extlist(self,drives,opfile):
        """

        list just extensions

        """
        print("listing Drives :" + drives)

        if self.overwrite is True:
            print('file exists overwriting in extension mode....'+'\n')
            append_write ='w'
            self.overwrite = False

        elif os.path.exists(opfile):
            print('appending.......')
            append_write = 'a'
        else:
            print('overwriting......')
            append_write = 'w'
        
        with open(opfile,append_write,encoding=self.encoding) as f:
            f.write("\n")
            for _,_,files in os.walk(drives):
                for name in files:
                    if '.' in name:
                        name = name[name.rfind('.'):]
                        f.write(name+"\n")
                        self.filecount +=1
                    else:
                        f.write(name+'\n')
                        self.filecount += 1 

    

    def fullfilepathlist(self,drives,opfile):
        """
        list a full file path
        """
        print("listing "+ drives)
        if self.overwrite is True:
            print('file exists overwriting in full path mode....'+'\n')
            append_write ='w'
            self.overwrite = False
            
        elif os.path.exists(opfile):
            print('appending.......')
            append_write = 'a'
        else:
            print('overwriting......')
            append_write = 'w'

        with open(opfile,append_write,encoding=self.encoding) as f:
            f.write("\n")
            for root,_,files in os.walk(drives):
                for name in files:
                    filepath = os.path.join(root,name)
                    f.write(filepath+'\n')
                    self.filecount+=1

    def uniqueext(self):
        unique_extension = []
        file_without_extension=[]
        
        with open(self.opfile,'r') as f:
            for line in f:
                araara = f.readline()
                if '.' in araara:
                    unique_extension.append(araara)
                else:
                    file_without_extension.append(araara)
        
        unique_all_file = set(unique_extension+file_without_extension)
        # listallfile = unique_extension+file_without_extension
        # allfilecount = len(listallfile)
        # unique_all_file = set(listallfile)
        # unique_file_count = len(unique_all_file)
        # unique_ext_count = len(set(unique_extension))

        with open(self.opfile,'w') as f:
            for elem in unique_all_file:
                f.write(elem)
                f.write('\n')

            # f.write("you have " + str(allfilecount) + 'files'+'\n')
            # f.write("you have "+ str(unique_file_count)+' unique files'+'\n')
            # f.write("you have " + str(allfilecount-unique_ext_count)+ "files without extensions"+'\n')
            # f.write("and "+ str(unique_ext_count)+ " unique extension")
        
    @staticmethod
    def help():
        print("""
        --ext: list only extension or  list full filepath"""+'\n'"""
                default : false (list full path)"""+'\n'"""
        --opfile: path to output file """+'\n'"""
                    default: create "dirlist.txt" at running directory"""+'\n'"""
        --encoding: encoding scheme use in listing file"""+'\n'"""
                    default: utf-8"""+'\n'"""
        --overwrite: am just too lazy to write 
        """)
    

if __name__ == "__main__":
    import argparse
    filelist.help()

    parser = argparse.ArgumentParser()
    parser.add_argument("--ext")
    parser.add_argument("--opfile")
    parser.add_argument("--encoding")
    parser.add_argument("--overwrite")
    parser.add_argument("--unique")
    args = parser.parse_args()
    ext = args.ext
    opfile = args.opfile
    encoding = args.encoding
    overwrite = args.overwrite
    unique = args.unique

    #the reason these two if is here is i need .lower()
    if overwrite is None:
        overwrite = True
    else: overwrite = overwrite.lower()

    if ext is None:
        ext = False
    else: ext = ext.lower()

    #can't scan ?
    boo = filelist(ext=ext,encoding=encoding,opfile=opfile,overwrite=overwrite)
    print('this is the first initiated overwrite value'+str(boo.overwrite)+'\n')
    boo.run()
    print(boo.filecount)
    if unique is None:
        pass
    else:
        boo.uniqueext()