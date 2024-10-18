# agent_torch/simulations/retail_simulation.py

def run_retail_simulation(num_agents, num_steps, products, promotions):
    # Initialize agents
    agents = [
        RetailCustomerAgent(
            agent_id=i,
            preferences=generate_preferences(products),
            budget=generate_budget()
        )
        for i in range(num_agents)
    ]

    for step in range(num_steps):
        active_promotions = {
            promo.product_id: promo
            for promo in promotions
            if promo.is_active(step)
        }

        for agent in agents:
            agent.decide_purchases(products, active_promotions, step)  # Pass current step

        # Forecast demand based on current agent carts
        demand = forecast_demand(agents, products)

        # Optionally, collect and analyze data here
        # ...

        # Reset agent carts for the next step
        for agent in agents:
            agent.cart = {}

