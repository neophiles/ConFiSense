import math


def simulate_emergency_fund(target, monthly_contrib, current_savings):
    """
    Simulate the growth of an emergency fund over time
    """

    # if monthly_contrib is 0 and current_savings is less than target, goal is unreachable
    # if current_savings is greater than or equal to target, time_months is 0
    # otherwise, calculate time_months as the ceiling of (target - current_savings)
    if monthly_contrib == 0 and current_savings < target:
        time_months = None
    elif current_savings >= target:
        time_months = 0
    else:
        time_months = math.ceil((target - current_savings) / monthly_contrib)
    
    return {
        "data": [current_savings, target],
        "summary": f"Goal reached in {time_months} months." if time_months is not None else "Goal is unreachable.",
        "math_explanation": {
            "title": "The 'Glass Box': How We Calculate",
            "sections": [
                {
                    "heading": "1. Assumptions",
                    "items": [
                        f"Target Emergency Fund: ₱{target:,}",
                        f"Monthly Contribution: ₱{monthly_contrib:,}",
                        f"Current Savings: ₱{current_savings:,}"
                    ]
                },
                {
                    "heading": "2. Formula",
                    "items": [
                        "Time in Months = (Target - Current) / Monthly Contribution",
                        "*If contribution is ₱0 and savings < target, goal is unreachable.*"
                    ]
                }
            ]
        }
    }



def simulate_budgeting(income, fixed_expenses, discretionary_pct, target_savings):
    """
    Simulate a monthly budget based on income, fixed expenses, discretionary percentage, and target savings
    """

    # calculate discretionary spending and potential savings
    # discretionary_pct is a percentage, so we divide by 100
    # total expenses is the sum of fixed expenses and discretionary spending
    # potential savings is income minus total expenses
    discretionary = income * (discretionary_pct / 100)
    total_expenses = fixed_expenses + discretionary
    potential_savings = income - total_expenses

    return {
        "data": {
            "Fixed Expenses": fixed_expenses,
            "Discretionary": discretionary,
            "Potential Savings": potential_savings
        },
        "summary": f"You can potentially save ₱{potential_savings:,.0f} per month.",
        "math_explanation": {
            "title": "The 'Glass Box': How We Calculate",
            "sections": [
                {
                    "heading": "1. Income Breakdown",
                    "items": [
                        f"Monthly Income: ₱{income:,}",
                        f"Fixed Expenses: ₱{fixed_expenses:,}",
                        f"Discretionary (%): {discretionary_pct}%",
                        f"Target Monthly Savings: ₱{target_savings:,}"
                    ]
                },
                {
                    "heading": "2. Formula",
                    "items": [
                        "Discretionary = Income × Discretionary %",
                        "Total Expenses = Fixed + Discretionary",
                        "Potential Savings = Income - Total Expenses"
                    ]
                }
            ]
        }
    }