# agent_torch/agents/retail_customer_agent.py

import torch
from agent_torch.agents.base_agent import BaseAgent

class RetailCustomerAgent(BaseAgent):
    def __init__(self, agent_id, preferences, budget):
        super().__init__(agent_id)
        self.preferences = preferences  # Dictionary of product preferences
        self.budget = budget  # Available spending budget
        self.cart = {}  # Items the agent intends to purchase

    def decide_purchases(self, products, promotions, current_step):
        for product_id, product in products.items():
            preference = self.preferences.get(product_id, 0)
            promotion = promotions.get(product_id, None)
            price = product.price

            # Apply promotion if available
            if promotion and promotion.is_active(current_step):
                price *= (1 - promotion.discount_rate)

            # Simple decision rule based on preference and price
            if preference > 0.5 and self.budget >= price:
                self.cart[product_id] = 1  # Purchase one unit
                self.budget -= price
