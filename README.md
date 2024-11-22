#Eternity Calculator - COMP 354

Overview

The Eternity Calculator is a scientific calculator developed as part of a group project for COMP 354: Introduction to Software Engineering. It provides a variety of advanced mathematical functions, including Logarithms, Exponential calculations, Gamma function, Standard Deviation, Mean Absolute Deviation (MAD), and more. The project includes both a back-end and front-end interface, making it a fully functional web-based calculator.

Supported Functions

LOG: Computes the logarithm of a number x with a custom base b. Syntax: log_b(x, b)
ARCCOS: Calculates the arccosine (inverse cosine) of a number. Syntax: arccos(x)
EXP: Performs an exponential calculation with three parameters: a * b^x. Syntax: exp(a, b, x)
GAMMA: Computes the Gamma function for a number x, using the Lanczos approximation. Syntax: gamma(x)
MAD: Calculates the Mean Absolute Deviation for a series of numbers. Syntax: mad([x1, x2, ..., xn])
STD: Computes the Standard Deviation for a series of numbers. Syntax: std([x1, x2, ..., xn])
SINH: Calculates the hyperbolic sine of a number. Syntax: sinh(x)
POW: Computes the power of a number x raised to an exponent y. Syntax: pow(x, y)
How to Use the Calculator

Accessing the Application:
The calculator is hosted as a web application. Once running, you can access it via a browser.
Navigate to the main page where you will see an input field and function buttons.
Input Format:
Enter expressions directly into the text field. Use standard mathematical syntax. For example:
log_b(10, 2) to compute the logarithm of 10 with base 2.
arccos(0.5) for inverse cosine.
exp(2, 3, 4) for 2 * 3^4.
gamma(5) to compute the Gamma function of 5.
The result will be shown after you press the "=" button.
Functionality:
LOG: Computes logarithms with a custom base.
ARCCOS: Calculates the arccosine of a number.
EXP: Performs exponential calculations using three parameters.
GAMMA: Computes the Gamma function for a given number.
MAD: Calculates the Mean Absolute Deviation of a set of numbers.
STD: Computes the Standard Deviation for a set of numbers.
SINH: Computes the hyperbolic sine of a number.
POW: Computes the power of a number raised to an exponent.
Error Handling:
The calculator provides clear error messages for unsupported expressions or invalid inputs.
Technologies Used

Python: The back-end logic for calculations.
Flask: The web framework used to serve the calculator.
HTML/CSS/JavaScript: The front-end interface to interact with users.
Bootstrap: For responsive and dynamic UI components.
Installation Instructions

Clone the Repository:
git clone <repository-url>
Set up Virtual Environment (Optional but recommended):
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install Dependencies:
pip install -r requirements.txt
Run the Application:
python app.py
The app will be available at http://127.0.0.1:5000/.
Contributors

Doan Gia Huy Vu and the rest of the COMP 354 team.
License

This project is licensed under the MIT License.
