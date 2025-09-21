[Skip to main content](#__docusaurus_skipToContent_fallback)

[![MEXC Logo](/api-docs-assets/img/mexc-logo.svg)![MEXC Logo](/api-docs-assets/img/mexc-logo.svg)](https://www.mexc.com/)[SpotV3](/api-docs/spot-v3/introduction)[Futures](/api-docs/futures/update-log)[Broker](/api-docs/broker/mexc-broker-introduction)

English

* [English](/api-docs/spot-v3/websocket-user-data-streams)
* [中文](/zh-MY/api-docs/spot-v3/websocket-user-data-streams)

* [Introduction](/api-docs/spot-v3/introduction)
* [Change Log](/api-docs/spot-v3/change-log)
* [FAQs](/api-docs/spot-v3/faqs)
* [General Info](/api-docs/spot-v3/general-info)
* [Market Data Endpoints](/api-docs/spot-v3/market-data-endpoints)
* [Sub-Account Endpoints](/api-docs/spot-v3/subaccount-endpoints)
* [Spot Account/Trade](/api-docs/spot-v3/spot-account-trade)
* [Wallet Endpoints](/api-docs/spot-v3/wallet-endpoints)
* [Websocket Market Streams](/api-docs/spot-v3/websocket-market-streams)
* [Websocket User Data Streams](/api-docs/spot-v3/websocket-user-data-streams)
* [Rebate Endpoints](/api-docs/spot-v3/rebate-endpoints)
* [Public API Definitions](/api-docs/spot-v3/public-api-definitions)

On this page

# Websocket User Data Streams

* The base API endpoint is: **<https://api.mexc.com>**
* A User Data Stream `listenKey` is valid for 60 minutes after creation.
* Doing a `PUT` on a `listenKey` will extend its validity for 60 minutes.
* Doing a `DELETE` on a `listenKey` will close the stream and invalidate the `listenKey`.
* websocket baseurl: **ws://wbs-api.mexc.com/ws**
* User Data Streams are accessed at **/ws?listenKey=listenKey**
  For example: **ws://wbs-api.mexc.com/ws?listenKey=pqia91ma19a5s61cv6a81va65sd099v8a65a1a5s61cv6a81va65sdf19v8a65a1**
* A single connection is only valid for 24 hours; expect to be disconnected at the 24 hour mark.
* Each UID can apply for a maximum of 60 listen keys (excluding invalid listen keys).
* Each listen key maximum support 5 websocket connection (which means each uid can applies for a maximum of 60 listen keys and 300 ws links).

## Listen Key[​](#listen-key "Direct link to Listen Key")

### Generate Listen Key[​](#generate-listen-key "Direct link to Generate Listen Key")

> **Response**

```
{
  "listenKey": "pqia91ma19a5s61cv6a81va65sdf19v8a65a1a5s61cv6a81va65sdf19v8a65a1"
}

```

**Required Permissions:** Account Read / SPOT\_ACCOUNT\_R

**HTTP Request**

* **POST** `/api/v3/userDataStream`

Starts a new data stream. The stream will close 60 minutes after creation unless a keepalive is sent.

**Parameters:**

NONE

---

### Get Valid Listen Keys[​](#get-valid-listen-keys "Direct link to Get Valid Listen Keys")

> **Response**

```
{
    "listenKey": [
        "c285bc363cfeac6646576b801a2ed1f9523310fcda9e927e509aaaaaaaaaaaaaa",
        "87cb8da0fb150e36c232c2c060bc3848693312008caf3acae73bbbbbbbbbbbb",
        "dc027517ebee2328b75268461a9df4d21addfac6ebebab8f5a6cccccccccccccc"
    ]
}

```

**Required Permissions:** Account Read / SPOT\_ACCOUNT\_R

**HTTP Request**

* **GET** `/api/v3/userDataStream`

Retrieves all currently valid listen keys.

**Parameters:**

NONE

---

### Extend Listen Key Validity[​](#extend-listen-key-validity "Direct link to Extend Listen Key Validity")

> **Response**

```
{
    "listenKey": "pqia91ma19a5s61cv6a81va65sdf19v8a65a1a5s61cv6a81va65sdf19v8a65a1"
}

```

**HTTP Request**

* **PUT** `/api/v3/userDataStream`

Extends the validity to 60 minutes from the time of this call. It is recommended to send a request every 30 minutes.

**Request Parameters:**

| Parameter | Data Type | Required | Description |
| --- | --- | --- | --- |
| listenKey | string | Yes |  |

---

### Close Listen Key[​](#close-listen-key "Direct link to Close Listen Key")

> **Response**

```
{
    "listenKey": "pqia91ma19a5s61cv6a81va65sdf19v8a65a1a5s61cv6a81va65sdf19v8a65a1"
}

```

**HTTP Request**

* **DELETE** `/api/v3/userDataStream`

Closes the user data stream.

**Request Parameters:**

| Parameter | Data Type | Required | Description |
| --- | --- | --- | --- |
| listenKey | string | Yes |  |

---

## Spot Account Update[​](#spot-account-update "Direct link to Spot Account Update")

After a successful subscription, whenever the account balance or available balance changes, the server will push updates of the account assets.

> **Request:**

```
{
    "method": "SUBSCRIPTION",
    "params": [
        "spot@private.account.v3.api.pb"
    ]
}

```

> **Response:**

```
{
  channel: "spot@private.account.v3.api.pb",
  createTime: 1736417034305,
  sendTime: 1736417034307,
  privateAccount {
    vcoinName: "USDT",
    coinId: "128f589271cb4951b03e71e6323eb7be",
    balanceAmount: "21.94210356004384",
    balanceAmountChange: "10",
    frozenAmount: "0",
    frozenAmountChange: "0",
    type: "CONTRACT_TRANSFER",
    time: 1736416910000
  }
}

```

**Request Parameter:** `spot@private.account.v3.api.pb`

**Response Parameters:**

| Parameter | Data Type | Description |
| --- | --- | --- |
| privateAccount | json | Account information |
| vcoinName | string | Asset name |
| balanceAmount | string | Available balance |
| balanceAmountChange | string | Change in available balance |
| frozenAmount | string | Frozen balance |
| frozenAmountChange | string | Change in frozen balance |
| type | string | Change type ([see details](#account_position "see details")) |
| time | long | Settlement time |

---

## Spot Account Deals[​](#spot-account-deals "Direct link to Spot Account Deals")

> **Request:**

```
{
    "method": "SUBSCRIPTION",
    "params": [
        "spot@private.deals.v3.api.pb"
    ]
}

```

> **Response:**

```
{
  channel: "spot@private.deals.v3.api.pb",
  symbol: "MXUSDT",
  sendTime: 1736417034332,
  privateDeals {
    price: "3.6962",
    quantity: "1",
    amount: "3.6962",
    tradeType: 2,
    isMaker:false,
    tradeId: "505979017439002624X1",
    orderId: "C02__505979017439002624115",
    feeAmount: "0.0003998377369698171",
    feeCurrency: "MX",
    time: 1736417034280
  }
}

```

**Request Parameter:** `spot@private.deals.v3.api.pb`

**Response Parameters:**

| Parameter | Data Type | Description |
| --- | --- | --- |
| symbol | string | Trading pair |
| sendTime | long | Event time |
| privateDeals | json | Account trade information |
| price | string | Trade price |
| quantity | string | Trade quantity |
| amount | string | Trade amount |
| tradeType | int | Trade type (1: Buy, 2: Sell) |
| tradeId | string | Trade ID |
| isMaker | Boolean | is maker |
| orderId | string | Order ID |
| clientOrderId | string | User-defined order ID |
| feeAmount | string | Fee amount |
| feeCurrency | string | Fee currency |
| time | long | Trade time |

---

## Spot Account Orders[​](#spot-account-orders "Direct link to Spot Account Orders")

> **Request:**

```
{
  "method": "SUBSCRIPTION",
  "params": [
      "spot@private.orders.v3.api.pb"
  ]
}

```

**Request Parameter:** `spot@private.orders.v3.api.pb`

> **Response:**

```
{
  channel: "spot@private.orders.v3.api.pb",
  symbol: "MXUSDT",
  sendTime: 1736417034281,
  privateOrders {
    clientId: "C02__505979017439002624115",
    price: "3.5121",
    quantity: "1",
    amount: "0",
    avgPrice: "3.6962",
    orderType: 5,
    tradeType: 2,
    remainAmount: "0",
    remainQuantity: "0",
    lastDealQuantity: "1",
    cumulativeQuantity: "1",
    cumulativeAmount: "3.6962",
    status: 2,
    createTime: 1736417034259
  }
}

```

**Response Parameters:**

| Parameter | Data Type | Description |
| --- | --- | --- |
| symbol | string | Trading pair |
| sendTime | long | Event time |
| privateOrders | json | Account order information |
| clientId | string | Order ID |
| price | bigDecimal | Order price |
| quantity | bigDecimal | Order quantity |
| amount | bigDecimal | Total order amount |
| avgPrice | bigDecimal | Average trade price |
| orderType | int | Order type: LIMIT\_ORDER (1), POST\_ONLY (2), IMMEDIATE\_OR\_CANCEL (3), FILL\_OR\_KILL (4), MARKET\_ORDER (5); Stop loss/take profit (100) |
| tradeType | int | Trade type (1: Buy, 2: Sell) |
| remainAmount | bigDecimal | Remaining amount |
| remainQuantity | bigDecimal | Remaining quantity |
| cumulativeQuantity | bigDecimal | Cumulative trade quantity |
| cumulativeAmount | bigDecimal | Cumulative trade amount |
| status | int | Order status: 1: Not traded, 2: Fully traded, 3: Partially traded, 4: Canceled, 5: Partially canceled |
| createTime | long | Order creation time |

[Previous

Websocket Market Streams](/api-docs/spot-v3/websocket-market-streams)[Next

Rebate Endpoints](/api-docs/spot-v3/rebate-endpoints)

* [Listen Key](#listen-key)
  + [Generate Listen Key](#generate-listen-key)
  + [Get Valid Listen Keys](#get-valid-listen-keys)
  + [Extend Listen Key Validity](#extend-listen-key-validity)
  + [Close Listen Key](#close-listen-key)
* [Spot Account Update](#spot-account-update)
* [Spot Account Deals](#spot-account-deals)
* [Spot Account Orders](#spot-account-orders)