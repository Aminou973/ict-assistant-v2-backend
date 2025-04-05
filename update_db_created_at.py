from sqlalchemy import create_engine, text

# URL de ta base PostgreSQL
DATABASE_URL = "postgresql://postgres:sRsTTXefqzAiVpnPnmAyjkLtKEYuNXSY@trolley.proxy.rlwy.net:29567/railway"

engine = create_engine(DATABASE_URL)

with engine.connect() as connection:
    with connection.begin():
        connection.execute(text("""
            ALTER TABLE setups
            ADD COLUMN IF NOT EXISTS created_at TIMESTAMP DEFAULT NOW()
        """))
        print("✅ Colonne created_at ajoutée avec succès.")