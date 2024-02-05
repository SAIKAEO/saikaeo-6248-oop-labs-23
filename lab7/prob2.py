class Numbers:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def add(self):
        return self.x + self.y

    @classmethod
    def display_factors(cls, num):
        half = num // 2
        return f'Factors of {num} is {half} and {half}' if num % 2 == 0 else f'Factors of {num} is {half} and {half + 1}'

    @staticmethod
    def is_valid_divisor(num):
        return f"{num} is {'not ' if num == 0 else ''}a valid divisor"


if __name__ == '__main__':
    numbers_instance = Numbers(2, 3)
    print(f'2 + 3 is {numbers_instance.add()}')
    print(Numbers.display_factors(6))
    print(Numbers.display_factors(7))
    print(Numbers.is_valid_divisor(2))
    print(Numbers.is_valid_divisor(0))
