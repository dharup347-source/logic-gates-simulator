"""
Logic Gates Simulator
A beginner project for Electronics & VLSI students.
"""

def AND(a, b):
    return a and b

def OR(a, b):
    return a or b

def NOT(a):
    return not a

def NAND(a, b):
    return not (a and b)

def NOR(a, b):
    return not (a or b)

def XOR(a, b):
    return a != b

def XNOR(a, b):
    return a == b


def get_binary_input(prompt):
    """Ask user for 0 or 1 and validate."""
    while True:
        value = input(prompt).strip()
        if value in ("0", "1"):
            return int(value)
        print("Please enter only 0 or 1.")


def main():
    print("=" * 40)
    print("   LOGIC GATES SIMULATOR")
    print("=" * 40)
    print("Available gates: AND, OR, NOT, NAND, NOR, XOR, XNOR")
    print()

    while True:
        gate = input("Enter gate type (or 'quit' to exit): ").strip().upper()

        if gate == "QUIT":
            print("Goodbye!")
            break

        if gate == "NOT":
            a = get_binary_input("Enter input (0 or 1): ")
            result = NOT(a)
            print(f"NOT {a} = {int(result)}")

        elif gate in ("AND", "OR", "NAND", "NOR", "XOR", "XNOR"):
            a = get_binary_input("Enter first input (0 or 1): ")
            b = get_binary_input("Enter second input (0 or 1): ")

            if gate == "AND":
                result = AND(a, b)
            elif gate == "OR":
                result = OR(a, b)
            elif gate == "NAND":
                result = NAND(a, b)
            elif gate == "NOR":
                result = NOR(a, b)
            elif gate == "XOR":
                result = XOR(a, b)
            elif gate == "XNOR":
                result = XNOR(a, b)

            print(f"{gate}({a}, {b}) = {int(result)}")

        else:
            print("Invalid gate. Please try again.")

        print("-" * 40)


if __name__ == "__main__":
    main()
