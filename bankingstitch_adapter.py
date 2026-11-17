import os
from .base import BankProvider

class StitchAdapter(BankProvider):
    def get_provider_name(self): return "Stitch"
    def is_configured(self): return bool(os.environ.get("STITCH_CLIENT_ID"))
    def validate_account(self, account_number): return {"valid": True}
    def prepare_withdrawal(self, amount, currency, destination):
        return {"status": "ready", "reference": "STITCH_REF",
                "instructions": ["Redirect to Stitch"],
                "redirect_url": "https://...", "reason": None}
    def get_withdrawal_status(self, reference):
        return {"status": "pending"}