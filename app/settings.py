"""Configuration de TaskFlow, lue depuis les variables d'environnement."""

import os

APP_NAME = "TaskFlow"
VERSION = os.getenv("APP_VERSION", "0.1.0")
DB_PATH = os.getenv("DB_PATH", "taskflow.db")
API_TOKEN = os.getenv("API_TOKEN", "")
NOTIFY_WEBHOOK_URL = os.getenv("NOTIFY_WEBHOOK_URL", "")

# Injection de pannes (cours M2 : déploiement progressif et robustesse).
# FAILURE_RATE : part des requêtes en erreur 500 (0 à 1). LATENCY_MS : latence ajoutée.
FAILURE_RATE = float(os.getenv("FAILURE_RATE", "0"))
LATENCY_MS = int(os.getenv("LATENCY_MS", "0"))
