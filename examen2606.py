#26/06

class Empleado: 
    def __init__(self, nombre, edad, salario):
        self.nombre=nombre
        self.edad=edad
        self.salario=salario

    def detalles(self):
        print("Nombre: ",self.nombre,"\nEdad: ",self.edad,"\nSalario: $",self.salario)
        print("______________________________")


class Gerente(Empleado):
    def __init__(self, nombre, edad, salario,departamento): #Polimorfismo
        super().__init__(nombre, edad, salario)
        self.departamento=departamento

    def detalles(self):#Polimorfismo
        print("Departamento: ",self.departamento) #Polimorfismo
        return super().detalles()
    

class Ingeniero(Empleado):
    def __init__(self, nombre, edad, salario, especialidad): #Polimorfismo
        super().__init__(nombre, edad, salario)
        self.especialidad=especialidad

    def detalles(self):#Polimorfismo
        print("Especialidad: ",self.especialidad) #Polimorfismo
        return super().detalles()
    

E1= Empleado("Erick",25,30000) #Polimorfismo
E1.detalles() #Polimorfismo

E2= Gerente("Amanda",40,150000,"23A") #Polimorfismo
E2.detalles() #Polimorfismo

E3= Ingeniero("Robert",54,1000000,"Analista en Sistemas") #Polimorfismo
E3.detalles() #Polimorfismo
