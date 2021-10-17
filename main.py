def zippear(*listas: list) -> list:
    result = []
    
    if not listas: return [] 
  
    lengths = map(lambda x: len(x), listas)
    
    for i in range(min(lengths)):
        
        result.append(tuple([lista[i] for lista in listas]))
        
    return result
       



a = [1, 2, 3]
b = ["Python", "Java", "Cpp"]
c = [4, 5, 6]

print(zippear(a, b, c)) #[(1, 'Python', 4), (2, 'Java', 5), (3, 'Cpp', 6)]
