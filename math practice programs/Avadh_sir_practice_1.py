import numpy as np


class EquationSolver:
    def __init__(self):
        """Initialize the solver with the equation definition."""
        self.user_equation = None

    def set_equation(self):
        """
        Set the equation dynamically based on user input.
        """
        equation_str = input("Enter the equation to solve (use 'x' as the variable): ")
        self.user_equation = equation_str

    def equation(self,x):
        """
        Evaluate the user-defined equation.
        """
        try:
            # Use eval to evaluate the equation dynamically
            return eval(self.user_equation)
        except Exception as e:
            print(f"Error in evaluating the equation: {e}")
            return None

    def avg(self, a, b,roundof, loop):
        avgval = (a + b) / 2
        ans = round(self.equation(avgval), roundof)
        print(f"0 => a : {a} b : {b} avgval : {avgval} ans : {ans}\n")

        for i in range(0, loop):
            if ans < 0:
                a = avgval
            else:
                b = avgval
            avgval = round((a + b) / 2, roundof)
            ans = round(self.equation(avgval), roundof)
            print(f"{i + 1} => a : {a} b : {b} avgval : {avgval} ans : {ans}\n")
        return i

    def solve(self):
        """
        Main function to solve the equation.
        It prompts the user for input and calculates the result.
        """
        while True:
            try:
                choice = int(input("Enter 1 to solve or 2 to exit (default 1): ") or 1)
                if choice == 1:
                    # if self.user_equation == None:
                    self.set_equation()
                    a = float(input("Enter the lower bound (a): "))
                    b = float(input("Enter the upper bound (b): "))
                    roundof = int(input("Enter the round of value (ex : eq.1234 || by default = 4) : ") or 4)
                    loop = int(input("Enter the loop count (loop): "))
                    self.avg(a, b,roundof, loop)
                elif choice == 2:
                    print("Exiting the solver. Goodbye!")
                    break
                else:
                    print("Invalid choice. Please enter 1 or 2.")
            except ValueError:
                print("Invalid input. Please enter a number.")


# Main execution
if __name__ == "__main__":
    solver = EquationSolver()
    solver.solve()
