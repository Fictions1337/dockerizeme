# DockerizeMe

This project consists of 3 components:
- frontend
- backend
- helper service

## Frontend

Static site comprising of `index.html` and `script.js` that should be served by `NGINX` running on port `80`.

## Backend

REST API written in `Python` using `FastAPI` library with 1 GET endpoint `/message` which returns `JSON` as response.

### Quick start

Before running the commands mentioned below, make sure to craete a **Python virtual environment** in the backend folder, for local development and testing.

```sh
cd backend
pip install --no-cache-dir -r requirements.txt
fastapi run main.py
```

### Running backend

To run the application use the following command. By default the app runs on port `8000`:

```sh
fastapi run main.py
```

To specify on which port the application should listen on, use the `--port` flag.

```sh
fastapi run main.py --port 8000
```

## Helper service

REST API written in `Python` using `FastAPI` library with 1 GET endpoint `/helper` which returns `JSON` as response.

### Quick start

Before running the commands mentioned below, make sure to craete a **Python virtual environment** in the helper-service folder, for local development and testing.

```sh
cd helper-service
pip install --no-cache-dir -r requirements.txt
```

### Running helper service

To run the application use the following command:

```sh
fastapi run main.py --port 9000
```

***

# Challenge

Each component needs to have its own `Dockerfile` created. A `compose.yaml` should also be created in the root of the repository to orchestrate the service. Every application should run on separate ports.

- Frontned - port 80
- Backend - port 8000
- Helper service - port 9000