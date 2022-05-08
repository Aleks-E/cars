### Prerequisites

Before you continue, you have to install Docker and Docker-Compose.

### Run App

- move to the project root directory
- run the docker container: `$ docker-compose up`
- open the browser
- insert the next address in browser: `http://localhost:8000/docs#`
- you will see the swagger window: 

<details><summary>

![rrrr](images/1.jpg)
</summary>
</details>

### Examples of usage:

<details><summary><h2>Endpoints:</h2></summary>

<hr>
<details><summary><h4>Create Dealer</h4></summary>

##### Description: creates a dealer with the specified parameters

##### URL: http://localhost:8000/dealer

##### Request:

- ````
    curl -X 'POST' \
      'http://localhost:8000/dealer' \
      -H 'accept: application/json' \
      -H 'Content-Type: application/json' \
      -d '{
      "dealer_name": "string",
      "address": "string",
      "phone": "string"
    }'
  ````

##### Responses:
- Successful Response:
  - status code: 201
  - Response body: 
      ````
      {"detail": "created"}
      ````
- Error: Conflict:

  - status code: 409
  - Response body:
      ````
      {"detail": "(psycopg2.errors.UniqueViolation) duplicate key value violates unique constraint \"dealer_dealer_name_key\"\nDETAIL:  Key (dealer_name)=(ee) already exists.\n\n[SQL: INSERT INTO dealer (dealer_name, address, phone) VALUES (%(dealer_name)s, %(address)s, %(phone)s) RETURNING dealer.id]\n[parameters: {'dealer_name': 'ee', 'address': 'string', 'phone': 'string'}]\n(Background on this error at: https://sqlalche.me/e/14/gkpj)"}
      ````
    
##### Note: field dealer_name should be unique
    
</details>

<hr>
<details><summary><h4>Get Dialers</h4></summary>

##### Description: search for dealers by specified parameters

##### URL: http://localhost:8000/dealer/search

##### Request (to get all dealers): 
- ````
    curl -X 'POST' \
      'http://localhost:8000/dealer/search' \
      -H 'accept: application/json' \
      -H 'Content-Type: application/json' \
      -d '{
    }'
    ````

##### Response:
- status code: 200
- Response body:
    ````
    [
      {
        "dealer_name": "gggg",
        "address": "string",
        "phone": "string",
        "id": 179
      },
      {
        "dealer_name": "vv",
        "address": "string",
        "phone": "string",
        "id": 182
      },
      {
        "dealer_name": "c",
        "address": "string",
        "phone": "string",
        "id": 183
      },
    ]
    ````
##### Request (to get specified dealer):
- ````
    curl -X 'POST' \
      'http://localhost:8000/dealer/search' \
      -H 'accept: application/json' \
      -H 'Content-Type: application/json' \
      -d '{
      "id": 179,
      "dealer_name": "gggg",
      "address": "string",
      "phone": "string"
    }'
    ````
##### Response:
- status code: 200
- Response body:
- ````
    [
      {
        "dealer_name": "gggg",
        "address": "string",
        "phone": "string",
        "id": 179
      }
    ]
    ````
##### Note - if there is not any dealers, the response will be:
- status code: 200
- Response body:
- ````
  []
  ````
</details>

<hr>
<details><summary><h4>Change Dealer</h4></summary>

##### Description: change dealer parameters

##### URL: http://localhost:8000/dealer/<dealer_id>

##### Request:
    ````
    curl -X 'PUT' \
      'http://localhost:8000/dealer/179' \
      -H 'accept: application/json' \
      -H 'Content-Type: application/json' \
      -d '{
      "dealer_name": "rr",
      "address": "string",
      "phone": "string"
    }'
    ````
##### Responses:
- Successful Response:
    - status code: 200
    - Response body:
    ````
    {"detail": "changed"}
    ````
- Error: Conflict
    - status code: 409
    - Response body:
    ````
    {"detail": "(psycopg2.errors.UniqueViolation) duplicate key value violates unique constraint \"dealer_dealer_name_key\"\nDETAIL:  Key (dealer_name)=(string) already exists.\n\n[SQL: UPDATE dealer SET dealer_name=%(dealer_name)s WHERE dealer.id = %(dealer_id)s]\n[parameters: {'dealer_name': 'string', 'dealer_id': 179}]\n(Background on this error at: https://sqlalche.me/e/14/gkpj)"}
    ````
