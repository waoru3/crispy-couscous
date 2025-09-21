[Skip to main content](https://www.mexc.com/api-docs/spot-v3/market-data-endpoints#__docusaurus_skipToContent_fallback "Skip to main content")
[![MEXC Logo](https://www.mexc.com/api-docs-assets/img/mexc-logo.svg)](https://www.mexc.com/ "https://www.mexc.com/")[SpotV3](https://www.mexc.com/api-docs/spot-v3/introduction "SpotV3")[Futures](https://www.mexc.com/api-docs/futures/update-log "Futures")[Broker](https://www.mexc.com/api-docs/broker/mexc-broker-introduction "Broker")
[](https://www.mexc.com/api-docs/spot-v3/market-data-endpoints "English")
  * [English](https://www.mexc.com/api-docs/spot-v3/market-data-endpoints "English")
  * [中文](https://www.mexc.com/zh-MY/api-docs/spot-v3/market-data-endpoints "中文")


  * [Introduction](https://www.mexc.com/api-docs/spot-v3/introduction "Introduction")
  * [Change Log](https://www.mexc.com/api-docs/spot-v3/change-log "Change Log")
  * [FAQs](https://www.mexc.com/api-docs/spot-v3/faqs "FAQs")
  * [General Info](https://www.mexc.com/api-docs/spot-v3/general-info "General Info")
  * [Market Data Endpoints](https://www.mexc.com/api-docs/spot-v3/market-data-endpoints "Market Data Endpoints")
  * [Sub-Account Endpoints](https://www.mexc.com/api-docs/spot-v3/subaccount-endpoints "Sub-Account Endpoints")
  * [Spot Account/Trade](https://www.mexc.com/api-docs/spot-v3/spot-account-trade "Spot Account/Trade")
  * [Wallet Endpoints](https://www.mexc.com/api-docs/spot-v3/wallet-endpoints "Wallet Endpoints")
  * [Websocket Market Streams](https://www.mexc.com/api-docs/spot-v3/websocket-market-streams "Websocket Market Streams")
  * [Websocket User Data Streams](https://www.mexc.com/api-docs/spot-v3/websocket-user-data-streams "Websocket User Data Streams")
  * [Rebate Endpoints](https://www.mexc.com/api-docs/spot-v3/rebate-endpoints "Rebate Endpoints")
  * [Public API Definitions](https://www.mexc.com/api-docs/spot-v3/public-api-definitions "Public API Definitions")


On this page
# Market Data Endpoints
## Download Historical Market Data[​](https://www.mexc.com/api-docs/spot-v3/market-data-endpoints#download-historical-market-data "Direct link to Download Historical Market Data")
Provides kline and trading data for all Spot pairs since 01-01-2023:[Historical Market Data](https://www.mexc.co/zh-CN/market-data-download "Historical Market Data")
## Test Connectivity[​](https://www.mexc.com/api-docs/spot-v3/market-data-endpoints#test-connectivity "Direct link to Test Connectivity")
> Response
```
{}  

```

  * **GET** `/api/v3/ping`


Test connectivity to the Rest API.
**Weight(IP):** 1
Parameter:
NONE
## Check Server Time[​](https://www.mexc.com/api-docs/spot-v3/market-data-endpoints#check-server-time "Direct link to Check Server Time")
> Response
```
{  
"serverTime":1645539742000  
}  

```

  * **GET** `/api/v3/time `


**Weight(IP):** 1
Parameter:
NONE
## API default symbol[​](https://www.mexc.com/api-docs/spot-v3/market-data-endpoints#api-default-symbol "Direct link to API default symbol")
> Request
```
GET /api/v3/defaultSymbols  

```

> Response
```
{  
"code":200,  
"data":[  
"GENE1USDT",  
"SNTUSDT",  
"SQUAWKUSDT",  
"HEGICUSDT",  
"GUMUSDT"  
],  
"msg":null  
}  

```

  * **GET** `/api/v3/defaultSymbols `


**Weight(IP):** 1
**Request**
NONE
**Response**
Name | Type | Description  
---|---|---  
symbol | string | symbol  
## Exchange Information[​](https://www.mexc.com/api-docs/spot-v3/market-data-endpoints#exchange-information "Direct link to Exchange Information")
> Response
```
{  
"symbol":"METALUSDT",  
"status":"1",  
"baseAsset":"METAL",  
"baseAssetPrecision":2,  
"quoteAsset":"USDT",  
"quotePrecision":5,  
"quoteAssetPrecision":5,  
"baseCommissionPrecision":2,  
"quoteCommissionPrecision":5,  
"orderTypes":[  
"LIMIT",  
"MARKET",  
"LIMIT_MAKER"  
],  
"isSpotTradingAllowed":true,  
"isMarginTradingAllowed":false,  
"quoteAmountPrecision":"1",  
"baseSizePrecision":"0.1",  
"permissions":[  
"SPOT",  
],  
"filters":[  
{  
"filterType":"PERCENT_PRICE_BY_SIDE",  
"bidMultiplierUp":"5",  
"askMultiplierDown":"0.2"  
},  
  
],  
"maxQuoteAmount":"2000000",  
"makerCommission":"0",  
"takerCommission":"0.0005",  
"quoteAmountPrecisionMarket":"1",  
"maxQuoteAmountMarket":"100000",  
"fullName":"Metal Blockchain",  
"tradeSideType":"1",  
"contractAddress":"xtokens",  
"st":false  
}  
  

```

  * **GET** `/api/v3/exchangeInfo`


Current exchange trading rules and symbol information
**Weight(IP):** 10
**Parameter** :
There are 3 possible options:
Method | **Example**  
---|---  
No parameter | curl -X GET "<https://api.mexc.com/api/v3/exchangeInfo>"  
symbol | curl -X GET "<https://api.mexc.com/api/v3/exchangeInfo?symbol=MXUSDT>"  
symbols | curl -X GET "<https://api.mexc.com/api/v3/exchangeInfo?symbols=MXUSDT,BTCUSDT>"  
**Response:**
Name | Type | Description  
---|---|---  
timezone | string | timezone  
serverTime | long | server Time  
rateLimits | Array | rate Limits  
exchangeFilters | Array | exchange Filters  
symbol | String | symbol  
status | String | status:1 - online, 2 - Pause, 3 - offline  
baseAsset | String | base Asset  
baseAssetPrecision | Int | base Asset Precision  
quoteAsset | String | quote Asset  
quotePrecision | Int | quote Precision  
quoteAssetPrecision | Int | quote Asset Precision  
baseCommissionPrecision | Int | base Commission Precision  
quoteCommissionPrecision | Int | quote Commission Precision  
orderTypes | Array | [Order Type](https://www.mexc.com/api-docs/spot-v3/market-data-endpoints#order_type "Order Type")  
isSpotTradingAllowed | Boolean | allow api spot trading  
isMarginTradingAllowed | Boolean | allow api margin trading  
permissions | Array | permissions  
filterType | String | filter type:PERCENT_PRICE_BY_SIDE  
bidMultiplierUp | String | bidMultiplierUp  
askMultiplierDown | String | askMultiplierDown  
maxQuoteAmount | String | max Quote Amount  
makerCommission | String | marker Commission  
takerCommission | String | taker Commission  
quoteAmountPrecision | string | min order amount  
baseSizePrecision | string | min order quantity  
quoteAmountPrecisionMarket | string | min order amount in market order  
maxQuoteAmountMarket | String | max quote Amount in market order  
tradeSideType | String | tradeSide Type:1 - All, 2 - buy order only, 3 - Sell order only, 4 - Close  
contractAddress | String | contract Address  
st | String | symbol st status:false,true  
filter parameter description:
  * lastPrice means using the latest trade price, orderPrice means the order placement price.
  * For buy orders (only for LIMIT, IMMEDIATE_OR_CANCEL, FILL_OR_KILL): `orderPrice <= lastPrice * bidMultiplierUp`
  * For sell orders: `orderPrice >= lastPrice * askMultiplierDown`


## Order Book[​](https://www.mexc.com/api-docs/spot-v3/market-data-endpoints#order-book "Direct link to Order Book")
> Response
```
{  
"lastUpdateId":1112416,  
"bids":[  
["15.00000","49999.00000"]  
],  
"asks":[  
["14.0000","1.0000"]  
]  
}  

```

  * **GET** `/api/v3/depth`


**Weight(IP):** 1
Parameter:
Name | Type | Mandatory | Description | Scope  
---|---|---|---|---  
symbol | string | YES | Symbol |   
limit | integer | NO | Returen number | default 100; max 5000  
Response:
Name | Type | Description  
---|---|---  
lastUpdateId | long | Last Update Id  
bids | list | Bid [Price, Quantity ]  
asks | list | Ask [Price, Quantity ]  
## Recent Trades List[​](https://www.mexc.com/api-docs/spot-v3/market-data-endpoints#recent-trades-list "Direct link to Recent Trades List")
> Response
```
[  
{  
"id":null,  
"price":"23",  
"qty":"0.478468",  
"quoteQty":"11.004764",  
"time":1640830579240,  
"isBuyerMaker":true,  
"isBestMatch":true  
}  
]  

```

  * **GET** `/api/v3/trades`


**Weight(IP):** 5
Parameter:
Name | Type | Mandatory | Description | Scope  
---|---|---|---|---  
symbol | string | YES |  |   
limit | integer | NO |  | Default 500; max 1000  
Response:
Name | Description  
---|---  
id | Trade id  
price | Price  
qty | Number  
quoteQty | Trade total  
time | Trade time  
isBuyerMaker | Was the buyer the maker?  
isBestMatch | Was the trade the best price match?  
## Compressed/Aggregate Trades List[​](https://www.mexc.com/api-docs/spot-v3/market-data-endpoints#compressedaggregate-trades-list "Direct link to Compressed/Aggregate Trades List")
> Response
```
[  
{  
"a":null,  
"f":null,  
"l":null,  
"p":"46782.67",  
"q":"0.0038",  
"T":1641380483000,  
"m":false,  
"M":true  
}  
]  

```

  * **GET** `/api/v3/aggTrades`


**Weight(IP):** 1
Get compressed, aggregate trades. Trades that fill at the time, from the same order, with the same price will have the quantity aggregated.
Parameters:
Name | Type | Mandatory | Description | Scope  
---|---|---|---|---  
symbol | string | YES |  |   
startTime | long | NO | Timestamp in ms to get aggregate trades from INCLUSIVE. |   
endTime | long | NO | Timestamp in ms to get aggregate trades until INCLUSIVE. |   
limit | integer | NO |  | Default 500; max 1000.  
startTime and endTime must be used at the same time.
Response:
Name | Description  
---|---  
a | Aggregate tradeId  
f | First tradeId  
l | Last tradeId  
p | Price  
q | Quantity  
T | Timestamp  
m | Was the buyer the maker?  
M | Was the trade the best price match?  
## Kline/Candlestick Data[​](https://www.mexc.com/api-docs/spot-v3/market-data-endpoints#klinecandlestick-data "Direct link to Kline/Candlestick Data")
> Response
```
[  
[  
1640804880000,  
"47482.36",  
"47482.36",  
"47416.57",  
"47436.1",  
"3.550717",  
1640804940000,  
"168387.3"  
]  
]  

```

  * **GET** `/api/v3/klines`


**Weight(IP):** 1
Kline/candlestick bars for a symbol. Klines are uniquely identified by their open time.
Parameters:
Name | Type | Mandatory | Description  
---|---|---|---  
symbol | string | YES |   
interval | ENUM | YES | ENUM: [Kline Interval](https://www.mexc.com/api-docs/spot-v3/market-data-endpoints#kline_interval "Kline Interval")  
startTime | long | NO |   
endTime | long | NO |   
limit | integer | NO | Default 500; max 1000.  
Response:
Index | Description  
---|---  
0 | Open time  
1 | Open  
2 | High  
3 | Low  
4 | Close  
5 | Volume  
6 | Close time  
7 | Quote asset volume  
## Current Average Price[​](https://www.mexc.com/api-docs/spot-v3/market-data-endpoints#current-average-price "Direct link to Current Average Price")
> Response
```
{  
"mins":5,  
"price":"9.35751834"  
}  

```

  * **GET** `/api/v3/avgPrice`


**Weight(IP):** 1
Parameters:
Name | Type | Mandatory | Description  
---|---|---|---  
symbol | string | YES |   
Response:
Name | Description  
---|---  
mins | Average price time frame  
price | Price  
## 24hr Ticker Price Change Statistics[​](https://www.mexc.com/api-docs/spot-v3/market-data-endpoints#24hr-ticker-price-change-statistics "Direct link to 24hr Ticker Price Change Statistics")
> Response
```
{  
"symbol":"BTCUSDT",  
"priceChange":"184.34",  
"priceChangePercent":"0.00400048",  
"prevClosePrice":"46079.37",  
"lastPrice":"46263.71",  
"bidPrice":"46260.38",  
"bidQty":"",  
"askPrice":"46260.41",  
"askQty":"",  
"openPrice":"46079.37",  
"highPrice":"47550.01",  
"lowPrice":"45555.5",  
"volume":"1732.461487",  
"quoteVolume":null,  
"openTime":1641349500000,  
"closeTime":1641349582808,  
"count":null  
}  
or  
[  
{  
"symbol":"BTCUSDT",  
"priceChange":"184.34",  
"priceChangePercent":"0.00400048",  
"prevClosePrice":"46079.37",  
"lastPrice":"46263.71",  
"bidPrice":"46260.38",  
"bidQty":"",  
"askPrice":"46260.41",  
"askQty":"",  
"openPrice":"46079.37",  
"highPrice":"47550.01",  
"lowPrice":"45555.5",  
"volume":"1732.461487",  
"quoteVolume":null,  
"openTime":1641349500000,  
"closeTime":1641349582808,  
"count":null  
},  
{  
"symbol":"ETHUSDT",  
"priceChange":"184.34",  
"priceChangePercent":"0.00400048",  
"prevClosePrice":"46079.37",  
"lastPrice":"46263.71",  
"bidPrice":"46260.38",  
"bidQty":"",  
"askPrice":"46260.41",  
"askQty":"",  
"openPrice":"46079.37",  
"highPrice":"47550.01",  
"lowPrice":"45555.5",  
"volume":"1732.461487",  
"quoteVolume":null,  
"openTime":1641349500000,  
"closeTime":1641349582808,  
"count":null  
}  
]  

```

  * **GET** `/api/v3/ticker/24hr`


**Weight(IP):**
Parameter | Symbols Provided | Weight  
---|---|---  
symbol | 1 | 1  
symbols | all | 40  
Parameters:
Name | Type | Mandatory | Description  
---|---|---|---  
symbol | string | NO | If the symbol is not sent, tickers for all symbols will be returned in an array.  
Response:
Name | Description  
---|---  
symbol | Symbol  
priceChange | price Change  
priceChangePercent | price change percent  
prevClosePrice | Previous close price  
lastPrice | Last price  
lastQty | Last quantity  
bidPrice | Bid best price  
bidQty | Bid best quantity  
askPrice | Ask best price  
askQty | Ask best quantity  
openPrice | Open  
highPrice | High  
lowPrice | Low  
volume | Deal volume  
quoteVolume | Quote asset volume  
openTime | Start time  
closeTime | Close time  
count |   
## Symbol Price Ticker[​](https://www.mexc.com/api-docs/spot-v3/market-data-endpoints#symbol-price-ticker "Direct link to Symbol Price Ticker")
> Response
```
{  
"symbol":"BTCUSDT",  
"price":"184.34"  
}  
or  
[  
{  
"symbol":"BTCUSDT",  
"price":"6.65"  
},  
{  
"symbol":"ETHUSDT",  
"price":"5.65"  
}  
]  

```

  * **GET** `/api/v3/ticker/price`


**Weight(IP):**
Parameter | Symbols Provided | Weight  
---|---|---  
symbol | 1 | 1  
symbols | all | 2  
Parameters:
Name | Type | Mandatory | Description  
---|---|---|---  
symbol | string | NO | If the symbol is not sent, all symbols will be returned in an array.  
Response:
Name | Description  
---|---  
symbol |   
price | Last price  
## Symbol Order Book Ticker[​](https://www.mexc.com/api-docs/spot-v3/market-data-endpoints#symbol-order-book-ticker "Direct link to Symbol Order Book Ticker")
> Response
```
{  
"symbol":"AEUSDT",  
"bidPrice":"0.11001",  
"bidQty":"115.59",  
"askPrice":"0.11127",  
"askQty":"215.48"  
}  
OR  
[  
{  
"symbol":"AEUSDT",  
"bidPrice":"0.11001",  
"bidQty":"115.59",  
"askPrice":"0.11127",  
"askQty":"215.48"  
},  
{  
"symbol":"AEUSDT",  
"bidPrice":"0.11001",  
"bidQty":"115.59",  
"askPrice":"0.11127",  
"askQty":"215.48"  
}  
]  

```

  * **GET** `/api/v3/ticker/bookTicker`


**Weight(IP):** 1
Best price/qty on the order book for a symbol or symbols.
Parameters:
Name | Type | Mandatory | Description  
---|---|---|---  
symbol | string | NO | If the symbol is not sent, all symbols will be returned in an array.  
Response:
Name | Description  
---|---  
symbol | Symbol  
bidPrice | Best bid price  
bidQty | Best bid quantity  
askPrice | Best ask price  
askQty | Best ask quantity  
[Previous General Info](https://www.mexc.com/api-docs/spot-v3/general-info "PreviousGeneral Info")[Next Sub-Account Endpoints](https://www.mexc.com/api-docs/spot-v3/subaccount-endpoints "NextSub-Account Endpoints")
  * [Download Historical Market Data](https://www.mexc.com/api-docs/spot-v3/market-data-endpoints#download-historical-market-data "Download Historical Market Data")
  * [Test Connectivity](https://www.mexc.com/api-docs/spot-v3/market-data-endpoints#test-connectivity "Test Connectivity")
  * [Check Server Time](https://www.mexc.com/api-docs/spot-v3/market-data-endpoints#check-server-time "Check Server Time")
  * [API default symbol](https://www.mexc.com/api-docs/spot-v3/market-data-endpoints#api-default-symbol "API default symbol")
  * [Exchange Information](https://www.mexc.com/api-docs/spot-v3/market-data-endpoints#exchange-information "Exchange Information")
  * [Order Book](https://www.mexc.com/api-docs/spot-v3/market-data-endpoints#order-book "Order Book")
  * [Recent Trades List](https://www.mexc.com/api-docs/spot-v3/market-data-endpoints#recent-trades-list "Recent Trades List")
  * [Compressed/Aggregate Trades List](https://www.mexc.com/api-docs/spot-v3/market-data-endpoints#compressedaggregate-trades-list "Compressed/Aggregate Trades List")
  * [Kline/Candlestick Data](https://www.mexc.com/api-docs/spot-v3/market-data-endpoints#klinecandlestick-data "Kline/Candlestick Data")
  * [Current Average Price](https://www.mexc.com/api-docs/spot-v3/market-data-endpoints#current-average-price "Current Average Price")
  * [24hr Ticker Price Change Statistics](https://www.mexc.com/api-docs/spot-v3/market-data-endpoints#24hr-ticker-price-change-statistics "24hr Ticker Price Change Statistics")
  * [Symbol Price Ticker](https://www.mexc.com/api-docs/spot-v3/market-data-endpoints#symbol-price-ticker "Symbol Price Ticker")
  * [Symbol Order Book Ticker](https://www.mexc.com/api-docs/spot-v3/market-data-endpoints#symbol-order-book-ticker "Symbol Order Book Ticker")


