# Eternity Calculator - COMP 354

## Overview

The **Eternity Calculator** is a scientific calculator developed as part of a group project for **COMP 354: Introduction to Software Engineering**. It provides a variety of advanced mathematical functions, including **Logarithms**, **Exponential calculations**, **Gamma function**, **Standard Deviation**, **Mean Absolute Deviation (MAD)**, and more. The project includes both a **back-end** and **front-end** interface, making it a fully functional web-based calculator.

## Supported Functions

1. **LOG**: Computes the logarithm of a number `x` with a custom base `b`.  
   **Syntax**: `log_b(x, b)`

2. **ARCCOS**: Calculates the arccosine (inverse cosine) of a number.  
   **Syntax**: `arccos(x)`

3. **EXP**: Performs an exponential calculation with three parameters: `a * b^x`.  
   **Syntax**: `exp(a, b, x)`

4. **GAMMA**: Computes the Gamma function for a number `x`, using the Lanczos approximation.  
   **Syntax**: `gamma(x)`

5. **MAD**: Calculates the Mean Absolute Deviation for a series of numbers.  
   **Syntax**: `mad([x1, x2, ..., xn])`

6. **STD**: Computes the Standard Deviation for a series of numbers.  
   **Syntax**: `std([x1, x2, ..., xn])`

7. **SINH**: Calculates the hyperbolic sine of a number.  
   **Syntax**: `sinh(x)`

8. **POW**: Computes the power of a number `x` raised to an exponent `y`.  
   **Syntax**: `pow(x, y)`

## How to Use the Calculator

### Accessing the Application

- The calculator is hosted as a web application. Once running, you can access it via a browser. 
- Navigate to the main page where you will see an input field and function buttons.

### Input Format

- Enter expressions directly into the text field using standard mathematical syntax. For example:
  - `log_b(10, 2)` to compute the logarithm of 10 with base 2.  
  - `arccos(0.5)` for inverse cosine.  
  - `exp(2, 3, 4)` for `2 * 3^4`.  
  - `gamma(5)` to compute the Gamma function of 5.

- After entering an expression, press the `=` button to see the result.

### Functionality

- **LOG**: Computes logarithms with a custom base.
- **ARCCOS**: Calculates the arccosine of a number.
- **EXP**: Performs exponential calculations using three parameters.
- **GAMMA**: Computes the Gamma function for a given number.
- **MAD**: Calculates the Mean Absolute Deviation of a set of numbers.
- **STD**: Computes the Standard Deviation for a set of numbers.
- **SINH**: Computes the hyperbolic sine of a number.
- **POW**: Computes the power of a number raised to an exponent.

### Error Handling

- The calculator provides clear error messages for unsupported expressions or invalid inputs.

## Technologies Used

- **Python**: Back-end logic for calculations.
- **Flask**: Web framework used to serve the calculator.
- **HTML/CSS/JavaScript**: Front-end interface to interact with users.
- **Bootstrap**: Used for responsive and dynamic UI components.

## Installation Instructions

1. **Clone the Repository**:
   - Open your terminal and run the following command:
     ```bash
     git clone <repository-url>
     ```

2. **Set up Virtual Environment** (Optional but recommended):
   - In your terminal, create and activate a virtual environment by running:
     ```bash
     python -m venv venv
     ```
   - To activate the virtual environment, use:
     ```bash
     source venv/bin/activate  # On Windows: venv\Scripts\activate
     ```

3. **Install Dependencies**:
   - Install the required dependencies by running:
     ```bash
     pip install -r requirements.txt
     ```

4. **Run the Application**:
   - Start the application by running:
     ```bash
     python combine_calculator.py
     ```

   - The app will be available at [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your web browser.

# Project Structure

The project has the following structure:

EternityCalculator/
│
├── app/
│   ├── templates/             # HTML templates for the web interface
│   │   └── combined_calculator_v3.html  # Main HTML template for the calculator
│   ├── static/                # Static files (CSS, JavaScript)
│   │   ├── css/               # CSS files
│   │   │   └── styles.css     # Styles for the web interface
│   │   └── js/                # JavaScript files
│   │       └── script.js      # Scripts for the web interface
│   ├── calculator.py          # Back-end logic for the calculator
│   └── testing_combine.py     # Unit tests for combined calculator functionality
│
├── venv/                      # (Optional) Virtual environment folder
├── README.md                  # This readme file
├── requirements.txt           # List of required Python packages
└── LICENSE                    # License file
