from fastapi import APIRouter, Request, HTTPException, Query
from typing import Optional, Sequence
from database.models import ResponseModel
import pdb

router = APIRouter()


@router.get('/status')
async def get_status():
    try:
        return {"Health OK"}

    except Exception as e:
        return {'Error: ' + str(e)}
    

@router.get('/')
async def home_page():
    try:
        return {"Home Page"}
    except Exception as e:
        return {"Error:" + str(e)}
    

'''
Router for Business and Symptom Data
Optional Parameters: business_id, diagnostic
'''
@router.get('/business/', status_code=200) #response_model=ResponseModel
async def get_business(
    request: Request, 
    business_id: Optional[int] = Query(None, example=1104), 
    diagnostic: Optional[str] = Query(None, example="True"),
    ) -> dict:

    keyQueries = ['business_id', 'diagnostic']
    parameters =  request.query_params.keys()

    pdb.set_trace()

    if 'diagnostic' in parameters:
        diagnostic = str(request.query_params['diagnostic'])
    if 'business_id' in parameters:
        business_id = request.query_params['business_id']
    if diagnostic is None and business_id is None:
        raise HTTPException(status_code=404, detail="Invalid request, Please pass valid business_id or diagnostic")

    result = {'value': 'business detail'}
    return result
