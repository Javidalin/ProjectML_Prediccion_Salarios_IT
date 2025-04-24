# Predicción de Salario Anual en el Sector IT

Este proyecto tiene como objetivo construir un modelo de Machine Learning capaz de predecir el **salario anual** de profesionales del sector tecnológico a partir de una serie de características personales y laborales extraídas de encuestas reales.

## Problema que se quiere resolver

En un mundo donde el sector tecnológico evoluciona constantemente, **conocer de forma aproximada el salario que se puede esperar según el perfil profesional** es clave para:

- Tomar decisiones de carrera (cambiar de país, aprender nuevas tecnologías, formarse más)
- Negociar condiciones laborales con más información
- Empresas que buscan establecer políticas salariales competitivas

Sin embargo, existen muchos factores que influyen en el salario: experiencia, nivel educativo, país, tamaño de la empresa, rol profesional, etc. Este proyecto intenta modelar esas relaciones **para predecir el salario lo más precisamente posible** usando técnicas de aprendizaje automático.

## Dataset

Los datos utilizados provienen de la encuesta anual de Stack Overflow, una de las mayores fuentes de información sobre desarrolladores a nivel mundial. ( https://survey.stackoverflow.co/ )
Las variables seleccionadas incluyen:

- Tipo de empleo (jornada completa, freelance…)
- Modalidad de trabajo (remoto, presencial…)
- Rol o combinación de roles dentro del sector
- Nivel educativo alcanzado
- Años de experiencia profesional
- País de residencia
- Tamaño de la empresa
- Salario anual en USD (variable objetivo)

## Modelo final

Después de entrenar y comparar múltiples algoritmos de regresión, el mejor rendimiento se obtuvo con **CatBoostRegressor**, alcanzando una puntuación de:

-  **R² ≈ 0.60**  
  (lo que indica que el modelo explica el 60% de la variabilidad en los salarios a partir de las variables disponibles)

## Tecnologías utilizadas

- Python 3
- pandas, NumPy
- scikit-learn
- CatBoost
- GridSearchCV para ajuste de hiperparámetros
- Jupyter Notebook
