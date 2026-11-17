import os
from .manual_adapter import ManualEFTAdapter
from .ozow_adapter import OzowAdapter
from .payfast_adapter import PayFastAdapter
from .peach_adapter import PeachAdapter
from .stitch_adapter import StitchAdapter

PROVIDERS = {
    "manual": ManualEFTAdapter,
    "ozow": OzowAdapter,
    "payfast": PayFastAdapter,
    "peach": PeachAdapter,
    "stitch": StitchAdapter,
}

def get_bank_provider():
    name = os.environ.get("BANK_PROVIDER", "manual").lower()
    if name not in PROVIDERS:
        raise ValueError(f"Unknown bank provider: {name}")
    return PROVIDERS[name]()

def get_all_providers():
    return [{"id": k, "name": v().get_provider_name(),
             "configured": v().is_configured()} for k, v in PROVIDERS.items()]