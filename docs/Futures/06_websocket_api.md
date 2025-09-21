# WebSocket API

WebSocket is a new Protocol in HTML5. It realizes full-duplex communication between client and server. A single handshake can establish the connection between the client and the server, and the server can actively send information to the client according to the rules. The advantages are as follows:

1. The request header information is relatively small about 2 bytes when the client and server transfer the data.
1. Both the client and the server can actively send data to each other.
1. No need to create or destroy TCP requests many times, saving bandwidth and server resources.

Developers are strongly advised to use the WebSocket API for market trends and buying/ selling depth information.

## Native WS connection address

- wss://contract.mexc.com/edge

## Detailed data interaction commands

> Send ping message

```json
{
  "method": "ping"
}
```

> Server return

```json
{
  "channel": "pong",
  "data": 1587453241453
}
```

List of subscribe/unsubscribe data commands ( ws identification is not required except the list of personal related commands)
If no ping is received within 1 minute, the connection will be disconnected. It is recommended to send a ping for 10-20 seconds
The ping message and server return are shown on the right

## Filter Subscription

> cancel default push

```json
{
  "subscribe": false,
  "method": "login",
  "param": {
    "apiKey": "mxU1TzSmRDW1o5AsE",
    "signature": "8c957a757ea31672eca05cb652d26bab7f46a41364adb714dda5475264aff120",
    "reqTime": "1611038237237"
  }
}
```

> asset only

```json
{
  "method": "personal.filter",
  "param": {
    "filters": [
      {
        "filter": "asset"
      }
    ]
  }
}
```

> ADLlevel only

```json
{
  "method": "personal.filter",
  "param": {
    "filters": [
      {
        "filter": "adl.level"
      }
    ]
  }
}
```

> deals only

```json
{
  "method": "personal.filter",
  "param": {
    "filters": [
      {
        "filter": "order.deal",
        "rules": []
      }
    ]
  }
}
```

> or

```json
{
  "method": "personal.filter",
  "param": {
    "filters": [
      {
        "filter": "order.deal"
      }
    ]
  }
}
```

> deal for symbol

```json
{
  "method": "personal.filter",
  "param": {
    "filters": [
      {
        "filter": "order.deal",
        "rules": [
          "BTC_USDT"
        ]
      }
    ]
  }
}
```

> coordinate

```json
{
  "method": "personal.filter",
  "param": {
    "filters": [
      {
        "filter": "order",
        "rules": [
          "BTC_USDT"
        ]
      },
      {
        "filter": "order.deal",
        "rules": [
          "EOS_USDT",
          "ETH_USDT",
          "BTC_USDT"
        ]
      },
      {
        "filter": "position",
        "rules": [
          "EOS_USDT",
          "BTC_USDT"
        ]
      },
      {
        "filter": "asset"
      }
    ]
  }
}
```

All private data will be pushed after login:order、order.deal、position、plan.order、stop.order、stop.planorder、risk.limit、adl.level、asset.

1. If want to cancel the default push,add params when login: `"subscribe":false`.
1. after login sucess,send "personal.filter" to filter the subscription，if want all data be pushed,send: `{"method":"personal.filter"}`or `{"method":"personal.filter","param":{"filters":[]}}`.
1. available key for filter:order、order.deal、position、plan.order、stop.order、stop.planorder、risk.limit、adl.level、asset.

only asset and adl.level not support for filter single currency or single future.
The filter event sent later will overwrites the previous one.

## Public Channels

### Tickers

> Subscribe

```json
{
  "method": "sub.tickers",
  "param": {}
}
```

> If you want to return content (the same with following subscription):

```json
{
  "method": "sub.tickers",
  "param": {},
  "gzip": false
}
```

> Unsubscribe

```json
{
  "method": "unsub.tickers",
  "param": {}
}
```

> Example

```json
{
  "channel": "push.tickers",
  "data": [
    {
      "fairPrice": 183.01,
      "lastPrice": 183,
      "riseFallRate": -0.0708,
      "symbol": "BSV_USDT",
      "volume24": 200
    },
    {
      "fairPrice": 220.22,
      "lastPrice": 220.4,
      "riseFallRate": -0.0686,
      "symbol": "BCH_USDT",
      "volume24": 200
    }
  ],
  "ts": 1587442022003
}
```

