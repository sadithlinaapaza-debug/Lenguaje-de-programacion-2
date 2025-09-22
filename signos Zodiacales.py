class Persona:
    def __init__(self, nombre, dia, mes):
        self.nombre = nombre
        self.dia = dia
        self.mes = mes

    def signo(self):
        if (self.mes == "enero" and self.dia >= 20) or (self.mes == "febrero" and self.dia <= 18):
            return "Acuario"
        elif (self.mes == "febrero" and self.dia >= 19) or (self.mes == "marzo" and self.dia <= 20):
            return "Piscis"
        elif (self.mes == "marzo" and self.dia >= 21) or (self.mes == "abril" and self.dia <= 19):
            return "Aries"
        elif (self.mes == "abril" and self.dia >= 20) or (self.mes == "mayo" and self.dia <= 20):
            return "Tauro"
        elif (self.mes == "mayo" and self.dia >= 21) or (self.mes == "junio" and self.dia <= 20):
            return "Géminis"
        elif (self.mes == "junio" and self.dia >= 21) or (self.mes == "julio" and self.dia <= 22):
            return "Cáncer"
        elif (self.mes == "julio" and self.dia >= 23) or (self.mes == "agosto" and self.dia <= 22):
            return "Leo"
        elif (self.mes == "agosto" and self.dia >= 23) or (self.mes == "septiembre" and self.dia <= 22):
            return "Virgo"
        elif (self.mes == "septiembre" and self.dia >= 23) or (self.mes == "octubre" and self.dia <= 22):
            return "Libra"
        elif (self.mes == "octubre" and self.dia >= 23) or (self.mes == "noviembre" and self.dia <= 21):
            return "Escorpio"
        elif (self.mes == "noviembre" and self.dia >= 22) or (self.mes == "diciembre" and self.dia <= 21):
            return "Sagitario"
        elif (self.mes == "diciembre" and self.dia >= 22) or (self.mes == "enero" and self.dia <= 19):
            return "Capricornio"
        else:
            return "Fecha inválida"

nombre = input("Ingresa tu nombre: ")
dia = float(input("Ingresa tu día de nacimiento: "))
mes = input("Ingresa tu mes de nacimiento: ")

persona = Persona(nombre,dia,mes)
print(f"{persona.nombre} nacio el {persona.dia} de {persona.mes} y tu signo es {persona.signo()}")
