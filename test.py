# teststring = "111111222222333333444444555555666666777777888888999999"
# test_tuple = []
# while len(teststring)>=6:
#     a = teststring[:6]
#     test_tuple.append(a)
#     teststring = teststring[6:]

# print('a :',a)
# print('teststring :',teststring)
# print(test_tuple)
## end of slice test
######################################################################################################################
import argparse
class testname():
    """
    docstring
    """
    def __init__(self,extension):
        self.extension = extension

parser = argparse.ArgumentParser()
parser.add_argument('--extension')
args = parser.parse_args()
extension = args.extension
test = testname(extension)
print(test.extension)
if test.extension is None:
    print('yes')
else:
    pass
