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
