#just insert any string in the given index
def mutate(string,yourstring,index):
     string = string[:index] + yourstring + string[index:]
     return string

if __name__ == "__main__":
    
    a = "123456"
    a = mutate(a,' love ',1)

    print(a)