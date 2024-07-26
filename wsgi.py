from app import app
from settings import PORT

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=PORT, debug=True)
