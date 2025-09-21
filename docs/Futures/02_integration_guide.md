# Integration guide

## Access to url

> general data structures

```json
{
  "success": true,
  "code": 0,
  "data": {
    "symbol": "BTC_USD",
    "fairPrice": 8000,
    "timestamp": 1587442022003
  }
}
```

> or

```json
{
  "success": false,
  "code": 500,
  "message": "System internal error!"
}
```

- <https://contract.mexc.com>

The corresponding API accepts a request of Type GET, POST, or DELETE. The content-type of POST request is: application/JSON.
Parameters are sent in JSON format (parameter naming rules are camel named), and get requests are sent in requestParam (parameter naming rules are '\_' delimited)

## Authentication method

> java example

```json
/**
* Gets the get request parameter string
*
* @param param get/delete Request parameters map
* @return
*/
public static String getRequestParamString(Map<String, String> param) {
  if (MapUtils.isEmpty(param)) {
    return "";
  }
  StringBuilder sb = new StringBuilder(1024);
  SortedMap<String, String> map = new TreeMap<>(param);
  for (Map.Entry<String, String> entry : map.entrySet()) {
    String key = entry.getKey();
    String value = StringUtils.isBlank(entry.getValue()) ? "" : entry.getValue();
    sb.append(key).append('=').append(urlEncode(value)).append('&');
  }
  sb.deleteCharAt(sb.length() - 1);
  return sb.toString();
}
public static String urlEncode(String s) {
  try {
    return URLEncoder.encode(s, "UTF-8").replaceAll("\\+", "%20");
    } catch (UnsupportedEncodingException e) {
      throw new IllegalArgumentException("UTF-8 encoding not supported!");
    }
  }
  /**
  * signature
  */
  public static String sign(SignVo signVo) {
    if (signVo.getRequestParam() == null) {
      signVo.setRequestParam("");
    }
    String str = signVo.getAccessKey() + signVo.getReqTime() + signVo.getRequestParam();
    return actualSignature(str, signVo.getSecretKey());
  }
  public static String actualSignature(String inputStr, String key) {
    Mac hmacSha256;
    try {
      hmacSha256 = Mac.getInstance("HmacSHA256");
      SecretKeySpec secKey =
      new SecretKeySpec(key.getBytes(StandardCharsets.UTF_8), "HmacSHA256");
      hmacSha256.init(secKey);
      } catch (NoSuchAlgorithmException e) {
        throw new RuntimeException("No such algorithm: " + e.getMessage());
        } catch (InvalidKeyException e) {
          throw new RuntimeException("Invalid key: " + e.getMessage());
        }
        byte[] hash = hmacSha256.doFinal(inputStr.getBytes(StandardCharsets.UTF_8));
        return Hex.encodeHexString(hash);
      }
      @Getter
      @Setter
      public static class SignVo {
        private String reqTime;
        private String accessKey;
        private String secretKey;
        private String requestParam; //get the request parameters are sorted in dictionary order, with & concatenated strings, POST should be a JSON string
      }
```

1. Signature is not required for public endpoint.

1. For private endpoint, ApiKey, Request-Time, Signature and Content-Type need to be passed into the header, must be specified as application / JSON, Recv-Window (optional) parameters, Signature is a signature string. The signature rules are as follows:

1. When signing, you need to get the request parameter string first. It is "" if there is no parameter:

For GET/DELETE requests, the service parameters are spliced in dictionary order with & interval, and finally the signature target string is obtained (in the API of batch operation, if there are special symbols such as comma in the parameter value, these symbols need to be URL encoded when signing).
For POST requests, the signature parameter is a JSON string (dictionary sorting is not required).

1. After obtaining the parameter string, the signature target string is spliced. The rule is: accessKey + timestamp + obtained parameter string.
1. The HMAC SHA256 algorithm is used to sign the target string, and finally the signature is passed into the header as a parameter.

Note：

1. When the service parameter participating in the signature is null, it does not participate in the signature. For the path parameter, it does not participate in the signature; note that when get request stitches the parameter and pass it in the URL, if the parameter is null, it will be parsed into "" in the background parsing, fixed post request, when the parameter is null, do not pass the parameter, or set the value of the parameter to "" when signing, otherwise signature verification will fail.
1. When requesting, put the value of Request-Time used in signing into the Request-Time parameter of the header, put the obtained signature string into the signature parameter of the header, put the Access Key of APIKEY into the ApiKey parameter of the header, and pass the other service parameters.
1. The obtained signature string does not need to be base64 encoded.

## Time security

All APIs that require signature process need to fill in header parameter of Request-time, which is timestamp in milliseconds, when receives the request, the system verifies the time range from which the request was issued. The request is considered invalid if the received req_time is less or more than 10 seconds (the default value) (the time window can be adjusted by sending an optional header parameter `recv-window` with a maximum value of 60, `recv_window` of 30 seconds or more is not recommended)

## Create API key

Users can [create API key](https://www.mexc.com/ucenter/openapi) in the personal center of MEXC, which is used for signature calculation and authentication, an API key is consist of two parts, secret key of Access keyAPI and secret key corresponding to Secret key.
