import requests
import logging
from django.conf import settings

logger = logging.getLogger(__name__)


class OllamaService:
    """Service pour interagir avec Ollama"""

    def __init__(self):
        self.api_url = settings.OLLAMA_API_URL
        self.default_model = settings.OLLAMA_DEFAULT_MODEL

    def get_available_models(self):
        """Récupérer la liste des modèles disponibles"""
        try:
            response = requests.get(
                f"{self.api_url}/api/tags",
                timeout=5
            )

            if response.status_code == 200:
                data = response.json()
                models = [model['name'] for model in data.get('models', [])]
                return models
            else:
                logger.error(f"Erreur récupération modèles: {response.status_code}")
                return []

        except requests.exceptions.RequestException as e:
            logger.error(f"Erreur connexion Ollama: {e}")
            return []

    def generate_response(self, prompt, model=None, stream=False):
        """Générer une réponse à partir d'un prompt"""
        if model is None:
            model = self.default_model

        try:
            response = requests.post(
                f"{self.api_url}/api/generate",
                json={
                    "model": model,
                    "prompt": prompt,
                    "stream": stream
                },
                timeout=120  # 2 minutes max
            )

            if response.status_code == 200:
                data = response.json()
                return {
                    'success': True,
                    'response': data.get('response', ''),
                    'model': model
                }
            else:
                logger.error(f"Erreur génération: {response.status_code}")
                return {
                    'success': False,
                    'error': f"Erreur {response.status_code}"
                }

        except requests.exceptions.Timeout:
            logger.error("Timeout lors de la génération")
            return {
                'success': False,
                'error': "La requête a pris trop de temps"
            }
        except requests.exceptions.RequestException as e:
            logger.error(f"Erreur génération: {e}")
            return {
                'success': False,
                'error': str(e)
            }

    def chat(self, messages, model=None):
        """Chat avec historique de conversation"""
        if model is None:
            model = self.default_model

        try:
            response = requests.post(
                f"{self.api_url}/api/chat",
                json={
                    "model": model,
                    "messages": messages,
                    "stream": False
                },
                timeout=120
            )

            if response.status_code == 200:
                data = response.json()
                return {
                    'success': True,
                    'message': data.get('message', {}),
                    'model': model
                }
            else:
                return {
                    'success': False,
                    'error': f"Erreur {response.status_code}"
                }

        except Exception as e:
            logger.error(f"Erreur chat: {e}")
            return {
                'success': False,
                'error': str(e)
            }
