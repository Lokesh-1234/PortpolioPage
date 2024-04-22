from flask import Flask, render_template, send_file
import os

app = Flask(__name__)


# Set the static folder to 'static'
app.static_folder = 'static'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download_resume')
def download_resume():
    # Get the directory path of the current file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the path to the resume file
    resume_path = os.path.join(current_dir, 'templates', 'resume.pdf')
    # Send the file for download
    return send_file(resume_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