Get the latest transaction price, buy-price, sell-price and 24 transaction volume of all the perpetual contracts on the platform without login. Send once a second after subscribing.
subscribe , unsubscribe, example is shown on the right.
**Response parameters:**
Parameter | Data Type | Description
---|---|---
symbol | string | the name of the contract
lastPrice | decimal | the last price
volume24 | decimal | 24 hours trading volume, according to the statistics count
riseFallRate | decimal | rise/fall rate
fairPrice | decimal | fair price

### Ticker

> Subscribe

```json
{
  "method": "sub.ticker",
  "param": {
    "symbol": "BTC_USDT"
  }
}
```

> Unsubscribe

```json
{
  "method": "unsub.ticker",
  "param": {
    "symbol": "BTC_USDT"
  }
}
```

> Example

```json
{
  "channel": "push.ticker",
  "data": {
    "ask1": 6866.5,
    "bid1": 6865,
    "contractId": 1,
    "fairPrice": 6867.4,
    "fundingRate": 0.0008,
    "high24Price": 7223.5,
    "indexPrice": 6861.6,
    "lastPrice": 6865.5,
    "lower24Price": 6756,
    "maxBidPrice": 7073.42,
    "minAskPrice": 6661.37,
    "riseFallRate": -0.0424,
    "riseFallValue": -304.5,
    "symbol": "BTC_USDT",
    "timestamp": 1587442022003,
    "holdVol": 2284742,
    "volume24": 164586129
  },
  "symbol": "BTC_USDT",
  "ts": 1587442022003
}
```

Get the latest transaction price, buy price, sell price and 24 transaction volume of a contract, send the transaction data without users' login, and send once a second after subscription.
subscribe , unsubscribe, example is shown on the right.
**Response parameters:**
Parameter | Data Type | Description
---|---|---
symbol | string | the name of the contract
lastPrice | decimal | last price
bid1 | decimal | bid/price
ask1 | decimal | ask/price
volume24 | decimal | 24 hours transaction volume, according to the statistical count
holdVol | decimal | hold volume
lower24Price | decimal | lowest price within 24 hours
high24Price | decimal | highest price in 24 hours
riseFallRate | decimal | rise fall rate
riseFallValue | decimal | rise fall value
indexPrice | decimal | index price
fairPrice | decimal | fair price
fundingRate | decimal | funding fee
timestamp | long | system timestamp

### Deal

> subscribe

```json
{
  "method": "sub.deal",
  "param": {
    "symbol": "BTC_USDT"
  }
}
```

> Unsubscribe

```json
{
  "method": "unsub.deal",
  "param": {
    "symbol": "BTC_USDT"
  }
}
```

> Example

```json
{
  "symbol": "BTC_USDT",
  "data": [
    {
      "p": 115309.8,
      "v": 55,
      "T": 2,
      "O": 3,
      "M": 1,
      "t": 1755487578276
    },
    {
      "p": 115309.8,
      "v": 11,
      "T": 1,
      "O": 3,
      "M": 1,
      "t": 1755487578275
    }
  ],
  "channel": "push.deal",
  "ts": 1755487578276
}
```

Access to the latest data without login, and keep updating.
Zipped push by default,if want all deal data push,please set `compress` to `false`
**Response parameters:**
Parameter | Data Type | Description
---|---|---
p | decimal | transaction price
v | decimal | volume
T | int | transaction direction,1:purchase,2:sell
O | int | open position, 1: open position,2:close position,3:position no change,volume is the additional position when O is 1
M | int | Is it auto-transact ? 1: Yes,2: No
t | long | transaction time

### Depth

> Subscription increments (all)

```json
{
  "method": "sub.depth",
  "param": {
    "symbol": "BTC_USDT"
  }
}
```

> Subscription increments (zipped push)

```json
{
  "method": "sub.depth",
  "param": {
    "symbol": "BTC_USDT",
    "compress": true
  }
}
```

> Full subscription (Limit could be 5, 10 or 20, default 20 without define., only subscribe to the full amount of one gear)

```json
{
  "method": "sub.depth.full",
  "param": {
    "symbol": "BTC_USDT",
    "limit": 5
  }
}
```

> unsubscribe (cancel the incremental subscription)

