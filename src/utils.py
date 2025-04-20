def custom_round_half(x: float) -> float:
    decimal = x - int(x)
    if decimal < 0.25:
        return float(int(x))
    elif decimal < 0.75:
        return float(int(x)) + 0.5
    else:
        return float(int(x)) + 1.0
