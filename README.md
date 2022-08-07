# Demo


## Installation
Setup Virtual Environment

```bash
python3 -m venv env
```

Activate Virtual Environment

```bash
source env/bin/activate
```

Install the required packages by running the following command:

```bash
pip3 install -r requirements.txt
```

Create an .env file in base directory using the following sample env and set the SECRET_KEY:
```bash
cp .env.sample .env
```

Run server using the following command

```bash
python3 manage.py runserver
```

## Endpoints
Get list of all devices

```bash
GET http://localhost:8000/api/v1/devices
```

Update connection status of a device to on

```bash
PATCH http://localhost:8000/api/v1/devices/:device_id
 -d connect_status=true
```

Update connection status of a device to off

```bash
PATCH http://localhost:8000/api/v1/devices/:device_id
 -d connect_status=false
```
