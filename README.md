# Nkoso Data

Nkoso Data is a small Python project for validating shipment records from CSV files. It checks whether each row contains the required fields, uses a valid date format, has a positive numeric weight, and contains a recognized shipment status.

This repository is designed to be easy to understand and extend, making it a good place for contributors to improve validation logic, expand business rules, or add tests.

## Project overview

The current implementation reads a CSV file, validates each row, and prints details about invalid shipments alongside a summary of total, valid, and invalid records.

## Repository structure

- `ingestion/app.py` – shipment validation logic and CLI runner
- `ingestion/test_app.py` – pytest tests covering valid and invalid shipment records
- `sample_shipments.csv` – sample shipment data for local testing
- `README.md` – project documentation

## Requirements

- Python 3.9+
- `pytest` for running the automated tests

## Quick start

1. Clone the repository:

   ```bash
   git clone <your-fork-url>
   cd nkoso-data
   ```

2. Run the validator against the sample CSV:

   ```bash
   python ingestion/app.py sample_shipments.csv
   ```

3. You should see validation output for each invalid record and a summary at the end.

## Validation rules

Each shipment record must include the following fields:

- `shipment_id`
- `origin`
- `destination`
- `ship_date`
- `weight_kg`
- `carrier`
- `status`

The validator also enforces these rules:

- `ship_date` must be in `YYYY-MM-DD` format
- `weight_kg` must be a number greater than `0`
- `status` must be one of:
  - `pending`
  - `in_transit`
  - `delivered`
  - `delayed`
  - `cancelled`

## Running tests

To run the project tests from the repository root:

```bash
pytest ingestion/test_app.py -q
```

## Contributing

We welcome contributions from anyone who wants to improve the project.

### Suggested workflow

1. Fork the repository and create a feature branch:

   ```bash
   git checkout -b feature/my-improvement
   ```

2. Create or update tests for the behavior you want to change.

3. Make the code change in the relevant module.

4. Run the test suite to verify the change:

   ```bash
   pytest ingestion/test_app.py -q
   ```

5. Commit your work with a clear message:

   ```bash
   git add .
   git commit -m "Add shipment validation for X"
   ```

6. Push your branch and open a pull request with a short summary of the change and why it matters.

### Contribution guidelines

- Keep the code simple and readable.
- Add or update tests whenever you change validation logic.
- Prefer small, focused pull requests.
- Document any new validation rule or CSV behavior clearly.
- Ensure your code still passes the existing tests before submitting.

## License

This project does not currently declare a license. If you plan to use or contribute to this repository publicly, consider adding one such as MIT or Apache 2.0.

## Need help?

If you are unsure about the validation behavior or how to extend the project, start by reading the validation logic in `ingestion/app.py` and the examples in `ingestion/test_app.py`.
