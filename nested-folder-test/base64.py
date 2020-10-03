string = "asdfjkl"
class base64(object):
    """
    docstring
    """
    def encode64(self):
        """
        docstring
        """
        encoded_string = ""
        for i in self.data:
            a = bin(ord(i))[2:]
            while len(a) < 8:
                a = '0' + a
            encoded_string += a
        self.data = encoded_string

        temp6_char = []
        

    def __init__(self,data):
        """
        docstring
        """
        self.data = data
    
    
    

data = "This is the best beginning to my hacking job"
a = base64(data)
a.encode64()
while len(self.data) >= 6:
            a = self.data[:6]
            temp6_char.append(a)
            self.data = self.data[:6]
        temp6_char.append(self.data)
        print(temp6_char)