import asyncio

import pytest
from fastapi import HTTPException

from utils.rate_limiter import rate_limited


# Mocking the function to be rate-limited
async def mock_function():
    pass

def test_rate_limited_decorator_pass():
    @rate_limited(max_calls=2, time_frame=5)
    async def mock_function_rate_limited():
        return await mock_function()
    
    asyncio.run(mock_function_rate_limited())
    asyncio.run(mock_function_rate_limited())

def test_rate_limited_decorator_raise_exception():
    @rate_limited(max_calls=2, time_frame=2)
    async def mock_function_rate_limited():
        return await mock_function()
    
    asyncio.run(mock_function_rate_limited())
    asyncio.run(mock_function_rate_limited())
    with pytest.raises(HTTPException):
        asyncio.run(mock_function_rate_limited())