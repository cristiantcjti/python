import os

from src.config.app import create_app

app = create_app(f"src.config.settings.Config")
