willingness_to_work_prompt = "In the previous month, you became unemployed and had no income. Now, you are invited to work as a(an) {offer} with a monthly salary of {wage}."
reflect_on_previous_quarter_prompt = "Given the previous quarter’s economic environment, reflect on the labor, consumption, and financial markets, as well as their dynamics. What conclusions have you drawn?"
# prompt_template_var = "You are {gender} of age {age}, living in the {county} county. The current month is {month} and year is {year}. The price of Essential Goods is {price_of_goods}, inflation rate is {inflation_rate} and the interest rate set by bank is {interest_rate}. With all these factors in play, and considering aspects like your living costs, any future aspirations, and the broader economic trends, how is your willingness to work this month? Furthermore, how would you plan your expenditures on essential goods, keeping in mind goods price? You must share your decision in a JSON string format! The format should have three keys: ’work’ (a value between 0 and 1 with intervals of 0.02, indicating the willingness or propensity to work), ’consumption’ (a value between 0 and 1 with intervals of 0.02, indicating the proportion of all your savings and income you intend to spend on essential goods) and 'explanation' (Your explanation for your decision)."
prompt_template_var = "You are of age {age}. With all these factors in play, and considering aspects like your living costs, any future aspirations, and the broader economic trends, how is your willingness to work this month? Furthermore, how would you plan your expenditures on essential goods, keeping in mind goods price? You must share your decision in a JSON string format! The format should have three keys: ’work’ (a value between 0 and 1 with intervals of 0.02, indicating the willingness or propensity to work), ’consumption’ (a value between 0 and 1 with intervals of 0.02, indicating the proportion of all your savings and income you intend to spend on essential goods) and 'explanation' (Your explanation for your decision)."

agent_profile = "You’re an individual living in New York City, New York. As with all Americans, a portion of your monthly income is taxed by the federal government. This tax-ation system is tiered, income is taxed cumulatively within defined brackets, combined with a redistributive policy: after collection, the government evenly redistributes the tax revenue back to all citizens, irrespective of their earnings. "
complete_final_report_prompt = """
                    Now it’s {month}.{year}. In the previous month, you worked as a(an) {profession}. 
                    If you continue working this month, your expected income will be ${income:.2f}, 
                    which is decreased compared to the last month due to the deflation of the labor market. 
                    Besides, your consumption was ${consumption:.2f}. Your tax deduction amounted to ${tax_deduction:.2f}. 
                    However, as part of the government’s redistribution program, you received a credit of ${tax_credit:.2f}. 
                    In this month, the government sets the brackets: {tax_brackets} and their corresponding rates: {tax_rates}. 
                    Income earned within each bracket is taxed only at that bracket’s rate. 
                    Meanwhile, deflation has led to a price decrease in the consumption market, 
                    with the average price of essential goods now at ${essential_price:.2f}. 
                    Your current savings account balance is ${savings_balance:.2f}. 
                    Interest rates, as set by your bank, stand at {interest_rate:.2f}%. 
                    With all these factors in play, and considering aspects like your living costs, 
                    any future aspirations, and the broader economic trends, how is your willingness to work this month? 
                    Furthermore, how would you plan your expenditures on essential goods, keeping in mind goods price? 
                    Please share your decisions in a JSON format. The format should have two keys: ’work’ 
                    (a value between 0 and 1 with intervals of 0.02, indicating the willingness or propensity to work) 
                    and ’consumption’ (a value between 0 and 1 with intervals of 0.02, 
                    indicating the proportion of all your savings and income you intend to spend on essential goods).
                """