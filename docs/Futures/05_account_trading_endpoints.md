# Account and trading endpoints

The API endpoint under the [Account and trading endpoints] module requires authentication.

> Response

```json
{
  "success": true,
  "code": 0,
  "data": [
    {
      "currency": "BTC",
      "positionMargin": 0,
      "availableBalance": 0,
      "cashBalance": 0,
      "frozenBalance": 0,
      "equity": 0,
      "unrealized": 0,
      "bonus": 0
    },
    {
      "currency": "ETH",
      "positionMargin": 0,
      "availableBalance": 0,
      "cashBalance": 0,
      "frozenBalance": 0,
      "equity": 0,
      "unrealized": 0,
      "bonus": 0
    },
    {
      "currency": "USDT",
      "positionMargin": 0,
      "availableBalance": 0.03176562,
      "cashBalance": 0.03176562,
      "frozenBalance": 0,
      "equity": 0.03176562,
      "unrealized": 0,
      "bonus": 0
    }
  ]
}
```

## Get all informations of user's asset

- **GET** `api/v1/private/account/assets`

**Required permissions:** Trade reading permission
Rate limit:20 times/2 seconds
**Request parameters:**
None
**Response parameters:**
Parameter | Data Type | Description\
---|---|---\
currency | string | currency\
positionMargin | decimal | position margin\
frozenBalance | decimal | frozen balance\
availableBalance | decimal | available balance\
cashBalance | decimal | drawable balance\
equity | decimal | total equity\
unrealized | decimal | unrealized profit and loss

## Get the user's single currency asset information

> Response

```json
{
  "success": true,
  "code": 0,
  "data": {
    "currency": "USDT",
    "positionMargin": 0,
    "availableBalance": 0.03176562,
    "cashBalance": 0.03176562,
    "frozenBalance": 0,
    "equity": 0.03176562,
    "unrealized": 0,
    "bonus": 0
  }
}
```

- **GET** `api/v1/private/account/asset/{currency}`

**Required permissions:** Account reading permission
Rate limit:20 times/2 seconds
**Request parameters:**
Parameter | Data Type | Mandatory | Description\
---|---|---|---\
currency | string | true | currency\
**Response parameters:**
Parameter | Data Type | Description\
---|---|---\
currency | string | currency\
positionMargin | decimal | position margin\
frozenBalance | decimal | frozen balance\
availableBalance | decimal | available balance\
cashBalance | decimal | drawable balance\
equity | decimal | total equity\
unrealized | decimal | unrealized profit and loss

## Get the user's asset transfer records

> Response

```json
{
  "success": true,
  "code": 0,
  "data": {
    "pageSize": 2,
    "totalCount": 88,
    "totalPage": 44,
    "currentPage": 1,
    "resultList": [
      {
        "id": 165230,
        "txid": "db13d56ca887429a8f5fe1d1cbc4559c",
        "currency": "USDT",
        "amount": 0.03176562,
        "type": "IN",
        "state": "SUCCESS",
        "createTime": 1609833219000,
        "updateTime": 1609833219000
      },
      {
        "id": 139320,
        "txid": "a57ff46de96545839185aff7343f9b7c",
        "currency": "USDT",
        "amount": 60.53383524,
        "type": "OUT",
        "state": "SUCCESS",
        "createTime": 1608200935000,
        "updateTime": 1608200935000
      }
    ]
  }
}
```

- **GET** `api/v1/private/account/transfer_record`

**Required permissions:** Account reading permission
Rate limit:20 times/2 seconds
**Request parameters:**
Parameter | Data Type | Mandatory | Description\
---|---|---|---\
currency | string | false | currency\
state | string | false | state:WAIT 、SUCCESS 、FAILED\
type | string | false | type:IN 、OUT\
page_num | int | true | current page number, default is 1\
page_size | int | true | page size, default 20, maximum 100\
**Response parameters:**
Parameter | Data Type | Description\
---|---|---\
pageSize | int | page size\
totalCount | int | the total count\
totalPage | int | the total page\
currentPage | int | the current page\
resultList | list | data consequence set\
id | long | id\
txid | string | flow number\
currency | string | currency\
amount | decimal | transfer amount\
type | string | type:IN 、OUT\
state | string | state:WAIT 、SUCCESS 、FAILED\
createTime | long | create time\
updateTime | long | update time

## Get the user's history position information

> Response

```json
{
  "success": false,
  "code": 0,
  "message": "",
  "data": [
    {
      "positionId": 0,
      "symbol": "",
      "positionType": 0,
      "openType": 0,
      "state": 0,
      "holdVol": 0.0,
      "frozenVol": 0.0,
      "closeVol": 0.0,
      "holdAvgPrice": 0.0,
      "openAvgPrice": 0.0,
      "closeAvgPrice": 0.0,
      "liquidatePrice": 0.0,
      "oim": 0.0,
      "im": 0.0,
      "holdFee": 0.0,
      "realised": 0.0,
      "adlLevel": 0,
      "leverage": 0,
      "createTime": "",
      "updateTime": "",
      "autoAddIm": false
    }
  ]
}
```

- **GET** `api/v1/private/position/list/history_positions`

