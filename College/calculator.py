class calculator:
    a= 10
    b= 20
    def add(self):
        sum=self.a+self.b
        print(sum)
    def sub(self):
        sub=self.a-self.b
        print(sub)
    def mult(self):
        mult=self.a*self.b
        print(mult)
    def div(self):
        div=self.a/self.b
        print(div)

x = calculator()
x.add()
x.mult()