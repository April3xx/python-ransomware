class testclass(object):
    """
    docstring
    """
    def __init__(self,attr1=None,attr2=False):
        if self.attr1 is None:
            self.attr2 = True

    def testtest(self):
        if self.attr2 is True:
            print("prayut hua kuy")

damn = testclass()
damn.testtest()