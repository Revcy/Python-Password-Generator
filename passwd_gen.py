import random as r

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''

def generate_password(length, chars):
    passwd = ''
    for _ in range(int(length)):
        passwd += chars[r.randrange(len(chars))]
    return passwd


while True:
    pwdc = int(input('Сколько паролей генерируем? # '))
    pwdlen = input('Какой длины формируем? # ')
    pwdcd = input('Добавляем цифры? (да, нет) # ')
    pwdcu = input('Добавляем заглавные буквы? (да, нет) # ')
    pwdcl = input('Добавляем строчные буквы? (да, нет) # ')
    pwdcc = input('Добавляем символы? (да, нет) # ')
    pwdce = input('Исключать ли неоднозначные символы il1Lo0O? (да, нет) # ')

    if pwdcd.lower() == 'да':
        chars += digits
    if pwdcu.lower() == 'да':
        chars += lowercase_letters
    if pwdcl.lower() == 'да':
        chars += uppercase_letters
    if pwdcc.lower() == 'да':
        chars += punctuation
    if pwdce.lower() == 'да':
        for i in range(len(chars)):
            if chars[i] in 'il1Lo0O':
                chars.replace(chars[i], '')

    print()
    print('Пароли: ')
    print()
    
    for _ in range(pwdc):
        print(generate_password(pwdlen, chars))

    print()

    quit_promt = input('Генерируем ещё? (да, нет) # ')
    if quit_promt.lower() == 'да':
        continue
    elif quit_promt.lower() == 'нет':
        print('Спасибо что воспрользовались генератором паролей!')
        break
    else:
        print('Значит хотите')
