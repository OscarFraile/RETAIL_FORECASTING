# Retail Forecasting — Predicción de Ventas por Producto y Tienda

Modelo de forecasting de ventas diarias para 10 productos en 2 tiendas (20 combinaciones), usando datos históricos de la competición M5 Forecasting de Kaggle. El sistema se escala automáticamente a todas las combinaciones producto-tienda mediante pipelines individuales.

## Tecnologías

Python · Pandas · Scikit-learn · LightGBM · Matplotlib · Jupyter Notebook

## Estructura del repositorio

```
├── 01_Documentos/
│   ├── 002_RETAIL_Transformaciones+Procesos.xlsx  # Documentación de transformaciones
│   └── 002_retail.yml                             # Configuración del entorno
│
├── 02_Datos/
│   ├── 01_Originales/
│   │   └── hipermercado.db                        # Dataset original (SQLite)
│   ├── 02_Validacion/
│   │   ├── DatosParaProduccion.csv
│   │   └── validacion.csv
│   └── 03_Trabajo/
│       ├── cat_resultado_calidad.pickle
│       ├── cat_resultado_eda.pickle
│       ├── df_tablon.pickle
│       ├── num_resultado_calidad.pickle
│       ├── num_resultado_eda.pickle
│       ├── trabajo.csv
│       ├── trabajo_resultado_calidad.pickle
│       ├── x_preseleccionado.pickle
│       └── y_preseleccionado.pickle
│
├── 03_Notebooks/
│   ├── 02_Desarrollo/
│   │   ├── 01_Set_Up.ipynb
│   │   ├── 02_Calidad_de_Datos.ipynb
│   │   ├── 04_Transformacion_de_datos.ipynb
│   │   ├── 05_Preselección_de_variables.ipynb
│   │   ├── 06_Modelizacion_para_Regresion.ipynb
│   │   └── 07_Preparacion_del_codigo_de_produccion.ipynb
│   └── 03_Sistema/
│       ├── 08_Codigo_de_reentrenamiento.ipynb
│       ├── 08_Codigo_de_reentrenamiento.py
│       ├── 09_Codigo_de_ejecucion.ipynb
│       ├── 09_Codigo_de_ejecucion.py
│       └── FuncionesAuxiliares.py
│
├── 04_Modelos/
│   ├── lista_modelos_retail.pickle   # Lista de los 20 modelos entrenados
│   ├── ohe_retail.pickle             # Pipeline de encoding
│   └── te_retail.pickle              # Pipeline de target encoding
│
├── 05_Resultados/
│   ├── variables_finales.pickle
│   └── hipermercado.db               # Base de datos con resultados
│
└── README.md
```

## El problema

Predecir las ventas diarias de productos de alimentación a nivel tienda-producto, incorporando variables temporales (día, mes, año, día de la semana), eventos especiales y precio de venta.

**Dataset:** M5 Forecasting (Kaggle) — ventas diarias desde enero 2013, tienda CA_3, categoría FOODS_3.

## Pipeline

**1. Validación temporal**
En forecasting no se puede hacer split aleatorio. El conjunto de validación está compuesto por los últimos datos disponibles de la serie temporal.

**2. Modelización individual**
Se desarrolla y valida el proceso completo para un único producto antes de escalar.

**3. Escalado a 20 combinaciones**
El proceso se encapsula en funciones auxiliares (`FuncionesAuxiliares.py`) y se itera sobre todas las combinaciones tienda-producto, generando un pipeline entrenado por cada una.

**Algoritmo:** HistGradientBoostingRegressor con RandomizedSearchCV.

## Producción

El sistema tiene dos modos:

- **Reentrenamiento** (`08_Codigo_de_reentrenamiento.ipynb/.py`): reentrena los 20 modelos sobre nuevos datos manteniendo la misma configuración.
- **Ejecución** (`09_Codigo_de_ejecucion.ipynb/.py`): carga los pipelines serializados y genera predicciones sin reentrenar.

## Cómo ejecutarlo

```bash
pip install -r requirements.txt

# Fase desarrollo: ejecutar notebooks en orden desde 03_Notebooks/02_Desarrollo/
# Fase producción: ejecutar 03_Notebooks/03_Sistema/09_Codigo_de_ejecucion.ipynb
```

---

Proyecto académico desarrollado durante el Master en Data Science de Evolve.
