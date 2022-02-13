from app import create_app
from config.config import DevelopmentConfig

app = create_app(config=DevelopmentConfig)

if __name__ == "__main__":
    app.run(debug=True)
