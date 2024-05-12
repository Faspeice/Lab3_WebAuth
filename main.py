from app.app import bp
from app.init import db,app
with app.app_context():
    db.create_all()
if __name__ == '__main__':
    app.register_blueprint(bp)
    app.run()



