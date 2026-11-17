# Copy this file to add a new bank. No core changes needed.
import os
from .base import BankProvider

class YourBankAdapter(BankProvider):
    def get_provider_name(self): return "Your Bank"
    def is_configured(self): return bool(os.environ.get("YOURBANK_API_KEY"))
    def validate_account(self, account_number): return {"valid": True}
    def prepare_withdrawal(self, amount, currency, destination):
        return {"status": "ready", "reference": "YOURBANK_REF",
                "instructions": ["..."], "redirect_url": None, "reason": None}
    def get_withdrawal_status(self, reference):
        return {"status": "pending"}