# Calculator functionality
class Calculator():
    def calculate(self, input_str):
        return "" # TODO

# CLI interface
if __name__ == "__main__":
    calc = Calculator()
    print("Complex DC Calculator (type EXIT to quit)")
    while True:
        try:
            line = input("> ").strip()
            if not line:
                continue
            if line.upper() in ("EXIT", "QUIT"):
                print("Goodbye!")
                break
            result = calc.calculate(line)
            if result is not None:
                print(result)
        except EOFError:
            # Handles Ctrl-D / end of input
            print("\nGoodbye!")
            break
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"Unexpected error: {e}")