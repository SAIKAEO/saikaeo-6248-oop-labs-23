class Cat:
    num_legs = 4

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def show_info(self):
        print(f"Cat name is {self.name} and its color is {self.color}")

    @classmethod
    def get_num_legs(cls):
        return cls.num_legs

    @staticmethod
    def get_owner_name():
        return "Lalisa Manobal"


if __name__ == "__main__":
    cat1 = Cat("Leo", "Brown")
    cat1.show_info()

    cat2 = Cat("Lily", "White")
    cat2.show_info()

    print(f"The number of legs of all cats is {Cat.get_num_legs()}")
    print(f"The owner of these cats is {Cat.get_owner_name()}")