```json
{
  "method": "unsub.depth",
  "param": {
    "symbol": "BTC_USDT"
  }
}
```

> Unsubscribe (cancel the full subscription, limit is not mandatory)

```json
{
  "method": "usub.depth.full",
  "param": {
    "symbol": "BTC_USDT"
  }
}
```

> Example

```json
{
  "channel": "push.depth",
  "data": {
    "asks": [
      [
        6859. 5,
        3251,
        1
      ]
    ],
    "bids": [],
    "version": 96801927
  },
  "symbol": "BTC_USDT",
  "ts": 1587442022003
}
```

subscribe , unsubscribe, example is shown on the right. Incremental depth subscription has merging enabled by default. If you do not want to enable it, please set `compress` to `false` when subscribing.
**Response Parameter:**
Parameter | Data Type | Description
---|---|---
asks | List | seller depth
bids | List | buyer depth
version | long | the version number
Tip: [411.8, 10, 1] 411.8 is price，10 is the order numbers of the contract ,1 is the order quantity

### K-line

> Subscribe

```json
{
  "method": "sub.kline",
  "param": {
    "symbol": "BTC_USDT",
    "interval": "Min60"
  }
}
```

> Unsubscribe

```json
{
  "method": "unsub.kline",
  "param": {
    "symbol": "BTC_USDT"
  }
}
```

> Example

```json
{
  "channel": "push.kline",
  "data": {
    "a": 233.74026934364474,
    "c": 6885,
    "h": 6910.5,
    "interval": "Min60",
    "l": 6885,
    "o": 6894.5,
    "q": 1611754,
    "symbol": "BTC_USDT",
    "t": 1587448800
  },
  "symbol": "BTC_USDT",
  "ts": 1587442022003
}
```

Get the k-line data of the contract and keep updating.
subscribe , unsubscribe, example is shown on the right.
interval optional parameters: Min1、Min5、Min15、Min30、Min60、Hour4、Hour8、Day1、Week1、Month1
**Response parameters:**
Parameter | Data Type | Description
---|---|---
symbol | string | the name of the contract
a | decimal | total transaction amount
c | decimal | the closing price
interval | string | interval: Min1、Min5、Min15、Min30、Min60、Hour4、Hour8、Day1、Week1、Month1
l | decimal | the lowest price
o | decimal | the opening price
q | decimal | total transaction volume
h | decimal | the highest price
t | long | trading time，unit：second（s）， the start time of the window（windowStart）

### Funding rate

> Subscribe

```json
{
  "method": "sub.funding.rate",
  "param": {
    "symbol": "BTC_USDT"
  }
}
```

> unsubscribe

```json
{
  "method": "unsub.funding.rate",
  "param": {
    "symbol": "BTC_USDT"
  }
}
```

> Example

```json
{
  "channel": "push.funding.rate",
  "data": {
    "rate": 0.001,
    "symbol": "BTC_USDT"
  },
  "symbol": "BTC_USDT",
  "ts": 1587442022003
}
```

Get the contract funding rate, and keep updating.
subscribe , unsubscribe, example is shown on the right.
**Response parameters:**
Parameter | Data Type | Description
---|---|---
symbol | string | the name of the contract
fundingRate | decimal | funding rate
nextSettleTime | long | next liquidate time

### Index price

> subscribe

```json
{
  "method": "sub.index.price",
  "param": {
    "symbol": "BTC_USDT"
  }
}
```

> unsubscribe

```json
{
  "method": "unsub.index.price",
  "param": {
    "symbol": "BTC_USDT"
  }
}
```

> Example

```json
{
  "channel": "push.index.price",
  "data": {
    "price": 0.001,
    "symbol": "BTC_USDT"
  },
  "symbol": "BTC_USDT",
  "ts": 1587442022003
}
```

Get the index price, and will keep updating if there is any changes.
subscribe , unsubscribe, example is shown on the right.
**Response parameters:**
Parameter | Data Type | Description
---|---|---
symbol | string | the name of the contract
price | decimal | price

### Fair price

> Subscribe

```json
{
  "method": "sub.fair.price",
  "param": {
    "symbol": "BTC_USDT"
  }
}
```

> Unsubscribe

```json
{
  "method": "unsub.fair.price",
  "param": {
    "symbol": "BTC_USDT"
  }
}
```

> Example

