class batman:
    """
    docstring
    """
    def __init__(self,name):
        self.name = name
    def __hello__(self):
        print("hello i am batman")
class robin(batman):
    """
  dfaf  
    """
    def __hello__(self):
        batman.__hello__(self)
        print("hello of robin")

a = robin("blob")
a.__hello__()