</details>

<hr>
<details><summary><h4>Delete Dealer</h4></summary>

##### URL: http://localhost:8000/dealer/<dealer_id>

##### Request:
````
curl -X 'DELETE' \
  'http://localhost:8000/dealer/1' \
  -H 'accept: application/json'
````
##### Responses:
- Successful Response:
    - status code: 200
    - Response body:
    ````
    {"detail": "deleted"}
    ````
- Error: Not Found
    - status code: 404
    - Response body:
    ````
    {"detail": "dealer with this ID doesn't exist"}
    ````
- Error: Conflict
  - status code: 409
  - Response body:
  ````
  {"detail": "(psycopg2.errors.ForeignKeyViolation) update or delete on table \"dealer\" violates foreign key constraint \"car_dealer_id_fkey\" on table \"car\"\nDETAIL:  Key (id)=(105) is still referenced from table \"car\".\n\n[SQL: DELETE FROM dealer WHERE dealer.id = %(id)s]\n[parameters: {'id': 105}]\n(Background on this error at: https://sqlalche.me/e/14/gkpj)"}
  ````
##### Note: For security reasons, it is forbidden to remove dealers who have cars. In this case, you will receive a response with the code 409 (see above)

</details>

<hr>
<details><summary><h4>Create Car</h4></summary>

##### Request:
- ````
    curl -X 'POST' \
      'http://localhost:8000/car' \
      -H 'accept: application/json' \
      -H 'Content-Type: application/json' \
      -d '{
      "model": "string",
      "dealer_id": 0
    }'
    ````
##### Responses:
- Successful Response:
  - status code: 201
  - Response body:
  - ````
    {"detail": "created"}
    ````
 
- Error: Not Found
  - status code: 404
  - Response body:
  - ````
    {"detail": "dealer with this ID doesn't exist"}
    ````
</details>

<hr>
<details><summary><h4>Get Cars</h4></summary>

##### Request (to get all cars):
````
curl -X 'POST' \
  'http://localhost:8000/car/search' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{

}'
````
##### Response:
- status code: 201
- Response body:
````
[
  {
    "model": "string",
    "dealer_id": 105,
    "id": 26
  },
  {
    "model": "string",
    "dealer_id": 105,
    "id": 27
  },
  {
    "model": "string",
    "dealer_id": 105,
    "id": 28
  },
  {
    "model": "string",
    "dealer_id": 135,
    "id": 25
  }
]
````
##### Request (to get specified car):
````
curl -X 'POST' \
  'http://localhost:8000/car/search' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "id": 26
}'
````
##### Response:
- status code: 200
- Response body
    ````
    [
      {
        "model": "string",
        "dealer_id": 105,
        "id": 26
      }
    ]
    ````
##### Note - if there is not any cars, the response will be:
- status code: 200
- Response body:
- ````
  []
  ````
</details>

<hr>
<details><summary><h4>Change Car</h4></summary>

##### Request:
````
curl -X 'PUT' \
  'http://localhost:8000/car/26' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "model": "string",
  "dealer_id": 105
}'
````
##### Responses:
- Successful Response:
  - status code: 200
  - Response body:
  ````
  {"detail": "changed"}
  ````
- Error: Not Found (example 1)
  - status code: 404
  - Response body
  ````
  {"detail": "car with this ID doesn't exist"}
  ````
  
- Error: Not Found (example 2)
  - status code: 404
  - Response body
  ````
  {"detail": "dealer with this ID doesn't exist"}
  ````
</details>

<hr>
<details><summary><h4>Delete Car</h4></summary>

##### Request:
````
curl -X 'DELETE' \
  'http://localhost:8000/car/26' \
  -H 'accept: application/json'
````
##### Response:
- Successful Response:
  - status code: 200
  - Response body:
    ````
    {"detail": "deleted"}
    ````
- Error: Not Found
  - status code: 404
  - Response body:
  ````
  {"detail": "car with this ID doesn't exist"}
  ````
</details>
</details>






