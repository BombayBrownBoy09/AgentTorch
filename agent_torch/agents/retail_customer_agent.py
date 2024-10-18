import random
import torch
from agent_torch.agents.base_agent import BaseAgent

class RetailCustomerAgent(BaseAgent):
    def __init__(self, agent_id, preferences, budget):
        super().__init__(agent_id)
        self.preferences = preferences  # Dictionary of product preferences
        self.budget = budget  # Available spending budget
        self.cart = {}  # Items the agent intends to purchase
        self.reorders = 0

    @staticmethod
    def generate_budget():
        """Generate a random budget for the agent."""
        return random.uniform(50, 150)

    @staticmethod
    def generate_preferences(products):
        """Generate a random preference for each product."""
        preferences = {}
        for product in products:
            preferences[product.product_id] = random.uniform(0, 1)  # Random preference between 0 and 1
        return preferences

    def decide_purchases(self, products, promotions, current_step):
        """Decide what the agent purchases."""
        for product in products:
            product_id = product.product_id  # Assuming product has a product_id attribute
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
