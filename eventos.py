#!/usr/bin/env python
# encoding: utf-8
import cliente
import aleatorio
import servico


# Classe de onde vao ser derivados todos os eventos. Contem apenas os atributos e metodos comuns a todos os eventos.
# Nao havera instancias desta classe num simulador
class Evento:

    def __init__(self, i, sim, servico):
        self.instant = i  # Instante de ocorrencia do evento
        self.simulator = sim  # Simulador onde ocorre o evento
        self.servico = servico

    # Metodo de comparacao entre dois eventos.
    # Determina se o evento corrente ocorre primeiro, ou nao, do que o evento e1
    # Se sim, devolve true; se nao, devolve false
    # Usado para ordenar por ordem crescente de instantes de ocorrencia a lista de eventos do simulador
    def __cmp__(self, other):
        if self.instant < other.instant:
            return -1
        elif self.instant > other.instant:
            return 1
        else:
            return 0


# Classe que representa a chegada de um cliente. Deriva de Evento
class Chegada(Evento):

    def __init__(self, i, sim, media_cheg, servico):
        Evento.__init__(self, i, sim, servico)
        self.media_cheg = media_cheg

    # Metodo que descreve o evento. Para ser usado na listagem da lista de eventos.
    def __str__(self):
        return "Chegada\t[" + str(self.instant) + "]"

    # Metodo que executa as acoes correspondentes a chegada de um cliente
    def executa(self):
        # Coloca cliente no servico - na fila ou a ser atendido, conforme o caso
        self.servico.insereClient(cliente.Client(), self.servico.proximo_servico)
        # Agenda nova chegada para daqui a aleatorio.exponencial(self.simulator.media_cheg) instantes
        self.simulator.insereEvento(Chegada(self.simulator.instant + aleatorio.exponencial(self.media_cheg), self.simulator, self.media_cheg, self.servico))

# Classe que representa a saida de um cliente. Deriva de Evento
class Saida(Evento):

    def __init__(self, i, sim, tipo_servico, client, servico):
        Evento.__init__(self, i, sim, servico)
        self.tipo_servico = tipo_servico
        self.client = client

    # Metodo que descreve o evento. Para ser usado na listagem da lista de eventos.
    def __str__(self):
        return "Saida\t\t[" + str(self.instant) + "]"

    # Metodo que executa as acoees correspondentes a saida de um cliente
    def executa(self):
        if not self.servico.proximo_servico:
            self.servico.removeClient(self.tipo_servico)  # Retira cliente do servico
        else:
            self.servico.removeClient(self.tipo_servico)  # Retira cliente do servico
            self.servico.proximo_servico.insereClient(self.client, self.tipo_servico)


