
# 📄 LaTeX to PDF Converter

A simple Flask-based web app to **convert LaTeX code into a downloadable PDF**. Users can paste raw LaTeX or equations, and the app compiles it into a clean PDF using `pdflatex`.

---

## 🚀 Features

* ✍️ Input LaTeX code via web interface
* 📄 Auto-wraps minimal document if raw equation is submitted
* ⚙️ Compiles using `pdflatex` via `subprocess`
* 📥 Downloads the compiled PDF
* 📁 All outputs stored in the `output/` folder
* 🎨 Styled with custom CSS (in `static/style.css`)

---

## 📁 Project Structure

```
latex-converter/
│
├── app.py                   # Main Flask backend
├── output/                  # Stores generated PDFs
│
├── static/
│   └── style.css            # Optional: styling for the frontend
│
├── templates/
│   └── index.html           # Main HTML form interface
│
├── README.md                # This file
```

---

## 🛠️ Requirements

* Python 3.x
* LaTeX distribution installed (`pdflatex` must be available)
* Recommended: `texlive-latex-base`

### Install requirements (Debian/Ubuntu):

```bash
sudo apt-get update
sudo apt-get install -y texlive-latex-base
```

### Python packages:

```bash
pip install flask
```

---

## 💡 How to Run

1. Clone the repo or copy the files into a directory:

```bash
git clone https://github.com/notsajeed/latex-converter.git
cd latex-converter
```

2. Run the Flask app:

```bash
python app.py
```

3. Open your browser and go to:

```
http://127.0.0.1:5000/
```

---

## 📤 Output

All generated `.pdf` files are stored in the `output/` directory. Temporary `.aux`, `.log`, and `.tex` files are automatically cleaned after compilation.

---

## ⚠️ Notes

* If `pdflatex` is not installed, the compilation will fail.
* Large or complex LaTeX documents might require additional packages (e.g., `amsmath`, `geometry`, etc.).
* Ensure your LaTeX code is valid to avoid compiler errors.

---

## 📄 License

MIT License — free for personal and commercial use.

---
