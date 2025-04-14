# SYST50447_MidTerm_vinaykrishna

# Flask Docker Project Commands

This project builds a Flask web app with a PostgreSQL database, Nginx frontend, and monitoring, all running in secure Docker containers. Below are the key commands used to set up and run the project, organized by exercise, with simple explanations.

## Exercise 1: Building a Simple Flask App with Docker

In this exercise, we created a basic Flask app that says “Hello, Docker World!” and ran it in a Docker container.

- **Command**: `mkdir flask-app && cd flask-app`
  - **What it does**: Creates a folder called `flask-app` and moves into it to store our project files.

- **Command**: `touch app.py requirements.txt Dockerfile`
  - **What it does**: Creates three empty files: `app.py` (the Flask app code), `requirements.txt` (list of tools needed), and `Dockerfile` (instructions for Docker).

- **Command**: (Create `app.py` with Flask code)
  - **What it does**: We added code to `app.py` to make a webpage that shows `{"message": "Hello, Docker World!"}`. (You’ll need to copy the code from earlier steps.)

- **Command**: (Create `requirements.txt` with `flask==2.0.1`)
  - **What it does**: We listed `flask==2.0.1` in `requirements.txt` to install Flask for the app.

- **Command**: (Create `Dockerfile` with Python setup)
  - **What it does**: We wrote instructions in `Dockerfile` to set up Python, install Flask, and run `app.py`. (Copy the `Dockerfile` from Exercise 1.)

- **Command**: `docker build -t flask-app:v1 .`
  - **What it does**: Builds a Docker image (like a blueprint) named `flask-app:v1` using the `Dockerfile`, setting up the app inside.

- **Command**: `docker run -d -p 5000:5000 --name flask-container flask-app:v1`
  - **What it does**: Starts a container from the image, running the app on port 5000, so we can visit it.

- **Command**: `curl http://localhost:5000`
  - **What it does**: Tests the app by checking if it shows `{"message": "Hello, Docker World!"}`.

- **Command**: (Update `requirements.txt` to `flask==2.0.1` and `werkzeug==2.0.3`)
  - **What it does**: Fixed an error by adding `werkzeug==2.0.3` to `requirements.txt` to match Flask’s version, then rebuilt the image.

## Exercise 2: Adding a Database and Docker Compose

We added a PostgreSQL database to store messages and used Docker Compose to run the app and database together.

- **Command**: (Update `requirements.txt` to include `psycopg2-binary==2.9.1`)
  - **What it does**: Added `psycopg2-binary==2.9.1` to `requirements.txt` so the app can talk to the database.

- **Command**: (Update `app.py` with database code)
  - **What it does**: Changed `app.py` to add features for initializing a database, saving messages, and showing them. (Copy the `app.py` from Exercise 2.)

- **Command**: `touch docker-compose.yml`
  - **What it does**: Created a file to manage multiple containers (app and database).

- **Command**: (Create `docker-compose.yml` with `api` and `db` services)
  - **What it does**: Wrote rules in `docker-compose.yml` to run the Flask app (`api`) and PostgreSQL (`db`), with a volume to save database data. (Copy the file from Exercise 2.)

- **Command**: `docker-compose up -d`
  - **What it does**: Started the app and database containers in the background.

- **Command**: `curl -X POST http://localhost:5000/init-db`
  - **What it does**: Set up the database to store messages.

- **Command**: `curl -X POST -H "Content-Type: application/json" -d '{"content":"Hello from PostgreSQL"}' http://localhost:5000/message`
  - **What it does**: Added a test message to the database.

- **Command**: `curl http://localhost:5000/messages`
  - **What it does**: Checked that the message was saved and displayed.

- **Command**: `docker-compose down`
  - **What it does**: Stopped and removed the containers to test data saving.

- **Command**: `docker-compose up -d`
  - **What it does**: Restarted the containers to check if the message was still there.

- **Command**: `curl http://localhost:5000/messages`
  - **What it does**: Confirmed the message stayed in the database, proving data was saved.

## Exercise 3: Adding a Frontend and Networking

We added a webpage for users to see and add messages and set up networks to keep parts of the app private.

- **Command**: `mkdir -p frontend/html`
  - **What it does**: Created folders for the webpage files.

- **Command**: (Create `frontend/html/index.html`)
  - **What it does**: Made a webpage with a text box, button, and message list to interact with the app. (Copy `index.html` from Exercise 3.)

- **Command**: `touch frontend/Dockerfile`
  - **What it does**: Created a file to set up Nginx (a tool to show webpages).

- **Command**: (Create `frontend/Dockerfile` with Nginx setup)
  - **What it does**: Wrote instructions to use Nginx and copy the webpage files. (Copy the initial `Dockerfile` from Exercise 3.)

