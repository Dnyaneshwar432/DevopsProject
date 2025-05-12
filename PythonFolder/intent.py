from flask import Flask, request, jsonify
import subprocess
from flask_cors import CORS
import gunicorn
app = Flask(__name__)
CORS(app)
@app.route('/run-python', methods=['POST'])
def run_python():
    data = request.json
    user_input = data.get('input', '')
    user_tools= data.get('devtools', '')


# Call external Python script with user input
    process = subprocess.Popen(['python3', 'my_script.py', user_input,user_tools],
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()

    if error:
        return jsonify({'error': error.decode()}), 500

    return jsonify({'result': output.decode().strip()})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
