# Market endpoints

The API endpoint under the [Market endpoints] module doesn't require authentication.

## Get the server time

> Request

```
curl "https://contract.mexc.com/api/v1/contract/ping"  

```

> Response

```json
{
  "success": true,
  "data": 1587442022003
}
```

- **GET** `api/v1/contract/ping`

rate limit: 20 times / 2 seconds
**Request parameters:**
None

## Get the contract information

> Request

```
curl "https://contract.mexc.com/api/v1/contract/detail"  

```

> Response

```json
{
  "success":true,
  "code":0,
  "data":[
  {
    "symbol":"BTC_USDT",
    "displayName":"BTC_USDT永续",
    "displayNameEn":"BTC_USDT SWAP",
    "positionOpenType":3,
    "baseCoin":"BTC",
    "quoteCoin":"USDT",
    "settleCoin":"USDT",
    "contractSize":0.0001,
    "minLeverage":1,
    "maxLeverage":125,
    "priceScale":2,
    "volScale":0,
    "amountScale":4,
    "priceUnit":0.5,
    "volUnit":1,
    "minVol":1,
    "maxVol":5000000,
    "bidLimitPriceRate":0.03,
    "askLimitPriceRate":0.03,
    "takerFeeRate":0.0006,
    "makerFeeRate":0.0002,
    "maintenanceMarginRate":0.004,
    "initialMarginRate":0.008,
    "riskBaseVol":150000,
    "riskIncrVol":150000,
    "riskIncrMmr":0.004,
    "riskIncrImr":0.004,
    "riskLevelLimit":5,
    "priceCoefficientVariation":0.05,
    "indexOrigin":[
    "Binance",
    "GATEIO",
    "HUOBI",
    "MXC"
    ],
    "state":0,
    "isNew":false,
    "isHot":true,
    "isHidden":false,
    "conceptPlate":[
    "mc-trade-zone-grey",
    "mc-trade-zone-pow"
    ],
    "riskLimitType":"BY_VOLUME",
    "maxNumOrders":[
    200,
    50
    ],
    "marketOrderMaxLevel":15,
    "marketOrderPriceLimitRate1":0.03,
    "marketOrderPriceLimitRate2":0.005,
    "triggerProtect":0.05,
    "appraisal":0,
    "showAppraisalCountdown":0,
    "automaticDelivery":0,
    "apiAllowed":false
  },
  ]
}
```

- **GET** `api/v1/contract/detail`

Rate limit: 1 times / 5 seconds
**Request parameters:**
Parameter | Date Type | Mandatory | Description\
---|---|---|---\
symbol | string | false | the name of the contract\
**Response parameters:**
Parameter | Date Type | Description\
---|---|---\
symbol | string | the name of the contract\
displayName | string | display name\
displayNameEn | string | english display name\
positionOpenType | int | position open type,1：isolated，2：cross，3：both\
baseCoin | string | base currency such as BTC\
quoteCoin | string | quote currency such as USDT\
settleCoin | string | liquidation currency such as USDT\
contractSize | decimal | contract value\
minLeverage | int | minimum leverage\
maxLeverage | int | maximum leverage\
priceScale | int | price scale\
volScale | int | quantity scale\
amountScale | int | amount scale\
priceUnit | int | price unit\
volUnit | int | volume unit\
minVol | decimal | minimum volume\
maxVol | decimal | maximum volume\
bidLimitPriceRate | decimal | bid limit price rate\
askLimitPriceRate | decimal | ask limit price rate\
takerFeeRate | decimal | taker rate\
makerFeeRate | decimal | maker rate\
maintenanceMarginRate | decimal | maintenance margin rate\
initialMarginRate | decimal | initial margin rate\
riskBaseVol | decimal | initial volume\
riskIncrVol | decimal | risk increasing volume\
riskIncrMmr | decimal | maintain increasing margin rate\
riskIncrImr | decimal | initial increasing margin rate\
riskLevelLimit | int | risk level limit\
priceCoefficientVariation | decimal | fair price coefficient variation\
indexOrigin | List | index origin\
state | int | status, 0:enabled,1:delivery, 2:completed, 3: offline, 4: pause\
apiAllowed | bool | whether support api\
conceptPlate | List | The zone, corresponding to the entryKey field of the section list\
riskLimitType | List | Risk limit type, BY_VOLUME: by the volume, BY_VALUE: by the position

