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

Before running the commands mentioned below, make sure to create a **Python virtual environment** in the backend folder, for local development and testing.

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

Before running the commands mentioned below, make sure to create a **Python virtual environment** in the helper-service folder, for local development and testing.

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

Each component needs to have its own `Dockerfile` created. A `compose.yaml` should also be created in the root of the repository to orchestrate the services. Every application should run on separate ports.

- Frontned - port 80
- Backend - port 8000
- Helper service - port 9000

# Hints

<details>
<summary>Foundation</summary>
We need to think about our base image from which we want to start. Our applications have 2 distinct base images that we can use. One for the frontend and the other for both the backend and the helper service. Make note of the technologies mentioned.

- [NGINX](https://hub.docker.com/_/nginx)
- [Python](https://hub.docker.com/_/python)
</details>

<details>
<summary>The steps we take...</summary>
When we think about a Dockerfile, we think about the layers we want to add on top of our foundation, slowly building out the environment needed for our application to run. We put down the steps we take to get to that point by installing what is missing, moving the files where they need to be, exposing the ports and lastly defining our entrypoint.
</details>

<details>
<summary>Leading the orchestra</summary>
A good dirigent knows how to lead its orchestra. Likewise, we need to describe to our dirigent (docker compose) how to orchestrate our apps and services in order for the whole system to run properly. We need to declare our services, where they are located, how they are built, and how will they listen for incoming information.

```yaml
services:
    frontend:
        build: ./frontend/.
        network_mode: host
```
</details>