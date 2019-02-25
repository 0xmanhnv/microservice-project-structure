import os
from src.app import create_app

env = os.environ.get('APP_ENV', 'dev')
app = create_app(env)

if __name__ == '__main__':
    app.run(debug=True, threaded=True, port=8000)
