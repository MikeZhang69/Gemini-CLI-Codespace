# Personal Investment Portfolio Application

This project is a personal investment portfolio management system, allowing users to track multi-asset investments, manage portfolios, and monitor basic financial data.

## Implemented Features

**Backend (NestJS):**
- User Authentication (Signup, Login) with JWT and bcrypt.
- User management (creation).
- Portfolio management (Create, Read, Update, Delete) for authenticated users.
- PostgreSQL database integration.

**Frontend (React):**
- User Signup and Login forms.
- Basic routing for authentication pages.
- Integration with the backend API for authentication.

**Containerization (Docker):**
- Dockerfiles for both backend and frontend services.
- Docker Compose setup for orchestrating the backend, frontend, and PostgreSQL database.

## Tech Stack

- **Frontend:** React, TypeScript, Axios, React Router DOM
- **Backend:** Node.js, NestJS, TypeScript, TypeORM, PostgreSQL, bcrypt, JWT
- **Database:** PostgreSQL
- **Containerization:** Docker, Docker Compose

## Getting Started with Docker Compose

To run this application using Docker Compose, ensure you have Docker and Docker Compose installed on your system. If you are in a GitHub Codespace, these should be pre-installed.

1.  **Navigate to the project root directory:**
    ```bash
    cd /workspaces/Gemini-CLI-Codespace/portfolio-app
    ```

2.  **Build and run the services:**
    This command will build the Docker images (if not already built or if changes were made to the Dockerfiles) and start all defined services (PostgreSQL database, backend, and frontend).
    ```bash
    docker-compose up --build
    ```

3.  **Access the Application:**
    Once the services are running, the frontend application will be accessible via your web browser.
    *   **In GitHub Codespaces:** Codespaces will automatically forward port 80 (for the frontend) and port 3000 (for the backend). Look for the "Ports" tab in your Codespace interface and click on the forwarded port 80 to open the application in your browser.
    *   **Locally:** If running Docker Compose locally, open your web browser and navigate to `http://localhost`.

    The frontend is configured to proxy API requests to the backend service using the service name defined in `docker-compose.yml` (e.g., `http://backend:3000`).

## Database Initialization

The `init.sql` file in the root of the `portfolio-app` directory is used to initialize the PostgreSQL database with a test user and a sample portfolio when the `db` service starts for the first time. The test user credentials are:
- **Email:** `test@example.com`
- **Password:** `password`

## Stopping the Application

To stop the running Docker Compose services, press `Ctrl+C` in the terminal where `docker-compose up` is running. To stop and remove the containers, networks, and volumes (for a clean slate), run:

```bash
docker-compose down -v
```
