import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

with open('./budejie.csv', 'r', encoding='utf-8')as f:
    f.readline()
    while True:
        a = f.readline().split('|')
        content = a[0]
        name = a[1].split('/')[-1].split('\n')[0]
        with open('./con_name.csv', 'a', encoding='utf-8')as e:
            print(content, name)
            e.write('%s|%s\r' % (content, name))


