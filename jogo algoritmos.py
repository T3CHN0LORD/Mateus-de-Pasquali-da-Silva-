 #Participantes#
 #Calebe Ferreira/TIA:32088116#
 #Gustavo Alves/TIA:32081286#
 #Mateus de Pasquali/TIA:32086997#
import random 

gold = 1000

vida = 200
ataque = 0

nome = input("Nome:")
print("Deusa Gaia:",nome,"Seja bem vindo ao plano divino,infelizmente você veio a falecer ao mundo que sua alma pertencia porém nós deuses damos uma nova oportunidade àqueles que foram justos e bondosos em vida.")
print("Deusa Gaia:Por você se encaixar nesses quesitos, você será reencarnado em um outro mundo chamado Arcadia, porém tome cuidado, pois esse mundo é diferente em relação ao qual você estava acostumado.")
print("Deusa Gaia:Neste mundo, há classes, há monstros reais, há demônios, ou seja há várias especies, portanto tome cuidado!")
print("Deusa Gaia:Você renascerá como um aventureiro humano, porém poderá escolher uma classe ou habilidade para poder enfrentar os perigos desse mundo.")
print("Deusa Gaia:Bem agora que tudo foi explicado você será teletransportado para esse mundo. Tenha cuidado e boa sorte!")

ver = 1

while ver != 0:
    classe = input("Qual classe você quer seguir(mago/guerreiro/curandeiro/assassino/caçador)")
    classe = classe.lower()
    if (classe == "mago") or (classe == "guerreiro") or (classe == "curandeiro") or (classe == "assassino") or (classe == "caçador"):
        print("Seja bem vindo ao nosso jogo",nome,"você escolheu a classe",classe)
        ver = 0
    else:
        print("Essa classe não existe, tente novamente")

print("Vamos começar nosso jogo \nVocê começa com a vida de:",vida)
print("Diriga-se a nossa guilda para poder selecionar algumas habilidades e uma missão")
print("Gerente da guilda: Bem-vindo(a) a nossa guilda",nome,"vejo que selecionou a classe",classe,". Qual habilidade você deseja selecionar?")
#sistema de compra de habilidades#
print('Existem 3 tipos de habilidades disponíveis para seu nível:', "Habilidade de Cura(Com esta habilidade você consegue aumentar sua vida em 10%) , Habilidade de Ataque(Com esta habilidade você consegue um bônus de ouro) ")
habilidade = 1
while habilidade != 0:
    escolha = input('Qual habilidade você gostaria de adiquirir? (Escreve o respectivo nome da habilidade desejada)')
    escolha = escolha.lower()
    if escolha == 'habilidade de cura':
        print('Parabéns pela sua escolha, sua vida aumentou em 10%')
        vida = vida + (vida * 0.1)  
        print("Sua vida agora:",vida)    
        habilidade = 0
    elif escolha == 'habilidade de ataque':
        print('Parabéns pela sua escolha, seu ataque aumentou em 10%')
        ataque = ataque + 7
        print("Seu dano de ataque adiconal", ataque)
        habilidade = 0
    elif escolha == 'habilidade mágica':
        print('Parabéns pela sua escolha, foi adicionado 100 de gold na sua bag')
        gold = gold + 100
        habilidade = 0
        
    else:
        print('Tente escrever novamente')

print("Seja bem vindo a loja, você atualmente possui", gold,"ouros")
compra = input("Digite o nome do produto que você quer\ndigite 'ataque' caso deseja aumentar em 3 seu dano,custa 250 de gold\ndigite 'vida' caso queira aumentar sua vida em 10%, custa 100 de gold\ncaso não tenha intenção de comprar nada, só de um enter: ")
if compra == 'vida':
    gold = gold - 100
    vida = vida + (vida * 0.1)
    print("Você atualmente possui", gold,"ouros")
    print("Sua vida agora:",vida)
elif compra == 'ataque':
    ataque = ataque + 3
    gold = gold - 250
    print("Você atualmente possui", gold,"ouros")
    print("Seu ataque está com o buff de", ataque,"de dano")
else:
    print('vamos continuar nosso jogo então')

