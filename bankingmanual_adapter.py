import os, uuid
from .base import BankProvider

class ManualEFTAdapter(BankProvider):
    def get_provider_name(self): return "Manual EFT"
    def is_configured(self): return bool(os.environ.get("BANK_ACCOUNT"))
    def validate_account(self, account_number): return {"valid": True}
    def prepare_withdrawal(self, amount, currency, destination):
        ref = f"EFT_{uuid.uuid4().hex[:8].upper()}"
        return {"status": "ready", "reference": ref,
                "instructions": [f"Amount: {currency} {amount:.2f}",
                                 f"To: {destination.get('account_number','N/A')}",
                                 f"Reference: {ref}",
                                 "Complete via your bank app."],
                "redirect_url": None, "reason": None}
    def get_withdrawal_status(self, reference):
        return {"status": "pending"}