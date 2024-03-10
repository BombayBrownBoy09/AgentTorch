from langchain_openai import ChatOpenAI
import torch
import torch.nn as nn
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from langchain.schema import StrOutputParser
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI
from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
)
from langchain_core.messages import SystemMessage
# define open AI key
OPENAI_API_KEY = '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'

def format_financial_report(config):
    month = config.get("month")
    year = config.get("year")
    profession = config.get("profession")
    income = config.get("income")
    consumption = config.get("consumption")
    tax_deduction = config.get("tax_deduction")
    tax_credit = config.get("tax_credit")
    tax_brackets = config.get("tax_brackets")
    tax_rates = config.get("tax_rates")
    essential_price = config.get("essential_price")
    savings_balance = config.get("savings_balance")
    interest_rate = config.get("interest_rate")

    report = f"Now it’s {month}.{year}. In the previous month, you worked as a(an) {profession}. If you continue working this month, your expected income will be ${income:.2f}, which is decreased compared to the last month due to the deflation of the labor market. Besides, your consumption was ${consumption:.2f}. Your tax deduction amounted to ${tax_deduction:.2f}. However, as part of the government’s redistribution program, you received a credit of ${tax_credit:.2f}. In this month, the government sets the brackets: {tax_brackets} and their corresponding rates: {tax_rates}. Income earned within each bracket is taxed only at that bracket’s rate. Meanwhile, deflation has led to a price decrease in the consumption market, with the average price of essential goods now at ${essential_price:.2f}. Your current savings account balance is ${savings_balance:.2f}. Interest rates, as set by your bank, stand at {interest_rate:.2f}%. With all these factors in play, and considering aspects like your living costs, any future aspirations, and the broader economic trends, how is your willingness to work this month? Furthermore, how would you plan your expenditures on essential goods, keeping in mind goods price? Please share your decisions in a JSON format. The format should have two keys: ’work’ (a value between 0 and 1 with intervals of 0.02, indicating the willingness or propensity to work) and ’consumption’ (a value between 0 and 1 with intervals of 0.02, indicating the proportion of all your savings and income you intend to spend on essential goods."
    return report

class LLMAgent():
    def __init__(self,agent_profile = None, memory = None,llm = None,openai_api_key = None) -> None:
        assert agent_profile is not None, "Agent profile is required"
        
        if llm is None:
            llm = self.llm = ChatOpenAI(model='gpt-3.5-turbo', openai_api_key=OPENAI_API_KEY, temperature=0)
        
        self.prompt = ChatPromptTemplate.from_messages(
                    [
                        SystemMessage(
                            content=agent_profile
                        ),  
                        MessagesPlaceholder(
                            variable_name="chat_history"
                        ),  
                        HumanMessagePromptTemplate.from_template(
                            "{agent_query}"
                        ), 
                    ]
                )
        
        if memory is not None:
            self.agent_memory = memory
        else:
            self.agent_memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
        
        self.llm_chain = LLMChain(
            llm=llm,
            prompt=self.prompt,
            verbose=False,
            memory=self.agent_memory,
        )
    
    def __call__(self,input):
        return self.llm_chain.predict(agent_query = input)
    
    def get_memory(self):
        return self.agent_memory.load_memory_variables({})

    def reflect(self,reflection_prompt):
        return self.llm_chain.predict(agent_query=reflection_prompt)


if __name__ == "__main__":
    agent_profile = """
                    You’re Adam Mills, 
                    a 40-year-old individual living in New York City, New York. As with all Americans, 
                    a portion of your monthly income is taxed by the federal government. This tax-ation system is 
                    tiered, income is taxed cumulatively within defined brackets, combined with a redistributive policy: 
                    after collection, the government evenly redistributes the tax revenue back to all citizens, 
                    irrespective of their earnings. 
                    """
    
    config = {
    "name": "Adam Mills",
    "age": 40,
    "city": "New York City",
    "state": "New York",
    "month": "2001.01",
    "year": 2001,
    "profession": "Professional Athlete",
    "income": 84144.58,
    "consumption": 49825.69,
    "tax_deduction": 28216.98,
    "tax_credit": 6351.29,
    "tax_brackets": [0.00, 808.33, 3289.58, 7016.67, 13393.75, 17008.33, 42525.00],
    "tax_rates": [0.10, 0.12, 0.22, 0.24, 0.32, 0.35, 0.37],
    "essential_price": 135.82,
    "savings_balance": 12456.42,
    "interest_rate": 3.00
    }   
    query = format_financial_report(config)
    # define open AI key
    agent = LLMAgent(agent_profile = agent_profile,open_api_key=OPENAI_API_KEY)
    print(agent(query))