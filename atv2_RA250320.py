# Nome: Gabriel Evangelista Correia    RA: 250320

instrucao = str(input())
instrucao = instrucao.replace(",", " ")
lista_comandos = instrucao.split()
tipo_escolhido = lista_comandos[0]
# print(lista_comandos)
numero_componentes = len(lista_comandos)
# print(numero_componentes)

zero = '00000'
ra = '00001'
sp = '00010'
gp = '00011'
tp = '00100'
t0 = '00101'
t1 = '00110'
t2 = '00111'
s0 = '01000'
s1 = '01001'
a0 = '01010'
a1 = '01011'
a2 = '01100'
a3 = '01101'
a4 = '01110'
a5 = '01111'
a6 = '10000'
a7 = '10001'
s2 = '10010'
s3 = '10011'
s4 = '10100'
s5 = '10101'
s6 = '10110'
s7 = '10111'
s8 = '11000'
s9 = '11001'
s10 = '11010'
s11 = '11011'
t3 = '11100'
t4 = '11101'
t5 = '11110'
t6 = '11111'

# lista de registradores em binario
lista_registradores_bin = [zero, ra, sp, gp, tp, t0, t1, t2, s0, s1, a0, a1, a2,
                           a3, a4, a5, a6, a7, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, t3, t4, t5, t6]
# lista de strings de registradores
lista_registradores_nome = ['zero', 'ra', 'sp', 'gp', 'tp', 't0', 't1', 't2', 's0', 's1', 'a0', 'a1', 'a2', 'a3',
                            'a4', 'a5', 'a6', 'a7', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 's10', 's11', 't3', 't4', 't5', 't6']


def instrucao_I():
    rd = '00000'
    rs1 = '00000'
    upcode_I = '0010011'
    # definir qual o rd
    for registrador in range(len(lista_registradores_nome)):
        if lista_comandos[1] == lista_registradores_nome[registrador]:
            rd = lista_registradores_bin[registrador]
        else:
            pass
        registrador = + 1

    # encontrando funct3
    if lista_comandos[0] == 'addi':
        funct3 = '000'
    if lista_comandos[0] == 'slli':
        funct3 = '001'

    # definir qual o rs1
    for registrador in range(len(lista_registradores_nome)):
        if lista_comandos[2] == lista_registradores_nome[registrador]:
            rs1 = lista_registradores_bin[registrador]
        else:
            pass
        registrador = + 1

    # ultimos 11 bits
    if lista_comandos[0] == 'addi':
        imediato_int = int(lista_comandos[3])
        imediato_bin = format(imediato_int, '11b')

    if lista_comandos[0] == 'slli':
        imediato_int = int(lista_comandos[3])
        imediato_bin = format(imediato_int, '5b')
        imediato_bin_completo = '0000000' + imediato_bin

    if lista_comandos[0] == 'addi':
        instrucao_final_bin = imediato_bin + rs1 + funct3 + rd + upcode_I
        instrucao_final_bin = format(instrucao_final_bin, '32b')
    if lista_comandos[0] == 'slli':
        instrucao_final_bin = imediato_bin_completo + rs1 + funct3 + rd + upcode_I

    print(instrucao_final_bin)


instrucao_I()
