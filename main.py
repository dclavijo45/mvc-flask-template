from config import PORT, HOST, DEBUG
from __init__ import app

if __name__ == "__main__":
    app.run(host=HOST, port=PORT, debug=bool(DEBUG))
