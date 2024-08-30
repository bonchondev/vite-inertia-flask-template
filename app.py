"""test."""

import os.path as op
import json
from typing import Any, Dict
from config import PUBLIC_FOLDER, STATIC_FOLDER, TEMPLATES
from flask import Flask, send_from_directory
from flask_inertia import Inertia, render_inertia
from flask_vite import Vite


ROOT_DIR = op.abspath(op.dirname(op.dirname(__file__)))
MANIFEST_FILE = op.join(
    ROOT_DIR,
    "static",
    "dist",
    "manifest.json",
)

def load_manifest() -> Dict[str, Dict[str, Any]]:
    try:
        with open(MANIFEST_FILE) as fi:
            manifest = json.load(fi)
    except:
        manifest = {}

    return {"manifest": manifest}


def create_app(config_filename: str) -> Flask:
    app = Flask(
        __name__,
        template_folder=TEMPLATES,
        static_folder=STATIC_FOLDER,
    )
    app.config.from_pyfile(f"{config_filename}.py")
    
    Inertia(app)
    Vite(app)
    # app.context_processor(load_manifest)

    # app.add_url_rule("/", "index", index)
    

    return app

app = create_app('dev')

@app.get('/')
def index():
    # return {}
    return render_inertia("Index", props={'amount': '$2,000'})

@app.get("/<path:path>")
def static_folder(path):
    return send_from_directory(STATIC_FOLDER, path)

@app.get("/favicon.ico")
def public_folder(path):
    return send_from_directory(PUBLIC_FOLDER, path)

if __name__ == '__main__':
    app.run()

