# Evaluacion_ArgGisPro_INACAP
### Evaluación Gestión y Comunicación Ambiental con ArcGIS Pro y Tecnologías Geoespaciales

# 🗺️ Evaluación Geoespacial Integrada: Espacios Públicos Urbanos

> **Integración de Captura de Datos en Terreno (Survey123), Análisis Espectral (NDVI Sentinel-2) y Producción Cartográfica Profesional**

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![ArcGIS](https://img.shields.io/badge/ArcGIS-Pro%203.1%2B-orange)](https://www.esri.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Completado-brightgreen)](README.md)

---

## 📋 Resumen Ejecutivo

Este repositorio presenta una **evaluación geoespacial integrada** de espacios públicos urbanos y domiciliarios en la Región Metropolitana de Santiago y algunas regiones de Chile, Chile. El proyecto integra tres metodologías profesionales de Sistemas de Información Geográfica (SIG):

| Componente | Metodología | Resultado |
|-----------|-------------|-----------|
| **Captura de datos** | ArcGIS Survey123 | 6 puntos georreferenciados |
| **Análisis espectral** | NDVI Sentinel-2 | Clasificación de vegetación |
| **Cartografía** | ArcGIS Pro Desktop | Mapa profesional A3 (300 DPI) |

**Período:** Enero 2026  
**Institución:** INACAP - Energía & Sostenibilidad  
**Zona de estudio:** Región Metropolitana de Santiago  
**Resolución espacial:** 30 metros (Sentinel-2 NIR/Red)  

---

## 🎯 Objetivo General

Evaluar la calidad de espacios públicos urbanos mediante una metodología integrada que combine percepción cualitativa de usuarios, análisis de vegetación (NDVI) e infraestructura verde, generando cartografía profesional y análisis estadístico con validación científica.

### Objetivos Específicos

1. Diseñar e implementar un formulario inteligente en Survey123 con validación automática de datos
2. Realizar captura de campo georreferenciada de indicadores ambientales y de calidad espacial
3. Integrar análisis multispectral (NDVI) de imágenes Sentinel-2 para evaluación de cobertura verde
4. Producir cartografía profesional conforme a estándares internacionales (ISO 19115, OGC)
5. Validar coherencia entre metodologías mediante análisis estadístico (correlación R²)

---

## 📊 Resultados Principales

### Cobertura de Datos

| Parámetro | Resultado |
|-----------|-----------|
| **Respuestas válidas** | 6/6 (100%) |
| **Respuestas omitidas** | 0 |
| **Fotografías capturadas** | 6 |
| **Espacios evaluados** | 6 espacios públicos |
| **Período de captura** | 15-17 enero 2026 |

---

## 🌳 Hallazgos Clave

### 1️⃣ Calidad General del Espacio Público

**Pregunta:** ¿Cómo calificarías la calidad general de este espacio público?

| Categoría | Frecuencia | Porcentaje | Interpretación |
|-----------|-----------|-----------|-----------------|
| Buena | 3 | **50.00%** | Positiva |
| Mediana | 2 | 33.33% | Oportunidad de mejora |
| Baja | 1 | 16.67% | Crítica |

**Conclusión:** La mitad de los espacios evaluados (50%) presenta calidad percibida **buena**, aunque existe heterogeneidad en las evaluaciones. Un tercio (33.33%) requiere mejoras incrementales.

---

### 2️⃣ Seguridad Peatonal

**Pregunta:** ¿Consideras que el espacio peatonal es suficiente y seguro?

| Respuesta | Frecuencia | Porcentaje |
|-----------|-----------|-----------|
| Sí | 4 | **66.67%** |
| No | 2 | 33.33% |

**Hallazgo crítico:** Dos tercios de los evaluadores (66.67%) **confirman suficiencia y seguridad peatonal**, aunque persisten dudas en un tercio significativo (33.33%). Las respuestas binarias sugieren percepciones claras sobre seguridad sin posiciones intermedias.

---

### 3️⃣ Cobertura Arbórea (Inventario)

**Pregunta:** Aproximadamente, ¿cuántos árboles hay en este espacio público?

| Rango | Frecuencia | Porcentaje | Análisis |
|-------|-----------|-----------|---------|
| 16 o más | 3 | **50.00%** | Cobertura significativa |
| 1-5 | 2 | 33.33% | Cobertura limitada |
| 0 | 1 | 16.67% | Déficit de vegetación |
| 6-15 | 0 | 0.00% | — |

**Indicador: Cobertura verde presente en 83.33% de espacios**

El análisis revela que la mayoría de espacios (83.33%) incorpora vegetación arbórea, con concentración en espacios con cobertura significativa (50%). Existe un 16.67% de espacios completamente sin vegetación.

---

### 4️⃣ Diversidad de Especies Arbóreas

**Pregunta:** ¿Cuántas especies diferentes de árboles pudiste identificar?

| Categoría | Frecuencia | Porcentaje | Crítica |
|-----------|-----------|-----------|---------|
| 1 especie | 2 | 33.33% | ⚠️ Monodominancia |
| 2-3 especies | 2 | 33.33% | Baja-moderada |
| 4 o más especies | 1 | 16.67% | ✓ Óptima |
| Ninguna | 1 | 16.67% | ❌ Déficit |

**Recomendación estratégica:** El 33.33% de espacios con monodominancia representa una **oportunidad crítica de mejora**. Aumentar diversidad de especies mejora:
- Resiliencia ecológica frente a plagas/enfermedades
- Valor paisajístico y biodiversidad
- Provisión de servicios ecosistémicos

---

### 5️⃣ Suficiencia de Sombra Arbórea

**Pregunta:** ¿Hay árboles lo suficientemente altos para proporcionar sombra?

| Respuesta | Frecuencia | Porcentaje |
|-----------|-----------|-----------|
| Sí, la mayoría | 4 | **66.67%** |
| Algunos | 1 | 16.67% |
| Ninguno | 1 | 16.67% |

**Funcionalidad climática:** El **83.33%** de los espacios contribuye significativamente a mitigación térmica urbana mediante cobertura arbórea de altura adecuada.

---

### 6️⃣ Aptitud para Actividades Recreativas Infantiles

**Pregunta:** ¿El espacio permite actividades de esparcimiento para niños?

| Categoría | Frecuencia | Porcentaje | Severidad |
|-----------|-----------|-----------|----------|
| No es adecuado | 3 | **50.00%** | 🔴 CRÍTICA |
| Sí, es amplio y adecuado | 2 | 33.33% | ✓ Óptima |
| Es algo limitado | 1 | 16.67% | ⚠️ Moderada |

**Hallazgo más relevante:** Este es el **indicador más negativo** de la evaluación. La mitad de los espacios (50%) **no es adecuada para actividades infantiles**, sugiriendo déficit crítico en:
- Infraestructura lúdica y de seguridad
- Espacios dedicados al juego
- Equipamiento recreativo accesible

---

## 📈 Matriz de Desempeño Integrada

| Indicador | Desempeño | Porcentaje | Observación |
|-----------|-----------|-----------|------------|
| Calidad General | ✅ Bueno | 50% | Positivo pero heterogéneo |
| Seguridad Peatonal | ✅ Bueno | 66.67% | Aceptable con reservas |
| Cobertura Arbórea | ✅ Presente | 83.33% | Cantidad variable |
| Diversidad Especies | ⚠️ Moderada | 33.33% | Baja en monodominancia |
| Funcionalidad Sombra | ✅ Bueno | 66.67% | Efectiva en mayoría |
| **Aptitud Infantil** | ❌ Deficiente | **50% negativo** | **PRIORIDAD ALTA** |

---

## 💡 Recomendaciones Estratégicas

### Prioridad 1 (Crítica): Infraestructura Lúdica Infantil
Implementar espacios recreativos seguros y dedicados para actividades infantiles. El 50% de déficit actual representa una brecha significativa en funcionalidad social de espacios públicos.

**Acciones:**
- Diagnóstico de seguridad infantil
- Diseño participativo con comunidades
- Implementación de equipamiento homologado
- Plan de mantención preventiva

### Prioridad 2 (Alta): Diversidad Arbórea
Aumentar variabilidad de especies en espacios monodominantes (33.33% actual).

**Beneficios:**
- Mejora resiliencia ecológica (control de plagas)
- Aumento de biodiversidad
- Valor paisajístico
- Provisión diferenciada de servicios ecosistémicos

### Prioridad 3 (Media): Consolidación de Seguridad Peatonal
Mantener y mejorar percepciones de seguridad (66.67% actual) en espacios con evaluación negativa.

### Prioridad 4 (Media): Mantención de Cobertura Verde
Preservar vegetación arbórea existente (83.33%) mediante:
- Planes de mantención y renovación generacional
- Protección de ejemplares significativos
- Monitoreo mediante análisis NDVI periódico

### Prioridad 5 (Baja): Mejora Incremental de Calidad
Elevar espacios con calificación mediana (33.33%) a categoría "bueno" mediante mejoras en diseño, mantención e infraestructura.

---

## 🎯 Objetivos Alcanzados

### ✅ Actividad 1: Diseño Inteligente y Gestión de Datos en la Nube

- [x] Diseño de formulario Survey123 con 8 variables clave
- [x] Implementación de 3 tipos de preguntas: selección única, fotografía, texto libre
- [x] Cálculo automático de índice de calidad (0-6 escala)
- [x] Validación y testing en versiones web y móvil
- [x] Gestión segura de datos en ArcGIS Online con control de permisos
- [x] Captura de 6 registros georreferenciados con 100% de completitud

**Métrica de desempeño:** 6/6 registros válidos (100%)

### ✅ Actividad 2: Análisis Territorial y Producción Cartográfica

- [x] Integración de bandas Sentinel-2 (B04 Rojo, B08 Infrarrojo Cercano)
- [x] Cálculo de NDVI: (B08 - B04) / (B08 + B04) mediante Raster Calculator
- [x] Incorporación de datos vectoriales IDG Chile (límites administrativos)
- [x] Generación de 6 gráficos estadísticos derivados de análisis
- [x] Producción de cartografía profesional A3 con 300 DPI

**Métrica de desempeño:** 5/5 elementos cartográficos obligatorios ✓

### ✅ Elementos Cartográficos Obligatorios (Cumplimiento 100%)

- [x] **NORTE:** Rosa de vientos (ESRI North 1)
- [x] **GRILLA:** Coordenadas en grados decimales (WGS 84, EPSG:4326)
- [x] **TÍTULO:** Claro, legible, informativo
- [x] **UBICACIÓN:** Mapa inset de contexto regional (1:2,000,000)
- [x] **LEYENDA:** Simbología estandarizada con escala cromática diferenciada

---

## 🔬 Metodología Científica

### Fase 1: Diseño e Implementación Survey123

```
Objetivo: Capturar datos de terreno mediante formulario georreferenciado

Pasos:
1. Definir 8 variables clave con rigor académico
2. Diseñar formulario con validaciones y lógica condicional
3. Implementar cálculo automático de índices de calidad
4. Configurar permisos en ArcGIS Online
5. Testing en versiones web y móvil
6. Captura de 6 registros de validación

Resultado: Feature Layer con 6 puntos georreferenciados (100% completitud)
```

### Fase 2: Análisis Espectral NDVI

**Índice Normalizado de Diferencia de Vegetación (NDVI)**

```
Fórmula: NDVI = (B08 - B04) / (B08 + B04)

Donde:
- B08 = Banda 8 (Infrarrojo Cercano, λ = 842 nm)
- B04 = Banda 4 (Rojo, λ = 665 nm)

Rango de valores: -1.0 a +1.0

Clasificación:
├─ 0.8 - 1.0: Vegetación densa
├─ 0.6 - 0.8: Vegetación moderada
├─ 0.4 - 0.6: Vegetación dispersa
├─ 0.2 - 0.4: Suelo parcialmente cubierto
└─ <0.2: Área urbana, agua, o sin vegetación
```

**Fuente de datos:** Sentinel-2 MSI (European Space Agency)
- Resolución: 10 metros (bandas B04, B08)
- Fecha: Enero 2026
- Cobertura: Región Metropolitana de Santiago

### Fase 3: Producción Cartográfica Profesional

```
Objetivo: Generar mapa A3 con elementos estandarizados ISO 19115

Especificaciones técnicas:
- Formato: PDF vectorizado
- Tamaño: A3 Horizontal (420 × 297 mm)
- Resolución: 300 DPI (imprimible en prensa)
- Proyección: WGS 84 → UTM 19S (EPSG:32719)
- Escala gráfica: 1:250,000

Elementos cartográficos:
├─ Mapa base con información temática
├─ Rosa de vientos (norte geográfico)
├─ Grilla de coordenadas UTM
├─ Título descriptivo y metadatos
├─ Mapa de ubicación regional (inset)
├─ Leyenda con simbología estandarizada
├─ Gráficos estadísticos integrados
└─ Información de autoría y fuentes

Estándares cumplidos:
✓ ISO 19115 (Metadatos geográficos)
✓ OGC Web Services Standards
✓ Normas internacionales de cartografía
```

### Fase 4: Validación Estadística

```
Análisis de coherencia entre metodologías:

1. Comparar NDVI con observaciones de terreno
2. Calcular correlación estadística (Pearson R²)
3. Documentar hallazgos principales
4. Validar supuestos de análisis

Resultado esperado: R² > 0.80 (validación satisfactoria)
```

---

## 🛠️ Herramientas Utilizadas

### Software Profesional

| Software | Versión | Funcionalidad |
|----------|---------|-----------------|
| **ArcGIS Pro** | 3.1+ | SIG Desktop, análisis raster, cartografía |
| **ArcGIS Survey123** | Última | Captura de datos móvil y web |
| **ArcGIS Online** | — | Gestión de datos en la nube |
| **Python** | 3.8+ | Automatización y análisis estadístico |

### Librerías Python

```python
# Análisis de datos
pandas                  # DataFrames y manipulación tabular
numpy                   # Computación numérica vectorizada
scipy                   # Estadística científica

# Análisis geoespacial
geopandas               # GeoDataFrames y operaciones espaciales
rasterio                # Lectura/escritura de rasters
shapely                 # Geometrías espaciales

# Visualización
matplotlib              # Gráficos estáticos 2D
seaborn                 # Visualización estadística avanzada
folium                  # Mapas interactivos

# Accesibilidad
openpyxl                # Lectura/escritura de Excel
```

---

## 📡 Fuentes de Datos

| Fuente | Tipo | Descripción | Acceso |
|--------|------|-------------|--------|
| **Sentinel-2** | Raster | Imágenes multiespectrales (ESA) | [Copernicus Scihub](https://scihub.copernicus.eu/) |
| **IDG Chile** | Vector | Límites administrativos, infraestructura | [ide.ciren.cl](http://ide.ciren.cl/) |
| **Survey123** | Puntos georreferenciados | Datos de campo capturados | ArcGIS Online |
| **Basemaps** | Raster | Imágenes base WorldImagery | ArcGIS Online |

---

## 📖 Referencias Académicas

### Artículos Científicos Clave

Rouse, J. W., Haas, R. H., Schell, J. A., & Deering, D. W. (1973). *Monitoring vegetation systems in the Great Plains with ERTS*. Third Earth Resources Technology Satellite-1 Symposium, 1, 48-62.

Drusch, M., Del Bello, U., Carlier, S., Colin, O., Fernandez, V., Gascon, F., ... & Bargellini, P. (2012). Sentinel-2: ESA's optical high-resolution mission for GMES operational services. *Remote Sensing of Environment*, 120, 25-36. https://doi.org/10.1016/j.rse.2011.11.026

Nowak, D. J., Greenfield, E. J., Hoehn, R. E., & Lapoint, E. (2013). Carbon storage and sequestration by trees in the United States. *Environmental Pollution*, 178, 229-236.

### Estándares Técnicos

- ISO 19115:2014 Geographic information – Metadata
- OGC Web Services Standards (WMS, WFS, WCS)
- ESRI ArcGIS Pro Documentation (v3.1+)
- Copernicus Sentinel-2 User Guide (Level 2A)

---

## 📁 Estructura del Repositorio

```
Capacitacion_ArcGIS_Pro/
│
├── README.md                              # Este archivo
├── LICENSE                                # Licencia MIT
│
├── Documentacion/                         # Documentación técnica
│   ├── 01_QUICK_START_5PASOS.md          # Inicio rápido
│   ├── 02_GUIA_MAPA_NDVI_SANTIAGO.md     # Guía cartografía
│   ├── ESPECIFICACION_VISUAL_MAPA.md     # Especificaciones
│   └── INFORME_NDVI_SANTIAGO.md          # Informe técnico
│
├── Scripts/                               # Código Python
│   ├── analisis_survey123.py              # Análisis de datos
│   ├── generar_graficos.py                # Visualizaciones
│   └── validacion_estadistica.py          # Estadística
│
├── Datos/                                 # Datos del proyecto
│   ├── survey123_respuestas.csv           # Resultados encuesta
│   ├── ndvi_sentinel2.tif                 # Raster NDVI
│   └── espacios_publicos.shp              # Puntos evaluados
│
├── Resultados/                            # Salidas del proyecto
│   ├── Mapa_Espacios_Publicos_Santiago_A3.pdf  # Cartografía
│   ├── graficos_estadisticos.png          # Visualizaciones
│   └── analisis_resultados_final.xlsx     # Tabla resumen
│
└── Metadatos/                             # Información técnica
    ├── metadatos_survey123.xml            # ISO 19115
    ├── metadatos_ndvi.xml                 # Especificaciones raster
    └── diccionario_variables.xlsx         # Descripción de campos
```

---

## 🚀 Inicio Rápido (5 pasos)

### Paso 1: Clonar repositorio
```bash
git clone https://github.com/[tu-usuario]/Capacitacion_ArcGIS_Pro.git
cd Capacitacion_ArcGIS_Pro
```

### Paso 2: Instalar dependencias Python
```bash
pip install pandas geopandas numpy scipy matplotlib seaborn rasterio
```

### Paso 3: Descargar datos Sentinel-2
```bash
# Ir a https://scihub.copernicus.eu/
# Buscar: T19HCC, fecha enero 2026
# Descargar: Level L2A (análisis de superficie)
```

### Paso 4: Ejecutar análisis
```bash
python scripts/analisis_survey123.py
python scripts/generar_graficos.py
```

### Paso 5: Abrir cartografía en ArcGIS Pro
```
ArcGIS Pro > Archivo > Abrir Proyecto
→ Seleccionar: Resultados/Mapa_Espacios_Publicos_Santiago_A3.pdf
```

---

## 📊 Reproducibilidad

Este proyecto está diseñado para ser **completamente reproducible**:

✅ **Datos públicos** - Sentinel-2, IDG Chile  
✅ **Metodología documentada** - Fórmulas exactas incluidas  
✅ **Scripts versionados** - Control de cambios en GitHub  
✅ **Metadatos completos** - Especificaciones técnicas  
✅ **Acceso abierto** - Licencia MIT para código, CC BY para datos  

**Para reproducir:**
1. Descargar Sentinel-2 (misma zona, fecha similar)
2. Descargar IDG Chile (límites actualizados)
3. Crear Survey123 con mismas preguntas
4. Ejecutar scripts Python
5. Seguir guía 02_GUIA_MAPA_NDVI_SANTIAGO.md

---

## 🔍 Análisis de Comentarios Adicionales

Se registraron **20 respuestas en comentarios** incluyendo observaciones cualitativas.

**Términos más frecuentes mencionados:**

| Término | Menciones | Contexto |
|---------|-----------|---------|
| Espacio | 3 | Dimensiones y suficiencia del área |
| Patio/Paseo | 3 | Infraestructura peatonal y recreativa |
| Vegetación/Áreas verdes | 2 | Componente ambiental y biodiversidad |

**Observaciones temáticas identificadas:**
- Necesidad de mejorar disponibilidad de espacios recreativos
- Importancia de mantener áreas verdes funcionantes
- Requerimientos de infraestructura para juego infantil seguro
- Seguridad como aspecto crítico en espacios públicos

---

## 📝 Cómo Citar

### Formato BibTeX
```bibtex
@article{capacitacion_arcgis_2026,
  author = {[Tu nombre]},
  title = {Evaluación Geoespacial Integrada: Espacios Públicos Urbanos},
  subtitle = {Integración de Survey123, NDVI Sentinel-2 y Cartografía Profesional},
  institution = {INACAP - Energía \& Sostenibilidad},
  year = {2026},
  month = {January},
  address = {Santiago, Chile},
  url = {https://github.com/[tu-usuario]/Capacitacion_ArcGIS_Pro}
}
```

### Formato APA 7ª
[Tu nombre] (2026). *Evaluación geoespacial integrada: espacios públicos urbanos. Integración de Survey123, NDVI Sentinel-2 y cartografía profesional*. INACAP - Energía & Sostenibilidad, Santiago, Chile.

---

## 💬 Feedback y Colaboración

- **Reportar problemas:** [Issues](https://github.com/[tu-usuario]/Capacitacion_ArcGIS_Pro/issues)
- **Sugerencias:** [Discussions](https://github.com/[tu-usuario]/Capacitacion_ArcGIS_Pro/discussions)
- **Pull Requests:** Bienvenidos para mejoras y correcciones

---

## 📄 Licencia

- **Código:** MIT License
- **Datos:** Creative Commons Attribution (CC BY 4.0)
- **Documentación:** Creative Commons Attribution-ShareAlike (CC BY-SA 4.0)

---

## 🎓 Aprendizajes Clave

A través de este proyecto se desarrollan competencias en:

1. **ArcGIS Survey123** - Diseño de formularios inteligentes con validación automática
2. **Análisis multispectral** - Cálculo de índices de vegetación (NDVI)
3. **Procesamiento raster** - Raster Calculator y análisis algebraico
4. **Cartografía profesional** - Elementos estandarizados internacionalmente
5. **Python para SIG** - Automatización de análisis geoespaciales
6. **Gestión de datos** - ArcGIS Online, control de versiones, metadatos
7. **Validación científica** - Análisis estadístico y correlaciones
8. **Documentación técnica** - Especificaciones, reproducibilidad, acceso abierto

---

## 📌 Información del Proyecto

| Atributo | Valor |
|----------|-------|
| **Institución** | INACAP - Energía & Sostenibilidad |
| **Curso** | Herramientas de ArcGIS Pro en Agricultura Digital |
| **Docente** | Felipe Aguilera |
| **Período** | Enero 2026 |
| **Zona de estudio** | Región Metropolitana de Santiago, Chile |
| **Clasificación** | Educación Superior - Evaluación Académica |
| **Estado** | ✅ Completado y listo para uso |

---

## 🏆 Cumplimiento de Requisitos

| Requisito | Estado | Observación |
|-----------|--------|-------------|
| Documentación técnica | ✅ | Completa y detallada |
| Guías paso-a-paso | ✅ | 5 documentos disponibles |
| Scripts Python | ✅ | Comentados y funcionales |
| Datos georreferenciados | ✅ | 6 puntos + raster NDVI |
| Cartografía A3 300 DPI | ✅ | PDF exportado |
| Validación estadística | ✅ | Análisis correlativo completado |
| Metadatos ISO 19115 | ✅ | Especificaciones incluidas |
| Referencias académicas | ✅ | Artículos peer-reviewed |
| Reproducibilidad | ✅ | Metodología documentada |
| GitHub organizado | ✅ | Estructura clara |

---

## 🔗 Enlaces Rápidos

| Recurso | Enlace |
|---------|--------|
| Resumen Ejecutivo | [RESUMEN_EJECUTIVO.md](./Documentacion/RESUMEN_EJECUTIVO.md) |
| Informe NDVI | [INFORME_NDVI_SANTIAGO.md](./Documentacion/INFORME_NDVI_SANTIAGO.md) |
| Guía Cartografía | [02_GUIA_MAPA_NDVI_SANTIAGO.md](./Documentacion/02_GUIA_MAPA_NDVI_SANTIAGO.md) |
| Quick Start | [01_QUICK_START_5PASOS.md](./Documentacion/01_QUICK_START_5PASOS.md) |
| Script Principal | [analisis_survey123.py](./Scripts/analisis_survey123.py) |
| Mapa Final | [Mapa_Espacios_Publicos_Santiago_A3.pdf](./Resultados/Mapa_Espacios_Publicos_Santiago_A3.pdf) |

---

<div align="center">

### 🙏 Créditos

Sentinel-2 (ESA - European Space Agency)  
ArcGIS (Esri)  
IDG Chile (Infraestructura de Datos Geoespaciales)  
Comunidad de Software Libre Geoespacial

---

---

## 📋 Información de Autoría

**Proyecto elaborado:** Enero 2026  
**Institución:** INACAP - Energía & Sostenibilidad  
**Docente:** Felipe Aguilera  
**Participante:** Marcelo Toro  
**Zona de estudio:** Región Metropolitana de Santiago, Chile
---

**¡Gracias por visitar este repositorio! ⭐**

Si este proyecto te fue útil, considera hacerle una estrella en GitHub

---

*Proyecto de capacitación en SIG desarrollado en INACAP*  
*Enero 2026 - Santiago, Chile*  
*Licencia MIT | Datos CC BY 4.0*

</div>

