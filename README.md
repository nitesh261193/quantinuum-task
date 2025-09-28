# Restful Booker API Testing Framework

This project contains automated API tests for the Restful Booker platform using Python with Behave BDD framework.

## Overview

The framework tests the Restful Booker API endpoints including:
- Authentication
- Create Booking
- Get Booking
- Update Booking
- Patch Update Booking
- Delete Booking

## Project Structure

```
├── features/                  # Behave feature files (Gherkin scenarios)
│   ├── create_booking.feature
│   ├── delete_booking.feature
│   ├── get_booking.feature
│   ├── update_booking.feature
│   └── update_patch_booking.feature
├── steps/                    # Step definitions
├── steps_definition/        # API request implementations
├── config.json             # Configuration file
└── requirements.txt        # Python dependencies
```

## Prerequisites

- Python 3.x
- pip (Python package installer)

## Installation

1. Create a virtual environment:
```bash
python -m venv .venv
```

2. Activate the virtual environment:
```bash
.venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running Tests

To run all tests:
```bash
python -m behave
```

To run specific feature:
```bash
python -m behave features/create_booking.feature
```

## API Endpoints Tested

- POST /auth - Authentication
- POST /booking - Create new booking
- GET /booking/{id} - Get booking details
- PUT /booking/{id} - Update booking
- PATCH /booking/{id} - Partial update booking
- DELETE /booking/{id} - Delete booking

