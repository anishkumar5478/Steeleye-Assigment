# FastAPI

This is API code developed over FastAPI usign python.

**FastAPI**
FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.

**FastAPI's** usage of **Pydantic** for expressing data types aligns quite well with how we model our own Schema models (using Pydantic).

**Uvicorn** is used to run the API server.

**Note this code developed for testing and assesment pourposes and is not ready for production**

To Run this code on your system please follow the following:

1. Python V3.6+ should be installed on your system.([Click here](https://www.python.org/downloads/) to download lastes version of python).
2. Open command prompt and run the following command to installed all the required libraries.\


Install fastapi 
```
pip install fastapi
```

install uvicorn

```
pip install uvicorn
```

install pydentic

```
pip install pydantic
```
Navigate to projectes repository

Run the following command to start the server
```
uvicorn main:app
```

Now open the mentioned localhost post port on your browser default(http://localhost:8000).

Navigate to API docs by adding **/docs** at the end of your localhost link for ex: http://localhost:8000/docs

Now execute the mentioned api's to test the enpoints.

```**/index**```
This endpoint returns the defaul home page for the api.


```**/get-by-counterparty**```
This endpoint returns TRADES BY COUNTER_PARTY


```**/trades/get-by-instrumentId**```
This endpoint returns TRADES BY INSTRUMENT_ID. 

```**/trades/get-by-instrumentName**```

This endpoint returns TRADES BY INSTRUMENT_NAME.

```**/trades/get-by-trader**```

This endpoint returns TRADES BY TRADER

```**/trades/values/get-by-minPrice**```
This end point accepts an integers value as query parameter and return the trades minimum price mentioned.

```**/trade/minprice**```
This endpoint returns trade with minimum price with threhosld value sent as query parameter.

```**/trade/maxprice**```
This endpoint returns trades with maximum price with threhosld value sent as query parameter.

```**/trade/get_by_min_max_price**```
This endpoint returns trades within range of price values sent as query parameters

```**/trade/get_by_start_end_date**```
This endpoint returns trades within  date range of sent as query parameters. 

```**/trade/get_by_tradeType**```
This endpoint returns tades by trade type.

```**/trade/get_by_buySellIndicator**```
This endpoint returns tades by Buy-Sell Indicator.

```**/trade/get_by_asset_class**```
This endpoint returns tades by assets class.

```**/trade/**```
This endpoint returns all the listed trades

```**/trade/{trade_id}**```
This endpoint returns trades by the trade id enteres in query parameter field.

```**/create_trade/{trade_id}**```

This endpoint creates a trade in the datbase

**BONOUS POINT**
```**/pagination/**``` 
This is a pagination endpoint where large number of trades are returned in pages(user has to enter page nunmber and page size)

```**/sort/**```
This endpoitn returns trades in sorted order.







