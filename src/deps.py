from collections import defaultdict
from datetime import datetime, timezone
from typing import Annotated

from fastapi import Depends, HTTPException, Request

# In-memory dictionary to track access count by IP and date
ip_access_log: dict[str, dict[str, int]] = defaultdict(dict)


async def rate_limiter(request: Request):
    # Get client IP address
    client_ip = request.client.host
    # Get current date as a string (e.g., "2025-04-20")
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    # Get the access count for the client IP and today's date
    today_count = ip_access_log[client_ip].get(today, 0)

    if today_count >= 3:
        raise HTTPException(status_code=429, detail="You've reached the daily limit of 3 clicks.")

    # Increment the access count for the client IP and today's date
    ip_access_log[client_ip][today] = today_count + 1


RateLimitDep = Annotated[None, Depends(rate_limiter)]
