from flask import Blueprint, request, jsonify
from flask_restx import Namespace, Resource
import logging
from elasticsearch import ConnectionError, RequestError
from app.controllers import IndexListController

# 검색 Namespace 생성
indexList_ns = Namespace('indexList', description='인덱스 목록 관련 API')

# 기본 검색 라우트
@indexList_ns.route('/')
class IndexListAPI(Resource):
    @indexList_ns.doc()
    def get(self):
        indexList_controller = IndexListController(request)
        try:
            result = indexList_controller.get_index_list()
            return result
        except ConnectionError as e:
            logging.error(f"Elasticsearch 연결 오류: {str(e)}", exc_info=True)
            return jsonify({'error': 'Search 서비스에 연결할 수 없습니다'}), 503
        except RequestError as e:
            logging.error(f"검색 쿼리 오류: {str(e)}", exc_info=True)
            return jsonify({'error': '잘못된 검색 요청입니다'}), 400
        except Exception as e:
            logging.error(f"예상치 못한 검색 오류: {str(e)}", exc_info=True)
            return jsonify({'error': '서버 내부 오류가 발생했습니다'}), 500