def fibonacci_1029():
    entrada = int(input())

    while (entrada > 0):
        n = int(input())

        num_call = [1, 1]
        result = [0, 1]
        for i in range(2, 41):
            num_call.append(num_call[i - 1] + num_call[i - 2] + 1)
            result.append(result[i - 1] + result[i - 2])

        print('fib({}) = {} calls = {}'.format(n, num_call[n] - 1, result[n]))
        entrada -= 1

def seq_granizo_1441():

    def is_entrada(var):
        return var != 0 and ((var & (var - 1)) == 0)

    while True:
        entrada = int(input())
        if entrada == 0:
            break
        var = 0
        while is_entrada(entrada) != True:
            if entrada > var:
                var = entrada
            if entrada % 2 == 0:
                entrada = int(entrada / 2)
            else:
                entrada = entrada * 3 + 1
        if entrada > var:
            var = entrada
        print(var)

def game_varetas_1366():
    while True:
        n = int(input())
        if not n: break
        s = 0
        for i in range(n):
            s += [int(x) for x in input().split()][1] // 2
        print(s // 2)

def procurando_nessy_1428():
    for g in range(int(input())):
        a, b = [int(x) for x in input().split()]
        print((a // 3) * (b // 3))

def movimentos_cavalo_1100():
    chars=['a','b','c','d','e','f','g','h']
    moves = [[-1,-2],[-1,2],[1,-2],[1,2],
             [2,1],[2,-1],[-2,1],[-2,-1]]

    def passeio(x,y):
        move = 0
        if (x==y):
            return move
        caminho_aux=[]
        caminho=[]

        for m in moves:
            teste=[]
            x1=m[0]+x[0]
            x2=m[1]+x[1]
            teste.append(x1)
            teste.append(x2)
            if ((teste[0]<8 and teste[0]>-1) and
                    (teste[1]<8 and teste[1]>-1)):
                caminho_aux.append(teste)
        while True:
            move +=1
            if (x == y):
                return move
            caminho=caminho_aux
            caminho_aux=[]

            if y in caminho:
                return move
            else:
                for pos in caminho:
                    for mm in moves:
                        x1=mm[0]+pos[0]
                        x2=mm[1]+pos[1]
                        teste.append(x1)
                        teste.append(x2)
                        if ((teste[0]<8 and teste[0]>-1) and
                                (teste[1]<8 and teste[1]>-1)):
                            caminho_aux.append(teste)
                caminho = []

    while(True):
        try:
            xx, yy = input().split(' ')
            x = list(xx)
            y = list(yy)
            x1 = int(chars.index(x[0]))
            x2 = int(x[1])-1
            y1 = int(chars.index(y[0]))
            y2 = int(y[1])-1
            x = [x2, x1]
            y = [y2, y1]

            move = passeio(x, y)
            print('To get from {} to {} takes {} knights moves.'.format(xx,yy,move))

        except EOFError:
            break

def tabela_hash_1256():
    n = int(input())
    check = 0

    while n:
        n -= 1
        m, c = [int(x) for x in input().split()]
        hash = {str(x): [] for x in range(m)}
        entrada = [int(x) for x in input().split()]

        if check:
            print()

        for i in entrada:
            resto = i % m
            hash[str(resto)].append(int(i))

        for i in hash:
            print('%d -> ' % int(i), end='')
            for j in hash[i]:
                print('%d -> ' % j, end='')
            print('\\')

        check = 1

def game_mat_paula_1192():
    q = int(input())
    for p in range(q):
        e = str(input())
        d1 = int(e[0])
        d2 = int(e[2])
        if d1 == d2:
            print(d1 * d2)
        elif e[1].isupper():
            print(d2 - d1)
        else:
            print(d1 + d2)

def eletricidade_1374():
    print('Fazer')

def loteria_1407():
    print('Fazer')

def cavalo_1513():
    print('Fazer')

game_varetas_1366()