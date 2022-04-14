lista_de_pacotes = {
    "288355555123888",
    "335333555584333",
    "223343555124001",
    "002111555874555",
    "111188555654777",
    "111333555123333",
    "432055555123888",
    "079333555584333",
    "155333555124001",
    "333188555584333",
    "555288555123001",
    "111388555123555",
    "288000555367333",
    "066311555874001",
    "110333555123555",
    "333488555584333",
    "455448555123001",
    "022388555123555",
    "432044555845333",
    "034311555874001" 
}

codigo_regioes = {
    "Sudeste": [1,99],
    "Sul": [100,199],
    "Centro-Oeste": [201,299],
    "Nordeste": [300,399],
    "Norte": [400,499],
}

codigo_produto = {
    "Joias": [0,1],
    "Livros": [2,111],
    "Eletronicos": [112,333],
    "Bebidas": [334,555],
    "Brinquedos": [556,888]
}

def identificandoRegiao(pacote=str) -> str :
    regiaoPacote = int(pacote)
    
    for regiao, codigo in codigo_regioes.items():
        if regiaoPacote >= codigo[0] and regiaoPacote <= codigo[1]:
            return regiao


def identificandoTipo(pacote=str) -> str: 
    tipoPacote = int(pacote)
    
    for produto, codigo in codigo_produto.items():
        if tipoPacote >= codigo[0] and tipoPacote <= codigo[1]:
            return produto


def pacoteValido(pacote=str) -> bool:

    regiaoOrigem = identificandoRegiao(pacote[0:3])
    regiaoDestino = identificandoRegiao(pacote[3:6])
    tipoProduto = identificandoTipo(pacote[-3:])
    codigoVendedorInativo = pacote[9:12]

    if  regiaoOrigem is None or regiaoDestino is None:
        return False
    
    if tipoProduto is None:
        return False

    if codigoVendedorInativo == "367":
        return False

    if tipoProduto == "Joias" and regiaoOrigem == "Centro-Oeste":
        return False

    return True


def rotaPacotes(regiaoNaRota=list):
    pacotesDespachados = list()

    for pacote in lista_de_pacotes:
        if not pacoteValido(pacote):
            continue
        else:
            regiaoPacote = identificandoRegiao(pacote[3:6])
            if regiaoPacote in regiaoNaRota:
                pacotesDespachados.append(pacote)
            else:
                continue
    return pacotesDespachados


def destino(pacote):
    return pacote[3:6]

#-------------------------------------- ITEMS --------------------------------------------------#
# 1. Identificar a região de destino de cada pacote, com totalização de pacotes (soma região);
def item1():
    valorInicial = 0
    regioes = codigo_regioes.keys()
    contadorRegiao = dict.fromkeys(regioes, valorInicial)

    for pacote in lista_de_pacotes:
        regiaoPacote = identificandoRegiao(pacote[3:6])

        if regiaoPacote is not None:
            print(f'O pacote de codigo {pacote} esta destinado a regiao {regiaoPacote}\n')
            contadorRegiao[regiaoPacote] += 1
        else:
            print(f'** pacote {pacote} esta com a regiao de destino invalida! **\n')

    print("-"*100)
    for regiao, somaPacotes in contadorRegiao.items():
        print(f'A regiao {regiao} tem {somaPacotes} pacotes destinados.')




#Saber quais pacotes possuem códigos de barras válidos e/ou inválidos;
def item2():
    for pacote in lista_de_pacotes:
        Valido = pacoteValido(pacote)

        if Valido is True:
            print(f'Pacote de codigo {pacote} é valido!\n')
        else:
            print(f'** Pacote de codigo {pacote} é invalido! **\n')



#Identificar os pacotes que têm como origem a região Sul e Brinquedos em seu conteúdo;
def item3():
    for pacote in lista_de_pacotes:
        regiaoOrigem = identificandoRegiao(pacote[0:3])
        tipoProduto = identificandoTipo(pacote[-3:])

        if regiaoOrigem == "Sul" and tipoProduto == "Brinquedos":
            print(f'O pacote de codigo {pacote} tem como origem a regiao Sul e eh um brinquedo.\n')
        else:
            print(f'** O pacote de codigo {pacote} nao tem a regiao Sul como origem e nao eh um brinquedo. **\n')



#4. Listar os pacotes agrupados por região de destino (Considere apenas pacotes válidos);
def item4():
    pacotesAgrupados = dict()

    for pacote in lista_de_pacotes:
        if pacoteValido(pacote) is False:
            continue
        
        regiaoDestino = identificandoRegiao(pacote[3:6])
        pacotesAgrupados.setdefault(regiaoDestino,list())
        pacotesAgrupados[regiaoDestino].append(pacote)
    

    for regiao in pacotesAgrupados:
        print(f'\n{"-"*10} {regiao.upper()} {"-"*10}\n')
        
        for pacote in pacotesAgrupados[regiao]:
            print(f'Codigo do pacote: {pacote}')