```json
{
  "channel": "push.fair.price",
  "data": {
    "price": 0.001,
    "symbol": "BTC_USDT"
  },
  "symbol": "BTC_USDT",
  "ts": 1587442022003
}
```

subscribe , unsubscribe, example is shown on the right.
**Response parameters**
Parameter | Data Type | Description
---|---|---
symbol | string | the name of the contract
price | decimal | price

## Private Channels

**Signature:**
The signature target string is: accessKey + timestamp, The HMAC SHA256 algorithm is used to sign the target string.
**Signature String:**
`"mx0aBYs33eIilxBW5C1657186536762"`

### Login authentication

> Payload

```json
{
  "channel": "rs.login",
  "data": "success",
  "ts": "1587442022003"
}
```

```json
{
  "method":"login",
  "param":{
    "apiKey":"apiKey",// openapi need to fill in this parameter，Parameters are constructed in accordance with the OpenAPI documentation
    "reqTime":"reqTime",// openapi need to fill in this parameters，Parameters are constructed in accordance with the OpenAPI documentation
    "signature":"signature"// openapi need to fill in this parameters，Parameters are constructed in accordance with the OpenAPI documentation
  }
}
```

**Response parameters:**
Success: none, failure: return the corresponding error message, channel = rs.error
Login successful (channel = rs.login)

### Order

> Payload

```json
{
  "channel": "push.personal.order",
  "data": {
    "category": 1,
    "createTime": 1610005069976,
    "dealAvgPrice": 0.731,
    "dealVol": 1,
    "errorCode": 0,
    "externalOid": "_m_95bc2b72d3784bce8f9efecbdef9fe35",
    "feeCurrency": "USDT",
    "leverage": 0,
    "makerFee": 0,
    "openType": 1,
    "orderId": "102067003631907840",
    "orderMargin": 0,
    "orderType": 5,
    "positionId": 1397818,
    "price": 0.707,
    "profit": -0.0005,
    "remainVol": 0,
    "side": 4,
    "state": 3,
    "symbol": "CRV_USDT",
    "takerFee": 4.386e-05,
    "updateTime": 1610005069983,
    "usedMargin": 0,
    "version": 2,
    "vol": 1
  },
  "ts": 1610005069989
}
```

`channel = push.personal.order`
Parameter | Data Type | Description
---|---|---
orderId | long | orderid
symbol | string | the name of the contract
positionId | long | position id
price | decimal | trigger price
vol | decimal | trigger volume
leverage | long | leverage
side | int | order side 1open long,2close short,3open short 4 close long
category | int | order category:1limit order, 2 system take-over delegate, 3 close delegate 4 ADL reduction
orderType | int | true
dealAvgPrice | decimal | transaction average price
dealVol | decimal | transaction volume
orderMargin | decimal | order margin
usedMargin | decimal | used margin
takerFee | decimal | taker fee
makerFee | decimal | maker fee
profit | decimal | close profit
feeCurrency | string | fee currency
openType | int | open type,1:isolated,2:cross
state | int | order state,1 uninformed,2 uncompleted,3 completed,4 cancelled,5 invalid
errorCode | int | error code, 0:normal, 1:param_invalid, 2:insufficient_balance, 3:position_not_exists, 4:position_not_enough, 5:position_liq, 6:order_liq, 7:risk_level_limit, 8:sys_cancel, 9:position_mode_not_match, 10:reduce_only_liq, 11:contract_not_enable, 12:delivery_cancel, 13:position_liq_cancel, 14:adl_cancel, 15:black_user_cancel, 16:settle_funding_cancel, 17:position_im_change_cancel, 18:ioc_cancel, 19:fok_cancel, 20:post_only_cancel, 21:market_cancel
externalOid | string | external order id
createTime | date | create time
updateTime | date | update time

### Asset

> Payload

```json
{
  "channel": "push.personal.asset",
  "data": {
    "availableBalance": 0.7514236,
    "bonus": 0,
    "currency": "USDT",
    "frozenBalance": 0,
    "positionMargin": 0
  },
  "ts": 1610005070083
}
```

`channel = push.personal.asset`
Parameter | Data Type | Description
---|---|---
currency | string | currency
positionMargin | decimal | position margin
frozenBalance | decimal | frozen balance
availableBalance | decimal | available balance
cashBalance | decimal | drawable balance

