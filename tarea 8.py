class ConversorTemperatura:
    def __init__(self, fahrenheit):
        self.fahrenheit = fahrenheit

    @staticmethod
    def celsius_a_fahrenheit(c):
        return (c * 9/5) + 32

    @classmethod
    def desde_celsius(cls, c):
        f = cls.celsius_a_fahrenheit(c)
        return cls(f)

t1 = ConversorTemperatura.desde_celsius(25)
print("Temperatura en Fahrenheit:", t1.fahrenheit)

print("0°C en Fahrenheit:", ConversorTemperatura.celsius_a_fahrenheit(0))
