from pathlib import Path
from flask import Flask
from flask_vite import Vite
from flask_inertia import Inertia

ROOT_DIR = Path(".")

TEMPLATES = Path(".") / "templates"

STATIC_FOLDER = Path(".") / "static"

PUBLIC_FOLDER = Path(".") / "public"


def create_app() -> Flask:

    app = Flask(
        __name__,
        template_folder=TEMPLATES,
        static_folder=STATIC_FOLDER,
    )

    app.config["INERTIA_TEMPLATE"] = "base.html"
    app.config["SECRET_KEY"] = "changeme"
    app.config["VITE_AUTO_INSERT"] = app.debug
    app.config["VITE_NPM_BIN_PATH"] = "pnpm"

    Inertia(app)

    Vite(app)

    return app
