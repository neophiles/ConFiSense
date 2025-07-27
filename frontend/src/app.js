let currentScenario = null;

const slider = (id, label, min, max, step, def) => ({ id, label, min, max, step, default: def });

const scenariosConfig = {
  emergency_fund: {
    label: "Building an Emergency Fund",
    endpoint: "/simulate/emergency-fund",
    sliders: [
      slider("target_amount", "Target Emergency Fund Amount (₱)", 5000, 500000, 1000, 100000),
      slider("monthly_contribution", "Monthly Savings Contribution (₱)", 500, 20000, 500, 5000),
      slider("current_savings", "Current Emergency Savings (₱)", 0, 100000, 1000, 20000),
    ],
  },

  budgeting: {
    label: "Effective Budgeting and Expense Tracking",
    endpoint: "/simulate/budgeting",
    sliders: [
      slider("income", "Monthly Income (₱)", 10000, 100000, 1000, 40000),
      slider("fixed_expenses", "Fixed Monthly Expenses (₱)", 0, 50000, 500, 15000),
      slider("discretionary_pct", "Discretionary Spending (% of Income)", 10, 50, 1, 20),
      slider("target_savings", "Target Monthly Savings (₱)", 0, 30000, 1000, 5000),
    ],
  },

  debt_reduction: {
    label: "Managing and Reducing Debt",
    endpoint: "/simulate/debt",
    sliders: [
      slider("total_debt", "Total Debt Amount (₱)", 20000, 1000000, 10000, 200000),
      slider("interest_rate", "Annual Interest Rate (%)", 5, 30, 0.5, 10),
      slider("monthly_payment", "Current Monthly Debt Payment (₱)", 1000, 50000, 1000, 5000),
      slider("additional_payment", "Additional Monthly Payment (₱)", 0, 20000, 500, 2000),
    ],
  },

  investing: {
    label: "Starting to Save and Invest for the Future",
    endpoint: "/simulate/investment",
    sliders: [
      slider("monthly_contribution", "Monthly Contribution (₱)", 500, 30000, 500, 5000),
      slider("investment_years", "Investment Horizon (Years)", 1, 40, 1, 10),
      slider("annual_return", "Expected Annual Return (%)", 1, 15, 0.1, 6),
      slider("current_savings", "Current Investment/Savings Amount (₱)", 0, 500000, 10000, 100000),
    ],
  },

  education_funding: {
    label: "Education Funding",
    endpoint: "/simulate/education",
    sliders: [
      slider("target_cost_today", "Target Education Cost (Today) (₱)", 100000, 3000000, 50000, 1000000),
      slider("years_until_enrollment", "Years Until Enrollment", 1, 18, 1, 5),
      slider("current_savings", "Current Education Savings (₱)", 0, 500000, 10000, 100000),
      slider("monthly_contribution", "Monthly Savings Contribution (₱)", 500, 20000, 500, 3000),
      slider("annual_return", "Expected Annual Investment Return (%)", 1, 10, 0.1, 5),
      slider("inflation_rate", "Annual Education Inflation Rate (%)", 3, 7, 0.1, 4),
    ],
  },

  major_purchase: {
    label: "Major Purchase Planning",
    endpoint: "/simulate/purchase",
    sliders: [
      slider("purchase_price", "Target Purchase Price (₱)", 500000, 10000000, 100000, 3000000),
      slider("down_payment_pct", "Desired Down Payment (%)", 10, 30, 1, 20),
      slider("years_to_save", "Years to Save for Down Payment", 1, 10, 1, 3),
      slider("current_savings", "Current Savings (₱)", 0, 1000000, 10000, 200000),
      slider("monthly_contribution", "Monthly Savings Contribution (₱)", 1000, 50000, 1000, 10000),
      slider("savings_return", "Expected Annual Savings Return (%)", 1, 5, 0.1, 3),
      slider("loan_interest", "Loan Interest Rate (Annual %)", 5, 15, 0.1, 8),
      slider("loan_term_years", "Loan Term (Years)", 5, 30, 1, 15),
    ],
  },
};

function showDashboard(buttonElement) {
    const scenario = buttonElement.dataset.scenario;
    currentScenario = scenario;

    const config = scenariosConfig[scenario]
    const sliderContainer = document.getElementById('slider-fields');
    sliderContainer.innerHTML = ''; // Clear existing sliders

    config.sliders.forEach(slider => {
        const wrapper = document.createElement('div');
        wrapper.className = 'mb-4';

        const label = document.createElement('label');
        label.textContent = slider.label;
        label.htmlFor = slider.id;

        const input = document.createElement('input');
        input.type = 'range';
        input.min = slider.min;
        input.max = slider.max;
        input.step = slider.step;
        input.value = slider.default;
        input.id = slider.id;
        input.className = 'w-full';

        const valueDisplay = document.createElement('span');
        valueDisplay.id = `${slider.id}-value`;
        valueDisplay.textContent = slider.default;

        input.addEventListener('input', () => {
            valueDisplay.textContent = input.value;
        });

        wrapper.appendChild(label);
        wrapper.appendChild(input);
        wrapper.appendChild(valueDisplay);
        sliderContainer.appendChild(wrapper);
    });

    document.getElementById('home').classList.add('hidden');
    document.getElementById('dashboard').classList.remove('hidden');
}

function showHome() {
    currentScenario = null;
    document.getElementById('home').classList.remove('hidden');
    document.getElementById('dashboard').classList.add('hidden');
}