# API Documentation

This document describes the Profile API endpoint implemented in `MyProfile/views.py`.

## Endpoint

- URL: `/api/me/`
- Method: `GET`
- Description: Returns a small profile object and a cat fact fetched from `https://catfact.ninja/fact`.

## Successful response (200)

Content-Type: `application/json`

Example body:

```json
{
  "status": "success",
  "user": {
    "email": "idaraobong05@gmail.com",
    "name": "Etim, Idaraobong Joseph",
    "stack": "Python/Django"
  },
  "timestamp": "2025-10-18T12:34:56.789Z",
  "fact": "Cats have five toes on their front paws, but only four toes on their back paws."
}
```

Notes:
- `timestamp` is generated on the server using Django's `timezone.now()` and will be returned in ISO 8601 format by DRF's default renderer.
- `fact` is taken from the external API's `fact` key.

## Error cases

The view handles several error conditions when making the external HTTP request:

- 504 Gateway Timeout: If the outgoing request to the cat fact service times out.
  - Response example: `{ "status": "error", "message": "The request timed out." }`

- 502 Bad Gateway: Network connection errors when attempting to reach the cat fact service.
  - Response example: `{ "status": "error", "message": "Network connection error." }`

- 4xx / 5xx from the external service: If `requests` raises an HTTPError, the view returns an error status with the external service's status code.
  - Response example: `{ "status": "error", "message": "HTTP error: 503" }` with matching HTTP status 503.

- 500 Internal Server Error: Any other request exception will return a 500 with the exception string.

## How to call

Using curl:

```bash
curl -s http://127.0.0.1:8000/api/me/
```

Using Python requests:

```python
import requests
resp = requests.get('http://127.0.0.1:8000/api/me/')
print(resp.status_code, resp.json())
```

## Implementation notes

- The endpoint is implemented as a DRF `APIView` in `MyProfile/views.py`.
- It uses the `requests` library to fetch a cat fact. There is no caching or rate-limiting implemented; in production you may want to add caching and better error handling.
