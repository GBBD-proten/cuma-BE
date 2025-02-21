from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search
import logging

from app.config import Config

from app.utils.paging import Paging

logging.basicConfig(level=logging.INFO)  # 로그 레벨 설정
logger = logging.getLogger(__name__)

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
        self.index = request.args.get('index', '')
        self.size = int(request.args.get('size', 10))
        self.page = int(request.args.get('page', 1))
        
        dateRange = request.args.get('dateRange', '')
        if('/' in dateRange):
            dateRange = dateRange.split(',')
            self.startDate = dateRange[0]
            self.endDate = dateRange[1]
        else:
            self.startDate = ''
            self.endDate = ''
            
        logger.info(f"query: {self.query}, index: {self.index}, size: {self.size}, page: {self.page}, startDate: {self.startDate}, endDate: {self.endDate}")


    def search_documents(self):
        try:
            # Elasticsearch-dsl Search 객체 생성
            search = Search(using=self.client, index=self.index)
            
            # 검색 쿼리 생성
            if(self.query != ''):
                search = search.query('multi_match', query=self.query, fields=['subject', 'content'], fuzziness='AUTO')
            else:
                search = search.query('match_all')
                
            # 날짜 쿼리 생성
            if(self.startDate != '' and self.endDate != ''):
                search = search.filter('range', date={'gte': self.startDate, 'lte': self.endDate})
                
            # 페이징 쿼리 생성성   
            paging = Paging(self.page, self.size)
            search = search.extra(from_=str(paging.startNum), size=str(self.size))

            logger.info(f"search query: {search.to_dict()}")
            
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

    
    



