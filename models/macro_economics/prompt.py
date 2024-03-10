willingness_to_work_prompt = "In the previous month, you became unemployed and had no income. Now, you are invited to work as a(an) {offer} with a monthly salary of {wage}."
reflect_on_previous_quarter_prompt = "Given the previous quarter’s economic environment, reflect on the labor, consumption, and financial markets, as well as their dynamics. What conclusions have you drawn?"
prompt_template = "You are {male} of age {age} and are {ethnicity}. You live in {area}. Give your willingness to work in {industry}, denote the willingness by giving a value between 0 and 1, with 0 being not willing at all and 1 being completely willing."
prompt_template_var = "You are {gender} of age {age}. Give your willingness to work, denote the willingness by giving a value between 0 and 1, with 0 being not willing at all and 1 being completely willing."
agent_profile = """
                    You’re an individual living in New York City, New York. As with all Americans, 
                    a portion of your monthly income is taxed by the federal government. This tax-ation system is 
                    tiered, income is taxed cumulatively within defined brackets, combined with a redistributive policy: 
                    after collection, the government evenly redistributes the tax revenue back to all citizens, 
                    irrespective of their earnings. 
                    """ 