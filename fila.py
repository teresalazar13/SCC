#!/usr/bin/env python
# encoding: utf-8
import eventos


# Classe que representa um servico com uma fila de espera associada
class Fila:

    # Construtor
    def __init__(self, sim):
        self.fila = []  # Fila de espera do servico
        self.simulator = sim  # #Referencia para o simulador a que pertence o servico
        self.estado = 0  # Variavel que regista o estado do servico: 0 - livre; 1 - ocupado
        self.temp_last = sim.instant  # Tempo que passou desde o ultimo evento. Neste caso 0, porque a simulacao ainda nao comecou.
        self.atendidos = 0  # Numero de clientes atendidos ate ao momento
        self.soma_temp_esp = 0
        self.soma_temp_serv = 0

    def insereClient(self, client):
        """Metodo que insere cliente (client) no servico"""
        if self.estado == 0:  # Se servico livre,
            self.estado += 1  # fica ocupado e agenda saida do cliente c para daqui a self.simulator.media_serv instantes
            self.simulator.insereEvento(eventos.Saida(self.simulator.instant + self.simulator.media_serv, self.simulator))
        else:
            self.fila.append(client)  # Se servico ocupado, o cliente vai para a fila de espera

    def removeClient(self):
        """Metodo que remove cliente do servico"""
        self.atendidos += 1  # Regista que acabou de atender + 1 cliente
        if not self.fila:  # Se a fila esta vazia,
            self.estado -= 1  # liberta o servico
        else:
            # vai buscar proximo cliente a fila de espera
            self.fila.pop(0)
            # agenda a sua saida para daqui a self.simulator.media_serv instantes
            self.simulator.insereEvento(eventos.Saida(self.simulator.instant + self.simulator.media_serv, self.simulator))

    def act_stats(self):
        """Metodo que calcula valores para estatisticas, em cada passo da simulacao ou evento"""
        # Calcula tempo que passou desde o ultimo evento
        temp_desd_ult = self.simulator.instant - self.temp_last
        # Actualiza variavel para o proximo passo/evento
        self.temp_last = self.simulator.instant
        # Contabiliza tempo de espera na fila
        # para todos os clientes que estiveram na fila durante o intervalo
        self.soma_temp_esp += (len(self.fila) * temp_desd_ult)
        # Contabiliza tempo de atendimento
        self.soma_temp_serv += (self.estado * temp_desd_ult)

    def relat(self):
        """Metodo que calcula valores finais estatisticos"""
        # Tempo medio de espera na fila
        temp_med_fila = self.soma_temp_esp / (self.atendidos+len(self.fila))
        # Comprimento medio da fila de espera
        # self.simulator.instant neste momento e o valor do tempo de simulacao,
        # uma vez que a simulacao comecou em 0 e este metodo so e chamado no fim da simulacao
        comp_med_fila = self.soma_temp_esp / self.simulator.instant
        # Tempo medio de atendimento no servico
        utilizacao_serv = self.soma_temp_serv / self.simulator.instant

        # Apresenta resultados
        print("Tempo medio de espera", temp_med_fila)
        print("Comp. medio da fila", comp_med_fila)
        print("Utilizacao do servico", utilizacao_serv)
        print("Tempo de simulacao", self.simulator.instant)
        print("Numero de clientes atendidos", self.atendidos)
        print("Numero de clientes na fila", len(self.fila))
