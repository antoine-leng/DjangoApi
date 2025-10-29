git clone https://github.com/antoine-leng/projet-django.git

cd projet-django

python -m venv .venv

source .venv/bin/activate   # macOS / Linux
# ou
.venv\Scripts\activate      # Windows

pip install -r requirements.txt

Créer le fichier .env 
exemple:
"""
DEBUG=True
SECRET_KEY=""""ta_cle_générée_ici""""
ALLOWED_HOSTS=localhost,127.0.0.1
"""

python manage.py migrate

python manage.py runserver
