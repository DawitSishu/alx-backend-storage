#!/usr/bin/env python3
"""
nosql
"""


import pymongo


def schools_by_topic(mongo_collection, topic):
    """specific school"""
    return mongo_collection.find({"topics": topic})
