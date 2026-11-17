import os
from .base import BankProvider

class PeachAdapter(BankProvider):
    def get_provider_name(self): return "Peach Payments"
    def is_configured(self): return bool(os.environ.get("PEACH_ENTITY_ID"))
    def validate_account(self, account_number): return {"valid": True}
    def prepare_withdrawal(self, amount, currency, destination):
        return {"status": "ready", "reference": "PEACH_REF",
                "instructions": ["Redirect to Peach"],
                "redirect_url": "https://...", "reason": None}
    def get_withdrawal_status(self, reference):
        return {"status": "pending"}