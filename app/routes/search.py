from flask import Blueprint, request, jsonify
from flask_restx import Namespace, Resource
import logging
from elasticsearch import ConnectionError, RequestError
from app.controllers.search import ElasticSearchController

# 검색 Namespace 생성
search_ns = Namespace('search', description='검색 관련 API')

def getSwaggerParams():
    return {
       'query': {'description': '검색어', 'type': 'string'},
       'index': {'description': '검색할 인덱스', 'type': 'string', 'default': 'site_*'},
       'size': {'description': '결과 개수', 'type': 'integer', 'default': 10},
       'page': {'description': '페이지 번호', 'type': 'integer', 'default': 1},
       'dateRange': {'description': '날짜 검색 (YYYYMMDDHHMMSS OR YYYYMMDD)', 'type': 'string'},
       'sort': {'description': '정렬 (date, view, like)', 'type': 'string', 'default': 'date'},
       'order': {'description': '정렬 순서 (desc, asc)', 'type': 'string', 'default': 'desc'}
   }

# 내림차순 검색 라우트
@search_ns.route('/')
class SearchDescAPI(Resource):
    @search_ns.doc(
        params=getSwaggerParams()
    )
    def get(self):
        try:
            search_controller = ElasticSearchController(request)
            result = search_controller.search()
            return result
        except ConnectionError as e:
            logging.error(f"Elasticsearch Connection Error: {str(e)}")
            return {'status': 'error', 'message': str(e)}, 503
        except RequestError as e:
            logging.error(f"Search Request Error: {str(e)}")
            return {'status': 'error', 'message': str(e)}, 400
        except ValueError as e:
            logging.error(f"Parameter Error: {str(e)}")
            return {'status': 'error', 'message': str(e)}, 400
        except Exception as e:
            logging.error(f"Unexpected Search Error: {str(e)}")
            return {'status': 'error', 'message': str(e)}, 500