## Get the transferable currencies

> Request

```
curl "https://contract.mexc.com/api/v1/contract/support_currencies"  

```

> Response

```json
{
  "success": true,
  "code": 0,
  "data": [
    "BTC",
    "ETH",
    "USDT"
  ]
}
```

- **GET** `api/v1/contract/support_currencies`

Rate limit: 20 times /2 seconds
**Request parameters:**
None
**Response parameters:**
The returned "data" field contains a list of string with each string represents a suppported currency.

## Get the contract‘s depth information

> Request

```
curl "https://contract.mexc.com/api/v1/contract/depth/BTC_USDT"  

```

> Response

```json
{
  "asks": [
    [
      3968.5,
      121
    ],
    [
      3968.6,
      160,
      4
    ]
  ],
  "bids": [
    [
      3968.4,
      179,
      4
    ],
    [
      3968,
      914,
      3
    ]
  ],
  "version": 1,
  "timestamp": 1587442022003
}
```

- **GET** `api/v1/contract/depth/{symbol}`

Rate limit: 20 times /2 seconds
**Request parameters:**
Parameter | Date Type | Mandatory | Description\
---|---|---|---\
symbol | string | true | the name of the contract\
limit | int | false | tier\
**Response parameters:**
Parameter | Data Type | Description\
---|---|---\
asks | List | the seller depth\
bids | List | the buyer depth\
version | long | the version number\
timestamp | long | system timestamp\
note: [411.8, 10, 1] 411.8 is the price，10 is the volume of contracts for this price,1 is the order quantity

## Get a snapshot of the latest N depth information of the contract

> Request

```
curl "https://contract.mexc.com/api/v1/contract/depth_commits/BTC_USDT/20"  

```

> Response

```json
{
  "success": true,
  "code": 0,
  "data": [
    {
      "asks": [
        [
          31792,
          59105,
          1
        ]
      ],
      "bids": [],
      "version": 1481763378
    }
  ]
}
```

- **GET** `api/v1/contract/depth_commits/{symbol}/{limit}`

Rate limit: 20 times /2 seconds
**Request parameter:**
Parameter | Data Type | Mandatory | Description\
---|---|---|---\
symbol | string | true | the name of the contract\
limit | int | true | count\
**Response parameters:**
Parameter | Data Type | Description\
---|---|---\
asks | List | the seller depth\
bids | List | the buyer depth\
version | long | the version number

## Get contract index price

> Request

```
curl "https://contract.mexc.com/api/v1/contract/index_price/BTC_USDT"  

```

> Response

```json
{
  "success": true,
  "code": 0,
  "data": {
    "symbol": "BTC_USDT",
    "indexPrice": 31104.6,
    "timestamp": 1609829627708
  }
}
```

- **GET** `api/v1/contract/index_price/{symbol}`

Rate limit: 20 times /2 seconds
**Request parameters:**
Parameter | Data Type | Mandatory | Description\
---|---|---|---\
symbol | string | true | the name of the contract\
**Response parameters:**
Parameter | Data Type | Description\
---|---|---\
symbol | string | trading pair\
indexPrice | decimal | index price\
timestamp | long | system timestamp

## Get contract fair price

> Request

```
curl "https://contract.mexc.com/api/v1/contract/fair_price/BTC_USDT"  

```

> Response

```json
{
  "success": true,
  "code": 0,
  "data": {
    "symbol": "BTC_USDT",
    "fairPrice": 31103.4,
    "timestamp": 1609829705178
  }
}
```

- **GET** `api/v1/contract/fair_price/{symbol}`

Rate limit:20 times/2 seconds
**Request parameters:**
Parameter | Data Type | Mandatory | Description\
---|---|---|---\
symbol | string | true | the name of the contract\
**Response parameters:**
Parameter | Data Type | Description\
---|---|---\
symbol | string | the name of the contract\
fairPrice | decimal | fair price\
timestamp | long | system timestamp

## Get contract funding rate

> Request

```
curl "https://contract.mexc.com/api/v1/contract/funding_rate/BTC_USDT"  

```

> Response

