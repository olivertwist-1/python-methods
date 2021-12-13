def insert(lista: list, index: int, item) -> list:

  """Insert the given item to your list"""

  if index == -1 or index >= len(lista):
     lista.append(item)
     return lista

  new_list = [item]

  for i in range(index, len(lista)):
     new_list.append(lista[i])

  lista = lista[: index]
  return lista + new_list
