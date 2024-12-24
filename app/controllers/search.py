from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, Q
import logging
from app.config import Config


elasticsearch_url = Config.ELASTICSEARCH_URL
logging.info(f"Elasticsearch URL: {elasticsearch_url}")
client = Elasticsearch(
    hosts=[elasticsearch_url],
    # request_timeout=30,
    # max_retries=3,
    # retry_on_timeout=True,
    # compatibility_mode=True, # 호환성 모드 활성화
    # headers={"Content-Type": "application/json"}
)

class ElasticSearchController: 
    def __init__(self, request):
        self.client = client
        self.query = request.args.get('query', '')
        self.index = request.args.get('index', 'dc_lol')
        self.size = int(request.args.get('size', 10))

    def search_documents(self):
        try:
            # Elasticsearch-dsl Search 객체 생성
            search = Search(using=self.client, index=self.index)
            
            # 검색 쿼리 생성
            query = Q('multi_match', query=self.query, fields=['subject', 'content'], fuzziness='AUTO')
            search = search.query(query)
            
            # 검색 실행
            response = search.execute()
            
            results = []
                
            for hit in response:
                results.append(hit.to_dict())
                
            return {
                'total': response['hits']['total']['value'],
                'results': results
            }
            
        except Exception as e:
            logging.error(f"Elasticsearch : {elasticsearch_url}")
            logging.error(f"Elasticsearch 검색 중 오류 발생: {str(e)}")
            raise

    
    



