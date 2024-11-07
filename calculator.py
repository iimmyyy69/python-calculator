class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        result = 0
        negative_result = False
        if b < 0:
            b = -b
            negative_result = not negative_result
        if a < 0:
            a = -a
            negative_result = not negative_result

        for _ in range(b):
            result = self.add(result, a)

        return -result if negative_result else result

        
    def divide(self, a, b):
        if b == 0:
            return "Cannot divide by zero"

        result = 0
        negative_result = False
        if a < 0:
            a = -a
            negative_result = not negative_result
        if b < 0:
            b = -b
            negative_result = not negative_result

        while a >= b:
            a = self.subtract(a, b)
            result = self.add(result, 1)

        return -result if negative_result else result
    
    def modulo(self, a, b):
        if b == 0:
            return "Cannot modulo by zero"

        negative_result = False
        if a < 0:
            negative_result = True

        a = abs(a)
        b = abs(b)
        while a >= b:
            a = self.subtract(a, b)
            result = a

        return -result if negative_result else result

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))