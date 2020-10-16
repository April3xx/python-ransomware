import os
class test():

    def path_traversal(self):
        for root, dirs, files in os.walk('.'):
            for name in files:
                yield(os.path.join(root,name))

    def fileext(self):
        for file in self.path_traversal():
            if file.split(".")[-1] != "txt":
                continue
            print(file.split(".")[-1])

if __name__ == "__main__":
    testobj = test()
    testobj.fileext()