```json
{
  "success": true,
  "code": 0,
  "data": {
    "symbol": "BTC_USDT",
    "fundingRate": -0.000489,
    "maxFundingRate": 0.001,
    "minFundingRate": -0.001,
    "collectCycle": 8,
    "nextSettleTime": 1609833600000,
    "timestamp": 1609829807577
  }
}
```

- **GET** `api/v1/contract/funding_rate/{symbol}`

Rate limit:20 times/2 seconds
**Request parameters:**
Parameter | Data Type | Mandatory | Description\
---|---|---|---\
symbol | string | true | the name of the contract\
**Response parameters:**
Parameter | Data Type | Description\
---|---|---\
symbol | string | the name of the contract\
fundingRate | decimal | funding rate\
maxFundingRate | decimal | max funding rate\
minFundingRate | decimal | min funding rate\
collectCycle | int | charge cycle\
nextSettleTime | long | next charge time\
timestamp | long | system timestamp

## K-line data

> Request

```
curl "https://contract.mexc.com/api/v1/contract/kline/BTC_USDT?interval=Min15&start=1609992674&end=1609992694"  

```

> Response

```json
{
  "success": true,
  "code": 0,
  "data": {
    "time": [
      1609740600
    ],
    "open": [
      33016.5
    ],
    "close": [
      33040.5
    ],
    "high": [
      33094.0
    ],
    "low": [
      32995.0
    ],
    "vol": [
      67332.0
    ],
    "amount": [
      222515.85925
    ]
  }
}
```

- **GET** `api/v1/contract/kline/{symbol}`

Rate limit:20 times/2 seconds
**Request parameters:**
Parameter | Data Type | Mandatory | Description\
---|---|---|---\
symbol | string | true | the name of the contract\
interval | string | false | interval: Min1、Min5、Min15、Min30、Min60、Hour4、Hour8、Day1、Week1、Month1,default: Min1\
start | long | false | start timestamp,seconds\
end | long | false | end timestamp,seconds\
**Response parameters:**
Parameter | Data Type | Description\
---|---|---\
open | double | the opening price\
close | double | the closing price\
high | double | the highest price\
low | double | the lowest price\
vol | double | volume\
time | long | time window\
Attention:
1、The maximum data in a single request is 2000 pieces. If your choice of start/end time and granularity of time results in more than the maximum volume of data in a single request, your request will only return 2000 pieces. If you want to get sufficiently fine-grained data over a larger time range, you need to make several times requests.
2、If only the start time is provided, then query the data from the start time to the current system time. If only the end time is provided, the 2000 pieces of data closest to the end time are returned. If neither start time nor end time is provided, the 2000 pieces of data closest to the current time in the system are queried.

## Get K-line data of the index price

> Request

```
curl "https://contract.mexc.com/api/v1/contract/kline/index_price/BTC_USDT?interval=Min15&start=1609992674&end=1609992694"  

```

> Response

```json
{
  "success": true,
  "code": 0,
  "data": {
    "time": [
      1609740900
    ],
    "open": [
      33039.0
    ],
    "close": [
      33233.1
    ],
    "high": [
      33352.3
    ],
    "low": [
      33007.9
    ],
    "vol": [
      0.0
    ],
    "amount": [
      0.0
    ]
  }
}
```

- **GET** `api/v1/contract/kline/index_price/{symbol}`

Rate limit:20 times/2 seconds
**Request parameters:**
Parameter | Data Type | Mandatory | Description\
---|---|---|---\
symbol | string | true | the name of the contract\
interval | string | false | interval: Min1、Min5、Min15、Min30、Min60、Hour4、Hour8、Day1、Week1、Month1,default: Min1\
start | long | false | start timestamp,seconds\
end | long | false | end timestamp,seconds\
**Response parameters:**
Parameter | Data Type | Description\
---|---|---\
open | double | the opening price\
close | double | the closing price\
high | double | the highest price\
low | double | the lowest price\
vol | double | volume\
time | long | time window\
Attention:
1、The maximum data in a single request is 2000 pieces. If your choice of start/end time and granularity of time results in more than the maximum volume of data in a single request, your request will only return 2000 pieces. If you want to get sufficiently fine-grained data over a larger time range, you need to make several times requests.
2、If only the start time is provided, then query the data from the start time to the current system time. If only the end time is provided, the 2000 pieces of data closest to the end time are returned. If neither start time nor end time is provided, the 2000 pieces of data closest to the current time in the system are queried.

