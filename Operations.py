class Operations:
    
    def setOption(self,index):
        self.index = index
        if index == 0:
            self.operation0()
        elif index == 1:
            self.operation1()
        elif index == 2:
            self.operation2()
        elif index == 3:
            self.operation3()
    def operation0(self):
        print('Operacion 0')
    def operation1(self):
        print('Operacion 1')
    def operation2(self):
        print('Operacion 2')
    def operation3(self):
        print('Operacion 3')    
        
