
"""
Model 3: Competitive Pricing
----------------------------

This module implements competitive pricing logic.

It considers the prices and occupancy of nearby parking lots to adjust pricing
and optionally suggest rerouting vehicles.
"""

from geopy.distance import geodesic

def competitive_pricing(
    my_location: tuple,
    competitors: list,
    my_price: float,
    my_capacity: int,
    my_occupancy: int,
    min_price: float = 5.0,
    max_price: float = 20.0
) -> float:
    """
    Compute competitive price adjustment.

    Parameters:
    - my_location: (lat, lon) tuple
    - competitors: list of dicts with keys: 'location', 'price'
    - my_price: float
    - my_capacity: int
    - my_occupancy: int

    Returns:
    - price: float
    """
    nearest_competitor = None
    min_distance = float("inf")

    for comp in competitors:
        dist = geodesic(my_location, comp["location"]).meters
        if dist < min_distance:
            min_distance = dist
            nearest_competitor = comp

    if nearest_competitor:
        if my_occupancy >= my_capacity:
            if my_price > nearest_competitor["price"]:
                return max(min_price, nearest_competitor["price"] - 1)
        elif nearest_competitor["price"] > my_price + 2:
            return min(max_price, my_price + 1)

    return round(my_price, 2)
