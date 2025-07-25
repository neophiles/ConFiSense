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
