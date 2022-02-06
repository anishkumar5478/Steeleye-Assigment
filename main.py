import datetime as dt
from fastapi import FastAPI ,Path, Query
from typing import Optional
from pydantic import BaseModel, Field
from fake_DB import Trade , TradeDetails;



app = FastAPI()




class tradeDetails(BaseModel):
    buySellIndicator: str = Field(description="A value of BUY for buys, SELL for sells.")

    price: float = Field(description="The price of the Trade.")

    quantity: int = Field(description="The amount of units traded.")


class trade(BaseModel):
    asset_class: Optional[str] = Field(alias="assetClass", default=None, description="The asset class of the instrument traded. E.g. Bond, Equity, FX...etc")

    counterparty: Optional[str] = Field(default=None, description="The counterparty the trade was executed with. May not always be available")

    instrument_id: str = Field(alias="instrumentId", description="The ISIN/ID of the instrument traded. E.g. TSLA, AAPL, AMZN...etc")

    instrument_name: str = Field(alias="instrumentName", description="The name of the instrument traded.")

    trade_date_time: dt.datetime = Field(alias="tradeDateTime", description="The date-time the Trade was executed")

    trade_details: tradeDetails = Field(alias="tradeDetails", description="The details of the trade, i.e. price, quantity")

    trader: Optional[str] = Field(default=None, description="The trader that executed the trade.")




@app.get("/")
def index():
    return {"Name": "steeleye limited"}


#  ----------------------SEAERCH TRADES (queary parameter) ----------------------


#------------ SEARCH TRADES BY COUNTER_PARTY  ------------
@app.get("/trades/get-by-counterparty")
def get_trades(*,counterparty:str=Query(None, description="The counterparty the trade eg. Tesla ,Apple,jaguar...etc")):
    
    for trade_id in Trade:
        if Trade[trade_id]["counterparty"] == counterparty:
            return Trade[trade_id]
    return {"error":"trade not found"}



#------------ SEARCH TRADES BY INSTRUMENT_ID ------------

@app.get("/trades/get-by-instrumentId")
def get_by_instrumentId(*,instrument_id:str=Query(None, description="The ISIN/ID of the instrument eg. TSLA, AAPL, AMZN...etc")):
    for trade_id in Trade:
        if Trade[trade_id]["instrument_id"] == instrument_id:
            return Trade[trade_id]
    return {"error":"trade not found"}  



#------------ SEARCH TRADES BY INSTRUMENT_NAME  ------------

@app.get("/trades/get-by-instrumentName")
def get_by_instrumentName(*,instrument_name:Optional[str]=Query(None, description="The name of the instrument eg. ABC, DEF, ...etc")):
    for trade_id in Trade:
        if Trade[trade_id]["instrument_name"] == instrument_name:
            return Trade[trade_id]
    return {"error":"trade not found"}


#------------ SEARCH TRADES BY TRADER  ------------
@app.get("/trades/get-by-trader")
def get_by_trader(*,trader:str=Query(None, description="The Single trade information by trader eg. John, Jane,ambani ...etc")):
    for trade_id in Trade:
        if Trade[trade_id]["trader"] == trader:
            return Trade[trade_id]
    return {"error":"trade not found"}



# ---------ADVANCED SEARCH TRADES (query parameters) ----------

# ----------- BY MINPRICE -----------

# -----------------optional query parameters
@app.get("/trades/values/get-by-minPrice")
def get_by_minPrice(*,minPrice:float=Query(None, description="The minimum price of the trade eg 100.00,200")):
    for trade_id in Trade:
        if Trade[trade_id]["trade_details"]["price"] >= minPrice:
            return Trade[trade_id]
    return {"error":"trade not found"}


@app.get("/trade/minprice")
def get_minprice(*,minprice:int=Query(None, description="The minimum price of the trade")):
    for trade_id in Trade:
        if Trade[trade_id]["trade_details"]["price"] >= minprice:
            return Trade[trade_id]
    return {"error":"trade not found"}

#----------------BY MAXPRICE ------------
@app.get("/trade/maxprice")
def get_maxprice(*,maxprice:Optional[int]=None):
    for trade_id in Trade:
        if Trade[trade_id]["trade_details"]["price"] <= maxprice:
            return Trade[trade_id]
    return {"error":"trade not found"} 

