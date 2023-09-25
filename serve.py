import subprocess
from flask import Flask, send_from_directory

DEFAULT_PORT = 8000
DIRECTORY = "build/html"
SPHINX_BUILD_CMD = "sphinx-build -b html src build/html"

try:
    print("Building Sphinx documentation...")
    subprocess.run(SPHINX_BUILD_CMD, shell=True, check=True)
    print("Built Sphinx documentation")
except subprocess.CalledProcessError:
    print("Sphinx build failed. Check your documentation configuration.")
    exit(1)

app = Flask(__name__)


@app.route("/")
def index():
    return send_from_directory(DIRECTORY, "index.html")


@app.route("/<path:filename>")
def serve_static(filename):
    return send_from_directory(DIRECTORY, filename)
