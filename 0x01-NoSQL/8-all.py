#!/usr/bin/env python3
"""
nosql
"""


import pymongo


def list_all(mongo_collection):
    """all docs """
    if not mongo_collection:
        return []
    docs = mongo_collection.find()
    return [doc for doc in docs]
