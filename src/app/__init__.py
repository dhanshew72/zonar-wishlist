"""
App
"""
from fastapi import FastAPI

from .routers import wishlist

app = FastAPI()
common_prefix = '/wishlist'
app.include_router(wishlist.router, prefix=common_prefix)
