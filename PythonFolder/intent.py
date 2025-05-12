from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/run-python', methods=['POST'])
def run_python():
    data = request.json
    user_input = data.get('input', '')

    # Call external Python script with user input
    process = subprocess.Popen(['python3', 'my_script.py', user_input],
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()

    if error:
        return jsonify({'error': error.decode()}), 500

    return jsonify({'result': output.decode().strip()})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
