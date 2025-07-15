
"""
Model 2: Demand-based Pricing
-----------------------------

This module implements a demand-based pricing logic.

Price is adjusted proportionally to a computed demand score based on multiple factors:
- Occupancy ratio
- Queue length
- Traffic conditions
- Special day
- Vehicle type weight
"""

import numpy as np

def demand_pricing(
    occupancy: int,
    capacity: int,
    queue_length: int,
    traffic_level: str,
    is_special: int,
    vehicle_weight: float,
    base_price: float = 10.0,
    lambda_: float = 0.5,
    min_price: float = 5.0,
    max_price: float = 20.0
) -> float:
    """
    Compute price based on weighted demand function.

    Parameters:
    - occupancy: int
    - capacity: int
    - queue_length: int
    - traffic_level: str ("low", "medium", "high")
    - is_special: int (0 or 1)
    - vehicle_weight: float
    - base_price: float
    - lambda_: float: scaling factor for demand
    - min_price: float
    - max_price: float

    Returns:
    - price: float
    """
    if capacity <= 0:
        return base_price

    traffic_weights = {"low": 0.2, "medium": 0.5, "high": 0.8}
    traffic_wt = traffic_weights.get(traffic_level, 0.5)

    demand = (
        0.4 * (occupancy / capacity) +
        0.2 * queue_length -
        0.1 * traffic_wt +
        0.2 * is_special +
        0.1 * vehicle_weight
    )

    demand = np.clip(demand, 0, 1)
    price = base_price * (1 + lambda_ * demand)
    price = np.clip(price, min_price, max_price)

    return round(price, 2)
