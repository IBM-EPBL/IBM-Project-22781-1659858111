## News Tracker

A web application to search for news from all media outlets and sites from just oa single place. You could even call it a news aggregator.

## Requirements

- Python 3.7 above

## How to setup

From inside the `src/` directory, do

- Create a `.env` file inside `src/news-tracker/` having the following `ENV` Variables.

```python
RAPID_API_KEY = '<YOUR RAPID API KEY>'
API_URI= "<YOUR RAPID API URI ENDPOINT>"
DB_URL="DATABASE=<databasename>;HOSTNAME=<your-hostname>;PORT=<portnumber>;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=<username>;PWD=<password>"
SECRET_KEY="<YOUR SECRET KEY, CAN BE ANYTHING>"
```

- Download `SSL` Certificate i.e. `DigiCertGlobalRootCA.crt` from IBM DB2 DashBoard(UI) and place it inside `src/news-tracker/`

- Table `USER` schema is represented as,

| ID       | USERNAME           | PASSWD  |
| ------------- |:-------------:| -----|
| `INT GENERATED BY DEFAULT AS IDENTITY NOT NULL`     | `VARCHAR(32) NOT NULL`| `VARCHAR(256) NOT NULL` |

- SQL Query for the table is represented by,
```sql
CREATE TABLE USER(
    ID INT GENERATED BY DEFAULT AS IDENTITY NOT NULL,
    USERNAME VARCHAR(32) NOT NULL,
    PASSWD VARCHAR(256) NOT NULL
  );
 ```


- ```pip install -r news-tracker/requirements.txt```
- ```python3 --app news-tracker run```

## Demo:
https://youtu.be/L4bWmnCylpI
