"""
Tests for validate_shipments_simple.py
Run with:  pytest test_validate_shipments.py -v
"""

from app import check_record


def make_valid_record():
    """A shipment that passes every check. Tests change one thing at a time."""
    return {
        "shipment_id": "SHP001",
        "origin": "Takoradi",
        "destination": "Accra",
        "ship_date": "2026-11-01",
        "weight_kg": "250.5",
        "carrier": "Nkoso Express",
        "status": "in_transit",
    }


def test_valid_record_has_no_problems():
    assert check_record(make_valid_record()) == []


def test_missing_field_is_reported():
    record = make_valid_record()
    record["destination"] = ""
    problems = check_record(record)
    assert "missing destination" in problems


def test_field_with_only_spaces_counts_as_missing():
    record = make_valid_record()
    record["carrier"] = "   "
    assert "missing carrier" in check_record(record)


def test_bad_date_format_is_reported():
    record = make_valid_record()
    record["ship_date"] = "03/11/2026"
    problems = check_record(record)
    assert any("bad date format" in p for p in problems)


def test_negative_weight_is_reported():
    record = make_valid_record()
    record["weight_kg"] = "-10"
    assert "weight must be more than 0" in check_record(record)


def test_weight_that_is_not_a_number_is_reported():
    record = make_valid_record()
    record["weight_kg"] = "abc"
    problems = check_record(record)
    assert any("not a number" in p for p in problems)


def test_unknown_status_is_reported():
    record = make_valid_record()
    record["status"] = "lost"
    problems = check_record(record)
    assert any("unknown status" in p for p in problems)


def test_several_problems_are_all_reported():
    record = make_valid_record()
    record["weight_kg"] = "abc"
    record["status"] = "lost"
    assert len(check_record(record)) == 2