## Get K-line data of the fair price

> Request

```
curl "https://contract.mexc.com/api/v1/contract/kline/fair_price/BTC_USDT?interval=Min15&start=1609992674&end=1609992694"  

```

> Response

```json
{
  "success": true,
  "code": 0,
  "data": {
    "time": [
      1609740900
    ],
    "open": [
      33041.0
    ],
    "close": [
      33233.3
    ],
    "high": [
      33354.8
    ],
    "low": [
      33009.4
    ],
    "vol": [
      0.0
    ],
    "amount": [
      0.0
    ]
  }
}
```

- **GET** `api/v1/contract/kline/fair_price/{symbol}`

Rate limit:20 times/2 seconds
**Request parameters:**
Parameter | Data Type | Mandatory | Description\
---|---|---|---\
symbol | string | true | the name of the contract\
interval | string | false | interval: Min1、Min5、Min15、Min30、Min60、Hour4、Hour8、Day1、Week1、Month1,default: Min1\
start | long | false | start timestamp,seconds\
end | long | false | end timestamp,seconds\
**Response parameters:**
Parameter | Data Type | Description\
---|---|---\
open | double | the opening price\
close | double | the closing price\
high | double | the highest price\
low | double | the lowest price\
vol | double | volume\
time | long | time window\
Attention:
1、The maximum data in a single request is 2000 pieces. If your choice of start/end time and granularity of time results in more than the maximum volume of data in a single request, your request will only return 2000 pieces. If you want to get sufficiently fine-grained data over a larger time range, you need to make several times requests.
2、If only the start time is provided, then query the data from the start time to the current system time. If only the end time is provided, the 2000 pieces of data closest to the end time are returned. If neither start time nor end time is provided, the 2000 pieces of data closest to the current time in the system are queried.

## Get contract transaction data

> Request

```
curl "https://contract.mexc.com/api/v1/contract/deals/BTC_USDT"  

```

> Response

```json
{
  "success": true,
  "code": 0,
  "data": [
    {
      "p": 31199,
      "v": 18,
      "T": 1,
      "O": 3,
      "M": 2,
      "t": 1609831235985
    },
    {
      "p": 31199,
      "v": 15,
      "T": 2,
      "O": 3,
      "M": 1,
      "t": 1609831234759
    }
  ]
}
```

- **GET** `api/v1/contract/deals/{symbol}`

Rate limit:20 times/2 seconds
**Request parameters:**
Parameter | Data Type | Mandatory | Description\
---|---|---|---\
symbol | string | true | the name of the contract\
limit | int | false | consequence set quantity ，maximum is 100, default 100 without setting\
**Response parameters:**
Parameter | Data Type | Description\
---|---|---\
p | decimal | transaction price\
v | decimal | quantity\
T | int | deal type,1:purchase,2:sell\
O | int | open position, 1: Yes,2: No, when O is 1, vol is additional position\
M | int | self-transact,1:yes,2:no\
t | long | transaction time

## Get contract trend data

> Request

```
curl "https://contract.mexc.com/api/v1/contract/ticker"  

```

> Response

```json
{
  "success": true,
  "code": 0,
  "data": {
    "symbol": "BTC_USDT",
    "lastPrice": 31199,
    "bid1": 31198.5,
    "ask1": 31199,
    "volume24": 40146908,
    "amount24": 124905007.4428,
    "holdVol": 55102960,
    "lower24Price": 27795,
    "high24Price": 33152.5,
    "riseFallRate": -0.0176,
    "riseFallValue": -562,
    "indexPrice": 31016.3,
    "fairPrice": 31199.5,
    "fundingRate": 0.001,
    "maxBidPrice": 31946.5,
    "minAskPrice": 30085.5,
    "timestamp": 1609831334016
  }
}
```

- **GET** `api/v1/contract/ticker`