**Required permissions:** Trade reading permissions
Rate limit:20 times/2 seconds
**Request parameters:**
Parameter | Data Type | Mandatory | Description\
---|---|---|---\
symbol | string | false | the name of the contract\
type | int | false | position type， 1long 2short\
page_num | int | true | current page number , default is 1\
page_size | int | true | page size , default 20, maximum 100\
**Response parameters:**
Parameter | Data Type | Description\
---|---|---\
code | number | Status code\
message | string | Misdescription (If there has )\
positionId | long | position id\
symbol | string | the name of the contract\
positionType | int | position type， 1 long 2 short\
openType | int | open type， 1isolated 2cross\
state | int | position state,1holding 2 system auto-holding 3closed\
holdVol | decimal | holding volume\
frozenVol | decimal | frozen volume\
closeAvgPrice | decimal | close average price\
openAvgPrice | decimal | open average price\
liquidatePrice | decimal | liquidation price\
oim | decimal | original initial margin\
im | decimal | initial margin， add or subtract items can be used to adjust the liquidate price\
holdFee | decimal | holding fee, positive means get it, negative means lost it\
realised | decimal | realized profit and loss\
adlLevel | int | adl level\
leverage | int | leverage multiple\
createTime | date | create time\
updateTime | date | update time\
autoAddIm | boolean | automatic margin

## Get the user's current holding position

> Response

```json
{
  "success": true,
  "code": 0,
  "data": [
    {
      "positionId": 1394650,
      "symbol": "ETH_USDT",
      "positionType": 1,
      "openType": 1,
      "state": 1,
      "holdVol": 1,
      "frozenVol": 0,
      "closeVol": 0,
      "holdAvgPrice": 1217.3,
      "openAvgPrice": 1217.3,
      "closeAvgPrice": 0,
      "liquidatePrice": 1211.2,
      "oim": 0.1290338,
      "im": 0.1290338,
      "holdFee": 0,
      "realised": -0.0073,
      "leverage": 100,
      "createTime": 1609991676000,
      "updateTime": 1609991676000,
      "autoAddIm": false
    }
  ]
}
```

- **GET** `api/v1/private/position/open_positions`

**Required permissions:** Trade reading permission
Rate limit:20 times/2 seconds
**Request parameters:**
Parameter | Data Type | Mandatory | Description\
---|---|---|---\
symbol | string | false | the name of the contract\
**Response parameters:**
Parameter | Data Type | Description\
---|---|---\
positionId | long | position id\
symbol | string | the name of the contract\
holdVol | decimal | holding volume\
positionType | int | position type， 1 long 2 short\
openType | int | open type， 1 isolated 2 cross\
state | int | position state,1holding. 2 system auto-holding 3 closed\
frozenVol | decimal | frozen volume\
closeVol | decimal | close volume\
holdAvgPrice | decimal | holdings average price\
closeAvgPrice | decimal | close average price\
openAvgPrice | decimal | open average price\
liquidatePrice | decimal | liquidate price\
oim | decimal | original initial margin\
adlLevel | int | the value of ADL is 1-5. If it is empty, wait for the refresh\
im | decimal | initial margin， add or subtract items can be used to adjust the liquidate price\
holdFee | decimal | holding fee, positive means get it, negative means lost it\
realised | decimal | realized profit and loss\
createTime | date | create time\
updateTime | date | update time

## Get details of user's funding rate

> Response

```json
{
  "success": true,
  "code": 0,
  "data": {
    "pageSize": 2,
    "totalCount": 73,
    "totalPage": 37,
    "currentPage": 1,
    "resultList": [
      {
        "id": 328033,
        "symbol": "SUSHI_USDT",
        "positionType": 1,
        "positionValue": 41.8899,
        "funding": 0.0837798,
        "rate": -0.002,
        "settleTime": 1606435200000
      },
      {
        "id": 327194,
        "symbol": "SUSHI_USDT",
        "positionType": 1,
        "positionValue": 34.2654,
        "funding": 0.0685308,
        "rate": -0.002,
        "settleTime": 1606406400000
      }
    ]
  }
}
```

- **GET** `api/v1/private/position/funding_records`

**Required permissions:** Trade reading permission
Rate limit:20 times/2 seconds
**Request parameters:**
Parameter | Data Type | Mandatory | Description\
---|---|---|---\
symbol | string | false | the name of the contract\
position_id | int | false | position id\
page_num | int | true | current page number, default is 1\
page_size | int | true | page size, default 20, maximum 100\
**Response parameters:**
Parameter | Data Type | Description\
---|---|---\
pageSize | int | page size\
totalCount | int | the total count\
totalPage | int | the total page\
currentPage | int | the current page\
resultList | list | data consequence list\
id | long | id\
symbol | string | the name of the contract\
positionId | long | position id\
positionType | int | 1 long 2 short\
positionValue | decimal | position value\
funding | decimal | funding\
rate | decimal | funding rate\
settleTime | date | liquidation time

## Get the user's current pending order

> Response

```json
{
  "success": false,
  "code": 0,
  "message": "",
  "data": [
    {
      "orderId": 0,
      "symbol": "",
      "positionId": 0,
      "price": 0.0,
      "vol": 0.0,
      "leverage": 0,
      "side": 0,
      "category": 0,
      "orderType": 0,
      "dealAvgPrice": 0.0,
      "dealVol": 0.0,
      "orderMargin": 0.0,
      "takerFee": 0.0,
      "makerFee": 0.0,
      "profit": 0.0,
      "feeCurrency": "",
      "openType": 0,
      "state": 0,
      "externalOid": "",
      "errorCode": 0,
      "usedMargin": 0.0,
      "createTime": "",
      "updateTime": "",
      "stopLossPrice": 0.0,
      "takeProfitPrice": 0.0
    }
  ]
}
```

- **GET** `api/v1/private/order/list/open_orders/{symbol}`

