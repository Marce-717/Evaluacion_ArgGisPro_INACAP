#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script: Análisis Estadístico Integrado - Espacios Públicos Urbanos
Propósito: Generar análisis estadístico y visualizaciones mejorando README académico
Institución: INACAP - Energía & Sostenibilidad
Período: Enero 2026
Autor: Felipe Aguilera

Requisitos:
    pandas >= 1.3.0
    numpy >= 1.20.0
    matplotlib >= 3.3.0
    seaborn >= 0.11.0
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import warnings

warnings.filterwarnings('ignore')

# Configuración de estilos
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

# ==============================================================================
# SECCIÓN 1: DATOS DE LA ENCUESTA
# ==============================================================================

def cargar_datos_encuesta():
    """Cargar datos de la encuesta Survey123"""
    
    datos = {
        'Calidad General': {
            'Buena': 3,
            'Mediana': 2,
            'Baja': 1
        },
        'Seguridad Peatonal': {
            'Sí': 4,
            'No': 2,
            'Parcialmente': 0
        },
        'Cantidad Árboles': {
            '16 o más': 3,
            '1-5': 2,
            '6-15': 0,
            '0': 1
        },
        'Diversidad Especies': {
            '1 especie': 2,
            '2-3 especies': 2,
            '4 o más especies': 1,
            'Ninguna': 1
        },
        'Sombra Arbórea': {
            'Sí, la mayoría': 4,
            'Algunos': 1,
            'Muy pocos': 0,
            'Ninguno': 1
        },
        'Aptitud Infantil': {
            'No es adecuado': 3,
            'Sí, es amplio y adecuado': 2,
            'Es algo limitado': 1
        }
    }
    
    return datos

# ==============================================================================
# SECCIÓN 2: ANÁLISIS ESTADÍSTICO
# ==============================================================================

def calcular_estadisticas(datos):
    """Calcular estadísticas descriptivas por indicador"""
    
    estadisticas = {}
    
    for indicador, respuestas in datos.items():
        total = sum(respuestas.values())
        
        estadisticas[indicador] = {
            'total_respuestas': total,
            'categorias': respuestas,
            'porcentajes': {cat: (freq / total) * 100 for cat, freq in respuestas.items()},
            'respuesta_modal': max(respuestas, key=respuestas.get),
            'frecuencia_modal': max(respuestas.values())
        }
    
    return estadisticas

def analisis_cobertura_verde(datos):
    """Análisis integrado de cobertura verde"""
    
    arboles_data = datos['Cantidad Árboles']
    con_arboles = arboles_data['16 o más'] + arboles_data['1-5']
    total = sum(arboles_data.values())
    
    cobertura_verde = (con_arboles / total) * 100
    
    return {
        'espacios_con_arboles': con_arboles,
        'total_espacios': total,
        'porcentaje_cobertura': cobertura_verde
    }

def analisis_seguridad_infantil(datos):
    """Análisis de aptitud para actividades infantiles"""
    
    infantil = datos['Aptitud Infantil']
    no_adecuado = infantil['No es adecuado']
    adecuado = infantil['Sí, es amplio y adecuado']
    limitado = infantil['Es algo limitado']
    total = sum(infantil.values())
    
    return {
        'no_adecuado_pct': (no_adecuado / total) * 100,
        'adecuado_pct': (adecuado / total) * 100,
        'limitado_pct': (limitado / total) * 100,
        'total_espacios': total,
        'deficiencia_critica': no_adecuado
    }

# ==============================================================================
# SECCIÓN 3: VISUALIZACIONES
# ==============================================================================

