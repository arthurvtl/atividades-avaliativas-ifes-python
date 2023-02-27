cont130 = 0
cont30100 = 0
cont0100 = 0
for i in range (10):
   num = float(input('Digite um número '))

   if num >= 30 and num <= 100:
      cont30100 += 1

   elif num > 1 and num <30:
      cont130 += 1

   elif num >= 0 and num >= 100:
      cont0100 += 1

print('possui {} números entre 1 e 30'.format(cont130))
print('possui {} números entre 30 e 100'.format(cont30100))
print('possui {} números que são menores ou iguais a zero e/ou maiores ou iguais a 100'.format(cont0100))


       


    