**Required permissions:** Trade reading permission
Rate limit:20 times/2 seconds
**Request parameters:**
Parameter | Data Type | Mandatory | Description\
---|---|---|---\
symbol | string | false | the name of the contract, return all the contract parameters if there no fill in\
page_num | int | true | current page number, default is 1\
page_size | int | true | page size default 20, maximum 100\
**Response parameters:**
Parameter | Data Type | Description\
---|---|---\
code | number | Status code\
message | string | Misdescription (If there has )\
orderId | long | orderid\
symbol | string | the name of the contract\
positionId | long | position id\
price | decimal | trigger price\
vol | decimal | trigger volume\
leverage | long | leverage\
side | int | order direction 1open long,2close short,3open short, 4 close long\
category | int | order category:1limit order, 2 system take-over delegate, 3 close delegate 4 ADL reduction\
orderType | int | 1:price limited order,2:post only Maker,3:transact or cancel instantly ,4 : transact completely or cancel completely，5:market orders,6 convert market price to current price\
dealAvgPrice | decimal | deal average price\
dealVol | decimal | transaction volume\
orderMargin | decimal | order margin\
usedMargin | decimal | used margin\
takerFee | decimal | taker fee\
makerFee | decimal | maker fee\
profit | decimal | close profit\
feeCurrency | string | fee currency\
openType | int | open type,1 isolated,2 cross\
state | int | order state,1 uninformed, 2uncompleted, 3completed, 4cancelled, 5invalid\
errorCode | int | error code,0:normal，1：parameter errors，2：account balance is insufficient，3：the position does not exist，4： position insufficient，5：For long positions, the order price is less than the close price, while for short positions, the order price is more than the close rice，6：When opening long, the close price is more than the fair price, while when opening short, the close price is less than the fair price ,7:exceed risk quota restrictions, 8: system canceled\
externalOid | string | external order ID\
createTime | date | create time\
updateTime | date | update time\
stopLossPrice | decimal | stop-loss price\
takeProfitPrice | decimal | take-profit price

## Get all of the user's historical orders

> Response

```json
{
  "success": false,
  "code": 0,
  "message": "",
  "data": [
    {
      "orderId": 0,
      "symbol": "",
      "positionId": 0,
      "price": 0.0,
      "vol": 0.0,
      "leverage": 0,
      "side": 0,
      "category": 0,
      "orderType": 0,
      "dealAvgPrice": 0.0,
      "dealVol": 0.0,
      "orderMargin": 0.0,
      "takerFee": 0.0,
      "makerFee": 0.0,
      "profit": 0.0,
      "feeCurrency": "",
      "openType": 0,
      "state": 0,
      "externalOid": "",
      "errorCode": 0,
      "usedMargin": 0.0,
      "createTime": "",
      "updateTime": "",
      "stopLossPrice": 0.0,
      "takeProfitPrice": 0.0
    }
  ]
}
```

- **GET** `api/v1/private/order/list/history_orders`

