#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys       
if __name__ == '__main__':
    lines = []  
    for line in sys.stdin:
        line = line.strip().split()
        lines.append(line)
    for i in sorted(set([i[0] for i in l])):
        sys.stdout.write('{}\t{}\n'.format(i,lines.count([i])))