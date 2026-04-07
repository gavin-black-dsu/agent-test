from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/write_file', methods=['GET'])
def write_file():
    filename = request.args.get('filename')
    text = request.args.get('text')

    if filename is None or text is None:
        return "Missing filename or text parameter", 400

    # Check if the filename is valid
    if not is_valid_filename(filename):
        return "Invalid filename", 400

    # Check if the file already exists
    if os.path.exists(f"uploaded/{filename}"):
        return "File already exists", 400

    # Write the text to the file
    try:
        with open(f"uploaded/{filename}", "w") as file:
            file.write(text)
    except Exception as e:
        return str(e), 500

    return "File written successfully"

def is_valid_filename(filename):
    # Check if the filename contains any special characters
    if not filename.isalnum():
        return False

    # Check if the filename has a valid extension
    valid_extensions = ['.txt', '.csv', '.json']
    if not any(filename.endswith(ext) for ext in valid_extensions):
        return False

    return True

if __name__ == '__main__':
    app.run()
