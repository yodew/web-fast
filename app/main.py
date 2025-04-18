#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：web-fast 
@File    ：main.py
@IDE     ：PyCharm 
@Author  ：lu.yu
@Date    ：4/10/2025 9:50 AM 
"""
from tortoise.contrib.fastapi import register_tortoise
from fastapi import FastAPI

def init_db(app: FastAPI):
    register_tortoise(
        app,
        db_url="sqlite://db.sqlite3",
        modules={"models": ["app.models.user"]},
        generate_schemas=True,
        add_exception_handlers=True,
    )
