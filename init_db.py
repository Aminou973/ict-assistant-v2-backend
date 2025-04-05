from app.database import Base, engine
from app import models

print("Création des tables...")
Base.metadata.create_all(bind=engine)
print("✅ Base de données initialisée.")
