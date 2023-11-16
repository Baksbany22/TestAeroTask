CREATE SCHEMA IF NOT EXISTS STG
    CREATE TABLE IF NOT EXISTS API_DATA (
    id INTEGER PRIMARY KEY,
    uid UUID,
    strain VARCHAR(255),
    cannabinoid_abbreviation VARCHAR(10),
    cannabinoid VARCHAR(255),
    terpene VARCHAR(255),
    medical_use VARCHAR(255),
    health_benefit VARCHAR(255),
    category VARCHAR(255),
    type VARCHAR(255),
    buzzword VARCHAR(255),
    brand VARCHAR(255)
    );
