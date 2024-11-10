from flask import Flask, render_template, request
from calculator import EternityCalculator

app = Flask(__name__)


def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/arccos', methods=['GET', 'POST'])
def arccos():
    error = None
    if request.method == 'POST':
        value = request.form.get('input')
        if not is_float(value):
            error = "Please enter a valid number."
        else:
            value = float(value)
            if value < -1 or value > 1:
                error = "Input for arccos must be between -1 and 1."
            else:
                calculator = EternityCalculator([])
                result = calculator.calculate_arccos(value)
                return render_template('arccos.html', result=result, input=value)
    return render_template('arccos.html', error=error)


@app.route('/exponential', methods=['GET', 'POST'])
def exponential():
    error = None
    if request.method == 'POST':
        input_data = request.form.get('input')
        try:
            a, b, x = [float(i) for i in input_data.split(',')]
            calculator = EternityCalculator([])
            result = calculator.calculate_exponential(a, b, x)
            return render_template('exponential.html', result=result, input=input_data)
        except ValueError:
            error = "Please enter three comma-separated numbers (a, b, x)."
    return render_template('exponential.html', error=error)


@app.route('/logarithm', methods=['GET', 'POST'])
def logarithm():
    error = None
    if request.method == 'POST':
        input_data = request.form.get('input')
        try:
            value, base = [float(i) for i in input_data.split(',')]
            calculator = EternityCalculator([])
            result = calculator.calculate_logarithm(value, base)
            return render_template('logarithm.html', result=result, input=input_data)
        except ValueError:
            error = "Please enter two comma-separated numbers (x, base)."
    return render_template('logarithm.html', error=error)


@app.route('/gamma', methods=['GET', 'POST'])
def gamma():
    error = None
    if request.method == 'POST':
        value = request.form.get('input')
        if not is_float(value):
            error = "Please enter a valid number."
        else:
            value = float(value)
            if value <= 0:
                error = "Gamma function is undefined for non-positive integers."
            else:
                calculator = EternityCalculator([])
                result = calculator.calculate_gamma(value)
                return render_template('gamma.html', result=result, input=value)
    return render_template('gamma.html', error=error)


@app.route('/mad', methods=['GET', 'POST'])
def mad():
    error = None
    if request.method == 'POST':
        input_data = request.form.get('input')
        try:
            number_list = [float(x) for x in input_data.split(',')]
            calculator = EternityCalculator(number_list)
            result = calculator.calculate_mad(number_list)
            return render_template('mad.html', result=result, input=input_data)
        except ValueError:
            error = "Please enter comma-separated numbers."
    return render_template('mad.html', error=error)


@app.route('/standard_deviation', methods=['GET', 'POST'])
def standard_deviation():
    error = None
    if request.method == 'POST':
        input_data = request.form.get('input')
        try:
            number_list = [float(x) for x in input_data.split(',')]
            calculator = EternityCalculator(number_list)
            result = calculator.calculate_standard_deviation()
            return render_template('standard_deviation.html', result=result, input=input_data)
        except ValueError:
            error = "Please enter comma-separated numbers."
    return render_template('standard_deviation.html', error=error)


@app.route('/sinh', methods=['GET', 'POST'])
def sinh():
    error = None
    if request.method == 'POST':
        value = request.form.get('input')
        if not is_float(value):
            error = "Please enter a valid number."
        else:
            value = float(value)
            calculator = EternityCalculator([])
            result = calculator.calculate_hyperbolic_sine(value)
            return render_template('sinh.html', result=result, input=value)
    return render_template('sinh.html', error=error)


@app.route('/power', methods=['GET', 'POST'])
def power():
    error = None
    if request.method == 'POST':
        input_data = request.form.get('input')
        try:
            base, exponent = [float(i) for i in input_data.split(',')]
            calculator = EternityCalculator([])
            result = calculator.PowerOf(base, exponent)
            return render_template('power.html', result=result, input=input_data)
        except ValueError:
            error = "Please enter two comma-separated numbers (base, exponent)."
    return render_template('power.html', error=error)


if __name__ == '__main__':
    app.run(debug=True)
