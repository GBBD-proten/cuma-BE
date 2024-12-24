from flask import Blueprint, request, jsonify
from flask_restx import Namespace, Resource
import logging
from elasticsearch import ConnectionError, RequestError
from app.controllers.search import ElasticSearchController

# 검색 Namespace 생성
search_ns = Namespace('search', description='검색 관련 API')

# 기본 검색 라우트
@search_ns.route('/')
class SearchAPI(Resource):
    @search_ns.doc(params={
       'query': {'description': '검색어', 'in': 'query', 'type': 'string'},
       'index': {'description': '검색할 인덱스', 'in': 'query', 'type': 'string', 'default': 'dc_lol'},
       'size': {'description': '결과 개수', 'in': 'query', 'type': 'integer', 'default': 10}
   })
    def get(self):
        search_controller = ElasticSearchController(request)
        try:
            result = search_controller.search_documents()
            return result
        except ConnectionError as e:
            logging.error(f"Elasticsearch 연결 오류: {str(e)}", exc_info=True)
            return jsonify({'error': 'Search 서비스에 연결할 수 없습니다'}), 503
        except RequestError as e:
            logging.error(f"검색 쿼리 오류: {str(e)}", exc_info=True)
            return jsonify({'error': '잘못된 검색 요청입니다'}), 400
        except Exception as e:
            logging.error(f"예상치 못한 검색 오류: {str(e)}", exc_info=True)
            logging.error(f"예상치 못한 검색 오류: {result}", exc_info=True)
            return jsonify({'error': '서버 내부 오류가 발생했습니다'}), 500

