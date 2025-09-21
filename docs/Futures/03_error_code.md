[Skip to main content](https://www.mexc.com/api-docs/futures/error-code#__docusaurus_skipToContent_fallback "Skip to main content")
[![MEXC Logo](https://www.mexc.com/api-docs-assets/img/mexc-logo.svg)](https://www.mexc.com/ "https://www.mexc.com/")[SpotV3](https://www.mexc.com/api-docs/spot-v3/introduction "SpotV3")[Futures](https://www.mexc.com/api-docs/futures/update-log "Futures")[Broker](https://www.mexc.com/api-docs/broker/mexc-broker-introduction "Broker")
[](https://www.mexc.com/api-docs/futures/error-code "English")

- [English](https://www.mexc.com/api-docs/futures/error-code "English")

- [中文](https://www.mexc.com/zh-MY/api-docs/futures/error-code "中文")

- [Update log](https://www.mexc.com/api-docs/futures/update-log "Update log")

- [Integration guide](https://www.mexc.com/api-docs/futures/integration-guide "Integration guide")

- [Error code](https://www.mexc.com/api-docs/futures/error-code "Error code")

- [Market endpoints](https://www.mexc.com/api-docs/futures/market-endpoints "Market endpoints")

- [Account and trading endpoints](https://www.mexc.com/api-docs/futures/account-and-trading-endpoints "Account and trading endpoints")

- [WebSocket API](https://www.mexc.com/api-docs/futures/websocket-api "WebSocket API")

On this page

# Error code

## Error code Example[​](https://www.mexc.com/api-docs/futures/error-code#error-code-example "Direct link to Error code Example")

Every endpoint has the potential for abnormalities.
The following is the error code information that the endpoint might return
code | description\
---|---\
0 | Operate succeed\
9999 | Public abnormal\
500 | Internal error\
501 | System busy\
401 | Unauthorized\
402 | Api_key expired\
406 | Accessed IP is not in the whitelist\
506 | Unknown source of request\
510 | Excessive frequency of requests\
511 | Endpoint inaccessible\
513 | Invalid request(for open api serves time more or less than 10s)\
600 | Parameter error\
601 | Data decoding error\
602 | Verify failed\
603 | Repeated requests\
701 | Account read permission is required\
702 | Account modify permission is required\
703 | Trade information read permission is required\
704 | Transaction information modify permission is required\
1000 | Account does not exist\
1001 | Contract does not exist\
1002 | Contract not activated\
1003 | Error in risk limit level\
1004 | Amount error\
2001 | Wrong order direction\
2002 | Wrong opening type\
2003 | Overpriced to pay\
2004 | Low-price for selling\
2005 | Balance insufficient\
2006 | Leverage ratio error\
2007 | Order price error\
2008 | The quantity is insufficient\
2009 | Positions do not exist or have been closed\
2011 | Order quantity error\
2013 | Cancel orders over maximum limit\
2014 | The quantity of batch order exceeds the limit\
2015 | Price or quantity accuracy error\
2016 | Trigger volume over the maximum\
2018 | Exceeding the maximum available margin\
2019 | There is an active open position\
2021 | The single leverage is not consistent with the existing position leverage\
2022 | Wrong position type\
2023 | There are positions over the maximum leverage\
2024 | There are orders with leverage over the maximum\
2025 | The holding positions is over the maximum allowable positions\
2026 | Modification of leverage is not supported for cross\
2027 | There is only one cross or isolated in the same direction\
2028 | The maximum order quantity is exceeded\
2029 | Error order type\
2030 | External order ID is too long (Max. 32 bits )\
2031 | The allowable holding position exceed the current risk limit\
2032 | Order price is less than long position force liquidate price\
2033 | Order price is more than short position force liquidate price\
2034 | The batch query quantity limit is exceeded\
2035 | Unsupported market price tier\
3001 | Trigger price type error\
3002 | Trigger type error\
3003 | Executive cycle error\
3004 | Trigger price error\
4001 | Unsupported currency\
2036 | The orders more than the limit, please contact customer service\
2037 | Frequent transactions, please try it later\
2038 | The maximum allowable position quantity is exceeded, please contact customer service!\
5001 | The take-price and the stop-loss price cannot be none at the same time\
5002 | The Stop-Limit order does not exist or has closed\
5003 | Take-profit and stop-loss price setting is wrong\
5004 | The take-profit and stop-loss order volume is more than the holding positions can be liquidated\
6001 | Trading forbidden\
6002 | Open forbidden\
6003 | Time range error\
6004 | The trading pair and status should be fill in\
6005 | The trading pair is not available\
[Previous Integration guide](https://www.mexc.com/api-docs/futures/integration-guide "PreviousIntegration guide")[Next Market endpoints](https://www.mexc.com/api-docs/futures/market-endpoints "NextMarket endpoints")

- [Error code Example](https://www.mexc.com/api-docs/futures/error-code#error-code-example "Error code Example")
