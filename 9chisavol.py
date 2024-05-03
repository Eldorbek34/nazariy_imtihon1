class Kalkulyator:
    def qoshish(self, x, y):
        return x + y

    def ayirish(self, x, y):
        return x - y

    def kopaytirish(self, x, y):
        return x * y

    def bolish(self, x, y):
        if y != 0:
            return x / y
        else:
            return "Nolga bo'lish mumkin emas"

    if __name__== "main":
       calculator = Calculator()

    a = float(input("Son kiriting: "))
    b = float(input("Son kiriting: "))

    print(f"Addition: {calculator.addition(a, b)}")
    print(f"Subtraction: {calculator.subtraction(a, b)}")
    print(f"Multiplication: {calculator.multiplication(a, b)}")
    print(f"Division: {calculator.division(a, b)}")
