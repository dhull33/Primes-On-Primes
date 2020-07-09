import os
import psycopg2


from flask import Flask
from config import DevelopmentConfig
from data.Database import Database


app = Flask(__name__)

db = Database().create()

db.execute(
    "INSERT INTO primes (id, prime) VALUES (%s, %s) RETURNING *;", ("2651243", "5")
)

a_prime = db.fetchone()
print(a_prime)

db.connection.commit()

db.close()
db.connection.close()


@app.route("/")
def hello_world():
    return "Hello World!"


if __name__ == "__main__":
    app.run()
