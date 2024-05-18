class Silnia:
    def calculate(self, num):
        if num == 0 or num == 1:
            return 1
        result = 1
        for i in range(2, num + 1):
            result *= i
        return result


class SymbolNewtona:
    def calculate(self, n, k, silnia):
        return silnia.calculate(n) // (silnia.calculate(k) * silnia.calculate(n - k))


class Prawdopodobienstwo:
    def __init__(self):
        self.symbol_newtona = SymbolNewtona()
        self.silnia = Silnia()

    def calculate(self, n, k, p):
        binomial_coefficient = self.symbol_newtona.calculate(n, k, self.silnia)
        return binomial_coefficient * (p ** k) * ((1 - p) ** (n - k))


class BinomialCalculator:
    def __init__(self):
        self.prawdopodobienstwo = Prawdopodobienstwo()

    def calculate_probability(self, n, k, p):
        return self.prawdopodobienstwo.calculate(n, k, p)


class User:
    def __init__(self, name):
        self.name = name

    def calculate_probability(self, n, k, p):
        calculator = BinomialCalculator()
        return calculator.calculate_probability(n, k, p)


user = User("Jan")
n = 5
k = 2
p = 0.5

probability = user.calculate_probability(n, k, p)
print(f"Prawdopodobieństwo {k} sukcesów w {n} próbach przy prawdopodobieństwie sukcesu {p}: {probability}")
