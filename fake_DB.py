import datetime as dt
from fastapi import FastAPI ,Path
from typing import Optional
from pydantic import BaseModel, Field





TradeDetails ={

    1:{
        "buySellIndicator":"buy",
        "price":100,
        "quantity":500,
    },
    2:{
        "buySellIndicator":"sell",
        "price":250,
        "quantity":100,

    },
    3:{
        "buySellIndicator":"SEll",
        "price":200,
        "quantity":800,
    },


    4:{

        "buySellIndicator":"Sell",
        "price":1000,
        "quantity":12,
    },
    5:{
        "buySellIndicator":"sell",
        "price":100.00,
        "quantity":1,

    },
    6:{
        "buySellIndicator":"buy",
        "price":925,
        "quantity":2,
    },

    7:{
        "buySellIndicator":"Buy",
        "price":650,
        "quantity":5,
    },
    8:{
        "buySellIndicator":"sell",
        "price":980,
        "quantity":10,

    },
    9:{
        "buySellIndicator":"BUY",
        "price":300,
        "quantity":420,
    },

    10:{
        "buySellIndicator":"buy",
        "price":100,
        "quantity":50,
    },
    11:{
        "buySellIndicator":"sell",
        "price":320,
        "quantity":200,

    },

     12:{
        "buySellIndicator":"sell",
        "price":620,
        "quantity":90,
    },
    13:{
        "buySellIndicator":"buy",
        "price":300,
        "quantity":150,
    },

    14:{
        "buySellIndicator":"sell",
        "price":950,
        "quantity":1000,
    },
    15:{
        "buySellIndicator":"sell",
        "price":780,
        "quantity":200,

    },
    16:{
        "buySellIndicator":"sell",
        "price":400,
        "quantity":300,
    },

    17:{
        "buySellIndicator":"buy",
        "price":1,
        "quantity":100,
    },
    18:{
        "buySellIndicator":"sell",
        "price":2,
        "quantity":200,

    },
    19:{
        "buySellIndicator":"buy",
        "price":300,
        "quantity":0,
    },

    20:{
        "buySellIndicator":"buy",
        "price":120,
        "quantity":60,
    },
    21:{
        "buySellIndicator":"sell",
        "price":240,
        "quantity":40,

    },
    22:{
        "buySellIndicator":"sell",
        "price":390,
        "quantity":300,
    },
        23:{
        "buySellIndicator":"sell",
        "price":100,
        "quantity":100,
    },
    24:{
        "buySellIndicator":"sell",
        "price":200,
        "quantity":200,

    },
    25:{
        "buySellIndicator":"buy",
        "price":300,
        "quantity":300,
    },


    
    26:{
        "buySellIndicator":"buy",
        "price":100,
        "quantity":100,
    },
    27:{
        "buySellIndicator":"sell",
        "price":258,
        "quantity":200,

    },
    28:{
        "buySellIndicator":"sell",
        "price":376,
        "quantity":300,
    },

    29:{
        "buySellIndicator":"buy",
        "price":100,
        "quantity":100,
    },
    30:{
        "buySellIndicator":"sell",
        "price":200,
        "quantity":200,

    },
    31:{
        "buySellIndicator":"buy",
        "price":300,
        "quantity":300,
    },

    32:{
        "buySellIndicator":"sell",
        "price":100,
        "quantity":100,
    },
    33:{
        "buySellIndicator":"sell",
        "price":200,
        "quantity":200,

    },
    34:{
        "buySellIndicator":"buy",
        "price":300,
        "quantity":300,
    },
   35:{
        "buySellIndicator":"buy",
        "price":100,
        "quantity":100,
    },
    36:{
        "buySellIndicator":"sell",
        "price":800,
        "quantity":1500,

    },
    37:{
        "buySellIndicator":"buy",
        "price":20,
        "quantity":500,
    },
   38:{
        "buySellIndicator":"buy",
        "price":100,
        "quantity":100,
    },
    39:{
        "buySellIndicator":"sell",
        "price":1200,
        "quantity":450,

    },
    34:{
        "buySellIndicator":"buy",
        "price":700,
        "quantity":250,
        }

    
   

    
    

}

