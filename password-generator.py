# coding:utf-8
# Importando bibliotecas necessárias p/ rodar o código
from random import sample, choice
import sys
from time import sleep

# Parte introdutória que aparecerá na tela do usuário
print('=' * 140)
sleep(0.5)
print('{} {:^140} {}'.format('\033[33m', 'Bem Vindo ao Gerador de Senhas!', '\033[m'))
sleep(0.5)
print('=' * 140)
sleep(0.5)
print(
    '{0}A OPÇÃO PERSONALIZADA RETORNARÁ COMBINAÇÕES DE UMA SENHA DEFINIDA ANTERIORMENTE, ENQUANTO A ALEATÓRIA IRÁ GERAR UMA SENHA TOTALMENTE NOVA BASEADA NAS  SUAS PREFERÊNCIAS.{1}'.format(
        '\033[7:40m', '\033[m'))
sleep(1.5)

escolha = str(input('Deseja um código Personalizado ou Aleatório? [P/A] '))
escolha = escolha.lower()
sleep(0.5)

while True:
    
    if escolha == 'p':
        password = input('Digite sua Senha: ')
        p = sample(password, len(password))
        s = ''.join(p)
        sleep(0.5)
        print(f'Nova Senha: {s}')
        break

    elif escolha == 'a':
        b = list()
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        simbols = ['@', '#', '$', '&', '*', '(', ')', '-', '_', '+', '=', '^', '~', ':', '.']
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z']
        LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                   'U', 'V', 'W', 'X', 'Y', 'Z']
        print('Responda com [S] ou [N], por favor.')
        sleep(1)
        z = 0

        n = str(input('A senha incluirá números? [S/N] '))
        while n not in 'SsNn':
            print('Não entendi, digite novamente por favor!')
            n = str(input('A senha incluirá números? [S/N] '))
        sleep(0.5)
        if n in 'Ss':
            z += 1

        s = str(input('A senha incluirá símbolos? [S/N] '))
        while s not in 'SsNn':
            print('Não entendi, digite novamente por favor!')
            s = str(input('A senha incluirá símbolos? [S/N] '))
        sleep(0.5)
        if s in 'Ss':
            z += 1

        li = str(input('A senha incluirá letras minúsculas? [S/N] '))
        while li not in 'SsNn':
            print('Não entendi, digite novamente por favor!')
            li = str(input('A senha incluirá letras minúsculas? [S/N] '))
        sleep(0.5)
        if li in 'Ss':
            z += 1

        la = str(input('A senha incluirá letras maiúsculas? [S/N] '))
        while la not in 'SsNn':
            print('Não entendi, digite novamente por favor!')
            la = str(input('A senha incluirá letras maiúsculas? [S/N] '))
        sleep(0.5)
        if la in 'Ss':
            z += 1

        while True:
            q = int(input('Quantos dígitos a senha deve conter? '))
            if q < z:
                print('Impossível a quantidade de caracteres ser menor que a quantidade de grupos de caracteres.')
                while True:
                    resp = input('Gostaria de escolhar a quantidade de caracteres novamente?[S/N]')
                    if resp in 'Nn':
                        sys.exit()
                    elif resp in 'Ss':
                        print('Ok!')
                        break
                    else:
                        print('Dê uma resposta válida, por favor.')
            else:
                break

        if n in 'Ss':
            if s in 'Ss':
                if li in 'Ss':
                    if la in 'Ss':
                        b = numbers + simbols + letters + LETTERS
                        while True:
                            numberscheck = simbolscheck = letterscheck = LETTERScheck = 0
                            password = sample(b, q)
                            for c in range(0, len(numbers)):
                                if numbers[c] in password:
                                    numberscheck += 1
                            for d in range(0, len(simbols)):
                                if simbols[d] in password:
                                    simbolscheck += 1
                            for e in range(0, len(letters)):
                                if letters[e] in password:
                                    letterscheck += 1
                            for f in range(0, len(LETTERS)):
                                if LETTERS[f] in password:
                                    LETTERScheck += 1
                            if numberscheck != 0 and simbolscheck != 0 and letterscheck != 0 and LETTERScheck != 0:
                                break

                    else:
                        b = numbers + simbols + letters
                        while True:
                            numberscheck = simbolscheck = letterscheck = LETTERScheck = 0
                            password = sample(b, q)
                            for c in range(0, len(numbers)):
                                if numbers[c] in password:
                                    numberscheck += 1
                            for d in range(0, len(simbols)):
                                if simbols[d] in password:
                                    simbolscheck += 1
                            for e in range(0, len(letters)):
                                if letters[e] in password:
                                    letterscheck += 1
                            if numberscheck != 0 and simbolscheck != 0 and letterscheck != 0:
                                break

                else:
                    if la in 'Ss':
                        b = numbers + simbols + LETTERS
                        while True:
                            numberscheck = simbolscheck = letterscheck = LETTERScheck = 0
                            password = sample(b, q)
                            for c in range(0, len(numbers)):
                                if numbers[c] in password:
                                    numberscheck += 1
                            for d in range(0, len(simbols)):
                                if simbols[d] in password:
                                    simbolscheck += 1
                            for f in range(0, len(LETTERS)):
                                if LETTERS[f] in password:
                                    LETTERScheck += 1
                            if numberscheck != 0 and simbolscheck != 0 and LETTERScheck != 0:
                                break

                    else:
                        b = numbers + simbols
                        while True:
                            numberscheck = simbolscheck = letterscheck = LETTERScheck = 0
                            password = sample(b, q)
                            for c in range(0, len(numbers)):
                                if numbers[c] in password:
                                    numberscheck += 1
                            for d in range(0, len(simbols)):
                                if simbols[d] in password:
                                    simbolscheck += 1

                            if numberscheck != 0 and simbolscheck != 0:
                                break

            else:
                if li in 'Ss':
                    if la in 'Ss':
                        b = numbers + letters + LETTERS
                        while True:
                            numberscheck = simbolscheck = letterscheck = LETTERScheck = 0
                            password = sample(b, q)
                            for c in range(0, len(numbers)):
                                if numbers[c] in password:
                                    numberscheck += 1
                            for e in range(0, len(letters)):
                                if letters[e] in password:
                                    letterscheck += 1
                            for f in range(0, len(LETTERS)):
                                if LETTERS[f] in password:
                                    LETTERScheck += 1
                            if numberscheck != 0 and letterscheck != 0 and LETTERScheck != 0:
                                break

                    else:
                        b = numbers + letters
                        while True:
                            numberscheck = simbolscheck = letterscheck = LETTERScheck = 0
                            password = sample(b, q)
                            for c in range(0, len(numbers)):
                                if numbers[c] in password:
                                    numberscheck += 1

                            for e in range(0, len(letters)):
                                if letters[e] in password:
                                    letterscheck += 1

                            if numberscheck != 0 and letterscheck != 0:
                                break

                else:
                    if la in 'Ss':
                        b = numbers + LETTERS
                        while True:
                            numberscheck = simbolscheck = letterscheck = LETTERScheck = 0
                            password = sample(b, q)
                            for c in range(0, len(numbers)):
                                if numbers[c] in password:
                                    numberscheck += 1
                            for f in range(0, len(LETTERS)):
                                if LETTERS[f] in password:
                                    LETTERScheck += 1
                            if numberscheck != 0 and LETTERScheck != 0:
                                break

                    else:
                        b = numbers
                        while True:
                            numberscheck = simbolscheck = letterscheck = LETTERScheck = 0
                            password = sample(b, q)
                            for c in range(0, len(numbers)):
                                if numbers[c] in password:
                                    numberscheck += 1

                            if numberscheck != 0:
                                break

        else:
            if s in 'Ss':
                if li in 'Ss':
                    if la in 'Ss':
                        b = simbols + letters + LETTERS
                        while True:
                            numberscheck = simbolscheck = letterscheck = LETTERScheck = 0
                            password = sample(b, q)

                            for d in range(0, len(simbols)):
                                if simbols[d] in password:
                                    simbolscheck += 1

                            for e in range(0, len(letters)):
                                if letters[e] in password:
                                    letterscheck += 1

                            for f in range(0, len(LETTERS)):
                                if LETTERS[f] in password:
                                    LETTERScheck += 1

                            if simbolscheck != 0 and letterscheck != 0 and LETTERScheck != 0:
                                break

                    else:
                        b = simbols + letters
                        while True:
                            numberscheck = simbolscheck = letterscheck = LETTERScheck = 0
                            password = sample(b, q)

                            for d in range(0, len(simbols)):
                                if simbols[d] in password:
                                    simbolscheck += 1

                            for e in range(0, len(letters)):
                                if letters[e] in password:
                                    letterscheck += 1

                            if simbolscheck != 0 and letterscheck != 0:
                                break

                else:
                    if la in 'Ss':
                        b = simbols + LETTERS
                        while True:
                            numberscheck = simbolscheck = letterscheck = LETTERScheck = 0
                            password = sample(b, q)

                            for d in range(0, len(simbols)):
                                if simbols[d] in password:
                                    simbolscheck += 1

                            for f in range(0, len(LETTERS)):
                                if LETTERS[f] in password:
                                    LETTERScheck += 1

                            if simbolscheck != 0 and LETTERScheck != 0:
                                break

                    else:
                        b = simbols
                        while True:
                            numberscheck = simbolscheck = letterscheck = LETTERScheck = 0
                            password = sample(b, q)

                            for d in range(0, len(simbols)):
                                if simbols[d] in password:
                                    simbolscheck += 1
                            if simbolscheck != 0:
                                break

            else:
                if li in 'Ss':
                    if la in 'Ss':
                        b = letters + LETTERS
                        while True:
                            numberscheck = simbolscheck = letterscheck = LETTERScheck = 0
                            password = sample(b, q)

                            for e in range(0, len(letters)):
                                if letters[e] in password:
                                    letterscheck += 1
                            for f in range(0, len(LETTERS)):
                                if LETTERS[f] in password:
                                    LETTERScheck += 1
                            if letterscheck != 0 and LETTERScheck != 0:
                                break

                    else:
                        b = letters
                        while True:
                            numberscheck = simbolscheck = letterscheck = LETTERScheck = 0
                            password = sample(b, q)

                            for e in range(0, len(letters)):
                                if letters[e] in password:
                                    letterscheck += 1

                            if letterscheck != 0:
                                break

                else:
                    if la in 'Ss':
                        b = LETTERS
                        while True:
                            numberscheck = simbolscheck = letterscheck = LETTERScheck = 0
                            password = sample(b, q)

                            for f in range(0, len(LETTERS)):
                                if LETTERS[f] in password:
                                    LETTERScheck += 1

                            if LETTERScheck != 0:
                                break

                    else:
                        print('Por favor, não foda e meta o pé')
                        sleep(2)
                        sys.exit()

        sleep(0.5)
        senha = ''.join(password)
        print('Nova Senha: {0}'.format(senha))
        break

    else:
        print('Por favor escreva sua escolha da mesma forma como foi apresentado.')
        escolha = str(input('Deseja um código Personalizado ou Aleatório? [P/A] '))
        escolha = escolha.lower()
        sleep(0.5)

sleep(1)
print(
    '{0}Muito obrigado por usar nossos serviços, estaremos aqui sempre que precisar de nós! Agora poderá proveitar sua vida online de uma forma mais segura!{1}'.format(
        '\033[32m', '\033[m'))
print()