#------------MIN_MAX_PRICE ------------
@app.get("/trade/get_by_min_max_price")
def get_by_min_max_price(*,min_price:Optional[int]=None,max_price:Optional[int]=None):
    
    for trade_id in Trade:
        if Trade[trade_id]["trade_details"]["price"] >= min_price and Trade[trade_id]["trade_details"]["price"] <= max_price:
            
            return Trade[trade_id]
    return {"error":"trade not found in this range "}

    
#------------BETWEEN STARTD DATE AND  END DATE ------------

@app.get("/trade/get_by_start_end_date")
def get_by_start_end_date(*,start_date:Optional[dt.datetime]=None,end_date:Optional[dt.datetime]=None):
    for trade_id in Trade:
        if Trade[trade_id]["trade_date"] >= start_date and Trade[trade_id]["trade_date"] <= end_date:
            return Trade[trade_id]
    return {"error":"trade not found in this date range "}


@app.get("/trade/get_by_tradeType")
def get_by_tradeType(*,trade_type:Optional[str]=Query(None, description="trade details")):
    for trade_id in Trade:
        if Trade[trade_id]["trade_details"]["trade_type"] == trade_type:
            return Trade[trade_id]
    return {"error":"trade not found"}


@app.get("/trade/get_by_buySellIndicator")
def get_by_buySellIndicator(*,buySellIndicator:Optional[str]=Query(None, description="search by trade type e,g sell,buy")):
    for trade_id in Trade:
        if Trade[trade_id]["trade_details"]["buySellIndicator"] == buySellIndicator:
            return Trade[trade_id]
    return {"error":"trade not found"}
    


@app.get("/trade/get_by_asset_class")
def get_by_asset_class(*,asset_class:Optional[str]=Query(None, description="search by asset class e,g Equity,FixedIncome,Derivative")):
    for trade_id in Trade:
        if Trade[trade_id]["asset_class"] == asset_class:
            return Trade[trade_id]
    return {"error":"trade not found"}




@app.get("/trade/")
def get_all_trades():
    return Trade

@app.get("/trade/{trade_id}")
def get_trade_by_id(trade_id:int=Path(None, description="The Single trade information by id",gt=0)):
    return Trade.get(trade_id)
    

@app.post("/create_trade/{trade_id}")
def create_trade(trade_id:int,Trades:trade):

    if trade_id in Trade:
        return {"error":"trade already exists"}
    Trade[trade_id] = Trades
    return Trade[trade_id]




#------------------------------------------------BONOUS  POINTS------------------------------------

# ------------------PAGINATION-------------------------------------------------
data =list(Trade.items())
data_length = len(data)

{
    "data":[...],
    "pagination":{
        "next_page":"Link to next page",
        "previous_page":"Link to previous page",
    },
    "count":"total no of items",
    "total":"total no of pages"
}




@app.get('/pagination/')
def get_bonous(page_num:int=1,page_size:int=10):
    start= (page_num-1)*page_size
    end= page_num*page_size
    
    response={
        "data":data[start:end],
        "total":data_length,
        "count":page_size,
        "pagination":{}     
    }

    if end >= data_length:
        response["pagination"]["next_page"]=None

        if page_num > 1:
            response["pagination"]["previous_page"]=f"http://localhost:8000/pagination/?page_num={page_num-1}&page_size={page_size}"
        else:
            response["pagination"]["previous_page"]=None

    else:
        if page_num >1:
            response["pagination"]["previous_page"]=f"http://localhost:8000/pagination/?page_num={page_num-1}&page_size={page_size}"
        else:
            response["pagination"]["previous_page"]=None

        response["pagination"]["next_page"]=f"http://localhost:8000/pagination/?page_num={page_num+1}&page_size={page_size}"

    return response

#-------------------END OF PAGINATION______-------------------------------


#--------------sorting------------------------------------------------------
@app.get("/sort/")
def get_sort():
    return sorted(Trade.items(),key=lambda x:x[1]["trade_details"]["price"])





        




    


