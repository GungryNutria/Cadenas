class Operations:

    def setOption(self, index, cadena):
        self.contador = 0
        self.pares = 0
        self.impares = 0
        self.index = index
        self.cadena = cadena
        if index == 0:
            self.operation0()
        elif index == 1:
            self.operation1()
        elif index == 2:
            self.operation2()
        elif index == 3:
            self.operation3()
        elif index == 4:
            self.operation4()
        elif index == 5:
            self.operation5()
        elif index == 6:
            self.operation6()
        elif index == 7:
            self.operation7()
        elif index == 8:
            self.operation8()

    def checkNumbers(self):
        for i in range(0, len(self.cadena)):
            if int(self.cadena[i]) > 1:
                print('salio un 2')
                return True
                break
            
            else:
                print('sigue la condicion')

    def operation0(self):
        if self.cadena[0] != 'b':
            print('No se cumple la condicion')
            print(self.cadena[0])
        else:
            print('El codigo Continua')
            if self.cadena[len(self.cadena)-2] == 'c' and self.cadena[len(self.cadena)-1] == 'b':

                print('Se cumple la cadena')
            else:
                print(self.cadena[len(self.cadena)-2])
                print('No se cumple la condicion')

    def operation1(self):
        if self.checkNumbers() == True:
            print('Tiene un numero que no es 0 y uno')
        else:
            for i in range(0, len(self.cadena)):
                if int(self.cadena[i]) == 0 and int(self.cadena[i+1]) == 0:
                    print('Se cumple la condicion')
                else:
                    print('No se cumplio la condicion')
                    break
        print('Operacion 1')

    def operation2(self):
        for i in range(0, len(self.cadena)):
            if self.cadena[i] == 'c':
                self.contador = self.contador + 1
                print('C cargada', self.contador)
        if self.contador % 2 == 0:
            print("Cantidad de C's pares")
        else:
            print('No se cumple la condicion')
        print('Operacion 2')

    def operation3(self):
        if self.checkNumbers() == True:
            print('Tiene un numero que no es 1 o 0')
        else:
            if int(self.cadena[0]) == 1:
                print('Continua el codigo.')
                for i in range(0, len(self.cadena)):
                    if int(self.cadena[i]) == 1 and int(self.cadena[i+1]) == 0:
                        print('Tiene la subcadena')
                        break
                    else:
                        print('Buscando.....')
                if int(self.cadena[len(self.cadena)-1]) == 0:
                    print('Termina en 0')
                else:
                    print('No termina en 0')

            else:
                print('No se cumplen las condiciones')
            print('Operacion 3 \n ---------------------------')

    def operation4(self):
        for i in range(0,len(self.cadena)):
            if self.cadena[i] == 'a' and self.cadena[i+1] == 'b':
                print('No se cumple la condicion')
                break
            else:
                print('La cadena continua')
        if self.cadena[len(self.cadena)-1] == 'c':
            print('Se cumple segunda condicion')
        else:
            print('No se cumple la segunda condicion')
        print('Operacion 4')

    def operation5(self):
        if self.cadena[0] == 'c':
            print('Si se cumple la primer condicion')
            if self.cadena[len(self.cadena)-2] == 'c' and self.cadena[len(self.cadena)-1] == 'b':
                print('Si se cumple la segunda condicion')
            else:
                print('No se cumple la segunda condicion')
        else:
            print('No se cumple la primer condicion')
        print('Operacion 5')

    def operation6(self):
        for i in range(0,len(self.cadena)):
            if self.cadena[i] == 'c' and self.cadena[i+1] == 'c' and self.cadena[i+2] == 'c':
                print('No se cumple la condicion')
                break
            else:
                print('Se cumple la condicion')
        print('Operacion 6')

    def operation7(self):
        for i in range(0,len(self.cadena)):
            if self.cadena[i] == 'a' and self.cadena[i+1] == 'b':
                print('Se cumple la primer condicion')
            else:
                print('No cumple la primer condicion')
            
            if self.cadena[i] == 'b' and self.cadena[i+1] == 'a':
                print('No se cumple la segunda condicion')
            else:
                print('si se cumple la segunda condicion')
                
        print('Operacion 7')

    def operation8(self):
        for i in range(0,len(self.cadena)):
            if self.cadena[i] == 'a':
                self.pares = self.pares +1
            elif self.cadena[i] == 'b':
                self.impares = self.impares +1
        if (self.pares % 2) == 0:
            print('Si cumple la primera condicion')
            if(self.impares % 2) == 0:
                print('No se cumple la segunda condicion')
            else:
                print('Si se cumple la segunda condicion')
        else:
            print('No se cumple la primera condicion')
        print('Operacion 8')
