def resolver_torres_hanoi(n: int, poste_de_origen: str, poste_de_destino: str, poste_auxiliar: str) -> None:
    if n == 1:
        print(f'Mover disco 1 de punto {poste_de_origen} hacia {poste_de_destino}.')
    else:
        # Mover n-1 discos del poste_de_origen al poste_auxiliar usando poste_de_destino como poste_auxiliar
        resolver_torres_hanoi(n - 1, poste_de_origen, poste_auxiliar, poste_de_destino)
        # Mover el disco más grande del poste_de_origen al poste_de_destino
        print(f'Mover disco {n} de punto {poste_de_origen} hacia punto {poste_de_destino}.')
        # Mover los n-1 discos del poste_auxiliar al poste_de_destino usando poste_de_origen como poste_auxiliar
        resolver_torres_hanoi(n - 1, poste_auxiliar, poste_de_destino, poste_de_origen)


resolver_torres_hanoi(3, 'origen', 'destino', 'auxiliar')
