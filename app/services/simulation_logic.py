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



def simulate_debt_management(debt, monthly_payment, interest_rate, extra_payment):
    """
    Simulate the process of paying off debt over time
    """

    # rate is the monthly interest rate, calculated from the annual interest rate
    # balance starts at the total debt
    # month is the counter for how many months it takes to pay off the debt
    # total_interest accumulates the total interest paid
    # history keeps track of the remaining balance each month
    # payment is the total monthly payment including any extra payment
    rate = interest_rate / 12 / 100
    balance = debt
    month = 0
    total_interest = 0
    history = []
    payment = monthly_payment + extra_payment


    # if payment is less than or equal to the interest accrued, debt cannot be reduced
    if payment <= balance * rate:
        return {
            "data": [],
            "summary": "Payment too low to reduce debt.",
            "math_explanation": {"title": "", "sections": []}
        }

    # loop until the balance is paid off
    # interest is calculated as the balance times the monthly rate
    # principal is the payment minus the interest
    # balance is reduced by the principal
    # total_interest is accumulated
    # month is incremented
    # history is updated with the remaining balance
    while balance > 0:
        interest = balance * rate
        principal = payment - interest
        balance -= principal
        total_interest += interest
        month += 1
        history.append(balance if balance > 0 else 0)

        if month > 600: # prevent infinite loop
            break

    return {
        "data": history,
        "summary": f"Debt paid off in {month} months with ₱{total_interest:,.0f} in interest.",
        "math_explanation": {
            "title": "The 'Glass Box': How We Calculate",
            "sections": [
                {
                    "heading": "1. Inputs",
                    "items": [
                        f"Total Debt: ₱{debt:,}",
                        f"Annual Interest Rate: {interest_rate}%",
                        f"Monthly Payment: ₱{monthly_payment:,}",
                        f"Extra Payment: ₱{extra_payment:,}"
                    ]
                },
                {
                    "heading": "2. Formula",
                    "items": [
                        "Monthly Interest = Balance × Monthly Rate",
                        "Principal = Payment - Interest",
                        "Balance -= Principal (until paid off)"
                    ]
                }
            ]
        }
    }
