# API Offering Request Scenarios

## Question:
Please find ways to request the list of offering APIs in order to receive the response code 200 or another response code.

## Answer:

### 1) Request That Should Return **200 OK**
This is the happy path and should always be your starting point.

**Conditions:**
*   Valid endpoint
*   Correct HTTP method
*   Valid authentication
*   Required headers present
*   Valid query parameters

**Example using curl:**
```bash
curl -X GET "https://api.provider.com/v1/catalog" \
     -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
     -H "Accept: application/json"
```

### 2) **400 Bad Request**
**How to trigger:**
*   Missing required query parameter
*   Invalid parameter format

**Example using curl:**
```bash
curl -X GET "https://api.provider.com/v1/catalog?limit=abc" \
     -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
     -H "Accept: application/json"
```

### 3) **401 Unauthorized**
**How to trigger:**
*   Missing Authorization header
*   Invalid or expired token

**Example using curl:**
```bash
curl -X GET "https://api.provider.com/v1/catalog" \
     -H "Accept: application/json"
```

### 4) **403 Forbidden**
**How to trigger:**
*   Valid token but insufficient role/permission

**Example using curl:**
```bash
curl -X GET "https://api.provider.com/v1/catalog" \
     -H "Authorization: Bearer valid_token_without_permission" \
     -H "Accept: application/json"
```

### 5) **404 Not Found**
**How to trigger:**
*   Wrong endpoint path
*   Non-existing resource ID

**Example using curl:**
```bash
curl -X GET "https://api.provider.com/v1/nonexist-catalog" \
     -H "Authorization: Bearer YOUR_ACCESS_TOKEN " \
     -H "Accept: application/json"
```

### 6) **405 Method Not Allowed**
**How to trigger:**
*   Use a non-implemented method.

**Example using curl:**
```bash
curl -X PUT "https://api.provider.com/v1/catalog" \
     -H "Authorization: Bearer YOUR_ACCESS_TOKEN " \
     -H "Accept: application/json"
```

### 7) **500 Internal Server Error**
**How to trigger:**
*   Backend dependency failure
*   Malformed payload that passes gateway but fails internally

**Example using curl:**
```bash
curl -X GET "https://api.provider.com/v1/catalog?sort=__unexpected_object__" \
     -H "Authorization: Bearer YOUR_ACCESS_TOKEN " \
     -H "Accept: application/json"
```
