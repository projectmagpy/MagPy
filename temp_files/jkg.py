__author__ = 'admin'

class calc():
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def add(self):
        print self.a+self.b




if __name__ == '__main__':
    c = calc(a = 5 ,b = 5)
    c.add()