Rate limit:20 times/2 seconds
**Request parameters:**
Parameter | Data Type | Mandatory | Description\
---|---|---|---\
symbol | string | false | the name of the contract\
**Response parameters:**
Parameter | Data Type | Description\
---|---|---\
symbol | string | the name of the contract\
lastPrice | decimal | the latest price\
bid1 | decimal | purchase price\
ask1 | decimal | sell price\
volume24 | decimal | 24 hours trading volume, according to the volume of statistical count\
amount24 | decimal | 24 hours transaction volume\
holdVol | decimal | total holdings\
lower24Price | decimal | lowest price within 24 hours\
high24Price | decimal | highest price within 24 hours\
riseFallRate | decimal | rise/fall rate\
riseFallValue | decimal | rise/fall value\
indexPrice | decimal | index price\
fairPrice | decimal | fair price\
fundingRate | decimal | funding rate\
timestamp | long | transaction timestamp

## Get all contract risk fund balance

> Request

```
curl "https://contract.mexc.com/api/v1/contract/risk_reverse"  

```

> Response

```json
{
  "success":true,
  "code":0,
  "data":[
  {
    "symbol":"BTC_USDT",
    "currency":"USDT",
    "available":425018.32968325152473812,
    "timestamp":1609831395734
  },
  {
    "symbol":"BTC_USD",
    "currency":"BTC",
    "available":5.00211366264782435,
    "timestamp":1609831395734
  },
  ]
}
```

- **GET** `api/v1/contract/risk_reverse`

Rate limit:20 times/2 seconds
**Request parameters:**
None
**Response parameters:**
parameter name | type | description\
---|---|---\
symbol | string | the name of the cntract\
currency | string | currency\
available | decimal | available balance\
timestamp | long | system timestamp

## Get contract risk fund balance history

> Request

```
curl "https://contract.mexc.com/api/v1/contract/risk_reverse/history?symbol=BTC_USDT&page_num=1&page_size=20"  

```

> Response

```json
{
  "success": true,
  "code": 0,
  "data": {
    "pageSize": 2,
    "totalCount": 42,
    "totalPage": 21,
    "currentPage": 1,
    "resultList": [
      {
        "symbol": "BTC_USDT",
        "currency": "USDT",
        "available": 424288.0531610467,
        "snapshotTime": 1609819200000
      },
      {
        "symbol": "BTC_USDT",
        "currency": "USDT",
        "available": 423989.8172441063,
        "snapshotTime": 1609804800000
      }
    ]
  }
}
```

- **GET** `api/v1/contract/risk_reverse/history`

Rate limit:20 times/2 seconds
**Request parameters:**
Parameter | Data Type | Mandatory | Description\
---|---|---|---\
symbol | string | true | the name of the contract\
page_num | int | true | current page number, default is 1\
page_size | int | true | the page size, default 20, maximum 100\
**Response parameters:**
Parameter | Data Type | Description\
---|---|---\
pageSize | int | page size\
totalCount | int | total count\
totalPage | int | total pages\
currentPage | int | current page\
resultList | list | data consequence set\
symbol | string | the name of the contract\
currency | string | liquidation currency\
available | decimal | balance\
snapshotTime | long | snapshot time

## Get contract funding rate history

> Request

```
curl "https://contract.mexc.com/api/v1/contract/funding_rate/history?symbol=BTC_USDT&page_num=1&page_size=20"  

```

> Response

```json
{
  "success": true,
  "code": 0,
  "data": {
    "pageSize": 2,
    "totalCount": 21,
    "totalPage": 11,
    "currentPage": 1,
    "resultList": [
      {
        "symbol": "BTC_USDT",
        "fundingRate": 0.000266,
        "settleTime": 1609804800000
      },
      {
        "symbol": "BTC_USDT",
        "fundingRate": 0.00029,
        "settleTime": 1609776000000
      }
    ]
  }
}
```

- **GET** `api/v1/contract/funding_rate/history`

Rate limit:20 times/2 seconds
**Request parameters:**
Parameter | Data Type | Mandatory | Description\
---|---|---|---\
symbol | string | true | the name of the contract\
page_num | int | true | current page number, default is 1\
page_size | int | true | the page size, default 20, maximum 1000\
**Response parameters:**
Parameter | Data Type | Description\
---|---|---\
pageSize | int | page size\
totalCount | int | the total count\
totalPage | int | the total pages\
currentPage | int | the current page\
resultList | list | data consequence set\
symbol | string | the name of the contract\
fundingRate | decimal | funding rate\
settleTime | long | liquidation time\\