print("Gerente da Guilda: Vejo que você selecionou umas habilidades interessantes, espero que seja um promissor aventureiro.")
print("Gerente da Guilda: Tenho uma missão ótima para você, uma missão que todos os iniciantes realizam.")
print("Gerente da Guilda: A missão se trata sobre eliminar alguns montros em uma região aqui perto de nossa cidade, você será teletransportado para uma região perto e a partir de lá você terá um leve auxílio.")
print(nome,": Muito obrigado(a) senhor! Tenho certeza que me saírei bem!")
print("Lucy:Ah vejo que você é o último a chegar",nome,"me chamo Lucy e seja bem-vindo ao acampamento para a missão inicial, guiarei vocês ao local da missão, aconselho todos a descançar está noite, pois cada um será levado a ponto diferente amanhã.")
print("Lucy:Bom dia aventureiros(as), como avisado ontem hoje vocês realizaram a missão inicial individualemte e cada um irá para uma direção.")
print("Lucy:",nome,",você irá para o noroeste tome cuidado, pois lá podem aparecer monstros do exército do Rei Demônio. Boa sorte!")
print(nome,":Obrigado pelo conselho Lucy, darei meu melhor no campo!")
print("Você entrou no campo de batalha, elimine os inimigos")



#criar sistema de batalha#

vidaInimigo = 100
poder1 = 20 
poder2 = 15
poder3 = 10

poderes = ['poder1', 'poder2', 'poder3']

poderInimigo = random.choice(poderes)  

print("Você não irá me derrotar")
if (vida > 0):
    while (vida <= 0):
        print('você morreu, tente novamente')
        print('aperte ctl + c')
    while vidaInimigo > 0:
        poderUsuario = input("Qual poder você deseja usar 1,2 ou 3:")
        if poderUsuario == '1':
            vidaInimigo = vidaInimigo - 50 - ataque
            print("Vida Inimiga:", vidaInimigo)
        elif poderUsuario == '2':
            vidaInimigo = vidaInimigo - 30 - ataque
            print("Vida Inimiga:", vidaInimigo) 
        elif poderUsuario == '3':
            vidaInimigo = vidaInimigo - 25 - ataque
            print("Vida Inimiga:", vidaInimigo) 
        else:
            print("Vez pulada, golpe não existente")
        poderInimigo = random.choice(poderes) 

        while (vida <= 0):
            print('você morreu, tente novamente')
            print('aperte ctl + c')

        if poderInimigo == "poder1":
            vida = vida - poder1
            print("Vida:", vida) 
        elif poderInimigo == "poder2":   
            vida = vida - poder2
            print("Você foi atingido pela fúria do dragão")
            print("Vida:", vida)    
        elif poderInimigo == "poder3":
            vida = vida - poder3
            print("você foi atingido pelo soco mortal")
            print("Vida:", vida)    
        else:
            print("Vez pulada, golpe não existente")

        
        while (vida <= 0):
            print('você morreu, tente novamente')
            print('aperte ctl + c')
            

        if vidaInimigo <= 0:
            print("O inimigo morreu \n Você recuperou 100 de vida \n Sua vida:",vida)
            vida = vida + 100
            print("Seja bem vindo a loja, você atualmente possui", gold,"ouros")
            compra = input("Digite o nome do produto que você quer\ndigite 'ataque' caso deseja aumentar em 3 seu dano,custa 250 de gold\ndigite 'vida' caso queira aumentar sua vida em 10%, custa 100 de gold\ncaso não tenha intenção de comprar nada, só de um enter: ")
            if compra == 'vida':
                gold = gold - 100
                vida = vida + (vida * 0.1)
                print("Você atualmente possui", gold,"ouros")
                print("Sua vida agora:",vida)
            elif compra == 'ataque':
                ataque = ataque + 3
                gold = gold - 250
                print("Você atualmente possui", gold,"ouros")
                print("Seu ataque está com o buff de", ataque,"de dano")
            else:
                print('vamo continuar nosso jogo então')

        while (vida <= 0):
            print('você morreu, tente novamente')
            print('aperte ctl + c')

            
        

print("Inimigos derrotados")
print(nome,":O inimigo pertencia ao exército do Rei Demônimo, fico feliz que o derrotei!")

