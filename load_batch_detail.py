import requests
from flask import jsonify
import os

class LoadBatchDetail():
    def __init__(self):
        self.GET_BATCH_URL = GET_BATCH_URL = "http://tpapi.tvisa.in/api/TPBatch/LoadBatchDetail"#?BatchId=1006
        
    def get_batch_details(self,Batch_id):    
        params_url = {'BatchId':Batch_id}
        r = requests.get(url = self.GET_BATCH_URL, params = params_url)
        data = r.json()
        TPBatchName = data['Data'][0]['TPBatchName']
        TPBatchId = data['Data'][0]['TPBatchId']
        TPCenterId = data['Data'][0]['TPCenterId']
        RTSPURL = data['Data'][0]['RTSPURL']
        return TPBatchName,TPBatchId,TPCenterId, RTSPURL