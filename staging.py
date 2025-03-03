import json
import pandas as pd
from sqlalchemy import create_engine
from subsription_event import generate_emails

def load_keys(path):
    with open(path, "r") as file:
        db = json.load(file)

    return db

def populate_df():

    data = [generate_emails() for _ in range(1)]

    headers = ['first_name', 'last_name', 'email']

    df = pd.DataFrame(data = data, columns = headers)

    print("\n")

    print(df.head())


def conn_db():

    db = load_keys("db.json")

    # conn_str = "dialect+driver://username:password@host:port/database"
    conn_str = f"{db["dialect"]}+{db["driver"]}://{db['username']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}"

    engine = create_engine(conn_str)

    print(engine) if engine else None

# df.to_sql(con = engine)

if __name__ == "__main__":
    populate_df()