#volta da batalha#
print("Lucy:Parabéns aos aventureiros(as) que retornaram!!")
print("Lucy:",nome,"fiquei sabendo que você teve que enfrentar um dos soldados do Rei Demônio, fico surpresa com que o derrotou.")
print(nome,":Não foi tão difícil assim, porém admito que tive que levar a sério a luta mesmo sendo minha inicial.")
print("Lucy:Que bom aventureiro(a), retorne a guilda e se fortaleça.")
print("Gerente da Guilda:Bem vindo de volta",nome,", fiquei sabendo que você derrotou sozinho um dos soldados do exercíto do Rei Demônio.")
print("Alarme do oeste da cidade começa tocar")
print("Todos os aventureiros se dirijam-se ao oeste pois o exercíto do Rei Demônio está atacando!!")
print("Gereente da Guilda:",nome,"antes de ir fortaleça-se novamente.")
#adicionar a parte da loja#
print(nome,":Certo agora que estou aprimorado posso ir para a batalha!")
print("Mikaela:Somente um aventureiro(a) chegou!?")
print("Mikaela:Pelo visto nossa batalha será rápida.")
print("Você não irá ganhar!!")
print(nome,":Não vá cantando vítória antes da hora!")
print("Batalha Final Iniciada")
#Sistema para a Batalha final#
vidaInimigo = 300
poder1 = 20 
poder2 = 15
poder3 = 10

poderes = ['poder1', 'poder2', 'poder3']

poderInimigo = random.choice(poderes)  

print("Você não irá me derrotar")
if (vida > 0):
    while (vida <= 0):
        print('você morreu, tente novamente')
        print('aperte ctl + c')
    while vidaInimigo > 0:
        poderUsuario = input("Qual poder você deseja usar 1,2 ou 3:")
        if poderUsuario == '1':
            vidaInimigo = vidaInimigo - 50 - ataque
            print("Vida Inimiga:", vidaInimigo)
        elif poderUsuario == '2':
            vidaInimigo = vidaInimigo - 30 - ataque
            print("Vida Inimiga:", vidaInimigo) 
        elif poderUsuario == '3':
            vidaInimigo = vidaInimigo - 25 - ataque
            print("Vida Inimiga:", vidaInimigo) 
        else:
            print("Vez pulada, golpe não existente")

        poderInimigo = random.choice(poderes) 

        while (vida <= 0):
            print('você morreu, tente novamente')
            print('aperte ctl + c')

        if poderInimigo == "poder1":
            vida = vida - poder1
            print("Vida:", vida) 
        elif poderInimigo == "poder2":   
            vida = vida - poder2
            print("Você foi atingido pela fúria do dragão")
            print("Vida:", vida)    
        elif poderInimigo == "poder3":
            vida = vida - poder3
            print("você foi atingido pelo soco mortal")
            print("Vida:", vida)    
        else:
            print("vez pulada")

        
        while (vida <= 0):
            print('você morreu, tente novamente')
            print('aperte ctl + c')
            

        if vidaInimigo <= 0:
            print("O inimigo morreu \n Você recuperou 100 de vida \n Sua vida:",vida)
            vida = vida + 100
            print("Seja bem vindo a loja, você atualmente possui", gold,"ouros")
            compra = input("Digite o nome do produto que você quer\ndigite 'ataque' caso deseja aumentar em 3 seu dano,custa 250 de gold\ndigite 'vida' caso queira aumentar sua vida em 10%, custa 100 de gold\ncaso não tenha intenção de comprar nada, só de um enter: ")
            if compra == 'vida':
                gold = gold - 100
                vida = vida + (vida * 0.1)
                print("Você atualmente possui", gold,"ouros")
                print("Sua vida agora:",vida)
            elif compra == 'ataque':
                ataque = ataque + 3
                gold = gold - 250
                print("Você atualmente possui", gold,"ouros")
                print("Seu ataque está com o buff de", ataque,"de dano")
            else:
                print('vamo continuar nosso jogo então')

        while (vida <= 0):
            print('você morreu, tente novamente')
            print('aperte ctl + c')

print("Gerente da Guilda:Você derrotou um dos generais do Rei Demônio")
print("Gerente da Guilda:Agora você pode criar a sua própria guilda ou seu grupo de aventureiros(as)")
print("Obrigado por jogar nosso jogo")
