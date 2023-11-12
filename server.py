from flask import Flask
from flask import Flask, send_from_directory
import subprocess
from pathlib import Path
import random
from shlex import split
import sys

app = Flask(__name__)


# Path for our main Svelte page
@app.route("/")
def base():
    return send_from_directory("client/public", "index.html")


# Path for all the static files (compiled JS/CSS, etc.)
@app.route("/<path:path>")
def home(path):
    return send_from_directory("client/public", path)


@app.route("/rand")
def hello():
    return str(random.randint(0, 100))


def run(cmd, cwd):
    print(f"RUNNING: {cmd}")
    if subprocess.run(split(cmd), cwd=cwd).returncode:
        print("FAILED")
        sys.exit(0)
    print("DONE")


def main():
    run("npm run build", cwd="client")
    # split("npx tailwindcss -o public/build/bundle.css --minify"),
    # run("npx tailwindcss -o public/build/bundle.css", cwd="client")

    # global_css = Path("client/public/global.css")
    # bundle_css = Path("client/public/build/bundle.css")
    # cmd = "npx tailwindcc -i global.css -o build/bundle.css --watch"
    # run(split(cmd), cwd="client/public", check=True)
    app.run(debug=False, host="localhost", port=8080)


if __name__ == "__main__":
    main()
