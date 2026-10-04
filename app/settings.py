"""Configuration de TaskFlow, lue depuis les variables d'environnement."""

import os

APP_NAME = "TaskFlow"
VERSION = os.getenv("APP_VERSION", "0.1.0")
DB_PATH = os.getenv("DB_PATH", "taskflow.db")
API_TOKEN = os.getenv("API_TOKEN", "")
NOTIFY_WEBHOOK_URL = os.getenv("NOTIFY_WEBHOOK_URL", "")
