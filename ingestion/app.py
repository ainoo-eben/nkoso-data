
"""
shipment validator - Nkoso Logistics
Reads shipments from a CSV file, checks each record, and prints the invalid ones.

Run:  python validate_shipments_simple.py sample_shipments.csv
"""

import csv
import sys
from datetime import datetime

# The fields every shipment must have
REQUIRED_FIELDS = ["shipment_id", "origin", "destination",
                   "ship_date", "weight_kg", "carrier", "status"]

# The only status values we accept
VALID_STATUSES = ["pending", "in_transit", "delivered", "delayed", "cancelled"]


def check_record(record):
    """Check one shipment. Returns a list of problems (empty list = valid)."""
    problems = []

    # Step 1: is every required field filled in?
    for field in REQUIRED_FIELDS:
        value = record.get(field)
        if value is None or value.strip() == "":
            problems.append("missing " + field)

    # Step 2: is the date in the format YYYY-MM-DD?
    if record.get("ship_date"):
        try:
            datetime.strptime(record["ship_date"], "%Y-%m-%d")
        except ValueError:
            problems.append("bad date format: " + record["ship_date"])

    # Step 3: is the weight a number greater than zero?
    if record.get("weight_kg"):
        try:
            if float(record["weight_kg"]) <= 0:
                problems.append("weight must be more than 0")
        except ValueError:
            problems.append("weight is not a number: " + record["weight_kg"])

    # Step 4: is the status one we know?
    if record.get("status") and record["status"] not in VALID_STATUSES:
        problems.append("unknown status: " + record["status"])

    return problems


def duplicate_shipment_rows(records):
    """Return a flag for each record, marking repeated non-empty shipment IDs."""
    seen_ids = set()
    duplicates = []

    for record in records:
        shipment_id = (record.get("shipment_id") or "").strip()
        is_duplicate = bool(shipment_id) and shipment_id in seen_ids
        duplicates.append(is_duplicate)
        if shipment_id:
            seen_ids.add(shipment_id)

    return duplicates


def main():
    # Get the file name from the command line
    if len(sys.argv) < 2:
        print("Usage: python test_app.py <file.csv>")
        return
    filename = sys.argv[1]

    # Read the CSV file into a list of records
    with open(filename, newline="") as f:
        records = list(csv.DictReader(f))

    # Check every record and collect the bad ones
    invalid_count = 0
    duplicate_rows = duplicate_shipment_rows(records)
    for row_number, (record, is_duplicate) in enumerate(
        zip(records, duplicate_rows), start=1
    ):
        problems = check_record(record)
        if is_duplicate:
            problems.append("duplicate shipment_id")
        if problems:
            invalid_count += 1
            print("Row", row_number, "(" + str(record.get("shipment_id")) + "):",
                  ", ".join(problems))

    # Print the summary
    print()
    print("Total records:", len(records))
    print("Valid:", len(records) - invalid_count)
    print("Invalid:", invalid_count)


if __name__ == "__main__":
    main()
