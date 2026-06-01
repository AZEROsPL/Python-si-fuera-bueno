for hora in range(24):
    for minuto in range(60):
        for segundo in range(60):
            for milisegundo in range(40000):
                print(f"{hora:02d}:{minuto:02d}:{segundo:02d}:{milisegundo:02d}")