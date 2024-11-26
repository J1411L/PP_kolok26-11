class Fibonacci:
    def __init__(self, n):
        if not isinstance(n, int) or n <= 0:
            raise ValueError("n должно быть натуральным числом (целым положительным).")
        self.n = n

    def generate(self):
        fib_sequence = []
        a, b = 0, 1
        for _ in range(self.n):
            fib_sequence.append(a)
            a, b = b, a + b
        return fib_sequence


def get_fibonacci(n):
    fib = Fibonacci(n)
    return fib.generate()


if __name__ == "__main__":
    try:
        n = int(input("Введите натуральное число n: "))
        print(get_fibonacci(n))
    except ValueError as e:
        print(e)