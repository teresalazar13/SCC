#!/usr/bin/env python
# encoding: utf-8
import fila
import lista
import eventos


# TODO - Distinguir entre os vários serviços, com filas de espera separadas e tempos de atendimento diferentes --
# TODO - Distinguir entre cliente A e B, que já foi perfurado ou polido e nao criar clientes ao calhas
# TODO - Neste momento, o evento de Saida tira o cliente da simulação, nós queremos que este vá para o próximo serviço --
# TODO - Adicionar numero de maquinas --
# TODO - O nr número de máquinas, tp de atendimentos e variação em cada serviço numa interface grafica


class Simulador:

    def __init__(self):
        # Tempo de execucao. Simulador para quando instant < execution_time
        self.execution_time = 1

        # Medias das distribuicoes de chegadas e de atendimento no servico
        media_cheg_A = 5
        media_cheg_B = 1.33
        media_serv_perfuracao_A = 1.5
        media_serv_polimento_A = 1.5
        media_serv_perfuracao_B = 1.5
        media_serv_polimento_B = 1.5
        media_serv_envernizamento = 1.5

        # Desvios-padrao
        desvio_padrao_perfuracao_A = 1.5
        desvio_padrao_polimento_A = 1.5
        desvio_padrao_perfuracao_B = 1.5
        desvio_padrao_polimento_B = 1.5
        desvio_padrao_envernizamento = 1.5

        # Numero de clientes que vao ser atendidos
        self.n_clientes = 100

        # Relogio de simulacao - variavel que contem o valor do tempo em cada instante
        self.instant = 0  # valor inicial a zero

        # Servicos
        self.client_queue_envernizamento = fila.Fila(self, 2, media_serv_envernizamento, desvio_padrao_envernizamento, None)
        self.client_queue_polimento_B = fila.Fila(self, 2, media_serv_polimento_B, desvio_padrao_polimento_B, self.client_queue_envernizamento)
        self.client_queue_perfuracao_B = fila.Fila(self, 1, media_serv_perfuracao_B, desvio_padrao_perfuracao_B, self.client_queue_polimento_B)
        self.client_queue_polimento_A = fila.Fila(self, 1, media_serv_polimento_A, desvio_padrao_polimento_A, self.client_queue_envernizamento)
        self.client_queue_perfuracao_A = fila.Fila(self, 1, media_serv_perfuracao_A, desvio_padrao_perfuracao_A, self.client_queue_polimento_A)

        # Lista de eventos - onde ficam registados todos os eventos que vao ocorrer na simulacao
        self.event_list = lista.Lista(self)

        # Agendamento da primeira chegada. Se nao for feito, o simulador nao tem eventos para simular
        self.insereEvento(eventos.Chegada(self.instant, self, media_cheg_A, None))
        self.insereEvento(eventos.Chegada(self.instant, self, media_cheg_B, None))

    def insereEvento(self, event):
        self.event_list.insert_event(event)

    # Metodo executivo do simulador
    def executa(self):
        # Enquanto nao atender todos os clientes
        # TODO - deve ser mudado para enquanto o tempo nao tive passado (done)
        while self.instant < self.execution_time:
            # print(self.event_list)  # Mostra lista de eventos - desnecessario; e apenas informativo
            event = self.event_list.remove_event()  # Retira primeiro evento (e o mais iminente) da lista de eventos
            self.instant = event.instant  # Actualiza relogio de simulacao
            self.act_stats()  # Actualiza valores estatisticos

            # Executa eventos
            event.executa(self.client_queue_perfuracao_A)
            event.executa(self.client_queue_polimento_A)
            event.executa(self.client_queue_perfuracao_B)
            event.executa(self.client_queue_polimento_B)
            event.executa(self.client_queue_envernizamento)
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
