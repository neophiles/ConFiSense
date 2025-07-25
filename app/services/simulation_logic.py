def simulate_emergency_fund(income, rate, goal, months):
    """
    Simulate the growth of an emergency fund over a specified number of months
    """
    
    savings = []
    current = 0
    for m in range(1, months + 1):
        current += income * rate
        savings.append(current)
    months_needed = next((i + 1 for i, v in enumerate(savings) if v >= goal), months)
    return {
        "data": savings,
        "summary": f"Goal reached in {months_needed} months.",
        "math_explanation": {
            "title": "The 'Glass Box': How We Calculate",
            "sections": [
                {
                    "heading": "1. Assumptions",
                    "items": [
                        f"Monthly Income: ₱{income}",
                        f"Savings Rate: {rate * 100:.0f}%",
                        f"Target Goal: ₱{goal}",
                        f"Time Frame: {months} months"
                    ]
                },
                {
                    "heading": "2. Projection Formula",
                    "items": [
                        "Each Month’s Savings = Previous + (Income × Rate)",
                        "*No taxes, emergencies, or interest included in this simple model.*"
                    ]
                }
            ]
        }
    }
