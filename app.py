from flask import Flask, render_template_string, request, jsonify
import os
from boltiotai import openai
from dotenv import load_dotenv
load_dotenv()

openai.api_key = RbxdBxgrHRpKPcFllHyyY7m6aET_GHh451Ta6mlXois
app = Flask(__name__)


def generate_course_content(course_title):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role":
            "system",
            "content":
            "You are an experienced educator tasked with creating comprehensive course content."
        }, {
            "role":
            "user",
            "content":
            f"""Generate educational content for a course titled "{course_title}". Include:
                    1. Objective of the Course (concise statement)
                    2. Sample Syllabus (main topics and modules)
                    3. Three Measurable Outcomes (using Bloom's Taxonomy levels: Knowledge, Comprehension, and Application)
                    4. Assessment Methods
                    5. Recommended Readings and Textbooks"""
        }])
    print(1)
    print(response)
    print(1)
    return response['choices'][0]['message']['content']


# HTML template
html_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Course Content Generator</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container">
        <h1 class="my-4">AI Course Content Generator</h1>
        <form method="POST" class="mb-3">
            <div class="mb-3">
                <label for="course_title" class="form-label">Course Title:</label>
                <input type="text" class="form-control" id="course_title" name="course_title" placeholder="Enter the course title" required>
            </div>
            <button type="submit" class="btn btn-primary">Generate Content</button>
        </form>
        {% if content %}
        <div class="card mt-4">
            <div class="card-header d-flex justify-content-between align-items-center">
                Output:
                <button class="btn btn-secondary btn-sm" id="copyButton">Copy</button>
            </div>
            <div class="card-body">
                <pre id="output" class="mb-0" style="white-space: pre-wrap;">{{ content }}</pre>
            </div>
        </div>
        {% endif %}
    </div>
    <script>
    document.getElementById('copyButton').addEventListener('click', function() {
        const output = document.getElementById('output');
        const textarea = document.createElement('textarea');
        textarea.value = output.textContent;
        document.body.appendChild(textarea);
        textarea.select();
        document.execCommand('copy');
        document.body.removeChild(textarea);
        alert('Copied to clipboard');
    });
    </script>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def home():
    content = None
    if request.method == 'POST':
        course_title = request.form['course_title']
        content = generate_course_content(course_title)
    return render_template_string(html_template, content=content)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)