**Required permissions:** Trade reading permission
Rate limit:20 times/2 seconds
**Request parameters:**
Parameter | Data Type | Mandatory | Description\
---|---|---|---\
symbol | string | false | the name of the contract\
states | string | false | order state,1 1 uninformed, 2uncompleted, 3completed, 4cancelled, 5invalid; multiple separate by ','\
category | int | false | order category:1limit order, 2 system take-over delegate, 3 close delegate 4 ADL reduction\
start_time | long | false | start time, start time and end time span can only check 90 days at a time, default return the last 7 days of data without fill in\
end_time | long | false | end time, start time, and end time spans can only be checked for 90 days at a time\
side | int | false | order direction long,2close short,3open short 4 close long\
page_num | int | true | current page number, default is 1\
page_size | int | true | page size, default 20, maximum 100\
**Response parameters:**
Parameter | Data Type | Description\
---|---|---\
code | number | Status code\
message | string | Misdescription (If there has )\
orderId | long | orderid\
symbol | string | the name of the contract\
positionId | long | position id\
price | decimal | trigger price\
vol | decimal | trigger volume\
leverage | long | leverage\
side | int | order direction 1open long,2close short,3open short 4 close long\
category | int | order category:1limit order, 2 system take-over delegate, 3 close delegate 4 ADL reduction\
orderType | int | 1:price limited order,2:Post Only Maker,3:transact or cancel instantly ,4 : transact completely or cancel completely，5:market orders,6 convert market price to current price\
dealAvgPrice | decimal | transaction average price\
dealVol | decimal | transaction volume\
orderMargin | decimal | order margin\
takerFee | decimal | taker fee\
makerFee | decimal | maker fee\
profit | decimal | close profit\
feeCurrency | string | fee currency\
openType | int | open type,1 isolated,2 cross\
state | int | order state,1 uninformed, 2 uncompleted, 3 completed, 4 cancelled, 5 invalid\
errorCode | int | error code,0:normal，1：parameter errors，2：account balance is insufficient，3：the position does not exist，4： position insufficient，5：For long positions, the order price is less than the close price, while for short positions, the order price is more than the close rice.，6：When opening long, the close price is more than the fair price, while when opening short, the close price is less than the fair price.\
externalOid | string | external order ID\
usedMargin | decimal | used margin\
createTime | date | create time\
updateTime | date | update tine\
stopLossPrice | decimal | stop-loss price\
takeProfitPrice | decimal | take-profit price\
**Note: The price returned from this interface is the platform's takeover price. If you want to query the liquidation price of a liquidation order, you can do so through the[Get the user's current holding position](https://mexcdevelop.github.io/apidocs/contract_v1_en/#get-the-user-39-s-current-holding-position) interface. For liquidation orders, the price will be the platform's takeover price, which may differ from the liquidation price. For more information, please refer to [Liquidation and Risk Limit](https://www.mexc.com/support/articles/360044646391).**

## Query the order based on the external number

> Response

```json
{
  "success": true,
  "code": 0,
  "data": {
    "orderId": "102015012431820288",
    "symbol": "ETH_USDT",
    "positionId": 1394917,
    "price": 1209.05,
    "vol": 1,
    "leverage": 0,
    "side": 2,
    "category": 1,
    "orderType": 5,
    "dealAvgPrice": 1208.35,
    "dealVol": 1,
    "orderMargin": 0,
    "takerFee": 0.0072501,
    "makerFee": 0,
    "profit": 0,
    "feeCurrency": "USDT",
    "openType": 1,
    "state": 3,
    "externalOid": "_m_f95eb99b061d4eef8f64a04e9ac4dad3",
    "errorCode": 0,
    "usedMargin": 0,
    "createTime": 1609992674000,
    "updateTime": 1609992674000
  }
}
```

- **GET** `api/v1/private/order/external/{symbol}/{external_oid}`

**Required permissions:** Trade reading permission
Rate limit:20 times/2 seconds
**Request parameters:**
Parameter | Data Type | Mandatory | Description\
---|---|---|---\
symbol | string | true | the name of the contract\
external_oid | string | true | external order ID\
**Response parameters:**
Parameter | Data Type | Description\
---|---|---\
orderId | long | orderid\
symbol | string | the name of the contract\
positionId | long | position id\
price | decimal | trigger price\
vol | decimal | trigger volume\
leverage | long | leverage\
side | int | order direction 1open long,2close short,3open short 4 close long\
category | int | order category:1limit order, 2 system take-over delegate, 3 close delegate 4 ADL reduction\
orderType | int | 1:price limited order,2:Post Only Maker,3:transact or cancel instantly ,4 : transact completely or cancel completely，5:market orders,6 convert market price to current price\
dealAvgPrice | decimal | transaction average price\
dealVol | decimal | transaction volume\
orderMargin | decimal | order margin\
takerFee | decimal | taker fee\
makerFee | decimal | maker fee\
profit | decimal | close profit\
feeCurrency | string | fee currency\
openType | int | open type,1isolated,2cross\
state | int | order state,1: uninformed,2uncompleted,3completed,4canceled,5invalid\
externalOid | string | external order ID\
createTime | date | create time\
updateTime | date | update time

## Query the order based on the order number

> Response

```json
{
  "success": true,
  "code": 0,
  "data": {
    "orderId": "102015012431820288",
    "symbol": "ETH_USDT",
    "positionId": 1394917,
    "price": 1209.05,
    "vol": 1,
    "leverage": 0,
    "side": 2,
    "category": 1,
    "orderType": 5,
    "dealAvgPrice": 1208.35,
    "dealVol": 1,
    "orderMargin": 0,
    "takerFee": 0.0072501,
    "makerFee": 0,
    "profit": 0,
    "feeCurrency": "USDT",
    "openType": 1,
    "state": 3,
    "externalOid": "_m_f95eb99b061d4eef8f64a04e9ac4dad3",
    "errorCode": 0,
    "usedMargin": 0,
    "createTime": 1609992674000,
    "updateTime": 1609992674000
  }
}
```

- **GET** `api/v1/private/order/get/{order_id}`

**Required permissions:** Trade reading permission
Rate limit:20 times/2 seconds
**Request parameters:**
Parameter | Data Type | Mandatory | Description\
---|---|---|---\
order_id | long | true | order ID\
**Response parameters:**
Parameter | Data Type | Description\
---|---|---\
orderId | long | orderid\
symbol | string | the name of the contract\
positionId | long | position id\
price | decimal | trigger price\
vol | decimal | trigger volume\
leverage | long | leverage\
side | int | order direction :1 open long,2close short,3open short, 4 close long\
category | int | order category:1limit order, 2 system take-over delegate, 3 close delegate 4 ADL reduction\
orderType | int | 1:price limited order,2:Post Only Maker,3:transact or cancel instantly ,4 : transact completely or cancel completely，5:market orders,6 convert market price to current price\
dealAvgPrice | decimal | transaction average price\
dealVol | decimal | transaction volume\
orderMargin | decimal | order margin\
takerFee | decimal | taker fee\
makerFee | decimal | maker fee\
profit | decimal | close profit\
feeCurrency | string | fee currency\
openType | int | open type,1isolated,2cross\
state | int | order state,1 uninformed, 2 uncompleted, 3completed, 4cancelled, 5 invalid\
externalOid | string | External order ID\
createTime | date | create time\
updateTime | date | update time

## Query the order in bulk based on the order number

- **GET** `/api/v1/private/order/batch_query`

**Required permissions:** Trade reading permission
Rate limit:5 times/2 seconds
**Request parameters:**
Parameter | Data Type | Mandatory | Description\
---|---|---|---\
order_ids | long | true | order number array，can be separated by "," for example :order_ids = 1,2,3(maximum 50 orders):\
**Response parameters:**
Parameter | Data Type | Description\
---|---|---\
orderId | long | orderid\
symbol | string | the name of the contract\
positionId | long | position id\
price | decimal | trigger price\
vol | decimal | trigger volume\
leverage | long | leverage\
side | int | order direction 1open long,2close short,3open short, 4 close long\
category | int | order category:1limit order, 2 system take-over delegate, 3 close delegate 4 ADL reduction\
orderType | int | 1:price limited order,2:Post Only Maker,3:transact or cancel instantly ,4 : transact completely or cancel completely，5:market orders,6 convert market price to current price\
dealAvgPrice | decimal | transaction average price\
dealVol | decimal | transaction volume\
orderMargin | decimal | order margin\
takerFee | decimal | taker fee\
makerFee | decimal | maker fee\
profit | decimal | close profit\
feeCurrency | string | fee currency\
openType | int | open type,1isolated,2cross\
state | int | order state,1: uninformed, 2uncompleted 3 completed, 4cancelled, 5invalid\
externalOid | string | external order ID\
createTime | date | create time\
updateTime | date | update time

## Get order transaction details based on the order ID

> Response

```json
{
  "success": true,
  "code": 0,
  "data": [
    {
      "id": "159274416",
      "symbol": "ETH_USDT",
      "side": 2,
      "vol": 1,
      "price": 1208.35,
      "feeCurrency": "USDT",
      "fee": 0.0072501,
      "timestamp": 1609992674000,
      "profit": 0,
      "category": 1,
      "orderId": "102015012431820288",
      "taker": true
    }
  ]
}
```

- **GET** `api/v1/private/order/deal_details/{order_id}`

**Required permissions:** Trade reading permission
Rate limit:20 times/2 seconds
**Request parameters:**
Parameter | Data Type | Mandatory | Description\
---|---|---|---\
order_id | long | true | order id\
**Response parameters:**
Parameter | Data Type | Description\
---|---|---\
id | long | transactionid\
symbol | string | the name of the contract\
side | int | order direction 1open long,2close short,3open short 4 close long\
vol | decimal | transaction volume\
price | decimal | transaction price\
fee | decimal | fee\
feeCurrency | string | fee currency\
profit | decimal | profit\
isTaker | boolean | Is it taker order\
category | int | order category:1limit order, 2 system take-over delegate, 3 close delegate 4 ADL reduction\
orderId | long | order id\
timestamp | long | transaction timestamp

## Get all transaction details of the user's order

> Response

```json
{
  "success":false,
  "code":0,
  "message":"",
  "data":[{
    "id":0,
    "symbol":"",
    "side":0,
    "vol":0.0,
    "price":0.0,
    "feeCurrency":"",
    "fee":0.0,
    "timestamp":"",
    "profit":0.0,
    "isTaker":false,
    "category":0,
    "orderId":0,
    "opponentOrderId":0,
  }]
}
```

- **GET** `api/v1/private/order/list/order_deals`

Rate limit:20 times/2 seconds
**Request parameters:**
Parameter | Data Type | Mandatory | Description\
---|---|---|---\
symbol | string | true | the name of the contact\
start_time | long | false | the starting time, the default is to push forward 7 days, and the maximum span is 90 days\
end_time | long | false | the end time, start and end time span is 90 days\
page_num | int | true | current page number, default is 1\
page_size | int | true | page size , default 20, maximum 100\
**Response parameters:**
Parameter | Data Type | Description\
---|---|---\
code | number | Status code\
message | string | Misdescription (If there has )\
id | long | order id\
symbol | string | the name of the contact\
side | int | order direction 1open long,2close short,3open short 4 close long\
vol | decimal | transaction volume\
price | decimal | transaction price\
fee | decimal | fee\
feeCurrency | string | currency\
profit | decimal | profit\
isTaker | boolean | is it taker order\
category | int | order category:1limit order, 2 system take-over delegate, 3 close delegate 4 ADL reduction\
orderId | long | order id\
timestamp | long | transaction timestamp

## Gets the trigger order list

> Response

```json
{
  "success": false,
  "code": 0,
  "message": "",
  "data": [
    {
      "id": 0,
      "symbol": "",
      "leverage": 0,
      "side": 0,
      "triggerPrice": 0.0,
      "price": 0.0,
      "vol": 0.0,
      "openType": 0,
      "triggerType": 0,
      "state": 0,
      "executeCycle": 0,
      "trend": 0,
      "orderType": 0,
      "orderId": 0,
      "errorCode": 0,
      "createTime": "",
      "updateTime": ""
    }
  ]
}
```

- **GET** `api/v1/private/planorder/list/orders`

Rate limit:20 times/2 seconds
**Request parameters:**
Parameter | Data Type | Mandatory | Description\
---|---|---|---\
symbol | string | false | the name of the contract\
states | string | false | order state,1 uninformed, 2uncompleted,3completed,4cancelled, 5invalid; Multiple separate by ','\
start_time | long | false | start time, start time and end time span can only check 90 days at a time, default return the last 7 days of data without fill in\
end_time | long | false | end time, start time, and end time spans can only be checked for 90 days at a time\
page_num | int | true | current page number, default is 1\
page_size | int | true | page size, default 20, maximum 100\
**Response parameters:**
Parameter | Data Type | Description\
---|---|---\
code | number | Status code\
message | string | Misdescription (If there has )\
id | int | trigger order id\
symbol | string | the name of the contract\
leverage | long | leverage\
side | int | order direction 1open long, 3open short\
triggerPrice | decimal | trigger price\
price | decimal | execute price\
vol | decimal | order volume\
openType | int | open type， 1isolated 2cross\
triggerType | int | trigger type,1: more than or equal, 2: less than or equal\
state | int | status,1: untriggered, 2: cancelled, 3: executed,4: invalid,5: execution failed\
executeCycle | int | execution cycle, unit: hours\
trend | int | trigger price type,1: latest price, 2: fair price, 3: index price\
errorCode | int | error code on failed execution, 0: normal\
orderId | long | order ID, Return on successful execution\
orderType | int | order type,1: limit order,2:Post Only Maker,3: close or cancel instantly 4: close or cancel completely,5: Market order\
createTime | long | create time\
updateTime | long | update time

## Get the Stop-Limit order list

> Response

```json
{
  "success": false,
  "code": 0,
  "message": "",
  "data": [
    {
      "id": 0,
      "orderId": 0,
      "symbol": "",
      "positionId": 0,
      "stopLossPrice": 0.0,
      "takeProfitPrice": 0.0,
      "state": 0,
      "triggerSide": 0,
      "positionType": 0,
      "vol": 0.0,
      "realityVol": 0.0,
      "placeOrderId": 0,
      "errorCode": 0,
      "version": 0,
      "isFinished": 0,
      "createTime": "",
      "updateTime": ""
    }
  ]
}
```

- **GET** `api/v1/private/stoporder/list/orders`

Rate limit:20 times/2 seconds
**Request parameters:**
Parameter | Data Type | Mandatory | Description\
---|---|---|---\
symbol | string | false | the name of the contact\
is_finished | int | false | final state indicator :0: uncompleted, 1: completed\
start_time | long | false | start time, start time and end time span can only check 90 days at a time, default return the last 7 days of data without fill in\
end_time | long | false | end time, start time, and end time spans can only be checked for 90 days at a time\
page_num | int | true | current page number, default is 1\
page_size | int | true | page size, default 20, maximum 100\
**Response parameters:**
Parameter | Data Type | Description\
---|---|---\
code | number | Status code\
message | string | Misdescription (If there has )\
id | long | Stop-Limit order ID\
symbol | string | the name of the contract\
orderId | long | limit order ID, which is 0 if it is based on a position\
positionId | long | position id\
stopLossPrice | decimal | stop-loss price\
takeProfitPrice | decimal | take-profit price\
state | int | status,1: untriggered, 2: cancelled, 3: executed,4: invalid,5: execution failed\
triggerSide | int | trigger direction, 0: untriggered , 1: taker-profit , 2: stop-loss\
positionType | int | position type,1: long, 2: short\
vol | decimal | trigger volume\
realityVol | decimal | actual number of orders\
placeOrderId | long | order id after successful delegation\
errorCode | int | errorCode,0: normal, other errorCode details\
isFinished | int | whether the order status is the end-state identifier (for query),0. Non-terminal, 1. Terminal\
version | int | version\
createTime | long | createTime\
updateTime | long | update time

## Get risk limits

> Response

```json
{
  "success": true,
  "code": 0,
  "data": {
    "BTC_USDT": [
      {
        "level": 1,
        "maxVol": 150000,
        "maxLeverage": 125,
        "mmr": 0.004,
        "imr": 0.008,
        "symbol": "BTC_USDT",
        "positionType": 2
      },
      {
        "level": 1,
        "maxVol": 150000,
        "maxLeverage": 125,
        "mmr": 0.004,
        "imr": 0.008,
        "symbol": "BTC_USDT",
        "positionType": 1
      }
    ]
  }
}
```

- **GET** `api/v1/private/account/risk_limit`

**Required permissions:** Trade reading permission
Rate limit:20 times/2 seconds
**Request parameters:**
Parameter | Data Type | Mandatory | Description\
---|---|---|---\
symbol | string | false | the name of the contract , not uploaded will return all\
**Response parameters:**
Parameter | Data Type | Description\
---|---|---\
symbol | string | the name of the contract\
positionType | int | position type 1:long，2:short\
level | int | current risk level\
maxVol | decimal | maximum position volume\
maxLeverage | int | maximum leverage rate\
mmr | decimal | maintenance margin rate\
imr | decimal | initial margin rate

## Gets the user's current trading fee rate

> Response

```json
{
  "success": true,
  "code": 0,
  "data": {
    "level": 0,
    "dealAmount": 1786.2594,
    "walletBalance": 0.03176562,
    "makerFee": 0.0002,
    "takerFee": 0.0006,
    "makerFeeDiscount": 1,
    "takerFeeDiscount": 1
  }
}
```

- **GET** `api/v1/private/account/tiered_fee_rate`

**Required permissions:** Trade reading permission
Rate limit:20 times/2 seconds
**Request parameters:**
Parameter | Data Type | Mandatory | Description\
---|---|---|---\
symbol | string | true | the name of the contract\
**Response parameters:**
Parameter | Data Type | Description\
---|---|---\
level | int | tiered trading fee rate\
dealAmount | int | the last 30 days' turnover\
walletBalance | int | wallet balance of yesterday\
makerFee | decimal | makerFee\
takerFee | int | takerFee\
makerFeeDiscount | decimal | makerFee discount\
takerFeeDiscount | decimal | takerFee discount

## Increase or decrease margin

> Response

```json
{
  "success": true,
  "code": 0
}
```

- **POST** `api/v1/private/position/change_margin`

**Required permissions:** Trading permission
Rate limit:20 times/2 seconds
**Request parameters:**
Parameter | Data Type | Mandatory | Description\
---|---|---|---\
positionId | long | true | position id\
amount | decimal | true | amount\
type | string | true | type ,ADD: increase,SUB: decrease\
**Response parameters:**
public parameters, success: true, success, false ,failure

## Get leverage

- **GET** `api/v1/private/position/leverage`

**Required permissions:** Trading permission
Rate limit:20 times/2 seconds
**Request parameters:**
Parameter | Data Type | Mandatory | Description\
---|---|---|---\
symbol | string | true | symbol\
**Response parameters:**
Parameter | Type | Description\
---|---|---\
positionType | int | positon type， 1:long 2:short\
level | int | risk level\
imr | decimal | The leverage risk limit level corresponds to initial margin rate\
mmr | decimal | Leverage risk limit level corresponds to maintenance margin rate\
leverage | int | leverage

## Switch leverage

- **POST** `api/v1/private/position/change_leverage`

**Required permissions:** Trading permission
Rate limit:20 times/2 seconds
**Request parameters:**
Parameter | Data Type | Mandatory | Description\
---|---|---|---\
positionId | long | true | position id\
leverage | int | true | leverage\
openType | int | false | Required when there is no position, openType, 1: isolated position, 2: full position\
symbol | string | false | equired when there is no position，symbol\
positionType | int | false | equired when there is no position, positionType: 1 Long 2:short\
**Response parameters:**
public parameters, success: true, success, false ,failure
**request parameters example:**

- Has positon:

```json
{
  "positionId": 1,
  "leverage": 20
}
```

- no positon:

```json
{
  "openType": 1,
  "leverage": 20,
  "symbol": "BTC_USDT",
  "positionType": 1
}
```

## Get position mode

- **GET** `api/v1/private/position/position_mode`

**Required permissions:** Trading permission
Rate limit:20 times/2 seconds
**Request parameters:**
None
**Response parameters:**
public parameters, success: true, success, false ,failure
position mode,1:hedge，2:one-way
**request parameters example:**

```json
{
  "success": true,
  "code": 0,
  "data": 2
}
```

## Change position mode

- **POST** `api/v1/private/position/change_position_mode`

**Required permissions:** Trading permission
Rate limit:20 times/2 seconds
**Request parameters:**
Parameter | Data Type | Mandatory | Description\
---|---|---|---\
positionMode | int | true | 1: Hedge，2, 2: One-way, the modification of the position mode must ensure that there are no active orders, planned orders, or unfinished positions, otherwise it cannot be modified. When switching the one-way mode in both directions, the risk limit level will be reset to level 1. If you need to change the call interface, modify\
**Response parameters:**
public parameters, success: true, success, false ,failure
**request parameters example:**

```json
{
  "success": true,
  "code": 0
}
```

## Order (Under maintenance)

> Response

```json
{
  "success": true,
  "code": 0,
  "data": 102057569836905984
}
```

USDT perpetual contract trading offers limit and market orders. You can place an order only you have enough money in your account. Once you place an order, your account funds will be frozen . The amount of funds frozen depends on the type and parameters specified in the order.

- **POST** `api/v1/private/order/submit`

**Required permissions:** Trading permission
Rate limit:20 times/2 seconds
**Request parameters:**
Parameter | Data Type | Mandatory | Description\
---|---|---|---\
symbol | string | true | the name of the contract\
price | decimal | true | price\
vol | decimal | true | volume\
leverage | int | false | leverage ,Leverage is necessary on Isolated Margin\
side | int | true | order direction 1 open long ,2close short,3open short ,4 close l\
type | int | true | orderType,1:price limited order,2:Post Only Maker,3:transact or cancel instantly ,4 : transact completely or cancel completely，5:market orders,6 convert market price to current price\
openType | int | true | open type,1:isolated,2:cross\
positionId | long | false | position Id，It is recommended to fill in this parameter when closing a position\
externalOid | string | false | external order ID\
stopLossPrice | decimal | false | stop-loss price\
takeProfitPrice | decimal | false | take-profit price\
positionMode | int | false | position mode,1:hedge,2:one-way,default: the user's current config\
reduceOnly | boolean | false | Default false,For one-way positions, if you need to only reduce positions, pass in true, and two-way positions will not accept this parameter.\
**Response parameters:**
success, success =true, data represent the order id success =false, failure data=null

## Bulk order (Under maintenance)

> Response

```json
[
  {
    "symbol": "BTC_USD",
    "price": 8800,
    "vol": 100,
    "leverage": 20,
    "side": 1,
    "type": 1,
    "openType": 1,
    "externalOid": "order1"
  },
  {
    "symbol": "BTC_USD",
    "price": 500,
    "vol": 100,
    "leverage": 50,
    "side": 3,
    "type": 1,
    "openType": 1,
    "externalOid": "order2"
  }
]
```

Order the contract in batch. Each contract can place 50 orders in the batch. This endpoint is not available for all users , please contact customer service to get this permission.

- **POST** `api/v1/private/order/submit_batch`

**Required permissions:** Trading permission
Rate limit:1/2 seconds
**Request parameters:**(maximum 50 )
Parameter | Data Type | Mandatory | Description\
---|---|---|---\
symbol | string | true | the name of the contract\
price | decimal | true | price\
vol | decimal | true | volume\
leverage | int | false | leverage ,Leverage is necessary on Isolated Margin\
side | int | true | order side 1open long,2close short,3open short, 4 close long\
type | int | true | order type :1 price limited order,2:Post Only Maker,3:transact or cancel instantly ,4 : transact completely or cancel completely，5:market orders,6 convert market price to current price\
openType | int | true | open type,1:isolated,2:cross\
positionId | long | false | position Id，It is recommended to fill in this parameter when closing a position\
externalOid | string | false | external order ID, return the existing order ID if it already exists\
stopLossPrice | decimal | false | stop-loss price\
takeProfitPrice | decimal | false | take-profit price\
**Response parameters:**
Parameter | Data Type | Description\
---|---|---\
externalOid | string | external order ID\
orderId | long | order ID, null on failure\
errorMsg | string | error message, not null when failed\
errorCode | int | error code, default is 0

## Cancel the order (Under maintenance)

> Response

```json
{
  "success": true,
  "code": 0,
  "data": [
    {
      "orderId": 101716841474621953,
      "errorCode": 2040,
      "errorMsg": "order not exist"
    },
    {
      "orderId": 108885377779302912,
      "errorCode": 2041,
      "errorMsg": "order state cannot be cancelled"
    },
    {
      "orderId": 108886241042563584,
      "errorCode": 0,
      "errorMsg": "success"
    }
  ]
}
```

Cancel the pending order placed before, each time can cancel up to 50 orders.

- **POST** `api/v1/private/order/cancel`

**Required permissions:** Trading permission
Rate limit:20 times/2 seconds
**Request parameters:**
Parameter | Data Type | Mandatory | Description\
---|---|---|---\
None | List | true | order id list, maximum 50\
**Response parameters:**
Parameter | Data Type | Description\
---|---|---\
orderId | long | order ID\
errorMsg | string | error message\
errorCode | int | error code，Not 0 means the revoke failed

## Cancel the order according to the external order ID (Under maintenance)

> Response

```json
{
  "symbol": "BTC_USDT",
  "externalOid": "mexc-a-001"
}
```

Cancel the uncompleted order under a contract according to the specified externalOid, only 1 order for each cancellation.

- **POST** `api/v1/private/order/cancel_with_external`

Rate limit:20 times/2 seconds
**Request parameters:**
Parameter | Data Type | Mandatory | Description\
---|---|---|---\
symbol | string | true | the name of the contract\
externalOid | string | true | external orderid

## Cancel all orders under a contract (Under maintenance)

Cancel all uncompleted orders under a contract.

- **POST** `api/v1/private/order/cancel_all`

**Required permissions:** Trading permission
Rate limit:20 times/2 seconds
**Request parameters:**
Parameter | Data Type | Mandatory | Description\
---|---|---|---\
symbol | string | false | the name of the contract, cancel specific orders placed under this contract when fill the symbol , otherwise , cancel all orders without filling\
**Response parameters:**
public parameters , success: true success, false failure

## Switch the risk level

- **POST** `api/v1/private/account/change_risk_level`
- Disabled The call returns the error code 8817 Prompt information: The risk restriction function has been upgraded. For details, please go to the web to view

## Trigger order (Under maintenance)

- **POST** `api/v1/private/planorder/place`

Rate limit:20 times/2 seconds
**Request parameters:**
Parameter | Data Type | Mandatory | Description\
---|---|---|---\
symbol | string | true | the name of the contract\
price | decimal | false | execut price, market price may not fill in\
vol | decimal | true | volume\
leverage | int | false | leverage , Leverage is necessary on Isolated Margin\
side | int | true | 1open long,2close short,3open short 4 close long\
openType | int | true | open type,1:isolated,2:cross\
triggerPrice | decimal | true | trigger price\
triggerType | int | true | trigger type,1: more than or equal, 2: less than or equal\
executeCycle | int | true | execution cycle,1: 24 hours,2: 7 days\
orderType | int | true | order type,1: limit order,2:Post Only Maker,3: close or cancel instantly ,4: close or cancel completely,5: Market order\
trend | int | true | trigger price type,1: latest price, 2: fair price, 3: index price\
**Response parameters:**
success, success =true, data value is the order ID, success =false, failure data=null

## Cancel the trigger order (Under maintenance)

> Response

```json
[
  {
    "symbol": "BTC_USDT",
    "orderId": 1
  },
  {
    "symbol": "ETH_USDT",
    "orderId": 2
  }
]
```

- **POST** `api/v1/private/planorder/cancel`

Rate limit:20 times/2 seconds
**Request parameters:**
Parameter | Data Type | Mandatory | Description\
---|---|---|---\
None | List | true | cancel the order list, maximum 50\
**CancelOrderRequest:**
Parameter | Data Type | Mandatory | Description\
---|---|---|---\
symbol | string | true | the name of the contract\
orderId | string | true | orderId\
**Response parameters:**
public parameters, Success: true success, false failure

## Cancel all trigger orders (Under maintenance)

- **POST** `api/v1/private/planorder/cancel_all`

Rate limit:20 times/2 seconds
**Request parameters:**
Parameter | Data Type | Mandatory | Description\
---|---|---|---\
symbol | string | false | the name of the contract, cancel specific orders placed under this contract when fill the symbol , otherwise , cancel all orders without filling\
**Response parameters:**
public parameters, Success: true success, false failure

## Cancel the Stop-Limit trigger order (Under maintenance)

> Response

```json
[
  {
    "stopPlanOrderId": 1
  },
  {
    "stopPlanOrderId": 2
  }
]
```

- **POST** `api/v1/private/stoporder/cancel`

Rate limit:20 times/2 seconds
**Request parameters:**
Parameter | Data Type | Mandatory | Description\
---|---|---|---\
none | List | true | cancel order list, maximum 50\
**CancelOrderRequest:**
Parameter | Data Type | Mandatory | Description\
---|---|---|---\
stopPlanOrderId | long | true | the Stop-Limit trigger order ID

## Cancel all Stop-Limit price trigger orders (Under maintenance)

- **POST** `api/v1/private/stoporder/cancel_all`

Rate limit:20 times/2 seconds
**Request parameters:**
Parameter | Data Type | Mandatory | Description\
---|---|---|---\
positionId | long | false | position id, fill in positionId，only cancel the trigger order of the corresponding position, and check the symbol without filling\
symbol | string | false | the name of the contact ,only cancels the delegate order under this contract based on the symbol, cancel all orders without filling the symbol\
**Response parameters:**
public parameters, success: true success ,false failure

## Switch Stop-Limit limited order price

- **POST** `api/v1/private/stoporder/change_price`

Rate limit:20 times/2 seconds
**Request parameters:**
Parameter | Data Type | Mandatory | Description\
---|---|---|---\
orderId | long | true | limit order id\
stopLossPrice | decimal | false | stop-loss price, take-profit and stop-loss price are empty or 0 at the same time, indicating to cancel and take profit\
takeProfitPrice | decimal | false | take-profit price，take-profit and stop-loss price are empty or 0 at the same time, indicating to cancel stop-loss and take profit\
**Response parameters:**
public parameters, success: true success ,false failure

## Switch the Stop-Limit price of trigger orders

- **POST** `api/v1/private/stoporder/change_plan_price`

Rate limit:20 times/2 seconds
**Request parameters:**
Parameter | Data Type | Mandatory | Description\
---|---|---|---\
stopPlanOrderId | long | true | the Stop-Limit price of trigger order id\
stopLossPrice | decimal | false | at least one stop-loss price and one take-profit price is not empty and must be more than 0\
takeProfitPrice | decimal | false | at least one take-profit price and stop-loss price is not empty and must be more than 0\
**Response parameters:**
public parameters, success: true success ,false failure
