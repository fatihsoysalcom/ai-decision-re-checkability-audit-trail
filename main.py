import datetime
import json

def make_credit_decision(applicant_data: dict) -> dict:
    """
    Simulates an AI-powered credit decision system, providing an audit trail
    for re-checkability and transparency.
    """
    # --- Input Data Logging (Transparency) ---
    # Log the exact input data received for the decision.
    # This is crucial for re-checking what the AI saw and ensuring data provenance.
    input_snapshot = applicant_data.copy()

    # --- Decision Logic (Simulated AI Rules) ---
    # In a real AI system, this would be a complex model inference.
    # Here, we use simple rules to demonstrate the concept of explainability.
    income = applicant_data.get('income', 0)
    credit_score = applicant_data.get('credit_score', 0)
    employment_years = applicant_data.get('employment_years', 0)
    has_defaults = applicant_data.get('has_defaults', False)

    decision = "REJECT"
    reasons = []
    decision_factors = [] # Structured factors influencing the decision

    # Rule 1: Basic income threshold
    if income < 30000:
        reasons.append("Income below minimum threshold (required: 30,000).")
        decision_factors.append({"factor": "income", "value": income, "threshold": 30000, "outcome": "negative"})
    else:
        decision_factors.append({"factor": "income", "value": income, "threshold": 30000, "outcome": "positive"})

    # Rule 2: Credit score check
    if credit_score < 650:
        reasons.append("Credit score too low (required: 650).")
        decision_factors.append({"factor": "credit_score", "value": credit_score, "threshold": 650, "outcome": "negative"})
    else:
        decision_factors.append({"factor": "credit_score", "value": credit_score, "threshold": 650, "outcome": "positive"})

    # Rule 3: Employment stability
    if employment_years < 2:
        reasons.append("Insufficient employment history (required: 2 years).")
        decision_factors.append({"factor": "employment_years", "value": employment_years, "threshold": 2, "outcome": "negative"})
    else:
        decision_factors.append({"factor": "employment_years", "value": employment_years, "threshold": 2, "outcome": "positive"})

    # Rule 4: Past defaults
    if has_defaults:
        reasons.append("Applicant has previous defaults.")
        decision_factors.append({"factor": "has_defaults", "value": has_defaults, "outcome": "negative"})

    # Final decision based on accumulated reasons
    if not reasons: # If no negative reasons were found
        decision = "APPROVE"
        reasons.append("All credit criteria met.")

    # --- Audit Trail / Explanation Generation (Re-checkability) ---
    # This structured output allows independent verification of the decision.
    # It includes the exact inputs, the decision, human-readable reasons, and
    # structured factors, making the AI's process transparent and auditable.
    audit_log = {
        "timestamp": datetime.datetime.now().isoformat(),
        "applicant_id": applicant_data.get('id', 'N/A'),
        "input_data_snapshot": input_snapshot, # The exact data used for this decision
        "decision": decision,
        "reasons": reasons, # Human-readable reasons for the decision
        "decision_logic_factors": decision_factors, # Structured factors that influenced the decision
        "system_version": "1.0.0" # Important for reproducibility over time
    }

    return audit_log

if __name__ == "__main__":
    print("--- AI Credit Decision System with Audit Trail ---")

    # Example 1: Applicant likely to be approved
    applicant_1 = {
        "id": "APP001",
        "age": 35,
        "income": 60000,
        "credit_score": 720,
        "employment_years": 5,
        "has_defaults": False
    }
    print("\nProcessing Applicant 1:")
    result_1 = make_credit_decision(applicant_1)
    print(json.dumps(result_1, indent=2, ensure_ascii=False))

    # Example 2: Applicant likely to be rejected due to low income and credit score
    applicant_2 = {
        "id": "APP002",
        "age": 28,
        "income": 25000,
        "credit_score": 600,
        "employment_years": 1,
        "has_defaults": False
    }
    print("\nProcessing Applicant 2:")
    result_2 = make_credit_decision(applicant_2)
    print(json.dumps(result_2, indent=2, ensure_ascii=False))

    # Example 3: Applicant rejected due to past defaults
    applicant_3 = {
        "id": "APP003",
        "age": 40,
        "income": 70000,
        "credit_score": 750,
        "employment_years": 10,
        "has_defaults": True
    }
    print("\nProcessing Applicant 3:")
    result_3 = make_credit_decision(applicant_3)
    print(json.dumps(result_3, indent=2, ensure_ascii=False))

    print("\n--- End of Demonstration ---")
    print("Each decision includes an 'input_data_snapshot', 'decision', 'reasons', and 'decision_logic_factors'.")
    print("This structured output allows for independent verification and re-checking of the AI's decision logic.")
