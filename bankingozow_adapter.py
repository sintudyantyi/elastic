import os
from .base import BankProvider

class OzowAdapter(BankProvider):
    def get_provider_name(self): return "Ozow"
    def is_configured(self): return bool(os.environ.get("OZOW_API_KEY"))
    def validate_account(self, account_number): return {"valid": True}
    def prepare_withdrawal(self, amount, currency, destination):
        # TODO: implement Ozow API call
        return {"status": "ready", "reference": "OZOW_REF",
                "instructions": ["Redirect to Ozow payment page"],
                "redirect_url": "https://pay.ozow.com/...", "reason": None}
    def get_withdrawal_status(self, reference):
        return {"status": "pending"}