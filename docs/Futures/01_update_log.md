[Skip to main content](https://www.mexc.com/api-docs/futures/update-log#__docusaurus_skipToContent_fallback "Skip to main content")
[![MEXC Logo](https://www.mexc.com/api-docs-assets/img/mexc-logo.svg)](https://www.mexc.com/ "https://www.mexc.com/")[SpotV3](https://www.mexc.com/api-docs/spot-v3/introduction "SpotV3")[Futures](https://www.mexc.com/api-docs/futures/update-log "Futures")[Broker](https://www.mexc.com/api-docs/broker/mexc-broker-introduction "Broker")
[](https://www.mexc.com/api-docs/futures/update-log "English")

- [English](https://www.mexc.com/api-docs/futures/update-log "English")

- [中文](https://www.mexc.com/zh-MY/api-docs/futures/update-log "中文")

- [Update log](https://www.mexc.com/api-docs/futures/update-log "Update log")

- [Integration guide](https://www.mexc.com/api-docs/futures/integration-guide "Integration guide")

- [Error code](https://www.mexc.com/api-docs/futures/error-code "Error code")

- [Market endpoints](https://www.mexc.com/api-docs/futures/market-endpoints "Market endpoints")

- [Account and trading endpoints](https://www.mexc.com/api-docs/futures/account-and-trading-endpoints "Account and trading endpoints")

- [WebSocket API](https://www.mexc.com/api-docs/futures/websocket-api "WebSocket API")

# Update log

Effective Time（UTC+8) | Endpoint | Update Type | Description\
---|---|---|---\
2021-01-15 | * | Add | Release of contract API\
2021-03-30 | * | adjust | the following endpoints to access the paths and the data return format (the original paths still supported, but will gradually abandoned) : get the user’s all history orders, get the user’s ongoing orders, get the user’s history position information, get the stop-limit orders list, get the trigger orders list, get the user’s all transaction details\
2022-07-07 | /contract/detail | Add | Get the contract information endpoint add a new field: apiAllowed(true or false),means Whether support API\
2022-07-25 | * | maintenance | place order endpoints and cancel orders endpoints will be closed temporarily. The query endpoints can still be used\
2024-01-31 | * | adjust | ws base url update:wss://contract.mexc.com/edge\
2025-04-09 | * | adjust | Subscribe to ws incremental depth data, with zipped push by default: `compress` is set to `true`\
2025-08-21 | * | adjust | Subscribe to ws deal data, with zipped push by default: `compress` is set to `true`\
[Next Integration guide](https://www.mexc.com/api-docs/futures/integration-guide "NextIntegration guide")
