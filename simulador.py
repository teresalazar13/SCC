#!/usr/bin/env python
# encoding: utf-8
import servico
import lista
import eventos

# TODO -> VERIFICAR QUANDO USAR DISTRIBUICAO NORMAL OU DISTRIBUICAO EXPONENCIAL NEGATIVA

class Simulador:

    def __init__(self):
        # Tempo de execucao
        self.execution_time = 480

        # Medias das distribuicoes de chegadas e de atendimento no servico
        media_cheg_A = 5
        media_cheg_B = 1.33
        media_serv_perfuracao_A = 2
        media_serv_polimento_A = 4
        media_serv_perfuracao_B = 0.75
        media_serv_polimento_B = 3
        media_serv_envernizamento = 1.4

        # Desvios-padrao
        desvio_padrao_perfuracao_A = 0.7
        desvio_padrao_polimento_A = 1.2
        desvio_padrao_perfuracao_B = 0.3
        desvio_padrao_polimento_B = 1
        desvio_padrao_envernizamento = 0.3

        # Seeds
        seed_perfuracao_A = 10
        seed_polimento_A = 20
        seed_perfuracao_B = 30
        seed_polimento_B = 40
        seed_envernizamento = 50

        # Numero de clientes que vao ser atendidos
        self.n_clientes = 100

        # Relogio de simulacao - variavel que contem o valor do tempo em cada instante
        self.instant = 0  # valor inicial a 0

        # Servicos
        self.client_queue_envernizamento = servico.Servico(self, 2, media_serv_envernizamento, desvio_padrao_envernizamento, None, seed_envernizamento)
        self.client_queue_polimento_B = servico.Servico(self, 2, media_serv_polimento_B, desvio_padrao_polimento_B, self.client_queue_envernizamento, seed_polimento_B)
        self.client_queue_perfuracao_B = servico.Servico(self, 1, media_serv_perfuracao_B, desvio_padrao_perfuracao_B, self.client_queue_polimento_B, seed_perfuracao_B)
        self.client_queue_polimento_A = servico.Servico(self, 1, media_serv_polimento_A, desvio_padrao_polimento_A, self.client_queue_envernizamento, seed_polimento_A)
        self.client_queue_perfuracao_A = servico.Servico(self, 1, media_serv_perfuracao_A, desvio_padrao_perfuracao_A, self.client_queue_polimento_A, seed_perfuracao_A)

        # Lista de eventos - onde ficam registados todos os eventos que vao ocorrer na simulacao
        self.event_list = lista.Lista(self)

        # Agendamento da primeira chegada. Se nao for feito, o simulador nao tem eventos para simular
        self.insereEvento(eventos.Chegada(self.instant, self, media_cheg_A, self.client_queue_perfuracao_A))
        self.insereEvento(eventos.Chegada(self.instant, self, media_cheg_B, self.client_queue_perfuracao_B))

    def insereEvento(self, event):
        self.event_list.insert_event(event)

    # Metodo executivo do simulador
    def executa(self):
        # Enquanto o tempo de execucao nao acabar
        while self.instant < self.execution_time:
            # print(self.event_list)  # Mostra lista de eventos - desnecessario; e apenas informativo
            event = self.event_list.remove_event()  # Retira primeiro evento (e o mais iminente) da lista de eventos
            self.instant = event.instant  # Actualiza relogio de simulacao
            self.act_stats()  # Actualiza valores estatisticos
            event.executa()  # Executa eventos
        self.relat()  # Apresenta resultados de simulacao finais

    # Metodo que actualiza os valores estatisticos do simulador
    def act_stats(self):
        # print("\n\n------------STATS - PERFURACAO A---------------\n\n")
        self.client_queue_perfuracao_A.act_stats()
        # print("\n\n------------STATS - POLIMENTO A---------------\n\n")
        self.client_queue_polimento_A.act_stats()
        # print("\n\n------------STATS - PERFURACAO B---------------\n\n")
        self.client_queue_perfuracao_B.act_stats()
        # print("\n\n------------STATS - POLIMENTO B---------------\n\n")
        self.client_queue_polimento_B.act_stats()
        # print("\n\n------------STATS - ENVERNIZAMENTO---------------\n\n")
        self.client_queue_envernizamento.act_stats()

    # Metodo que apresenta os resultados de simulacao finais
    def relat(self):
        print("\n\n------------FINAL RESULTS - PERFURACAO A---------------\n\n")
        self.client_queue_perfuracao_A.relat()
        print("\n\n------------FINAL RESULTS - POLIMENTO A---------------\n\n")
        self.client_queue_polimento_A.relat()
        print("\n\n------------FINAL RESULTS - PERFURACAO B---------------\n\n")
        self.client_queue_perfuracao_B.relat()
        print("\n\n------------FINAL RESULTS - POLIMENTO B---------------\n\n")
        self.client_queue_polimento_B.relat()
        print("\n\n------------FINAL RESULTS - ENVERNIZAMENTO---------------\n\n")
        self.client_queue_envernizamento.relat()


if __name__ == '__main__':
    s = Simulador()
    s.executa()
