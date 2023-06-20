def getNextToken(command):
    command.pop(0)
    return command


def caso_select(command):
    getNextToken(command)
    if command[0] == '*':
        getNextToken(command)
        if command[0] == 'FROM':
            getNextToken(command)
            if command[0] not in comandos_reservados:
                getNextToken(command)
                if command[0] == ';':
                    return True
                elif command[0] == 'ORDER':
                    getNextToken(command)
                    if command[0] == 'BY':
                        getNextToken(command)
                        if command[0] not in comandos_reservados:
                            getNextToken(command)
                            if command[0] == ';':
                                return True
                elif command[0] == 'WHERE':
                    getNextToken(command)
                    if command[0] not in comandos_reservados:
                        getNextToken(command)
                        if command[0] == '=':
                            getNextToken(command)
                            if command[0] not in comandos_reservados:
                                getNextToken(command)
                                if command[0] == ';':
                                    return True
    elif command[0] not in comandos_reservados:
        getNextToken(command)
        if command[0] == ',':
            getNextToken(command)
            while True:
                if command[0] not in comandos_reservados:
                    getNextToken(command)
                    if command[0] == 'FROM':
                        getNextToken(command)
                        break
                    elif command[0] == ',':
                        getNextToken(command)
                    else:
                        return False
                else:
                    return False
            if command[0] not in comandos_reservados:
                getNextToken(command)
                if command[0] == ';':
                    return True
        elif command[0] == 'FROM':
            getNextToken(command)
            if command[0] not in comandos_reservados:
                getNextToken(command)
                if command[0] == ';':
                    return True
            
    return False
    

def caso_use(command):
    getNextToken(command)
    if command[0] not in comandos_reservados:
        getNextToken(command)
        if command[0] == ';':
            return True
    return False
    

def caso_create(command):
    getNextToken(command)
    if command[0] == 'DATABASE':
        getNextToken(command)
        if command[0] not in comandos_reservados:
            getNextToken(command)
            if command[0] == ';':
                return True
    elif command[0] == 'TABLE':
        getNextToken(command)
        if command[0] not in comandos_reservados:
            getNextToken(command)
            if command[0] == '(':
                getNextToken(command)
                while True:
                    if command[0] not in comandos_reservados:
                        getNextToken(command)
                        if command[0] in tipos:
                            getNextToken(command)
                            if command[0] == ',':
                                getNextToken(command)
                            elif command[0] == ')':
                                getNextToken(command)
                                break
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
                if command[0] == ';':
                    return True
    return False

    
def caso_truncate(command):
    getNextToken(command)
    if command[0] == 'TABLE':
        getNextToken(command)
        if command[0] not in comandos_reservados:
            getNextToken(command)
            if command[0] == ';':
                return True
    return False


def caso_delete(command):
    getNextToken(command)
    if command[0] == 'FROM':
        getNextToken(command)
        if command[0] not in comandos_reservados:
            getNextToken(command)
            if command[0] == 'WHERE':
                getNextToken(command)
                if command[0] not in comandos_reservados:
                    getNextToken(command)
                    if command[0] == '=':
                        getNextToken(command)
                        if command[0] not in comandos_reservados:
                            getNextToken(command)
                            if command[0] == ';':
                                return True
    return False


def caso_update(command):
    getNextToken(command)
    if command[0] not in comandos_reservados:
        getNextToken(command)
        if command[0] == 'SET':
            getNextToken(command)
            if command[0] not in comandos_reservados:
                getNextToken(command)
                if command[0] == '=':
                    getNextToken(command)
                    if command[0] not in comandos_reservados:
                        getNextToken(command)
                        if command[0] == 'WHERE':
                            getNextToken(command)
                            if command[0] not in comandos_reservados:
                                getNextToken(command)
                                if command[0] == '=':
                                    getNextToken(command)
                                    if command[0] not in comandos_reservados:
                                        getNextToken(command)
                                        if command[0] == ';':
                                            return True
    return False


def caso_insert(command):
    cont_col = 0
    cont_val = 0
    getNextToken(command)
    if command[0] == 'INTO':
        getNextToken(command)
        if command[0] not in comandos_reservados:
            getNextToken(command)
            if command[0] == '(':
                getNextToken(command)
                while True:
                    if command[0] not in comandos_reservados:
                        getNextToken(command)
                        cont_col += 1
                        if command[0] == ')':
                            getNextToken(command)
                            break
                        elif command[0] == ',':
                            getNextToken(command)
                        else:
                            return False
                    else:
                        return False
                if command[0] == 'VALUES':
                    getNextToken(command)
                    if command[0] == '(':
                        getNextToken(command)
                        while True:
                            if command[0] not in comandos_reservados:
                                getNextToken(command)
                                cont_val += 1
                                if command[0] == ')':
                                    getNextToken(command)
                                    break
                                elif command[0] == ',':
                                    getNextToken(command)
                                else:
                                    return False
                            else:
                                return False
                        if cont_col != cont_val:
                            return False
                        else:
                            if command[0] == ';':
                                return True
    return False
    

def alteraComando(command):
    command = command.replace('(', ' ( ')
    command = command.replace(')', ' ) ')
    command = command.replace(',', ' , ')
    command = command.replace(';', ' ; ')
    return command

tipos = ['int', 'float', 'string', 'char', 'bool']
comandos_reservados = ['SELECT', '*', 'FROM', 'WHERE', 'ORDER', 'BY', 'TRUNCATE', 'DELETE', 'CREATE', 'DATABASE', '=', ';', 'VALUES',
                       'TABLE', 'INSERT', '(', ')', 'UPDATE', ',', 'INTO', 'int', 'float', 'string', 'char', 'bool']

while True:
    comando = input('Insira um comando a ser reconhecido: ')
    comando = alteraComando(comando)
    comando = comando.split(' ')
    comando = [i for i in comando if i]
    print(comando)

    comando_rec = comando
    if comando[0] == 'SELECT':
        print(caso_select(comando_rec))
    elif comando[0] == 'USE':
        print(caso_use(comando_rec))
    elif comando[0] == 'CREATE':
        print(caso_create(comando_rec))
    elif comando[0] == 'INSERT':
        print(caso_insert(comando_rec))
    elif comando[0] == 'UPDATE':
        print(caso_update(comando_rec))
    elif comando[0] == 'DELETE':
        print(caso_delete(comando_rec))
    elif comando[0] == 'TRUNCATE':
        print(caso_truncate(comando_rec))

    cont = input('Deseja reconhecer mais comandos[S/N]: ')
    if cont == 'N':
        print('Fim da execução')
        break

# SELECT * FROM alunos;
# SELECT nome, idade FROM alunos;
# DELETE FROM alunos WHERE idade = 20;
# UPDATE alunos SET nome = bruno WHERE nome = markesley;