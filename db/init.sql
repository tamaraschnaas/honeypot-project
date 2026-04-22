CREATE TABLE IF NOT EXISTS cowrie_events (
    id SERIAL PRIMARY KEY,
    event_time TIMESTAMP,
    src_ip TEXT,
    event_type TEXT,
    username TEXT,
    password TEXT,
    command TEXT,
    raw_json JSONB
);
