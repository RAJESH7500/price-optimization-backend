import uuid


# function to generate 6 digit unique id
def create_unique_id():
    generated_uuid = uuid.uuid4()
    return generated_uuid.int % 1000000


# Function to Calculate demand forecast based on historical sales, stock, and customer rating
def calculate_demand_forecast(product):
    return round(
        (product["units_sold"] * 0.6)
        + (product["stock_available"] * 0.2)
        + (product["customer_rating"] * 10)
    )
