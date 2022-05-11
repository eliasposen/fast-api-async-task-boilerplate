# FastAPI-PonyORM-RQ Boilerplate

:warning: :wrench: :construction_worker: Work in Progress :construction_worker: :wrench: :warning:

## Overview

Boilerplate project for a microservice that is easy to extend with new endpoints that trigger asynchronous and synchronous actions.

## Stack

- [FastAPI](https://fastapi.tiangolo.com/)
- [PonyORM](https://docs.ponyorm.org/toc.html)
- [Python-RQ](https://python-rq.org/)

## Goals :rocket:

- [x] FastAPI authentication/authorization via OAuth2 & JWT token
- [x] Sample public and private endpoints
- [x] Retrieve async task info by UUID via task endpoint
- [x] Sample async task implementation with associated POST endpoint
- [ ] User roles
- [ ] User management via endpoints
- [ ] SSO via SAML 2.0
- [ ] Dockerfile and docker-compose configurations
- [ ] K8s/Helm deployment specs and charts
- [ ] Usage and extension documentation

## Installation

### Environment

```
conda create -n boilerpate python=3.10
conda activate boilerpate
poetry install
```

(Assumes all following command are within `boilerpate` virtual environment)

### Database

Configure PostgreSQL database variables in `.env`. The microservice expects the database to exist and for the database user to have access.

### Githooks

```
pre-commit install
```

### Start Webserver

```
source .env
uvicorn app.api.main:app --reload
```

Swagger documentation served at http://localhost:8000/docs

### Start RQ Worker

```
rq worker
```

### Create User

Create user via CLI. Run following for help message

```
python -m scripts.create_user --help
```
