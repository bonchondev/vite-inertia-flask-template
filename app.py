"""test."""

from config import PUBLIC_FOLDER, STATIC_FOLDER, TEMPLATES
from flask import Flask, current_app, send_from_directory
from flask_inertia import Inertia, render_inertia
from flask_vite import Vite

def create_app(config_filename: str) -> Flask:
    app = Flask(
        __name__,
        template_folder=TEMPLATES,
        static_folder=STATIC_FOLDER,
    )
    app.config.from_pyfile(f"{config_filename}.py")

    Inertia(app)
    Vite(app)

    return app

app = create_app('dev')

@app.get('/')
def index():
    # ~pages~, ~api calls~, ~tailwind~, ~props~
    return render_inertia("Index", props={'amount': '$2,000'})

@app.get('/about')
def about():
    return render_inertia("About", props={'amount': '$7,000'})


@app.post('/data')
def data():
    return {'dollars': 100}

@app.get("/<path:path>")
def static_folder(path):
    return send_from_directory(STATIC_FOLDER, path)

@app.get("/favicon.ico")
def public_folder(path):
    return send_from_directory(PUBLIC_FOLDER, path)

if __name__ == '__main__':
    app.run()
