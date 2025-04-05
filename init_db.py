from app.database import engine
from app import models

print("🧹 Suppression des anciennes tables...")
models.Base.metadata.drop_all(bind=engine)

print("📦 Création des nouvelles tables...")
models.Base.metadata.create_all(bind=engine)

print("✅ Base de données initialisée avec succès !")
