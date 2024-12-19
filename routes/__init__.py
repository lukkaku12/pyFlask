from routes.user_routes import user_bp
from routes.post_routes import post_bp

def register_routes(app):
    app.register_blueprint(user_bp, url_prefix="/api")
    app.register_blueprint(post_bp, url_prefix="/api")