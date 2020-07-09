#!/usr/bin/env python3
"""
Author: David Hull
Date: 7/9/20
Description: Something really dope.
"""
import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()


class Database(object):
    def __init__(
        self,
        dbname=f"{os.getenv('DB_NAME')}",
        user=f"{os.getenv('DB_USER')}",
        password=f"{os.getenv('DB_PWD')}",
        host=f"{os.getenv('DB_HOST')}",
        port=f"{os.getenv('DB_PORT')}",
    ):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.connection = psycopg2.connect(
            dbname=self.dbname,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port,
        )

    def create(self):

        return self.connection.cursor()
