from abc import ABC, abstractmethod

# Abstract product
class Product(ABC):
    @abstractmethod
    def operation(self):
        pass

# Concrete product
class ConcreteProductA(Product):
    def operation(self):
        return "Product A"

class ConcreteProductB(Product):
    def operation(self):
        return "Product B"

# Creator
class Creator(ABC):
    @abstractmethod
    def create_product(self):
        pass

# Concrete Creator
class ConcreteCreatorA(Creator):
    def create_product(self):
        return ConcreteProductA()

class ConcreteCreatorB(Creator):
    def create_product(self):
        return ConcreteProductB()

# Testing Factory
def test_factory():
    creator_a = ConcreteCreatorA()
    creator_b = ConcreteCreatorB()

    product_a = creator_a.create_product()
    product_b = creator_b.create_product()

    print(product_a.operation())  # Output: Product A
    print(product_b.operation())  # Output: Product B

test_factory()
