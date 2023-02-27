a1 = str(input('Olá, qual seu nome? '))
print('{}, digite suas notas relativas ao: 1°, 2° e 3° bimestre e diremos se você já está aprovado ou não para o 4° bimestre'.format(a1))

a11 = float(input('1° Bimestre: '))
a12 = float(input('2° Bimestre: '))
a13 = float(input('3° Bimestre: '))
mfa1 = (a11 + a12 + a13) /3

print(' ')
print('=-'*100)
print(' ')

a2 = str(input('Olá, qual seu nome? '))
print('{}, digite suas notas relativas ao: 1°, 2° e 3° bimestre e diremos se você já está aprovado ou não para o 4° bimestre'.format(a2))

a21 = float(input('1° Bimestre: '))
a22 = float(input('2° Bimestre: '))
a23 = float(input('3° Bimestre: '))
mfa2 = (a21 + a22 + a23) /3

print(' ')
print('=-'*100)
print(' ')

a3 = str(input('Olá, qual seu nome? '))
print('{}, digite suas notas relativas ao: 1°, 2° e 3° bimestre e diremos se você já está aprovado ou não para o 4° bimestre'.format(a3))

a31 = float(input('1° Bimestre: '))
a32 = float(input('2° Bimestre: '))
a33 = float(input('3° Bimestre: '))
mfa3 = (a31 + a32 + a33) /3

print(' ')
print('=-'*100)
print(' ')


if mfa1 >= 70:
    print('{}, você foi aprovado!'.format(a1))

elif 50 <= mfa1 < 70:
    print('{}, você está de recuperação, sua média considerando os três primeiros bimestres foi: {}'.format(a1,mfa1))
    print('{}, qual sua nota relativa ao 4° bimestre?: '.format(a1))
    a14 = float(input('4° Bimestre: '))
    mfa14 = (a11 + a12 + a13 + a14) /4
    if mfa14 >= 70:
        print('{}, utilizando sua nota relativa ao 4° bimestre, você foi aprovado! com a média de: {}'.format(a1,mfa14))
    else:
        print('{}, mesmo com sua nota do 4° bimestre, você não foi aprovado, com a média de: {}'.format(a1,mfa14))

else:
    print('{}, você está reprovado.'.format(a1))

print(' ')
print('=-'*100)
print(' ')


if mfa2 >= 70:
    print('{}, você foi aprovado!'.format(a2))

elif 50 <= mfa2 < 70:
    print('{}, você está de recuperação, sua média considerando os três primeiros bimestres foi: {}'.format(a2,mfa2))
    print('{}, qual sua nota relativa ao 4° bimestre?: '.format(a2))
    a24 = float(input('4° Bimestre: '))
    mfa24 = (a21 + a22 + a23 + a24) /4
    if mfa24 >= 70:
        print('{}, utilizando sua nota relativa ao 4° bimestre, você foi aprovado! com a média de: {}'.format(a2,mfa24))
    else:
        print('{}, mesmo com sua nota do 4° bimestre, você NÃO foi aprovado! com a média de: {}'.format(a2,mfa24))
else:
    print('{}, você está reprovado.'.format(a2))

print(' ')
print('=-'*100)
print(' ')


if mfa3 >= 70:
    print('{}, você foi aprovado!'.format(a3))

elif 50 <= mfa3 < 70:
    print('{}, você está de recuperação, sua média considerando os três primeiros bimestres foi: {}'.format(a3,mfa3))
    print('{}, qual sua nota relativa ao 4° bimestre?: '.format(a3))
    a34 = float(input('4° Bimestre: '))
    mfa34 = (a31 + a32 + a33 + a34) /4
    if mfa34 >= 70:
        print('{}, utilizando sua nota relativa ao 4° bimestre, você foi aprovado, com a média de: {}'.format(a3,mfa34))
    else:
        print('{}, mesmo com sua nota do 4° bimestre, você NÃO foi aprovado, com a média de: {}'.format(a3,mfa34))

else:
    print('{}, você está reprovado.'.format(a3))



    



