import matplotlib.pyplot as plt
import numpy as np

class Simulacao:

    def inicia_motorista(self):
        # inicializando motorista
        motorista = {
            "disponivel" : 1
        }
        
        return motorista

    def inicia_caminhao(self, chance_defeito):
        # inicializando caminhao
        caminhao = {
            "disponivel" : 1,
            "chance_defeito" : chance_defeito 
        }

        return caminhao
    
    #Primeira parte do DCA
    def inicia_pedido(self):

        # inicializando pedido
        # Gera um float na Normal, arredonda para coletar o numero de nos de uma rota de um pedido
        # de 1 a 10 nós
        pedido = {
            "nos" : int( np.random.normal(loc=5, scale=2, size=None)),
            "restricao" : 1000
        }
        
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

    # implementacao da pert, numpy + simulacao de distribuicoes
    def pert(self, o, m, p, lamb):

            alpha = 1 + lamb * ((m - o) / (p - o))
            beta = 1 + lamb * ((p - m) / (p - o))
            
            x = np.random.beta(alpha, beta, size=None)

            return  o + x * (p - o)
    
    #sorteio do tempo de deslocamento em meio urbano por um caminhão
    def sorteia_tempo_urbano(self, mean, sigma, chance_problema):
        
        # tempo de deslocamento em cidade
        tempo = int(np.random.lognormal(mean=mean, sigma=sigma, size=None))  

        # chance de algum imprevisto ocorrer no deslocamento na cidade
        if np.random.randint(1, 100) < chance_problema:
            tempo += np.random.lognormal(mean=120, sigma=60, size=None)

        return tempo

    #sorteio do tempo de deslocamento em meio urbano por um caminhão de frota privada
    def sorteia_tempo_rodoviario(self, c, d, scale, chance_problema, chance_parada):
        
        # tempo de deslocamento em rodovia
        tempo = float(burr_fast(c, d))

        # chance de algum imprevisto ocorrer no deslocamento em rodovia
        if np.random.randint(1, 100) < chance_problema:
            problema = np.random.lognormal(mean=1, sigma=0.5, size=None)
            tempo += problema
        # chance do nó ser uma parada
        if np.random.randint(1, 100) < chance_parada:

            parada = self.sorteia_parada(0.5, 1, 2)
            print(f"parada = {parada}")
            tempo += parada
        return (tempo, problema, parada)
    
    def sorteia_parada(self, tempo_o, tempo_m, tempo_p):

        # tempo de manobra + planejamento
        tempo = 0.45

        #sorteia tempo de descarga
        tempo += self.pert(tempo_o, tempo_m, tempo_p, 4)
    
        #sorteia tempo de carga
        tempo += self.pert(tempo_o, tempo_m, tempo_p, 4)

        return tempo 
    
    def sorteia_carga(self, tempo_o, tempo_m, tempo_p):

        # tempo de manobra + planejamento
        tempo = 0.45

        #sorteia tempo de carga
        tempo = self.pert(tempo_o, tempo_m, tempo_p, 4)

        return tempo

    
    def sorteia_descarga(self, tempo_o, tempo_m, tempo_p):

        # tempo de manobra + planejamento
        tempo = 0.45

        #sorteia tempo de descarga
        tempo = self.pert(tempo_o, tempo_m, tempo_p, 4)
    
        return tempo
    
    
def burr_fast(c, k):
    u = np.random.random()
    return ((1 - u) ** (-1 / k) - 1) ** (1 / c)

def plotar_distribuicao(dados):
    plt.figure(figsize=(12, 6))

    plt.hist(dados, bins=100, density=True, alpha=0.5, label="")

    plt.title("Comparação das distribuições")
    plt.xlabel("Valor")
    plt.ylabel("Densidade")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    s = Simulacao()
    
    # print(s.sorteia_tempo_rodoviario(2, 3, 1, 10, 40))
    


    # while len(a) < 100:
    #     a.append(s.inicia_pedido())
