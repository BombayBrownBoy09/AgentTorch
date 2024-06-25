import pytest
import dspy
import os

from agent_torch.llm.llm import DspyLLM, LangchainLLM

OPENAI_API_KEY = os.environ.get("OPENAPI_API_KEY", "***")


class BasicQAEcon(dspy.Signature):
    """
    You are an individual living during the COVID-19 pandemic. You need to decide your willingness to work each month and portion of your assests you are willing to spend to meet your consumption demands, based on the current situation of NYC.
    """

    history = dspy.InputField(
        desc="may contain your decision in the previous months", format=list
    )
    question = dspy.InputField(
        desc="will contain the number of COVID cases in NYC, your age and other information about the economy and your identity, to help you decide your willingness to work and consumption demands"
    )
    answer = dspy.OutputField(
        desc="will contain single float value, between 0 and 1, representing realistic probability of your willingness to work. No other information should be there."
    )


class COT(dspy.Module):
    def __init__(self, qa):
        super().__init__()
        self.generate_answer = dspy.ChainOfThought(qa)

    def forward(self, question, history):
        prediction = self.generate_answer(question=question, history=history)
        return dspy.Prediction(answer=prediction)


@pytest.fixture
def agent_profile():
    return "You are a human in the midst of a COVID outbreak."


@pytest.fixture
def user_prompt():
    return "Your age is {age} {gender},{unemployment_rate} the number of COVID cases is {covid_cases}."


@pytest.fixture
def sampling_args():
    return {
        "month": "January",
        "year": "2020",
        "covid_cases": 1200,
        "device": "cpu",
        "current_memory_dir": "simulation_memory_output/",
        "unemployment_rate": 0.05,
    }


@pytest.fixture
def num_agents():
    # the number of agents is based on the unique combinations of the prompt variables
    # which correspond to the population attributes.
    return 12


@pytest.fixture
def dspy_llm():
    llm = DspyLLM(qa=BasicQAEcon, cot=COT, openai_api_key=OPENAI_API_KEY)
    llm.initialize_llm()

    return llm


@pytest.fixture
def langchain_llm(agent_profile):
    llm = LangchainLLM(agent_profile=agent_profile, openai_api_key=OPENAI_API_KEY)
    llm.initialize_llm()

    return llm
