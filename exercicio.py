import statistics

def calcular_media(notas):
    """Calcula a média aritmética das notas."""
    if not notas:
        return 0
    return statistics.mean(notas)

def calcular_moda(notas):
    """Retorna a moda das notas. Trata casos de mais de uma moda ou nenhuma."""
    if not notas:
        return None
    try:
        return statistics.mode(notas)
    except statistics.StatisticsError:
        # Caso haja empate (multimodal), o multimode retorna todas as modas
        return statistics.multimode(notas)
    
c= calcular_media([1,2,3,4,5,6,7,8,9])
print(c)
m= calcular_moda([15,6,7,8,9])
print(m)
