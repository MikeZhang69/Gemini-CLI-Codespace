def calculate_npv(initial_investment, cash_flows, discount_rate):
    """
    Calculate Net Present Value (NPV).
    initial_investment: float, negative value (cash outflow)
    cash_flows: list of floats, cash inflows per period
    discount_rate: float, as a percentage (e.g., 10 for 10%)
    Returns: float, NPV value
    """
    r = discount_rate / 100.0
    npv = -initial_investment
    for t, cf in enumerate(cash_flows, start=1):
        npv += cf / ((1 + r) ** t)
    return npv

def some_existing_function():
    # Existing function implementation
    pass

def another_existing_function():
    # Another existing function implementation
    pass
