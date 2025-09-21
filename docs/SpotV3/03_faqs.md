[Skip to main content](#__docusaurus_skipToContent_fallback)

[![MEXC Logo](/api-docs-assets/img/mexc-logo.svg)![MEXC Logo](/api-docs-assets/img/mexc-logo.svg)](https://www.mexc.com/)[SpotV3](/api-docs/spot-v3/introduction)[Futures](/api-docs/futures/update-log)[Broker](/api-docs/broker/mexc-broker-introduction)

English

* [English](/api-docs/spot-v3/faqs)
* [中文](/zh-MY/api-docs/spot-v3/faqs)

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

# FAQs

## Q1: How many API Keys can a user apply?[​](#q1-how-many-api-keys-can-a-user-apply "Direct link to Q1: How many API Keys can a user apply?")

Each account can create up to 30 API Keys. The validity of an API Key without a linked IP address is 90 days, and the API Key will expire automatically. Each API Key can be linked to a maximum of 10 IP addresses.

## Q2: How many sub-accounts can a main account apply?[​](#q2-how-many-sub-accounts-can-a-main-account-apply "Direct link to Q2: How many sub-accounts can a main account apply?")

Each main account can create up to 30 sub-accounts. The sub-accounts will automatically inherit the main account rates. However, sub-accounts created via API cannot be logged in on Web.

## Q3: Why are there often issues of disconnections and expired sessions?[​](#q3-why-are-there-often-issues-of-disconnections-and-expired-sessions "Direct link to Q3: Why are there often issues of disconnections and expired sessions?")

If stable access is not possible, it is recommended to use Japan or Singapore AWS cloud servers for access.

## Q4: What should I do after an error is reported for exceeding the limit frequency?[​](#q4-what-should-i-do-after-an-error-is-reported-for-exceeding-the-limit-frequency "Direct link to Q4: What should I do after an error is reported for exceeding the limit frequency?")

After exceeding the interface access frequency limit, you will not be able to continue accessing the interface. It will resume to normal after 10 minutes to keep the interface access frequency below the limit.

## Q5: How many orders can an account place?[​](#q5-how-many-orders-can-an-account-place "Direct link to Q5: How many orders can an account place?")

Each account can hold up to 500 valid orders that are not completely filled.

## Q6:Why does WebSocket always disconnect?[​](#q6-does-websocket-always-disconnect "Direct link to q6-does-websocket-always-disconnect")

1. If there is no valid subscription, it will disconnect in 30 seconds.
2. If the subscription is successful, and there is no traffic in 60 seconds, it will automatically disconnect.
3. To ensure a stable connection, a Pong reply is required upon receiving the Ping message sent from the server.

## Q7: Why am I unable to subcribe to multiple channels on WebSocket?[​](#q7-why-am-i-unable-to-subcribe-to-multiple-channels-on-websocket "Direct link to Q7: Why am I unable to subcribe to multiple channels on WebSocket?")

WebSocket currently allows subscription to up to 30 channels via a single link. Any subscription will be invalid after the limit is exceeded. To subscribe to more channels, it is recommended to create multiple links.

[Previous

Change Log](/api-docs/spot-v3/change-log)[Next

General Info](/api-docs/spot-v3/general-info)

* [Q1: How many API Keys can a user apply?](#q1-how-many-api-keys-can-a-user-apply)
* [Q2: How many sub-accounts can a main account apply?](#q2-how-many-sub-accounts-can-a-main-account-apply)
* [Q3: Why are there often issues of disconnections and expired sessions?](#q3-why-are-there-often-issues-of-disconnections-and-expired-sessions)
* [Q4: What should I do after an error is reported for exceeding the limit frequency?](#q4-what-should-i-do-after-an-error-is-reported-for-exceeding-the-limit-frequency)
* [Q5: How many orders can an account place?](#q5-how-many-orders-can-an-account-place)
* [Q6 does WebSocket always disconnect?](#q6-does-websocket-always-disconnect)
* [Q7: Why am I unable to subcribe to multiple channels on WebSocket?](#q7-why-am-i-unable-to-subcribe-to-multiple-channels-on-websocket)