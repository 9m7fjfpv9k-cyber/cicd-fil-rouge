"""Configuration de TaskFlow."""

APP_NAME = "TaskFlow"
VERSION = "0.1.0"
DB_PATH = "taskflow.db"

# Jeton exigé pour supprimer une tâche (en-tête X-API-Token).
# TODO : à déplacer dans une variable d'environnement avant la mise en prod.
API_TOKEN = "tf_live_9f8c2b7e41d64a0b8e3c5f17a2d9b6e4c1f0a8d7"

NOTIFY_WEBHOOK_URL = ""
