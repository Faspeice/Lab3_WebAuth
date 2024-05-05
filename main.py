from app.app import app
from app.init import db
with app.app_context():
    db.create_all()
if __name__ == '__main__':
    app.run()



