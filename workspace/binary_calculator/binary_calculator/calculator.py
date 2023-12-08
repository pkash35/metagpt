## calculator.py

class Calculator:
    def __init__(self, binary1: str, binary2: str):
        self.binary1 = binary1
        self.binary2 = binary2

    def add(self) -> str:
        # Convert binary to integer, add them and convert back to binary
        return bin(int(self.binary1, 2) + int(self.binary2, 2))[2:]

    def subtract(self) -> str:
        # Convert binary to integer, subtract them and convert back to binary
        return bin(int(self.binary1, 2) - int(self.binary2, 2))[2:]

    def multiply(self) -> str:
        # Convert binary to integer, multiply them and convert back to binary
        return bin(int(self.binary1, 2) * int(self.binary2, 2))[2:]

    def divide(self) -> str:
        # Convert binary to integer, divide them and convert back to binary
        # Ensure division by zero is handled
        if int(self.binary2, 2) == 0:
            return "Cannot divide by zero"
        return bin(int(self.binary1, 2) // int(self.binary2, 2))[2:]
