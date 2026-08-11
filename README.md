# Calculadora de Diluciones de Laboratorio ($C_1V_1 = C_2V_2$)

Herramienta en línea de comandos/script para calcular de forma rápida y precisa los parámetros faltantes en diluciones químicas y biológicas a partir de una solución madre.

---

## El problema

En los laboratorios, calcular manualmente las concentraciones o los volúmenes necesarios para preparar soluciones puede llevar a errores humanos de transcripción o de cálculo. Esta herramienta automatiza la resolución de la fórmula de dilución, permitiendo obtener de forma instantánea cualquier variable desconocida ($C_1$, $V_1$, $C_2$ o $V_2$) a partir de los tres datos conocidos.

---

## Cómo funciona

La aplicación utiliza la ecuación de conservación de masa para soluciones idealizadas:

$$C_1 \cdot V_1 = C_2 \cdot V_2$$

Donde $C_1$ y $V_1$ son la concentración y el volumen de la solución madre, y $C_2$ y $V_2$ representan la concentración y el volumen de la solución diluida deseada. El programa despeja automáticamente la variable incógnita introducida por el usuario, asegurando la consistencia dimensional entre las unidades.

---

## Uso

### Ejecución

Asegúrate de tener instalado el entorno correspondiente y ejecuta el programa desde la terminal:

```bash
python calculadora_diluciones.py

## validaciones
La herramienta ejecuta controles automáticos de calidad para evitar errores de laboratorio y excepciones en el código:Valores no numéricos: Captura y rechaza caracteres alfabéticos o símbolos especiales mediante el manejo de excepciones (ValueError)
Valores negativos o cero: Invalida cualquier entrada menor o igual a cero ($C \le 0$ o $V \le 0$).
Incongruencia de concentración ($C_1 \le C_2$): Rechaza intentos donde la concentración deseada sea mayor o igual que la solución madre (no es posible concentrar mediante dilución).
Incongruencia de volumen ($V_2 < V_1$): Notifica si el volumen total solicitado es inferior al volumen alícuota requerido de la solución madre.

---
## Limitaciones conocidas
Incompatibilidad de unidades heterogéneas: No realiza conversión automática de unidades (ej. Molar a mM, o mL a L). Los datos de concentración y volumen deben ingresarse en la misma escala dimensional.

Sin soporte para diluciones seriadas: Diseñado únicamente para diluciones simples de un solo paso.

Efectos físicos no contemplados: No calcula contracciones/expansiones de volumen al mezclar ciertos solventes, ni variaciones por temperatura o densidad en soluciones altamente concentradas.

