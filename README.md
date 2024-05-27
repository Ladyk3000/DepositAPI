# Deposit Calculator API

This API calculates deposit amounts over specified periods with a given interest rate.

## Endpoints

### POST /calculate-deposit

**Request:**
```json
{
    "date": "31.01.2021",
    "periods": 3,
    "amount": 10000,
    "rate": 6
}
```

**Response:**
```json
{
    "deposits": [
        {"date": "31.01.2021", "amount": 10050.0},
        {"date": "28.02.2021", "amount": 10100.25},
        {"date": "31.03.2021", "amount": 10150.75}
    ]
}
```

**Error Response:**
```json
{
    "detail": "Error message explaining the validation failure"
}
```

## Project Structure

```
deposit_calculator/
├── app/
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   └── utils.py
├── tests/
│   ├── test_main.py
│   └── test_utils.py
├── Dockerfile
├── requirements.txt
└── README.md
```

## Running the Application

### Local Development

1. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

2. **Run the application:**
    ```sh
    uvicorn app.main:app --reload
    ```

    The API will be available at `http://127.0.0.1:8000`.

### Docker

1. **Build the Docker image:**
    ```sh
    docker build -t deposit-calculator .
    ```

2. **Run the Docker container:**
    ```sh
    docker run -p 8000:8000 deposit-calculator
    ```

    The API will be available at `http://127.0.0.1:8000`.

## Running Tests

1. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

2. **Run the tests:**
    ```sh
    pytest
    ```

    To see the test coverage report:
    ```sh
    pytest --cov=app --cov-report=term-missing
    ```

## API Details

### Request Fields

- `date` (string): The start date of the deposit in `dd.mm.yyyy` format.
- `periods` (integer): The number of months for the deposit (1 to 60).
- `amount` (integer): The initial amount of the deposit (10,000 to 3,000,000).
- `rate` (float): The interest rate (1 to 8).

### Response Fields

- `deposits` (list): A list of objects, each containing:
  - `date` (string): The date of the deposit.
  - `amount` (float): The amount of the deposit on that date.

## Code Coverage

To ensure the reliability and maintainability of the codebase, at least 80% of the code is covered by unit tests. This is verified using `pytest` and `pytest-cov`.

```sh
pytest --cov=app --cov-report=term-missing
```

This will display a detailed report of the test coverage, highlighting any lines of code that are not covered by tests.

