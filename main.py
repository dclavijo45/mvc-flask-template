from database.integrations.ma_integration import ma
from database.integrations.db_integration import db
from database.migrate import define_models
from config import PORT, HOST, DEBUG
from __init__ import app

db.init_app(app)
ma.init_app(app)

with app.app_context():
    define_models()
    db.create_all()

app.run(host=HOST, port=PORT, debug=bool(DEBUG))