contI = 0
contTS = 0
contIT = 0
contNA = 0

for i in range(5):
    sexo = int(input(f"Digite o sexo do trabalhador {i+1} (1 = Feminino // 2 = Masculino): "))
    idade = int(input(f"Digite a idade da trabalhador {i+1} em anos : "))
    ts = int(input(f"Digite o tempo de serviço da trabalhador {i+1} em anos: "))

    if (sexo == 1): 

        if (idade>=60 and ts<25):
            print("Está pessoa pode se aposentar pela idade")
            contI += 1

        elif (ts>=30 and idade<55):
            print("Está pessoa pode se aposentar pelo tempo de serviço")
            contTS += 1

        elif (idade>=60 and ts>=35):
            print("Está pessoa pode se aposentar pela idade e pelo tempo de serviço")
            contIT += 1

        else:
            print("Está pessoa não pode se aposentar")
            contNA += 1

    elif (sexo==2):

        if (idade>=65 and ts<35):
            print("Esta pessoa pode se aposentar pela idade")
            contI+=1

        elif (ts>=35 and idade<60):
            print("Esta pessoa pode se aposentar pelo tempo de serviço")
            contTS+=1

        elif (idade>=60 and ts>=35):
            print("Esta pessoa pode se aposentar pela idade e pelo tempo de serviço")
            contIT+=1

        else:
            print("Esta pessoa não pode se aposentar")
            contNA+=1

print(f"{contI} trabalhadores poderão se aposentar por idade")

print(' ')

print(f"{contTS} trabalhadores poderão se aposentar por tempo de serviço")

print(' ')

print(f"{contIT} trabalhadores poderão se aposentar por idade e tempo de serviço")

print(' ')

print(f"{contNA} trabalhadore não poderão vão se aposentar")