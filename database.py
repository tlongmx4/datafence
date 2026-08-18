import sqlite3

conn = sqlite3.connect('database.db')
conn.execute("PRAGMA foreign_keys = ON")
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS person (
    id INTEGER PRIMARY KEY,
    name TEXT,
    aliases BLOB,
    addresses BLOB,
    date_of_birth TEXT,
    email TEXT
)""")

c.execute("""CREATE TABLE IF NOT EXISTS broker (
    id INTEGER PRIMARY KEY,
    name TEXT,
    opt_out_url TEXT,
    process_type TEXT,
    requires_captcha BOOLEAN,
    avg_removal_days INTEGER
)""")

c.execute("""CREATE TABLE IF NOT EXISTS listing (
    id INTEGER PRIMARY KEY,
    person_id INTEGER,
    broker_id INTEGER,
    matched_url TEXT,
    confidence_score REAL,
    status TEXT,
    found_at TEXT,
    submitted_at TEXT,
    removed_at TEXT,
    last_checked_at TEXT,
    FOREIGN KEY (person_id) REFERENCES person(id),
    FOREIGN KEY (broker_id) REFERENCES broker(id)
)""")

conn.commit()
conn.close()

