import pytest

from populations import NYC as nyc
from agent_torch.llm.archetype import Archetype, LLMArchetype
from agent_torch.llm.behavior import Behavior

from fixtures.llm_behavior import (
    dspy_llm,
    langchain_llm,
    user_prompt,
    agent_profile,
    sampling_args,
    num_agents,
)


# run the `test_llm_behavior` test for all types of LLMs
@pytest.fixture(params=["dspy_llm", "langchain_llm"])
def llm(request):
    return request.getfixturevalue(request.param)


def test_llm_behavior(llm, user_prompt, num_agents, sampling_args):
    archetypes_args = {"llm": llm, "user_prompt": user_prompt, "num_agents": num_agents}

    archetype = LLMArchetype(**archetypes_args)
    earning_behavior = Behavior(archetype=archetype, region=nyc)
    output = earning_behavior.sample(sampling_args)

    assert output is not None
    assert len(output) == num_agents
    assert output[0] is not None
