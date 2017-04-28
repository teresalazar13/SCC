#!/usr/bin/env python
# encoding: utf-8
import eventos
from aleatorio import Aleatorio

# Classe que representa um servico com uma fila de espera associada
class Servico:

    def __init__(self, sim, numero_de_maquinas, media_serv, desvio_padrao, proximo_servico, seed):
        self.fila = []  # Fila de espera do servico
        self.simulator = sim  # Referencia para o simulador a que pertence o servico
        self.estado = 0  # Variavel que regista o estado do servico: 0 - livre; 1 - ocupado
        self.temp_last = sim.instant  # Tempo que passou desde o ultimo evento. Neste caso 0, pq a sim ainda nao comecou
        self.atendidos = 0  # Numero de clientes atendidos ate ao momento
        self.soma_temp_esp = 0
        self.soma_temp_serv = 0
        self.numero_de_maquinas = numero_de_maquinas
        self.media_serv = media_serv
        self.desvio_padrao = desvio_padrao
        self.proximo_servico = proximo_servico
        self.seed = seed
        self.aux_rand = 0

    # Metodo que insere cliente no serviço
    def insereClient(self, client, tipo_servico):
        if self.estado < self.numero_de_maquinas:  # Se servico livre(se estado menor que numero de atendedores)
            self.estado += 1  # Fica ocupado e agenda saida do cliente
            self.simulator.insereEvento(eventos.Saida(self.simulator.instant + Aleatorio.normal(self.media_serv, self.desvio_padrao, self.seed)[0], self.simulator, tipo_servico, client, self))
        else:
            self.fila.append(client)  # Se servico ocupado, o cliente vai para a fila de espera

    # Metodo que remove cliente do serviço
    def removeClient(self, tipo_servico):
        self.atendidos += 1  # Regista que acabou de atender + 1 cliente
        if not self.fila:  # Se a fila esta vazia,
            self.estado -= 1  # liberta o servico
        else:
            # vai buscar proximo cliente a fila de espera e agenda a sua saida
            if self.aux_rand == 0:
                ran = Aleatorio.normal(self.media_serv, self.desvio_padrao, self.seed)
                random_number = ran[0]
                self.aux_rand = ran[1]
            else:
                random_number = self.aux_rand
                self.aux_rand = 0
            self.simulator.insereEvento(eventos.Saida(self.simulator.instant + random_number, self.simulator, tipo_servico, self.fila.pop(0), self))

    # Metodo que calcula valores para estatisticas, em cada passo da simulacao ou evento
    def act_stats(self):
        # Calcula tempo que passou desde o ultimo evento
        temp_desd_ult = self.simulator.instant - self.temp_last
        # Actualiza variavel para o proximo passo/eventosd
        self.temp_last = self.simulator.instant
        # Contabiliza tempo de espera na fila
        # para todos os clientes que estiveram na fila durante o intervalo
        self.soma_temp_esp += (len(self.fila) * temp_desd_ult)
        # Contabiliza tempo de atendimento
        self.soma_temp_serv += (self.estado * temp_desd_ult)

    # Metodo que calcula valores finais estatisticos
    def relat(self):
        # Tempo medio de espera na fila
        temp_med_fila = self.soma_temp_esp / (self.atendidos + len(self.fila))
        # Comprimento medio da fila de espera
        # self.simulator.instant neste momento e o valor do tempo de simulacao,
        # uma vez que a simulacao comecou em 0 e este metodo so e chamado no fim da simulacao
        comp_med_fila = self.soma_temp_esp / self.simulator.instant
        # Tempo medio de atendimento no servico
        utilizacao_serv = (self.soma_temp_serv / self.simulator.instant) / self.numero_de_maquinas

        # Apresenta resultados
        print("Tempo medio de espera", temp_med_fila)
        print("Comp. medio da fila", comp_med_fila)
        print("Utilizacao do servico", utilizacao_serv)
        print("Tempo de simulacao", self.simulator.instant)
        print("Numero de clientes atendidos", self.atendidos)
        print("Numero de clientes na fila", len(self.fila))
