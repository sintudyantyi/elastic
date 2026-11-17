import os
from .base import BankProvider

class PayFastAdapter(BankProvider):
    def get_provider_name(self): return "PayFast"
    def is_configured(self): return bool(os.environ.get("PAYFAST_MERCHANT_ID"))
    def validate_account(self, account_number): return {"valid": True}
    def prepare_withdrawal(self, amount, currency, destination):
        return {"status": "ready", "reference": "PF_REF",
                "instructions": ["Redirect to PayFast"],
                "redirect_url": "https://www.payfast.co.za/...", "reason": None}
    def get_withdrawal_status(self, reference):
        return {"status": "pending"}