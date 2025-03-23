# math_equations.py

def equation_1(A, B, R):
    """
    Function to check if the Pythagorean theorem holds true for A, B, and R.

    Equation: A^2 + B^2 = R^2
    """
    return A**2 + B**2 == R**2

def equation_2(A, B):
    """
    Function to expand (A - B)^2.
    
    Equation: (A - B)^2 = A^2 - 2*A*B + B^2
    """
    return A**2 - 2*A*B + B**2

def equation_3(A, B):
    """
    Function to expand (A + B)^2.
    
    Equation: (A + B)^2 = A^2 + 2*A*B + B^2
    """
    return A**2 + 2*A*B + B**2
