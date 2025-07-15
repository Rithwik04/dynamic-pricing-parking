
"""
Model 1: Baseline Linear Pricing
--------------------------------

This module implements the baseline linear pricing logic.

Price increases linearly with occupancy ratio:
    P_{t+1} = P_t + α * (occupancy / capacity)

where:
- α is a tunable sensitivity parameter.
- Price is bounded between a minimum and maximum value for stability.
"""

def linear_pricing(
    current_price: float,
    occupancy: int,
    capacity: int,
    alpha: float = 2.0,
    base_price: float = 10.0,
    min_price: float = 5.0,
    max_price: float = 20.0
) -> float:
    """
    Compute the next price based on linear occupancy logic.

    Parameters:
    - current_price: float, the current price in dollars
    - occupancy: int, number of parked vehicles
    - capacity: int, maximum vehicles that can be parked
    - alpha: float, sensitivity to occupancy (default: 2.0)
    - base_price: float, minimum starting price (default: 10.0)
    - min_price: float, minimum allowable price (default: 5.0)
    - max_price: float, maximum allowable price (default: 20.0)

    Returns:
    - price: float, next price rounded to 2 decimals
    """
    if capacity <= 0:
        return base_price

    occupancy_ratio = occupancy / capacity
    next_price = current_price + alpha * occupancy_ratio

    # Bound the price
    next_price = max(min_price, min(max_price, next_price))

    return round(next_price, 2)
