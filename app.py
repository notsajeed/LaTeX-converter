from flask import Flask, render_template, request, send_file, send_from_directory
import subprocess
import uuid
import os

app = Flask(__name__)
OUTPUT_DIR = "output"

# Ensure output folder exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html', filename=None)

@app.route('/convert', methods=['POST'])
def convert():
    raw_code = request.form['latex']

    if r'\documentclass' not in raw_code:
        # Auto-wrap in minimal LaTeX document
        latex_code = f"""
    \\documentclass{{article}}
    \\usepackage{{amsmath}}
    \\usepackage[utf8]{{inputenc}}
    \\usepackage{{geometry}}
    \\geometry{{margin=1in}}

    \\begin{{document}}

    \\[
    {raw_code}
    \\]

    \\end{{document}}
    """
    else:
        latex_code = raw_code

    session_id = str(uuid.uuid4())
    tex_filename = f"{session_id}.tex"
    pdf_filename = f"{session_id}.pdf"
    tex_path = os.path.join(OUTPUT_DIR, tex_filename)
    pdf_path = os.path.join(OUTPUT_DIR, pdf_filename)

    # Save LaTeX code to .tex file
    with open(tex_path, 'w', encoding='utf-8') as f:
        f.write(latex_code)

    try:
        # Compile LaTeX using pdflatex
        result = subprocess.run(
            ['pdflatex', '-interaction=nonstopmode', '-output-directory', OUTPUT_DIR, tex_path],
            capture_output=True,
            text=True,
            timeout=45
        )

        print("STDOUT:\n", result.stdout)
        print("STDERR:\n", result.stderr)

        if result.returncode != 0 or not os.path.exists(pdf_path):
            error = "❌ LaTeX Compilation Failed. See log below."
            output = result.stdout + "\n" + result.stderr
        else:
            filename = pdf_filename
            # 🧹 optional: don't show logs if successful


        # Instead of sending file directly, show download button
        return render_template('index.html', filename=pdf_filename)

    except subprocess.TimeoutExpired:
        return "<h2>⏰ Compilation timed out</h2>", 500

    except Exception as e:
        return f"<h2>⚠️ Unexpected Error:</h2><pre>{str(e)}</pre>", 500

    finally:
        # Optional: clean up intermediate files
        for ext in ['.aux', '.log', '.tex']:
            temp_file = os.path.join(OUTPUT_DIR, f"{session_id}{ext}")
            if os.path.exists(temp_file):
                os.remove(temp_file)

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(OUTPUT_DIR, filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True, threaded=True)

