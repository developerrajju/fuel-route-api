# Fuel Route API

A Django REST API that helps truck drivers optimize fuel stops during long-distance routes across the United States.

## Project Overview

This application calculates the most efficient fuel stops for a truck route based on:

- Route origin and destination
- Fuel station locations
- Fuel prices at each station
- Truck fuel tank capacity
- Fuel consumption rate

The goal is to minimize total fuel cost while ensuring the truck can complete the journey.

## Features

- Fuel station management
- Route optimization
- Geocoding support for station coordinates
- REST API endpoints
- Cost-efficient fuel stop recommendations
- Scalable service-based architecture

## Tech Stack

- Python 3
- Django
- Django REST Framework
- PostgreSQL (recommended)
- Geocoding Service Integration

## Project Structure

```text
<img width="392" height="442" alt="image" src="https://github.com/user-attachments/assets/3c280112-043e-4bbc-b2f3-8602462ea36b" />

```

## Setup

### Clone Repository

```bash
git clone https://github.com/developerrajju/fuel-route-api.git
cd fuel-route-api
```

### Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Migrations

```bash
python manage.py migrate
```

### Start Server

```bash
python manage.py runserver
```

## Current Development Tasks

- Add latitude and longitude for all fuel stations
- Implement route optimization engine
- Create API documentation
- Add automated tests
- Improve error handling and logging

## Interview Highlights

This project demonstrates:

- Django backend development
- REST API design
- Service layer architecture
- Database modeling
- External API integration
- Route optimization concepts

## License

For educational and assessment purposes.
