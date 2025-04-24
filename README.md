# Annual Salary Prediction in the IT Sector / Predicción de Salario Anual en el Sector IT

This project aims to build a Machine Learning model capable of predicting the **annual salary** of IT professionals based on a series of personal and work-related characteristics extracted from real surveys. / Este proyecto tiene como objetivo construir un modelo de Machine Learning capaz de predecir el **salario anual** de profesionales del sector tecnológico a partir de una serie de características personales y laborales extraídas de encuestas reales.

## Problem to be Solved / Problema que se quiere resolver

In a world where the tech sector is constantly evolving, **knowing approximately the salary one can expect based on their professional profile** is key for: / En un mundo donde el sector tecnológico evoluciona constantemente, **conocer de forma aproximada el salario que se puede esperar según el perfil profesional** es clave para:

- Making career decisions (relocating, learning new technologies, pursuing further education) / Tomar decisiones de carrera (cambiar de país, aprender nuevas tecnologías, formarse más)
- Negotiating working conditions with more information / Negociar condiciones laborales con más información
- Companies aiming to establish competitive salary policies / Empresas que buscan establecer políticas salariales competitivas

However, many factors influence salary: experience, education level, country, company size, professional role, etc. / Sin embargo, existen muchos factores que influyen en el salario: experiencia, nivel educativo, país, tamaño de la empresa, rol profesional, etc.

This project aims to model these relationships **to predict salary as accurately as possible** using machine learning techniques. / Este proyecto intenta modelar esas relaciones **para predecir el salario lo más precisamente posible** usando técnicas de aprendizaje automático.

## Dataset

The data used comes from the annual Stack Overflow survey, one of the largest sources of developer information worldwide. (https://survey.stackoverflow.co/) You can download the public 2024 dataset used here. A sample of the cleaned dataset is also included in `/src/data_sample`. / Los datos utilizados provienen de la encuesta anual de Stack Overflow, una de las mayores fuentes de información sobre desarrolladores a nivel mundial. (https://survey.stackoverflow.co/) Podéis descargar el dataset público utilizado de 2024, también se adjunta una muestra del dataset limpio en `/src/data_sample`.

The selected variables include: / Las variables seleccionadas incluyen:

- Type of employment (full-time, freelance…) / Tipo de empleo (jornada completa, freelance…)
- Work modality (remote, on-site…) / Modalidad de trabajo (remoto, presencial…)
- Role or combination of roles within the sector / Rol o combinación de roles dentro del sector
- Education level achieved / Nivel educativo alcanzado
- Years of professional experience / Años de experiencia profesional
- Country of residence / País de residencia
- Company size / Tamaño de la empresa
- Annual salary in USD (target variable) / Salario anual en USD (variable objetivo)

## Final Model / Modelo final

After training and comparing multiple regression algorithms, the best performance was achieved with **CatBoostRegressor**, reaching a score of: / Después de entrenar y comparar múltiples algoritmos de regresión, el mejor rendimiento se obtuvo con **CatBoostRegressor**, alcanzando una puntuación de:

- **R² ≈ 0.60**  
  (indicating that the model explains about 60% of the variability in salaries based on the available variables) / (lo que indica que el modelo explica el 60% de la variabilidad en los salarios a partir de las variables disponibles)

## Why an R² of 0.60 is a Great Result / Por qué un R² de 0.60 es un Excelente Resultado

An R² of 0.60 means the model explains 60% of salary variation, which is strong for real-world human data. / Un R² de 0.60 significa que el modelo explica el 60% de la variación salarial, lo cual es sólido para datos humanos reales.
External factors like negotiation, company culture, or tech stack are not in the dataset. / Factores externos como la negociación, la cultura de la empresa o el stack tecnológico no están en el dataset.
Reaching 0.60 shows the model captures useful patterns without overfitting. / Alcanzar 0.60 indica que el modelo capta patrones útiles sin sobreajustarse.


## Technologies Used / Tecnologías utilizadas

- Python 3
- pandas, NumPy
- scikit-learn
- CatBoost
- GridSearchCV for hyperparameter tuning / GridSearchCV para ajuste de hiperparámetros  
- Jupyter Notebook