Trade ={
    1:{
        "asset_class":"Bond",
        "counterparty":"Tesla",
        "instrument_id":"TSLA",
        "instrument_name":"ABC",
        "trade_date":dt.datetime.now(),
        "trade_details":TradeDetails[1],
        "trader":"ABC",
        

        
        },
    
    2:{
            "asset_class":"Equity",
            "counterparty":"Mahiendra",
            "instrument_id":"AAPL",
            "instrument_name":"Apple",
            "trade_date":dt.datetime.now(),
            "trade_details":TradeDetails[2],
            "trader":"DEF",
           
            },


            
    3:{
         
            "asset_class":"FX",
            "counterparty":"jaguar",
            "instrument_id":"AAPL",
            "instrument_name":"abc",
            "trade_date":dt.datetime.now(),
            "trade_details":TradeDetails[3],
            "trader":"DEF",
           },



    4:{
        "asset_class":"Bond",
        "counterparty":"tesla",
        "instrument_id":"AMZN",
        "instrument_name":"ABC",
        "trade_date":dt.datetime.now(),
        "trade_details":TradeDetails[4],
        "trader":"ABC",
        

        
        },
    
    5:{
            "asset_class":"Equity",
            "counterparty":"mahiendra",
            "instrument_id":"AAPL",
            "instrument_name":"DEF",
            "trade_date":dt.datetime.now(),
            "trade_details":TradeDetails[5],
            "trader":"DEF",
           
            },


            
    6:{
         
            "asset_class":"Equity",
            "counterparty":"apple",
            "instrument_id":"AAPL",
            "instrument_name":"DFG",
            "trade_date":dt.datetime.now(),
            "trade_details":TradeDetails[6],
            "trader":"DEF",
           },
    7:{
        "asset_class":"Bond",
        "counterparty":"Tesla",
        "instrument_id":"TSLA",
        "instrument_name":"ABC",
        "trade_date":dt.datetime.now(),
        "trade_details":TradeDetails[7],
        "trader":"ABC",
        

        
        },
    
    8:{
            "asset_class":"FixedIncome",
            "counterparty":"mama",
            "instrument_id":"AAPL",
            "instrument_name":"DEF",
            "trade_date":dt.datetime.now(),
            "trade_details":TradeDetails[8],
            "trader":"DEF",
           
            },


            
    9:{
         
            "asset_class":"Derivative",
            "counterparty":"alibaba",
            "instrument_id":"AAPL",
            "instrument_name":"DFG",
            "trade_date":dt.datetime.now(),
            "trade_details":TradeDetails[9],
            "trader":"Ambani",
           },
    10:{
        "asset_class":"Bond",
        "counterparty":"Tesla",
        "instrument_id":"TSLA",
        "instrument_name":"ABC",
        "trade_date":dt.datetime.now(),
        "trade_details":TradeDetails[10],
        "trader":"ambani",
    },
    11:{
        "asset_class":"Bond",
        "counterparty":"Tesla",
        "instrument_id":"TSLA",
        "instrument_name":"ABC",
        "trade_date":dt.datetime.now(),
        "trade_details":TradeDetails[11],
        "trader":"Bilgates",
        

        
        },
    
    12:{
            "asset_class":"Equity",
            "counterparty":"Samsung",
            "instrument_id":"AAPL",
            "instrument_name":"DEF",
            "trade_date":dt.datetime.now(),
            "trade_details":TradeDetails[12],
            "trader":"John",
           
            },


            
    13:{
         
            "asset_class":"Equity",
            "counterparty":"jaguar",
            "instrument_id":"AAPL",
            "instrument_name":"DFG",
            "trade_date":dt.datetime.now(),
            "trade_details":TradeDetails[13],
            "trader":"John",
           },



    14:{
        "asset_class":"Bond",
        "counterparty":"Tesla",
        "instrument_id":"TSLA",
        "instrument_name":"ABC",
        "trade_date":dt.datetime.now(),
        "trade_details":TradeDetails[14],
        "trader":"john",
        

        
        },
    
    15:{
            "asset_class":"Equity",
            "counterparty":"Mahiendra",
            "instrument_id":"AAPL",
            "instrument_name":"DEF",
            "trade_date":dt.datetime.now(),
            "trade_details":TradeDetails[15],
            "trader":"Jane",
           
            },


            
    16:{
         
            "asset_class":"Equity",
            "counterparty":"jaguar",
            "instrument_id":"Aydf",
            "instrument_name":"DFG",
            "trade_date":dt.datetime.now(),
            "trade_details":TradeDetails[16],
            "trader":"jane",
           },
    17:{
        "asset_class":"Bond",
        "counterparty":"Tesla",
        "instrument_id":"TSLA",
        "instrument_name":"ABC",
        "trade_date":dt.datetime.now(),
        "trade_details":TradeDetails[17],
        "trader":"ABC",
        

        
        },
    
    18:{
            "asset_class":"Equity",
            "counterparty":"Mahiendra",
            "instrument_id":"AAPL",
            "instrument_name":"DEF",
            "trade_date":dt.datetime.now(),
            "trade_details":TradeDetails[18],
            "trader":"DEF",
           
            },


            
    19:{
         
            "asset_class":"Equity",
            "counterparty":"jaguar",
            "instrument_id":"AAPL",
            "instrument_name":"DFG",
            "trade_date":dt.datetime.now(),
            "trade_details":TradeDetails[19],
            "trader":"DEF",
           },
    20:{
        "asset_class":"Bond",
        "counterparty":"Tesla",
        "instrument_id":"TSLA",
        "instrument_name":"ABC",
        "trade_date":dt.datetime.now(),
        "trade_details":TradeDetails[20],
        "trader":"ABC",
    },

    21:{
        "asset_class":"Bond",
        "counterparty":"Tesla",
        "instrument_id":"TSLA",
        "instrument_name":"ABC",
        "trade_date":dt.datetime.now(),
        "trade_details":TradeDetails[21],
        "trader":"ABC",
        

        
        },
    
    22:{
            "asset_class":"Equity",
            "counterparty":"Mahiendra",
            "instrument_id":"AAPL",
            "instrument_name":"DEF",
            "trade_date":dt.datetime.now(),
            "trade_details":TradeDetails[22],
            "trader":"DEF",
           
            },


            
    23:{
         
            "asset_class":"Equity",
            "counterparty":"jaguar",
            "instrument_id":"AAPL",
            "instrument_name":"DFG",
            "trade_date":dt.datetime.now(),
            "trade_details":TradeDetails[23],
            "trader":"DEF",
           },



    24:{
        "asset_class":"Bond",
        "counterparty":"Tesla",
        "instrument_id":"TSLA",
        "instrument_name":"ABC",
        "trade_date":dt.datetime.now(),
        "trade_details":TradeDetails[24],
        "trader":"ABC",
        

        
        },
    
    25:{
            "asset_class":"Equity",
            "counterparty":"Mahiendra",
            "instrument_id":"AAPL",
            "instrument_name":"DEF",
            "trade_date":dt.datetime.now(),
            "trade_details":TradeDetails[25],
            "trader":"DEF",
           
            },


            
    26:{
         
            "asset_class":"Equity",
            "counterparty":"jaguar",
            "instrument_id":"AAPL",
            "instrument_name":"DFG",
            "trade_date":dt.datetime.now(),
            "trade_details":TradeDetails[26],
            "trader":"DEF",
           },
    27:{
        "asset_class":"Bond",
        "counterparty":"Tesla",
        "instrument_id":"TSLA",
        "instrument_name":"ABC",
        "trade_date":dt.datetime.now(),
        "trade_details":TradeDetails[27],
        "trader":"ABC",
        

        
        },
    
    28:{
            "asset_class":"Equity",
            "counterparty":"Mahiendra",
            "instrument_id":"AAPL",
            "instrument_name":"DEF",
            "trade_date":dt.datetime.now(),
            "trade_details":TradeDetails[28],
            "trader":"DEF",
           
            },


            
    29:{
         
            "asset_class":"Equity",
            "counterparty":"jaguar",
            "instrument_id":"AAPL",
            "instrument_name":"DFG",
            "trade_date":dt.datetime.now(),
            "trade_details":TradeDetails[29],
            "trader":"DEF",
           },
    30:{
        "asset_class":"Bond",
        "counterparty":"Tesla",
        "instrument_id":"TSLA",
        "instrument_name":"ABC",
        "trade_date":dt.datetime.now(),
        "trade_details":TradeDetails[30],
        "trader":"ABC",
    },
    31:{
        "asset_class":"Bond",
        "counterparty":"Tesla",
        "instrument_id":"TSLA",
        "instrument_name":"ABC",
        "trade_date":dt.datetime.now(),
        "trade_details":TradeDetails[31],
        "trader":"ABC",
        

        
        },
    
    32:{
            "asset_class":"Equity",
            "counterparty":"Mahiendra",
            "instrument_id":"AAPL",
            "instrument_name":"DEF",
            "trade_date":dt.datetime.now(),
            "trade_details":TradeDetails[32],
            "trader":"DEF",
           
            },


            
    33:{
         
            "asset_class":"Equity",
            "counterparty":"jaguar",
            "instrument_id":"AAPL",
            "instrument_name":"DFG",
            "trade_date":dt.datetime.now(),
            "trade_details":TradeDetails[33],
            "trader":"DEF",
           },



    34:{
        "asset_class":"Bond",
        "counterparty":"Tesla",
        "instrument_id":"TSLA",
        "instrument_name":"ABC",
        "trade_date":dt.datetime.now(),
        "trade_details":TradeDetails[34],
        "trader":"ABC",
        

        
        },
    
    35:{
            "asset_class":"Equity",
            "counterparty":"Mahiendra",
            "instrument_id":"AAPL",
            "instrument_name":"DEF",
            "trade_date":dt.datetime.now(),
            "trade_details":TradeDetails[35],
            "trader":"DEF",
           
            },


            
    36:{
         
            "asset_class":"Equity",
            "counterparty":"jaguar",
            "instrument_id":"AAPL",
            "instrument_name":"DFG",
            "trade_date":dt.datetime.now(),
            "trade_details":TradeDetails[36],
            "trader":"DEF",
           },
    37:{
        "asset_class":"Bond",
        "counterparty":"Tesla",
        "instrument_id":"TSLA",
        "instrument_name":"ABC",
        "trade_date":dt.datetime.now(),
        "trade_details":TradeDetails[37],
        "trader":"ABC",
        

        
        },
    
    38:{
            "asset_class":"Equity",
            "counterparty":"Mahiendra",
            "instrument_id":"AAPL",
            "instrument_name":"DEF",
            "trade_date":dt.datetime.now(),
            "trade_details":TradeDetails[38],
            "trader":"DEF",
           
            },


            
    39:{
         
            "asset_class":"Equity",
            "counterparty":"jaguar",
            "instrument_id":"AAPL",
            "instrument_name":"DFG",
            "trade_date":dt.datetime.now(),
            "trade_details":TradeDetails[39],
            "trader":"DEF",
           },
    40:{
        "asset_class":"Bond",
        "counterparty":"Tesla",
        "instrument_id":"TSLA",
        "instrument_name":"ABC",
        "trade_date":dt.datetime.now(),
        "trade_details":TradeDetails[4],
        "trader":"ABC",
    }





      
}
