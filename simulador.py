#!/usr/bin/env python
# encoding: utf-8
import fila
import lista
import eventos


class Simulador:

    def insereEvento(self, event):
        self.event_list.insert_event(event)

    def __init__(self):
        # Medias das distribuicoes de chegadas e de atendimento no servico
        self.media_cheg = 1
        self.media_serv = 1.5

        # Numero de clientes que vao ser atendidos
        self.n_clientes = 100

        # Relogio de simulacao - variavel que contem o valor do tempo em cada instante
        self.instant = 0  # valor inicial a zero

        # Servico - pode haver mais do que um num simulador
        self.client_queue = fila.Fila(self)
        # Lista de eventos - onde ficam registados todos os eventos que vao ocorrer na simulacao
        # Cada simulador so tem uma
        self.event_list = lista.Lista(self)

        # Agendamento da primeira chegada
        # Se nao for feito, o simulador nao tem eventos para simular
        self.insereEvento(eventos.Chegada(self.instant, self))

    # Metodo executivo do simulador
    def executa(self):
        # Enquanto nao atender todos os clientes
        while self.client_queue.atendidos < self.n_clientes:
            print(self.event_list)  # Mostra lista de eventos - desnecessario; e apenas informativo
            event = self.event_list.remove_event()  # Retira primeiro evento (e o mais iminente) da lista de eventos
            self.instant = event.instant  # Actualiza relogio de simulacao
            self.act_stats()  # Actualiza valores estatisticos
            event.executa(self.client_queue)  # Executa evento
        self.relat()  # Apresenta resultados de simulacao finais

    # Metodo que actualiza os valores estatisticos do simulador
    def act_stats(self):
        self.client_queue.act_stats()

    # Metodo que apresenta os resultados de simulacao finais
    def relat(self):
        print("\n\n------------FINAL RESULTS---------------\n\n")
        self.client_queue.relat()


if __name__ == '__main__':
    s = Simulador()
    s.executa()
