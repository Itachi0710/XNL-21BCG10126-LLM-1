class ComplianceAgent:
    def __init__(self):
        pass

    def check_compliance(self, transaction_data):
        if transaction_data['amount'] > 1000000:
            print("Compliance check passed.")
        else:
            print("Compliance check failed.")
