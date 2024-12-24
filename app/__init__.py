from flask import Flask
from flask_cors import CORS
from flask_restx import Api
from app.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # CORS 설정
    CORS(app)
    
    # Swagger UI 설정
    api = Api(app,
            title='커뮤니티마스터 API',
            version='1.0',
            description='커뮤니티마스터 API',
            doc='/docs')  # Swagger UI 경로
    
    # 라우트 등록
    from app.routes import search_ns
    
    api.add_namespace(search_ns)
    
    return app