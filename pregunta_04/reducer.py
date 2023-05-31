#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
if __name__ == '__main__':
    lista = []
    for line in sys.stdin:
        line = line.strip()
        line = line.split()
        lista.append(line)
    s_lista =set([x[0] for x in lista])
    s_lista = sorted(s_lista, key=lambda x: x[0])
    for i in s_lista:
        sys.stdout.write("{},{}\n".format(i.lista.count([i])))