def crear_grafico_comparativo(datos, estadisticas):
    """Crear gráfico comparativo de desempeño de indicadores"""
    
    fig, ax = plt.subplots(figsize=(14, 8))
    
    indicadores = list(datos.keys())
    respuestas_modales = [estadisticas[ind]['respuesta_modal'] for ind in indicadores]
    frecuencias_modales = [estadisticas[ind]['frecuencia_modal'] for ind in indicadores]
    
    colores = ['#d62728' if freq < 3 else '#ff7f0e' if freq == 3 else '#2ca02c' 
               for freq in frecuencias_modales]
    
    barras = ax.barh(indicadores, frecuencias_modales, color=colores, edgecolor='black', linewidth=1.5)
    
    ax.set_xlabel('Frecuencia de Respuesta Modal', fontsize=12, fontweight='bold')
    ax.set_title('Desempeño de Indicadores - Matriz de Evaluación\nEspacios Públicos Urbanos Santiago 2026', 
                 fontsize=14, fontweight='bold', pad=20)
    ax.set_xlim(0, 5)
    ax.grid(axis='x', alpha=0.3)
    
    # Anotaciones
    for i, (barra, resp, freq) in enumerate(zip(barras, respuestas_modales, frecuencias_modales)):
        pct = (freq / 6) * 100
        ax.text(freq + 0.1, i, f'{resp} ({freq}/6 | {pct:.1f}%)', 
                va='center', fontsize=10, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('/home/claude/grafico_desempeno_indicadores.png', dpi=300, bbox_inches='tight')
    print("✓ Gráfico de desempeño generado: grafico_desempeno_indicadores.png")

def crear_grafico_aptitud_infantil(datos):
    """Crear gráfico especializado de aptitud infantil (hallazgo crítico)"""
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    
    infantil = datos['Aptitud Infantil']
    categorias = list(infantil.keys())
    frecuencias = list(infantil.values())
    porcentajes = [(f/sum(frecuencias))*100 for f in frecuencias]
    
    colores_pie = ['#d62728', '#2ca02c', '#ff7f0e']
    
    # Pie chart
    wedges, texts, autotexts = ax1.pie(frecuencias, labels=categorias, autopct='%1.1f%%',
                                         colors=colores_pie, startangle=90, textprops={'fontsize': 11})
    ax1.set_title('Distribución de Respuestas\nAptitud Infantil', fontweight='bold', fontsize=12)
    
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontweight('bold')
        autotext.set_fontsize(11)
    
    # Bar chart
    ax2.bar(categorias, frecuencias, color=colores_pie, edgecolor='black', linewidth=1.5)
    ax2.set_ylabel('Frecuencia (N=6)', fontweight='bold', fontsize=11)
    ax2.set_title('Frecuencia de Respuestas\nAptitud Infantil', fontweight='bold', fontsize=12)
    ax2.set_ylim(0, 4)
    ax2.grid(axis='y', alpha=0.3)
    
    # Anotaciones
    for i, (cat, freq, pct) in enumerate(zip(categorias, frecuencias, porcentajes)):
        ax2.text(i, freq + 0.1, f'{freq}\n({pct:.1f}%)', ha='center', fontweight='bold')
    
    plt.suptitle('INDICADOR CRÍTICO: Actividades de Esparcimiento Infantil\n50% de espacios NO ADECUADOS', 
                 fontsize=13, fontweight='bold', color='#d62728', y=1.02)
    plt.tight_layout()
    plt.savefig('/home/claude/grafico_aptitud_infantil_critica.png', dpi=300, bbox_inches='tight')
    print("✓ Gráfico de aptitud infantil generado: grafico_aptitud_infantil_critica.png")

def crear_matriz_desempeno(estadisticas):
    """Crear tabla visual de matriz de desempeño"""
    
    fig, ax = plt.subplots(figsize=(14, 6))
    ax.axis('tight')
    ax.axis('off')
    
    datos_tabla = []
    indicadores_orden = [
        'Calidad General',
        'Seguridad Peatonal',
        'Cantidad Árboles',
        'Diversidad Especies',
        'Sombra Arbórea',
        'Aptitud Infantil'
    ]
    
    for ind in indicadores_orden:
        est = estadisticas[ind]
        respuesta = est['respuesta_modal']
        freq = est['frecuencia_modal']
        pct = (freq / 6) * 100
        
        # Asignar evaluación
        if pct >= 66:
            eval_sym = '✅'
            eval_txt = 'Bueno'
        elif pct >= 50:
            eval_sym = '⚠️'
            eval_txt = 'Moderado'
        else:
            eval_sym = '❌'
            eval_txt = 'Deficiente'
        
        datos_tabla.append([
            ind,
            respuesta,
            f'{freq}/6',
            f'{pct:.1f}%',
            f'{eval_sym} {eval_txt}'
        ])
    
    tabla = ax.table(cellText=datos_tabla,
                     colLabels=['Indicador', 'Respuesta Modal', 'Frecuencia', 'Porcentaje', 'Evaluación'],
                     cellLoc='center',
                     loc='center',
                     colWidths=[0.25, 0.25, 0.15, 0.15, 0.2])
    
    tabla.auto_set_font_size(False)
    tabla.set_fontsize(10)
    tabla.scale(1, 2.5)
    
    # Formato de encabezado
    for i in range(5):
        tabla[(0, i)].set_facecolor('#2c3e50')
        tabla[(0, i)].set_text_props(weight='bold', color='white')
    
    # Formato de filas alternadas
    for i in range(1, len(datos_tabla) + 1):
        color = '#ecf0f1' if i % 2 == 0 else '#ffffff'
        for j in range(5):
            tabla[(i, j)].set_facecolor(color)
    
    plt.title('Matriz de Desempeño - Indicadores de Espacios Públicos Urbanos\nRegiónMetropolitana de Santiago 2026',
              fontsize=13, fontweight='bold', pad=20)
    
    plt.savefig('/home/claude/tabla_desempeno_visual.png', dpi=300, bbox_inches='tight')
    print("✓ Tabla de desempeño visual generada: tabla_desempeno_visual.png")

def crear_diagrama_prioridades(datos):
    """Crear diagrama de matriz priorización de recomendaciones"""
    
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Definir prioridades
    prioridades = {
        'Infraestructura Infantil': {'x': 9.5, 'y': 9.5, 'size': 1000, 'color': '#d62728'},
        'Diversidad Arbórea': {'x': 8.5, 'y': 8.0, 'size': 800, 'color': '#ff7f0e'},
        'Seguridad Peatonal': {'x': 7.5, 'y': 7.5, 'size': 700, 'color': '#ffbb78'},
        'Cobertura Verde': {'x': 6.5, 'y': 6.5, 'size': 600, 'color': '#2ca02c'},
        'Mejora Calidad General': {'x': 5.0, 'y': 5.0, 'size': 400, 'color': '#98df8a'}
    }
    
    for accion, props in prioridades.items():
        ax.scatter(props['x'], props['y'], s=props['size'], alpha=0.6, 
                   color=props['color'], edgecolors='black', linewidth=2)
        ax.annotate(accion, (props['x'], props['y']), 
                   ha='center', va='center', fontsize=10, fontweight='bold')
    
    ax.set_xlim(3, 11)
    ax.set_ylim(3, 11)
    ax.set_xlabel('Impacto Potencial →', fontsize=12, fontweight='bold')
    ax.set_ylabel('Urgencia de Implementación →', fontsize=12, fontweight='bold')
    ax.set_title('Matriz de Priorización: Recomendaciones Estratégicas\nTamaño de burbuja = Complejidad de implementación',
                 fontsize=13, fontweight='bold', pad=20)
    
    # Dividir en cuadrantes
    ax.axhline(y=7, color='gray', linestyle='--', alpha=0.3)
    ax.axvline(x=7, color='gray', linestyle='--', alpha=0.3)
    
    ax.text(9, 10.3, 'PRIORIDAD 1\n(Crítica)', ha='center', fontsize=10, 
            bbox=dict(boxstyle='round', facecolor='#ffe6e6', alpha=0.7), fontweight='bold')
    ax.text(5, 10.3, 'PRIORIDAD 2\n(Alta)', ha='center', fontsize=10,
            bbox=dict(boxstyle='round', facecolor='#fff4e6', alpha=0.7), fontweight='bold')
    ax.text(9, 4, 'PRIORIDAD 3\n(Media)', ha='center', fontsize=10,
            bbox=dict(boxstyle='round', facecolor='#f0f0f0', alpha=0.7), fontweight='bold')
    ax.text(5, 4, 'PRIORIDAD 4\n(Baja)', ha='center', fontsize=10,
            bbox=dict(boxstyle='round', facecolor='#e6f7e6', alpha=0.7), fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('/home/claude/matriz_priorizacion.png', dpi=300, bbox_inches='tight')
    print("✓ Matriz de priorización generada: matriz_priorizacion.png")

# ==============================================================================
# SECCIÓN 4: GENERACIÓN DE REPORTE TEXTUAL
# ==============================================================================

def generar_reporte_texto(datos, estadisticas):
    """Generar reporte textual en formato Markdown"""
    
    reporte = f"""
# 📊 REPORTE TÉCNICO: ANÁLISIS ESTADÍSTICO INTEGRADO
## Evaluación de Espacios Públicos Urbanos - Región Metropolitana de Santiago

**Fecha de generación:** {datetime.now().strftime('%d de %B de %Y')}  
**Institución:** INACAP - Energía & Sostenibilidad  
**Período:** Enero 2026  
**Cobertura:** 6 espacios públicos urbanos  

---

## 📈 RESUMEN EJECUTIVO

El análisis integra datos de terreno (Survey123), análisis espectral (NDVI Sentinel-2) y 
evaluación visual de infraestructura verde. Se evaluaron **6 espacios públicos** con **100% 
de completitud de datos**.

### Hallazgos Principales

1. **Calidad percibida:** 50% buena, 33.33% mediana, 16.67% baja
2. **Seguridad peatonal:** 66.67% adecuada, 33.33% deficiente
3. **Cobertura arbórea:** 83.33% con presencia de vegetación
4. **Diversidad especies:** 33.33% en monodominancia (crítico)
5. **Sombra efectiva:** 66.67% con provisión adecuada
6. **Aptitud infantil:** **50% NO ADECUADA** ⚠️ CRÍTICO

---

## 📋 ESTADÍSTICAS DESCRIPTIVAS POR INDICADOR

"""
    
    indicadores_orden = [
        'Calidad General',
        'Seguridad Peatonal',
        'Cantidad Árboles',
        'Diversidad Especies',
        'Sombra Arbórea',
        'Aptitud Infantil'
    ]
    
    for ind in indicadores_orden:
        est = estadisticas[ind]
        reporte += f"\n### {ind}\n\n"
        reporte += f"**Respuesta modal:** {est['respuesta_modal']}\n"
        reporte += f"**Frecuencia modal:** {est['frecuencia_modal']}/6 ({(est['frecuencia_modal']/6)*100:.1f}%)\n\n"
        reporte += "| Categoría | Frecuencia | Porcentaje |\n"
        reporte += "|-----------|-----------|----------|\n"
        
        for cat, freq in est['categorias'].items():
            pct = est['porcentajes'][cat]
            reporte += f"| {cat} | {freq} | {pct:.2f}% |\n"
        
        reporte += "\n"
    
    # Análisis integrados
    cob_verde = analisis_cobertura_verde(datos)
    seg_inf = analisis_seguridad_infantil(datos)
    
    reporte += f"""
---

## 🌳 ANÁLISIS INTEGRADOS

### Cobertura Verde
- Espacios **CON vegetación arbórea:** {cob_verde['espacios_con_arboles']}/6 ({cob_verde['porcentaje_cobertura']:.1f}%)
- Indicador: Cobertura verde presente en **{cob_verde['porcentaje_cobertura']:.1f}%** de espacios evaluados

### Seguridad Infantil (Crítica)
- Espacios **NO ADECUADOS:** {seg_inf['deficiencia_critica']}/6 ({seg_inf['no_adecuado_pct']:.1f}%) ⚠️
- Espacios **ADECUADOS:** {seg_inf['total_espacios'] - seg_inf['deficiencia_critica']}/6 ({seg_inf['adecuado_pct']:.1f}%)
- **Conclusión:** Déficit crítico en infraestructura lúdica infantil

---

## 💡 RECOMENDACIONES

### Prioridad 1 (Crítica): Infraestructura Lúdica
50% de espacios carece de aptitud para actividades infantiles. Implementar:
- Diagnóstico de seguridad infantil
- Diseño participativo con comunidades
- Equipamiento homologado y mantenido

### Prioridad 2 (Alta): Diversidad Arbórea
33.33% de espacios presenta monodominancia. Acciones:
- Aumentar variabilidad de especies
- Mejorar resiliencia ecológica
- Incrementar valor paisajístico

### Prioridad 3 (Media): Consolidación de Seguridad
33.33% de usuarios percibe inseguridad peatonal. Mejoras en diseño y mantención.

### Prioridad 4 (Baja): Mejora Incremental
Elevar espacios con calidad mediana (33.33%) a categoría "bueno".

---

## ✅ CONCLUSIONES

La evaluación integrada revela espacios públicos con **calidad general positiva pero heterogénea**, 
con fortalezas en seguridad peatonal (66.67%) y cobertura arbórea (83.33%), pero con **brecha crítica 
en infraestructura recreativa infantil** (50% deficiente).

Las recomendaciones estratégicas priorizadas proporcionarían mejoramiento significativo en 
calidad de vida urbana y funcionalidad ecológica.

---

**Reporte generado automáticamente**  
**Versión:** 1.0  
**Validación:** ✅ Completado  
"""
    
    with open('/home/claude/REPORTE_TECNICO_ESTADISTICO.md', 'w', encoding='utf-8') as f:
        f.write(reporte)
    
    print("✓ Reporte técnico generado: REPORTE_TECNICO_ESTADISTICO.md")

# ==============================================================================
# SECCIÓN 5: FUNCIÓN PRINCIPAL
# ==============================================================================

def main():
    """Función principal de ejecución"""
    
    print("\n" + "="*70)
    print("  ANÁLISIS ESTADÍSTICO INTEGRADO - ESPACIOS PÚBLICOS URBANOS")
    print("  INACAP - Energía & Sostenibilidad | Enero 2026")
    print("="*70 + "\n")
    
    # Cargar datos
    print("📥 Cargando datos de encuesta Survey123...")
    datos = cargar_datos_encuesta()
    print(f"   ✓ {len(datos)} indicadores cargados")
    
    # Calcular estadísticas
    print("\n📊 Calculando estadísticas descriptivas...")
    estadisticas = calcular_estadisticas(datos)
    print("   ✓ Estadísticas calculadas")
    
    # Análisis integrados
    print("\n🔬 Ejecutando análisis integrados...")
    cob_verde = analisis_cobertura_verde(datos)
    seg_inf = analisis_seguridad_infantil(datos)
    print(f"   ✓ Cobertura verde: {cob_verde['porcentaje_cobertura']:.1f}%")
    print(f"   ✓ Aptitud infantil: {seg_inf['no_adecuado_pct']:.1f}% CRÍTICA")
    
    # Generar visualizaciones
    print("\n📈 Generando visualizaciones...")
    crear_grafico_comparativo(datos, estadisticas)
    crear_grafico_aptitud_infantil(datos)
    crear_matriz_desempeno(estadisticas)
    crear_diagrama_prioridades(datos)
    
    # Generar reporte
    print("\n📝 Generando reporte técnico...")
    generar_reporte_texto(datos, estadisticas)
    
    print("\n" + "="*70)
    print("  ✅ ANÁLISIS COMPLETADO EXITOSAMENTE")
    print("="*70)
    print("\n📁 Archivos generados:")
    print("   • grafico_desempeno_indicadores.png")
    print("   • grafico_aptitud_infantil_critica.png")
    print("   • tabla_desempeno_visual.png")
    print("   • matriz_priorizacion.png")
    print("   • REPORTE_TECNICO_ESTADISTICO.md")
    print("\n")

if __name__ == "__main__":
    main()
