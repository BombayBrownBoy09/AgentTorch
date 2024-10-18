import random
import torch
from agent_torch.agents.base_agent import BaseAgent

class RetailCustomerAgent(BaseAgent):
    def __init__(self, agent_id, preferences, budget):
        super().__init__(agent_id)
        self.preferences = preferences  # Dictionary of product preferences
        self.budget = budget  # Available spending budget
        self.cart = {}  # Items the agent intends to purchase

def generate_budget():
    """Generate a random budget for the agent."""
    return random.uniform(50, 150)

def decide_purchases(agent, products, promotions, current_step):
    """Function to decide what the agent purchases."""
    for product in products:
        product_id = product.product_id  # Assuming product has a product_id attribute
        preference = agent.preferences.get(product_id, 0)
        promotion = promotions.get(product_id, None)
        price = product.price

        # Apply promotion if available
        if promotion and promotion.is_active(current_step):
            price *= (1 - promotion.discount_rate)

        # Simple decision rule based on preference and price
        if preference > 0.5 and agent.budget >= price:
            agent.cart[product_id] = 1  # Purchase one unit
            agent.budget -= price

# Define generate_preferences as a standalone function
def generate_preferences(products):
    preferences = {}
    for product in products:
        preferences[product] = random.uniform(0, 1)  # Random preference between 0 and 1
    return preferences