### Position

> Payload

```json
{
  "channel": "push.personal.position",
  "data": {
    "autoAddIm": false,
    "closeAvgPrice": 0.731,
    "closeVol": 1,
    "frozenVol": 0,
    "holdAvgPrice": 0.736,
    "holdFee": 0,
    "holdVol": 0,
    "im": 0,
    "leverage": 15,
    "liquidatePrice": 0,
    "oim": 0,
    "openAvgPrice": 0.736,
    "openType": 1,
    "positionId": 1397818,
    "positionType": 1,
    "realised": -0.0005,
    "state": 3,
    "symbol": "CRV_USDT"
  },
  "ts": 1610005070157
}
```

`channel = push.personal.position`
Parameter | Data Type | Description
---|---|---
positionId | long | position id
symbol | string | the name of the contract
holdVol | decimal | hold volume
positionType | int | position type， 1long 2short
openType | int | open type， 1isolated 2cross
state | int | position state,1holding2system holding 3closed
frozenVol | decimal | frozen volume
closeVol | decimal | close volume
holdAvgPrice | decimal | hold average price
closeAvgPrice | decimal | close average price
openAvgPrice | decimal | open average price
liquidatePrice | decimal | liquidate price
oim | decimal | original initial margin
adlLevel | int | the value of ADL is 1-5. If it is empty, wait for the refresh
im | decimal | initial margin， add or subtract this item can be used to adjust the liquidate price
holdFee | decimal | hold fee, positive means u get it, negative means lose it
realised | decimal | realized profit and loss
createTime | date | create time
updateTime | date | update time

### Risk limitation

`channel = push.personal.risk.limit`
Parameter | Data Type | Description
---|---|---
symbol | string | the name of the contract
positionType | int | position type 1:long，2:short
riskSource | int | Source of risk 0:other 1: Liquidation Service
level | int | current risk level
maxVol | decimal | maximum position volume
maxLeverage | int | maximum leverage ratio
mmr | decimal | maintenance margin rate
imr | decimal | initial margin rate

### Adl automatic reduction of position level

> Payload

```json
{
  "channel": "push.personal.adl.level",
  "data": {
    "adlLevel": 0,
    "positionId": 1397818
  },
  "ts": 1610005032231
}
```

`channel = push.personal.adl.level`
Parameter | Data Type | Description
---|---|---
adlLevel | int | the current adl level ：1-5
positionId | long | position id

### Position Mode

```json
{
  "channel": "push.personal.position.mode",
  "data": {
    "positionMode": 1
  },
  "ts": 1610005070157
}
```

`channel = push.personal.position.mode`
Parameter | Data Type | Description
---|---|---
positionMode | int | position mode,1:hedge，2:one-way

## How is depth information maintained

> Example: Submit subscription information

```json
{
  "method": "sub.deal",
  "param": {
    "symbol": "BTC_USDT"
  }
}
```

> subscribe succeed response

```json
{
  "channel": "rs.sub.deal",
  "data": "success",
  "ts": "1587442022003"
}
```

> subscribe failed response

```json
{
  "channel": "rs.error",
  "data": "Contract doesn't exist!",
  "ts": "1587442022003"
}
```

**How is incremental depth information maintained:**

1. Though /api/v1/contract/depth/BTC_USDT to get full amount of depth information, save the current version.
1. Subscribe to ws depth information, if the received data version more than the current version after update, the later received update cover the previous one at the same price.
1. Through /api/v1/contract/depth_commits/BTC_USDT/1000 get the latest 1000 depth snapshots.
1. Discard version data from the snapshot obtained by Version (less than step 3 ) for the same price in the current cached depth information
1. Update the contents of the deep snapshots to the local cache and keep updating from the event received by the WS
1. The version of each new event should be exactly equal to version+1 of the previous event, otherwise packet loss may occur. In case of packet loss or discontinuous version of the event retrieved, please re-initialize from Step 3.
1. The amount of hanging orders in each event represents the absolute value of the current hanging orders of the price, rather than the relative change.
1. If the amount of a hanging order corresponding to a certain price is 0, it means that the hanging order at that price has been cancelled, the price should be removed.

**Subscriptions，subscribe succeed response:**
channel : rs. + subscription method， data is "success"
