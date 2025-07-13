IACS API

This API is currently under development. The final goal is to provide programmatic access to IACS (Integrated Administration and Control System) data, as curated by the [IACS Data Community of Practice](https://europe-land.eu/de/iacs-data-community-of-practice/), enabling users to query, retrieve, and analyze agricultural and land use data across Europe.

## Features

- Access to harmonized IACS datasets
- Query endpoints for parcels, crops, and land use
- Support for filtering and aggregation
- RESTful interface with JSON responses

## Getting Started

### Clone the repository

```sh
git clone https://github.com/yourusername/iacs-api.git
cd iacs-api
```

### Set up a virtual environment and install dependencies

```sh
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
uv init
```

### Configure environment variables

Create a `.env` file in the root directory and add:

```env
# Application
APP_NAME="My FastAPI App"
APP_DESCRIPTION="My awesome API"
APP_VERSION="0.1.0"

# Database
POSTGRES_USER="postgres"
POSTGRES_PASSWORD="changethis"
POSTGRES_SERVER="db"
POSTGRES_PORT=5432
POSTGRES_DB="DIACS"

# Security
SECRET_KEY="your-secret-key-here"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=30
REFRESH_TOKEN_EXPIRE_DAYS=7


# Admin User
ADMIN_NAME="Admin"
ADMIN_EMAIL="admin@example.com"
ADMIN_USERNAME="admin"
ADMIN_PASSWORD="changethis"

# Environment
ENVIRONMENT="local"
```

### Set up a PostgreSQL database

1. Create a database named `IACS`.
2. Ensure the PostGIS extension is enabled:

```sql
CREATE EXTENSION IF NOT EXISTS postgis;
```

### Start the development server

```sh
fastapi dev run.py
```

## Usage

Example request to fetch parcel data:
```http
GET /api/parcels?country=DE&year=2022
```

## Documentation

See the [API documentation](docs/API.md) for detailed endpoint descriptions and usage examples.

## Data Source

All data is sourced from the [IACS Data Community of Practice](https://europe-land.eu/de/iacs-data-community-of-practice/).

## License

See [LICENSE](LICENSE) for details.