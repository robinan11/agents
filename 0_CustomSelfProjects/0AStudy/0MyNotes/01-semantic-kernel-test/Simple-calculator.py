
from typing import Annotated                # Imports Annotated from the typing module. Used for better function annotations/hints, especially with plugins in semantic_kernel.


class CalculatorPlugin:
    """A simple calculator plugin."""
    # @kernel_function(description="Evaluates a simple math expression.")
    # def calculate(self, expression: Annotated[str, "A math expression to evaluate"]) -> Annotated[str, "The result as a string."]:
    def calculate(self, expression: str) -> str:

        try:
            allowed_chars = set("0123456789+-*/(). ")
            if not set(expression).issubset(allowed_chars):
                return "Only basic arithmetic expressions allowed."
            result = eval(expression, {"__builtins__": {}})
            return str(result)
        except Exception as e:
            return f"Error: {str(e)}"
        

calc = CalculatorPlugin()

print(calc.calculate("2 + 3 * 4"))
        