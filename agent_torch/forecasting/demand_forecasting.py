# agent_torch/forecasting/demand_forecasting.py

def forecast_demand(agents, products):
    """
    Forecast demand based on agent carts.
    """
    demand = {product_id: 0 for product_id in products.keys()}
    for agent in agents:
        for product_id in agent.cart.keys():
            demand[product_id] += agent.cart[product_id]
    return demand
