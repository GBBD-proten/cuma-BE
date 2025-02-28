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

class IndexListController: 
    def __init__(self, request):
        self.client = client

    def get_index_list(self):
        get_alias = self.client.indices.get_alias()
        
        index_list = []
        for index in get_alias:
            kor_index = ""
            if(index == "site_dc"):
                kor_index = "디씨인사이드"
            elif(index == "site_fmkorea"):
                kor_index = "FM코리아"
                
            index_json = {
                "indexName": index,
                "korIndexName": kor_index
            }
            index_list.append(index_json)
            
        result = {
            "status": "success",
            "result": index_list,
        }
        
        return result
    
    



