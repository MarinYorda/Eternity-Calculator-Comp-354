from calculator import EternityCalculator

# Test for Standard Deviation, Mean, and Variance with user-provided values
user_input = input("Enter the values for which you want to calculate Standard Deviation, Mean, and Variance, separated by spaces: ")
array = [float(num) for num in user_input.split()]
eternity_calc = EternityCalculator(array)

# Calculate and print the Standard Deviation
print(f"Standard Deviation: {eternity_calc.calculate_standard_deviation()}")

# Calculate and print the Mean
mean_result = eternity_calc.calculate_mean()
print(f"Mean: {mean_result}")

# Calculate and print the Variance
variance_result = eternity_calc.calculate_variance()
print(f"Variance: {variance_result}")

# Test the Gamma function with a user-provided input
try:
    x_value = float(input("Enter a number to calculate its Gamma function: "))
    gamma_result = eternity_calc.calculate_gamma(x_value)
    print(f"Gamma({x_value}) = {gamma_result}")
except ValueError as e:
    print(f"Gamma Error: {e}")

# Test the Exponential function with user-provided inputs
try:
    a = float(input("Enter the value of 'a' in the exponential function a * b^x: "))
    b = float(input("Enter the value of 'b' in the exponential function a * b^x: "))
    x = float(input("Enter the value of 'x' in the exponential function a * b^x: "))
    exponential_result = eternity_calc.calculate_exponential(a, b, x)
    print(f"{a} * {b}^{x} = {exponential_result}")
except ValueError as e:
    print(f"Exponential Error: {e}")

# Test Mean Absolute Deviation (MAD) with user-provided values
user_input = input("Enter the values for which you want to calculate Mean Absolute Deviation (MAD), separated by spaces: ")
array = [float(num) for num in user_input.split()]
mad_value = eternity_calc.calculate_mad(array)
print(f"MAD = {mad_value}")

# Test the Logarithmic Function with user-provided value and base
try:
    log_value = float(input("Enter the number to calculate its logarithm: "))
    log_base = float(input("Enter the base for the logarithm (e.g., 10 for log10, 2 for log2, or leave blank for natural log): ") or 2.718281828459045)
    
    log_result = eternity_calc.calculate_logarithm(log_value, base=log_base)
    print(f"log_{log_base}({log_value}) = {log_result}")

except ValueError as e:
    print(f"Logarithm Error: {e}")

# Test the Arccos Function with user-provided input
try:
    arccos_input = float(input("Enter a number to calculate its arccos (must be in range [-1, 1]): "))
    arccos_result = eternity_calc.calculate_arccos(arccos_input)
    print(f"arccos({arccos_input}) = {arccos_result}")
except ValueError as e:
    print(f"Arccos Error: {e}")
    
# Test the Hyperbolic sine function with user-provided inputs
try:
    user_input = float(input("Enter a number to calculate its hyperbolic sine function: "))
    result = eternity_calc.calculate_hyperbolic_sine(user_input)
    print(f"sinh({user_input}) = {result}")
    
except ValueError as e:
    print(f"Hyperbolic sine function error: {e}")

# Test the Power function with user-provided input
try:
    base = float(input("Enter the base for the power function: "))
    power = float(input("Enter the exponent for the power function: "))
    power_result = eternity_calc.PowerOf(base, power)
    print(f"{base} to the power of {power} = {power_result}")
except ValueError as e:
    print(f"Power Function Error: {e}")
