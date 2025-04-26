import joblib

# Cargar el modelo que tienes
model = joblib.load('model.pkl')

# Ver qué es realmente
print(type(model))

# Si es un GridSearchCV:
if hasattr(model, 'best_estimator_'):
    print("Es un GridSearchCV, extrayendo best_estimator_...")
    model = model.best_estimator_
    print(type(model))

# Confirmar que el modelo tiene .predict
if hasattr(model, 'predict'):
    print("OK: el modelo tiene método predict.")
else:
    print("ERROR: el modelo no tiene método predict.")

# Guardar modelo limpio
joblib.dump(model, 'modelo_limpio.pkl')
print("Modelo limpio guardado como modelo_limpio.pkl")
