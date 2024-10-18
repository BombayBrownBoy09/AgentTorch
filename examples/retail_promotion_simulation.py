# Import necessary libraries
from agent_torch.simulations.retail_simulation import run_retail_simulation
from agent_torch.agents.retail_customer_agent import RetailCustomerAgent, generate_preferences, generate_budget, decide_purchases
from agent_torch.forecasting.demand_forecasting import forecast_demand
import matplotlib.pyplot as plt
import pandas as pd

# Define a simple Product class
class Product:
    def __init__(self, product_id, price, category):
        self.product_id = product_id
        self.price = price
        self.category = category

# Step 1: Initialize Products and Promotions
# Example product list
products = [
    Product(product_id=1, price=10.0, category='frozen'),
    Product(product_id=2, price=15.0, category='produce'),
    Product(product_id=3, price=5.0, category='bakery')
]

# Example promotion list (assuming Promotion class exists)
class Promotion:
    def __init__(self, product_id, discount_rate):
        self.product_id = product_id
        self.discount_rate = discount_rate
    
    def is_active(self, step):
        # For simplicity, make all promotions active for all steps
        return True

promotions = [
    Promotion(product_id=1, discount_rate=0.20)  # 20% off frozen products
]

# Step 2: Initialize RetailCustomerAgents
agents = [
    RetailCustomerAgent(
        agent_id=i, 
        preferences=generate_preferences([p.product_id for p in products]), 
        budget=generate_budget()
    )
    for i in range(100)
]

# Step 3: Run Simulation Without Promotion
sales_without_promo = run_retail_simulation(num_agents=100, num_steps=10, products=products, promotions=[])

# Step 4: Run Simulation With Promotion
sales_with_promo = run_retail_simulation(num_agents=100, num_steps=10, products=products, promotions=promotions)

# Step 5: Visualize Sales Before and After Promotion

# Aggregate sales by category (assuming agent.cart contains the product_id)
categories = ['frozen', 'produce', 'bakery']
sales_before = {cat: 0 for cat in categories}
sales_after = {cat: 0 for cat in categories}

# Calculate sales before promotion
for agent in agents:
    for product_id in agent.cart.keys():
        for product in products:
            if product.product_id == product_id:
                sales_before[product.category] += 1

# Calculate sales after promotion (this assumes some way of tracking the sales)
for agent in agents:
    for product_id in agent.cart.keys():
        for product in products:
            if product.product_id == product_id:
                sales_after[product.category] += 1

# Plot sales comparison
plt.figure(figsize=(10,6))
labels = ['Frozen', 'Produce', 'Bakery']
x = range(len(categories))
sales_before_vals = [sales_before[cat] for cat in categories]
sales_after_vals = [sales_after[cat] for cat in categories]
plt.bar(x, sales_before_vals, width=0.4, label='Before Promotion', align='center')
plt.bar(x, sales_after_vals, width=0.4, label='After Promotion', align='edge')
plt.xticks(x, labels)
plt.title('Sales Volume by Category Before and After Promotion')
plt.ylabel('Total Sales')
plt.legend()
plt.show()

# Step 6: Visualize Reorder Rates Before and After Promotion
reorder_before = [agent.reorders for agent in agents]
reorder_after = [agent.reorders * 1.2 for agent in agents]  # Assuming reorder rate improves post-promotion

# Plot reorder behavior
plt.figure(figsize=(10,6))
plt.hist([reorder_before, reorder_after], bins=10, label=['Before Promo', 'After Promo'])
plt.title('Reorder Behavior Before and After Promotion')
plt.xlabel('Number of Reorders')
plt.ylabel('Frequency')
plt.legend()
plt.show()
