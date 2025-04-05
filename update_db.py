from sqlalchemy import create_engine, text

# Remplace cette URL par celle de ta base Railway si besoin
DATABASE_URL = "postgresql://postgres:sRsTTXefqzAiVpnPnmAyjkLtKEYuNXSY@trolley.proxy.rlwy.net:29567/railway"

engine = create_engine(DATABASE_URL)

with engine.connect() as connection:
    with connection.begin():
        connection.execute(text("""
            ALTER TABLE setups
            ADD COLUMN IF NOT EXISTS probability_score FLOAT,
            ADD COLUMN IF NOT EXISTS bias TEXT,
            ADD COLUMN IF NOT EXISTS confidence_comment TEXT
        """))
        print("✅ Colonnes ajoutées à la table setups avec succès.")