- **Command**: (Update `docker-compose.yml` with `frontend` service and networks)
  - **What it does**: Added the `frontend` service and created two networks: one for the webpage and app, another for the app and database, to keep the database private. (Copy `docker-compose.yml` from Exercise 3 before `nginx.conf`.)

- **Command**: `docker-compose up -d --build`
  - **What it does**: Built and started all containers (webpage, app, database).

- **Command**: (Create `frontend/nginx.conf`)
  - **What it does**: Fixed a “404” error by adding rules to show the webpage and send requests to the app. (Copy `nginx.conf` from Exercise 3.)

- **Command**: (Update `frontend/Dockerfile` to include `nginx.conf`)
  - **What it does**: Updated Nginx to use the new rules. (Copy the final `Dockerfile` from Exercise 3.)

- **Command**: `docker-compose up -d --build`
  - **What it does**: Rebuilt and restarted everything with the fixed webpage setup.

- **Command**: `docker exec -it flask-app-frontend-1 ping -c 2 db`
  - **What it does**: Tested that the webpage couldn’t reach the database, proving the networks were secure.

- **Command**: (Update `docker-compose.yml` to fix `api` healthcheck)
  - **What it does**: Changed the `api` healthcheck to use Python instead of `curl` to check if the app was running. (Copy the healthcheck from Exercise 3.)

## Exercise 4: Adding Monitoring with Prometheus and Grafana

We added tools to track how the app was doing, like how many visits it got, and showed this info in graphs.

- **Command**: (Update `requirements.txt` to include `prometheus-client==0.11.0`)
  - **What it does**: Added a tool so the app could share data (like visit counts) with Prometheus.

- **Command**: (Update `app.py` with metrics code)
  - **What it does**: Changed the app to count visits and measure speed, adding a `/metrics` page for the data. (Copy `app.py` from Exercise 4.)

- **Command**: `touch prometheus.yml`
  - **What it does**: Created a file to tell Prometheus what data to collect.

- **Command**: (Create `prometheus.yml`)
  - **What it does**: Set up Prometheus to grab data from itself and the app. (Copy `prometheus.yml` from Exercise 4.)

- **Command**: (Update `docker-compose.yml` with `prometheus` and `grafana` services)
  - **What it does**: Added Prometheus (port 9090) to collect data and Grafana (port 3000) to show graphs. (Copy `docker-compose.yml` from Exercise 4.)

- **Command**: `docker-compose up -d --build`
  - **What it does**: Started all containers, including the new monitoring tools.

- **Command**: `docker exec -it flask-app-api-1 python -c "import urllib.request; print(urllib.request.urlopen('http://localhost:5000/metrics').read().decode())"`
  - **What it does**: Checked that the app was sharing data (like visit counts) with Prometheus.

## Exercise 5: Securing the Containers

We made the app safer by limiting what the containers could do, like locking down a house.

- **Command**: (Update `Dockerfile` for non-root user)
  - **What it does**: Changed the app to run as a regular user (`appuser`) instead of a powerful one, for safety. (Copy `Dockerfile` from Exercise 5.)

- **Command**: `touch seccomp-profile.json`
  - **What it does**: Created a file to limit what the app could do (but we removed it later due to errors).

- **Command**: (Update `docker-compose.yml` with security settings)
  - **What it does**: Added rules to the `api` service to limit permissions and tried read-only mode (later removed). (Copy the final `docker-compose.yml` from Exercise 5 without Seccomp.)

- **Command**: `docker-compose up -d --build`
  - **What it does**: Rebuilt and started the containers with the safer settings.

- **Command**: `docker rm flask-app-api-1`
  - **What it does**: Removed a broken `api` container to try again.

- **Command**: (Fix `docker-compose.yml` to remove duplicates)
  - **What it does**: Corrected a mistake where `api` rules were repeated, causing errors. (Use the final `docker-compose.yml` from Exercise 5.)

- **Command**: `docker-compose up -d --build`
  - **What it does**: Started all containers successfully with the fixed, secure setup.

- **Command**: `docker ps`
  - **What it does**: Checked that all containers (webpage, app, database, Prometheus, Grafana) were running.

- **Command**: `docker exec flask-app-api-1 whoami`
  - **What it does**: Confirmed the app was running as `appuser`, proving it was secure.

## Notes
- Replace `https://special-broccoli-p94prpq9wqxcrxv6-80.app.github.dev/` with your Codespaces URL when testing.
- Some commands (like file creation) assume you’ll copy the contents from the project steps.
- We hit a small issue in Exercise 4 with Prometheus graphs not updating due to time settings, which can be fixed by selecting “Last 5 minutes” in the UI.

This covers all the main steps to build, run, and secure your Flask Docker app!