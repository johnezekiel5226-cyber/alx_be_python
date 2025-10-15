class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Returns the sum of two numbers."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Returns the product of two numbers and prints the class attribute."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b


# Demonstration
if __name__ == "__main__":
    # Using the static method
    result_add = Calculator.add(10, 5)
    print(f"Addition Result: {result_add}")

    # Using the class method
    result_multiply = Calculator.multiply(4, 3)
    print(f"Multiplication Result: {result_multiply}")
