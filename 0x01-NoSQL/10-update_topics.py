#!/usr/bin/env python3
"""
nosql
"""


import pymongo


def update_topics(mongo_collection, name, topics):
    """update school"""
    return mongo_collection.update_many({"name": name},
                                        {"$set": {"topics": topics}})
