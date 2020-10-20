class bidict(dict):
    """
    two way dictionary
    """
    def __setitem__(self,key,value):
        if key in self:
            del self[key]
        if value in self:
            del self[value]
        dict.__setitem__(self,key,value)
        dict.__setitem__(self,value,key)

    def __delitem__(self,key):
        try:
            dict.__delitem__(self,self[key])
        except:
            pass
        
        dict.__delitem__(self,key)
       
    
    def __len__(self):
        return dict.__len__(self)//2

WIDE_MAP = dict((i, i+100) for i in range(1, 10))
WIDE_MAP.update( dict((WIDE_MAP[k], k) for k in WIDE_MAP) )
print(WIDE_MAP)