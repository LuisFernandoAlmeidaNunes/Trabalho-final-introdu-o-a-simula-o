import matplotlib.pyplot as plt
import numpy as np

class Simulacao:

    #Primeira parte do DCA
    def inicia_pedido(self):

        # inicializando pedido
        pedido = {
            "nos" : 0,
            "restricao" : 1000
        }

        # Gera um float na Normal, arredonda para coletar o numero de nos de uma rota de um pedido
        # de 1 a 10 nós
        
        pedido["nos"] = int(
            np.random.normal(loc=5, scale=2, size=None)
        )
        
        if np.random.randint(1,10) > 9:
            r = np.random.randint(1,3)
            # Consideramos 3 tipos de pedidos sensiveis a transporte
            # muito sensiveis tem limite de 24h
            # sensiveis a limite de tempo 48h     
            # pouco sensiveis a limite de tempo 72h     
            if r == 1:
                pedido["restricao"] = 24
            elif r == 2:
                pedido["restricao"] = 48
            else:
                pedido["restricao"] = 72

        return pedido

    #sorteio do tempo de deslocamento em meio urbano por um caminhão de frota privada
    def sorteia_tempo_urbano_privado(self):
        
        # tempo de deslocamento em cidade
        tempo = int(np.random.lognormal(mean=50, sigma=30, size=None))

        # chance de algum imprevisto ocorrer no deslocamento na cidade
        if np.random.randint(1, 100) > 95:
            tempo += np.random.lognormal(mean=120, sigma=60, size=None)

        return tempo
    
    
    #sorteio do tempo de deslocamento em meio urbano por um caminhão de frota privada
    def sorteia_tempo_rodoviario_privado(self):
        
        # tempo de deslocamento em cidade
        tempo = np.random.

        # chance de algum imprevisto ocorrer no deslocamento na cidade
        if np.random.randint(1, 100) > 95:
            tempo += np.random.lognormal(mean=120, sigma=60, size=None)

        return tempo
    
    def plotar_histogramas_cenarios(self, salvar=False):

        if salvar:
            plt.savefig("histogramas_cenarios.png", dpi=200, bbox_inches='tight')

        plt.show()
        


if __name__ == "__main__":
    s = Simulacao()
    a = []
    print(s.inicia_pedido())
    # while len(a) < 100:
    #     a.append(s.inicia_pedido())

    # print(a)
    # import json

    # with open("cenario3.json", "r", encoding="utf-8") as f_json:
    #     dados = json.load(f_json)
    
    # m = Metricas(dados["info"]["prazo"], dados["info"]["vlr_multa"], dados["info"]["vlr_contrato"])


    # cenarios = f.simular_fases(qtde_simulacoes=100000, prep=dados["prep"], fund=dados["fund"], fundA=dados["fundA"], fundB=dados["fundB"],
    #               laje=dados["laje"], alvenaria=dados["alvenaria"], acab_interno=dados["acab_interno"], pint=dados["pint"],
    #               pintA=dados["pintA"], pintB=dados["pintB"])

    # cenarios, multa_media, prob_preju, (j, k) = m.calcula(cenarios)

    # c = 0
    # print("----------------------------------------------------------------")
    # for i in cenarios:
    #     print(f"Simulação {c:2}: Duração total: {i[0]:8} dias | " +
    #                 f"Custo total: R$ {i[1]:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.') +
    #                 f"| {dados['info']['vlr_contrato'] - i[1]:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.'))
    #     c+=1

    # print("----------------------------------------------------------------")
    # print(f"Multa media: R$ {multa_media:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.') + f" ({j} cenarios de {len(cenarios)})")
    # print(f"Considerado viavel pela diretoria de finanças da empresa: {dados['info']['mult_media'] <= multa_media}")
    # print(f"Probabilidade de prejuizo: {prob_preju} ({k} cenarios de {len(cenarios)})")

    # m.plotar_histogramas_cenarios(cenarios=cenarios, salvar=True)