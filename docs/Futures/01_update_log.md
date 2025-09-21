# Update log

Effective Time（UTC+8) | Endpoint | Update Type | Description\
---|---|---|---\
2021-01-15 | * | Add | Release of contract API\
2021-03-30 | * | adjust | the following endpoints to access the paths and the data return format (the original paths still supported, but will gradually abandoned) : get the user’s all history orders, get the user’s ongoing orders, get the user’s history position information, get the stop-limit orders list, get the trigger orders list, get the user’s all transaction details\
2022-07-07 | /contract/detail | Add | Get the contract information endpoint add a new field: apiAllowed(true or false),means Whether support API\
2022-07-25 | * | maintenance | place order endpoints and cancel orders endpoints will be closed temporarily. The query endpoints can still be used\
2024-01-31 | * | adjust | ws base url update:wss://contract.mexc.com/edge\
2025-04-09 | * | adjust | Subscribe to ws incremental depth data, with zipped push by default: `compress` is set to `true`\
2025-08-21 | * | adjust | Subscribe to ws deal data, with zipped push by default: `compress` is set to `true`\\
