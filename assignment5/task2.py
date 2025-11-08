class LoanApprovalSystem:
    def __init__(self):
        self.minimum_credit_score = 650
        self.minimum_income = 30000
        self.maximum_debt_ratio = 0.43

    def calculate_debt_ratio(self, monthly_debt, monthly_income):
        return monthly_debt / monthly_income if monthly_income > 0 else float('inf')

    def evaluate_loan(self, applicant_data):
        credit_score = applicant_data['credit_score']
        annual_income = applicant_data['annual_income']
        monthly_debt = applicant_data['monthly_debt']
        monthly_income = annual_income / 12
        loan_amount = applicant_data['loan_amount']
        
        debt_ratio = self.calculate_debt_ratio(monthly_debt, monthly_income)
        
        if credit_score < self.minimum_credit_score:
            return False, "Credit score below minimum requirement"
            
        if annual_income < self.minimum_income:
            return False, "Income below minimum requirement"
            
        if debt_ratio > self.maximum_debt_ratio:
            return False, "Debt-to-income ratio too high"
            
        if loan_amount > annual_income * 4:
            return False, "Loan amount exceeds maximum allowable based on income"
            
        return True, "Loan approved"

def test_loan_system():
    loan_system = LoanApprovalSystem()
    
    test_cases = [
        {
            'name': 'Sarah Johnson',
            'credit_score': 720,
            'annual_income': 75000,
            'monthly_debt': 1500,
            'loan_amount': 200000
        },
        {
            'name': 'Michael Chen',
            'credit_score': 680,
            'annual_income': 65000,
            'monthly_debt': 1200,
            'loan_amount': 180000
        },
        {
            'name': 'Maria Rodriguez',
            'credit_score': 700,
            'annual_income': 70000,
            'monthly_debt': 1300,
            'loan_amount': 190000
        },
        {
            'name': 'James Smith',
            'credit_score': 690,
            'annual_income': 68000,
            'monthly_debt': 1400,
            'loan_amount': 185000
        },
        {
            'name': 'Aisha Patel',
            'credit_score': 710,
            'annual_income': 72000,
            'monthly_debt': 1350,
            'loan_amount': 195000
        }
    ]
    
    for applicant in test_cases:
        result, message = loan_system.evaluate_loan(applicant)
        print(f"\nApplicant: {applicant['name']}")
        print(f"Credit Score: {applicant['credit_score']}")
        print(f"Annual Income: ${applicant['annual_income']:,}")
        print(f"Monthly Debt: ${applicant['monthly_debt']:,}")
        print(f"Loan Amount: ${applicant['loan_amount']:,}")
        print(f"Decision: {'Approved' if result else 'Denied'}")
        print(f"Reason: {message}")

if __name__ == "__main__":
    test_loan_system()
