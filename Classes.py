

class CLASSNAME:
    
    def __init__(self, name):
        #Config
        self.name = name

    def __str__(self):
        return "{}".format(self.name)
    
    def print(self):
        print("{}".format(self.name))
        
        

class Class_Exception(Exception):
    pass







