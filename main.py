import os

log_level = os.getenv("DEBUG_SUPER_LONG_DEBUG_SUPER_LONG_DEBUG_SUPER_LONG", "").lower() == "true"

print(f"{log_level=}")
