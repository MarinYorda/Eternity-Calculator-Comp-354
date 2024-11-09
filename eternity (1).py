class EternityCalculator:
    def __init__(self, array=None):
        self.array = array if array else []

    def calculate_mean(self):
        return sum(self.array) / len(self.array) if self.array else 0

    def calculate_variance(self):
        mean = self.calculate_mean()
        cal1 = sum((x - mean) ** 2 for x in self.array)
        return cal1 / len(self.array) if self.array else 0

    def calculate_standard_deviation(self):
        variance = self.calculate_variance()
        return self.custom_sqrt(variance)

    # Gamma function using Lanczos approximation without built-in math functions
    def calculate_gamma(self, x):
        if x <= 0 and x == int(x):
            raise ValueError("Gamma function is undefined for non-positive integers.")

        g = 7
        p = [
            0.99999999999980993,
            676.5203681218851,
            -1259.1392167224028,
            771.32342877765313,
            -176.61502916214059,
            12.507343278686905,
            -0.13857109526572012,
            9.9843695780195716e-6,
            1.5056327351493116e-7
        ]

        if x < 0.5:
            return self.custom_pi() / (self.custom_sin(self.custom_pi() * x) * self.calculate_gamma(1 - x))
        else:
            x -= 1
            y = p[0]
            for i in range(1, len(p)):
                y += p[i] / (x + i)
            t = x + g + 0.5
            return self.custom_sqrt(2 * self.custom_pi()) * (t ** (x + 0.5)) * self.custom_exp(-t) * y

    # Mean Absolute Deviation (MAD) function
    def calculate_mad(self, array):
        if not array:
            return 0
        mean = sum(array) / len(array)
        absolute_sum = sum(abs(x - mean) for x in array)
        mad = absolute_sum / len(array)
        return mad

    # Logarithm function using the Newton-Raphson method for natural log
    def calculate_logarithm(self, value, base=None):
        if value <= 0:
            raise ValueError("Logarithm is undefined for non-positive values.")
        if base is None:
            base = self.custom_e()
        elif base <= 0 or base == 1:
            raise ValueError("Logarithm base must be positive and not equal to 1.")
        
        # Calculate the natural logarithm using the Newton-Raphson method
        def natural_logarithm(x):
            tolerance = 1e-10
            n = 0
            result = x - 1

            while n < 100:
                exp_result = self.custom_exp(result)
                result -= (exp_result - x) / exp_result
                if abs(exp_result - x) < tolerance:
                    break
                n += 1
            return result
        
        # Calculate logarithm with any base using the change of base formula
        return natural_logarithm(value) / natural_logarithm(base)
    
    # Exponential function for a * b^x without using built-in power
    def calculate_exponential(self, a, b, x):
        result = a * self.PowerOf(b, x)
        return result

    # Arccos function approximation using Taylor series expansion
    def calculate_arccos(self, x):
        if x < -1 or x > 1:
            raise ValueError("Input for arccos must be in the range [-1, 1].")
        
        # Taylor series approximation of arccos(x) around 0
        result = 0
        term = x
        factor = 1
        n = 0
        while abs(term) > 1e-10:
            result += term / (2 * n + 1)
            factor *= (2 * n + 1) / (2 * n + 2)
            term *= (x * x) * factor
            n += 1
        
        return self.custom_pi() / 2 - result
    
    # Hyperbolic sine function using approximation of e
    def calculate_hyperbolic_sine(self, x):
        e = 2.718281828459045235360287471352
        result = ((e**x) - e**(-x))/2
        return result
    
    # Power function without using built-in functions
    def PowerOf(self, base, power):
        # Handle zero base cases
        if base == 0:
            return 0 if power > 0 else float('inf')

        # If power is zero, result is 1
        if power == 0:
            return 1

        # If power is an integer
        result = 1
        if power == int(power):
            for _ in range(abs(int(power))):
                result *= base
            if power < 0:
                result = 1 / result
        else:
            # For non-integer power, use the exponential and logarithm method
            result = self.custom_exp(power * self.calculate_logarithm(base))
        return result
    

    # Custom implementations of necessary math functions
    def custom_pi(self):
        return 3.141592653589793
    
    def custom_e(self):
        return 2.718281828459045

    def custom_sin(self, x):
        # Taylor series expansion for sin(x)
        sine = 0
        term = x
        n = 1
        sign = 1
        while abs(term) > 1e-10:
            sine += term
            term = -term * x * x / ((2 * n) * (2 * n + 1))
            n += 1
        return sine

    def custom_exp(self, x):
        # Taylor series expansion for exp(x)
        result = 1
        term = 1
        n = 1
        while abs(term) > 1e-10:
            term *= x / n
            result += term
            n += 1
        return result

    def custom_sqrt(self, x):
        # Newton's method for square root
        if x < 0:
            raise ValueError("Cannot compute square root of a negative number.")
        guess = x
        epsilon = 1e-10
        while abs(guess * guess - x) > epsilon:
            guess = (guess + x / guess) / 2
        return guess
