import re
import cmath

class Calculator:
    def __init__(self):
        self.stack = []

    # Number Parsing
    def parse_number(self, token):
        token = token.replace(" ", "")
        if re.match(r"^[+-]?\d+(\.\d+)?$", token):
            return complex(float(token), 0)
        elif re.match(r"^[+-]?j\d+(\.\d+)?$", token):
            return complex(0, float(token.replace("j", "")))
        elif re.match(r"^[+-]?\d+(\.\d+)?[+-]j\d+(\.\d+)?$", token):
            real, imag = re.split(r"(?=[+-]j)", token)
            return complex(float(real), float(imag.replace("j", "")))
        else:
            raise ValueError("Invalid token")

    # Canonical Form
    def canonical(self, z: complex) -> str:
        a = 0 if abs(z.real) < 1e-10 else z.real
        b = 0 if abs(z.imag) < 1e-10 else z.imag
        sign = "+" if b >= 0 else "-"
        return f"{a:.9f}".rstrip('0').rstrip('.') + f" {sign} j{abs(b):.9f}".rstrip('0').rstrip('.')

    # Error Handling Helpers
    def require_stack(self, n):
        # Ensure the stack has at least n elements.
        if len(self.stack) < n:
            return False
        return True

    # Command Execution
    def execute(self, command: str):
        self.stack = [] # Reset stack for each execution
        tokens = command.strip().split()
        i = 0
        result = None

        while i < len(tokens):
            token = tokens[i].lower()

            # PUSH
            if token == "push":
                i += 1
                if i >= len(tokens):
                    raise ValueError("Invalid Token: Missing value for push")
                start = i
                j = i
                while j < len(tokens) and tokens[j].lower() not in (
                    "push", "pop", "add", "sub", "mul", "div", "delete",
                    "abs", "sin", "asin", "cos", "acos", "sqr", "sqrt"
                ):
                    j += 1
                num_tokens = tokens[start:j]
                num_str = "".join(num_tokens)
                num = self.parse_number(num_str)
                self.stack.append(num)
                i = j
                continue

            # POP
            elif token == "pop":
                if not self.stack:
                    return "Error: stack underflow"
                result = self.canonical(self.stack.pop())

            # ADD
            elif token == "add":
                if not self.require_stack(2):
                    return "Error: stack underflow"
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.append(a + b)

            # SUB
            elif token == "sub":
                if not self.require_stack(2):
                    return "Error: stack underflow"
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.append(a - b)

            # MUL
            elif token == "mul":
                if not self.require_stack(2):
                    return "Error: stack underflow"
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.append(a * b)

            # DIV
            elif token == "div":
                if not self.require_stack(2):
                    return "Error: stack underflow"
                b = self.stack.pop()
                a = self.stack.pop()
                if b == 0:
                    return "Error: division by zero"
                self.stack.append(a / b)

            # DELETE
            elif token == "delete":
                if not self.require_stack(1):
                    return "Error: stack underflow"
                self.stack.pop()

            # ABS
            elif token == "abs":
                if not self.require_stack(1):
                    return "Error: stack underflow"
                a = self.stack.pop()
                self.stack.append(complex(abs(a), 0))

            # SIN
            elif token == "sin":
                if not self.require_stack(1):
                    return "Error: stack underflow"
                a = self.stack.pop()
                self.stack.append(cmath.sin(a))

            # ASIN
            elif token == "asin":
                if not self.require_stack(1):
                    return "Error: stack underflow"
                a = self.stack.pop()
                self.stack.append(cmath.asin(a))

            # COS
            elif token == "cos":
                if not self.require_stack(1):
                    return "Error: stack underflow"
                a = self.stack.pop()
                self.stack.append(cmath.cos(a))

            # ACOS
            elif token == "acos":
                if not self.require_stack(1):
                    return "Error: stack underflow"
                a = self.stack.pop()
                self.stack.append(cmath.acos(a))

            # SQR
            elif token == "sqr":
                if not self.require_stack(1):
                    return "Error: stack underflow"
                a = self.stack.pop()
                self.stack.append(a ** 2)

            # SQRT
            elif token == "sqrt":
                if not self.require_stack(1):
                    return "Error: stack underflow"
                a = self.stack.pop()
                self.stack.append(cmath.sqrt(a))

            else:
                raise ValueError(f"Unknown command: {token}")

            i += 1

        return result


# CLI
if __name__ == "__main__":
    calc = Calculator()
    print("Complex DC Calculator")
    while True:
        try:
            command = input("cdc> ")
            result = calc.execute(command)
            if result:
                print(result)
        except Exception as e:
            print(f"Error: {e}")
