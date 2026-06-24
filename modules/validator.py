def validate_weight(weight, field_name):
    if weight <= 0:
        raise ValueError(f"{field_name} must be greater than zero.")