import numpy as np


class EquationSolver:
    def __init__(self):
        """Initialize the solver with the equation definition."""
        pass

    @staticmethod
    def equation(x):
        """
        Define the equation to solve.
        Equation: x^3 + 9x + 1
        """
        return (x ** 3) + (9 * x) + 1
        # return (x ** 3) - (3 * x) + 1.06
        # return (10 ** x) + np.sin(np.radians(x)) + (2 * x)
    
    def avg(self,a ,b,loop):
      avgval = (a+b)/2
      ans = round(self.equation(avgval),3)
      print(f"0 => a : {a} b : {b} avgval : {avgval} ans : {ans}\n")
      
      for i in range(0,loop):
            if ans < 0:
                  a = avgval
                  
            else:
                  b = avgval
            avgval = round((a+b)/2,3)
            ans = round(self.equation(avgval),3)
            print(f"{i+1} => a : {a} b : {b} avgval : {avgval} ans : {ans}\n")
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
                    a = float(input("Enter the lower bound (a): "))
                    b = float(input("Enter the upper bound (b): "))
                    loop = int(input("Enter the loop count (loop): "))
                    result = self.avg(a,b,loop)
                    # print(f"The solution to the equation is approximately x = {result+1}")
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
