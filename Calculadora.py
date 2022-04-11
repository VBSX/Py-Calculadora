#Calculadora simples para calculos simples!
#o objetivo da mesma era entender melhor o conceito de classes...
class calculadora:
    def __init__(self, numero1, operador, numero2):
        self.operador = operador
        self.numero1 = numero1
        self.numero2 = numero2
    
    
    def calcular(self):
        while self.operador == '+':
            resultado = (self.numero1) + (self.numero2)
            return print('\nO resultado deu:', resultado)
        
        while self.operador == '-':
            resultado = (self.numero1) - (self.numero2)
            return print('\nO resultado deu:', resultado)
        
        while self.operador == '/':
            resultado = (self.numero1) / (self.numero2)
            return print('\nO resultado deu:', resultado)
        
        while self.operador == '*':
            resultado = (self.numero1) * (self.numero2)
            return print('\nO resultado deu:', resultado)

print('Seja bem vindo a Calculadora Python')
num1 = float(input('coloque um número: \n' ))
operação = input('coloque o operador: \n' )
num2 = float(input('coloque o segundo número: \n'))

calc = calculadora(num1, operação, num2)
calc.calcular()
