# cdc.py
import re

class Calculator:
    def __init__(self):
        self.stack = []

    def parse_number(self, token):
        # Normalize "j5" or "-j2" forms
        token = token.replace(" ", "")
        if re.match(r"^[+-]?\d+(\.\d+)?$", token):
            return complex(float(token), 0)
        elif re.match(r"^[+-]?j\d+(\.\d+)?$", token):
            return complex(0, float(token.replace("j", "")))
        elif re.match(r"^[+-]?\d+(\.\d+)?[+-]j\d+(\.\d+)?$", token):
            real, imag = re.split(r"(?=[+-]j)", token)
            return complex(float(real), float(imag.replace("j", "")))
        else:
            raise ValueError("Invalid number format")

    def canonical(self, z: complex) -> str:
        # Canonical form: a ± jb, normalized
        a = 0 if abs(z.real) < 1e-10 else z.real
        b = 0 if abs(z.imag) < 1e-10 else z.imag
        sign = "+" if b >= 0 else "-"
        return f"{a:g} {sign} j{abs(b):g}"

    def execute(self, command: str):
        tokens = command.strip().split()
        i = 0
        while i < len(tokens):
            token = tokens[i].lower()
            if token == "push":
                i += 1
                if i >= len(tokens):
                    raise ValueError("Missing value for push")
                num_str = tokens[i]
                num = self.parse_number(num_str)
                self.stack.append(num)
            elif token == "pop":
                if not self.stack:
                    return "Error: stack underflow"
                return self.canonical(self.stack.pop())
            else:
                raise ValueError(f"Unknown command: {token}")
            i += 1
        return None


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