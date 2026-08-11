def calcular_dilucion(c1, c2,v2):
    v1 = (c2 * v2) / c1
    disolvente = v2 - v1    
    return v1, disolvente  
  


c1 = float(input("Introduce la concentración madre (C1): "))
c2 = float(input("Introduce la concentración deseada (C2): "))
v2 = float(input("Introduce el volumen final (V2): "))

if c1 <= 0 or c2 <= 0 or v2 <= 0:
    print("Error: todos los valores deben ser mayores que cero")
elif c2 > c1:
    print("Error: la concentración deseada debe ser menor que la madre")
elif c2 == c1:
    print("No se requiere dilución: usa la solución madre directamente.")
else:
    factor = c1 / c2
    v1, disolvente = calcular_dilucion(c1, c2, v2)
    print(f"\nNecesitas tomar {v1:.2f} mL de la solución madre.")
    print(f"Necesitas añadir {disolvente:.2f} mL de disolvente para obtener {v2:.2f} mL de la solución deseada.")
    print(f"El factor de dilución es 1:{factor:.1f}")
    
  