#5. Listar o número de pacotes enviados por cada vendedor (Considere apenas pacotes válidos);
def item5():
    vendedores = dict()

    for pacote in lista_de_pacotes:
        if pacoteValido(pacote) is False:
            continue
        
        codigoVendedor = pacote[9:12]
        vendedores.setdefault(codigoVendedor,list())
        vendedores[codigoVendedor].append(pacote)

    for vendedor in vendedores:
        print(f'\n{"-"*10} Codigo do Vendedor: {vendedor} {"-"*10}\n')

        for pacote in vendedores[vendedor]:
            print(f'Codigo dos pacotes vendidos: {pacote}')



#6. Gerar o relatório/lista de pacotes por destino e por tipo (Considere apenas pacotes válidos);
def item6():
    infoPacote = dict()

    for pacote in lista_de_pacotes:
        if pacoteValido(pacote) is False:
            continue
        else:
            regiaoDestino = identificandoRegiao(pacote[3:6])
            tipoProduto = identificandoTipo(pacote[-3:])

            regiaoEtipo = (regiaoDestino,tipoProduto)
            infoPacote.setdefault(pacote,list())
            infoPacote[pacote].append(regiaoEtipo)
    

    print(f'\n{"-"*10} LISTA DE PACOTES POR REGIAO {"-"*10}\n')

    for regiao in codigo_regioes.keys():
        print(f'\n--- REGIAO {regiao} ---\n')
        for pacote, valores in infoPacote.items():
            if valores[0][0] == regiao:
                print(f'Codigo do pacote: {pacote}')


    print(f'\n{"-"*10} LISTA DE PACOTES POR TIPO DE PRODUTO {"-"*10}\n')

    for tipo in codigo_produto.keys():
        print(f'\n--- {tipo} ---\n')
        for pacote, valores in infoPacote.items():
            if valores[0][1] == tipo:
                print(f'Codigo do pacote: {pacote}')



#7. Se o transporte dos pacotes para o Norte passa pela Região Centro-Oeste, quais são os pacotes que devem ser despachados no mesmo caminhão?
def item7():
    regiaoDaRota = ["centro-Oeste","Norte"]
    pacotesDespachados = rotaPacotes(regiaoDaRota)
    
    if len(pacotesDespachados) == 0:
        print(f'Nenhum pacote para essa rota!')
    else:
        for despachado in pacotesDespachados:
            print(f'Pacotes validos despachados: {despachado}\n')



#8. Se todos os pacotes fossem uma fila qual seria a ordem de carga para o Norte no caminhão para descarregar os pacotes da Região Centro Oeste primeiro;
def item8():
    regiaoNaRota = ["Centro-Oeste","Norte"]
    pacotesDespachados = rotaPacotes(regiaoNaRota)

    if len(pacotesDespachados) == 0:
        print(f'Nenhum pacote para essa rota!')
    else:
        cont = 0
        pacotesDespachados.sort(key=destino)

        print(f'\n{"-"*15} ORDEM DE DESPACHO {"-"*15}\n')
        for despachado in pacotesDespachados:
            cont += 1
            print(f'{cont}- Pacotes validos a serem despachados: {despachado}\n')



#9. No item acima considerar que as jóias fossem sempre as primeiras a serem descarregadas;
def item9():
    regiaoNaRota = ["Centro-Oeste","Norte"]
    pacotesDespachados = rotaPacotes(regiaoNaRota)

    if len(pacotesDespachados) == 0:
        print(f'Nenhum pacote para essa rota!')
    else:
        cont = 0
        pacotesDespachados.sort(key=destino)

        CentroOesteJoias = []
        joias = ["000","001"]

        for pacote in pacotesDespachados:
            if identificandoRegiao(pacote[3:6]) == "Centro-Oeste" and pacote[-3:] in joias:
                pacotesDespachados.remove(pacote)
                CentroOesteJoias.append(pacote)
            else:
                continue

        CentroOesteJoias.extend(pacotesDespachados)
        print(f'\n{"-"*15} ORDEM DE DESPACHO {"-"*15}\n')
        for despachado in CentroOesteJoias:
            cont += 1
            print(f'{cont}- Pacotes validos a serem despachados: {despachado}\n')



#10. Listar os pacotes inválidos.
def item10():
    print(f'{"-"*5} LISTA DE PACOTES INVALIDOS {"-"*5}\n')
    for pacote in lista_de_pacotes:
        valido = pacoteValido(pacote)
        if not valido:
            print(f'Codigo do pacote: {pacote}.')
        else:
            continue



#item1()

#item2()

#item3()

#item4()

#item5()

#item6()  

#item7()

#item8()

#item9()

#item10()