import tkinter as tk
import simulador
import lista
import servico
import cliente
import eventos


FONT = ("Verdana", 12)


class Menu(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        wdw = tk.Frame(self)

        wdw.pack(side="top", fill="both", expand=True)

        self.frames = {}

        for F in (MenuStart, MenuSimulator):
            frame = F(wdw, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MenuStart)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class MenuStart(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Simulador SCC - Fábrica", font=FONT)
        label.pack(pady=10, padx=10)


        button = tk.Button(self, text="START",command=lambda: controller.show_frame(MenuSimulator), font = FONT, width=20)
        button.pack()

        button2 = tk.Button(self, text="SAIR", command=lambda: quit(), font = FONT, width=20)
        button2.pack(pady=20, padx=20)


class MenuSimulator(tk.Frame):

    def validate(self, action, index, value_if_allowed, prior_value, text, validation_type, trigger_type, widget_name):
        if value_if_allowed == '':
            return True
        elif text in '0123456789.-+':
            try:
                float(value_if_allowed)
                return True
            except ValueError:
                return False
        else:
            return False
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Introduzir valores: ", font=FONT)
        label.pack()

        vcmd = (self.register(self.validate), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

        #Tempo de simulação
        label_sim = tk.Label(self, text = "Tempo de simulação: ")
        temp_sim = tk.Entry(self, validate="key", validatecommand = vcmd)
        label_sim.pack()
        temp_sim.pack()
        temp_sim.focus_set()

        #Número de maquinas
        label_temp = tk.Label(self, text = "Número de máquinas: ")
        labem_temp = tk.Entry(self, validate="key", validatecommand = vcmd)


        #Média de Chegadas A
        label_chegA = tk.Label(self, text = "Média de chegadas A: ")
        chegA = tk.Entry(self, validate="key")
        label_chegA.pack()
        chegA.pack()
        chegA.focus_set()

        #Média de Chegadas B
        label_chegB = tk.Label(self, text = "Média de chegadas B: ")
        chegB = tk.Entry(self, validate ="key")
        label_chegB.pack()
        chegB.pack()
        chegB.focus_set()

        #Perfuração
        #Nº Atendedores A
        label_atendPerfA = tk.Label(self, text = "Nº Atendedores Perfuração A: ")
        perf_atendA = tk.Entry(self, validate="key")
        label_atendPerfA.pack()
        perf_atendA.pack()
        perf_atendA.focus_set()

        #Desvio Padrão A
        label_desvioPerfA = tk.Label(self, text="Desvio padrão Perfuração A:")
        perf_desvioA = tk.Entry(self, validate="key")
        label_desvioPerfA.pack()
        perf_desvioA.pack()
        perf_desvioA.focus_set()

        #Media serviço A
        label_mediaPerfA = tk.Label(self, text="Media de serviço Perfuração A: ")
        perf_mediaA = tk.Entry(self, validate="key")
        label_mediaPerfA.pack()
        perf_mediaA.pack()
        perf_mediaA.focus_set()

        #NºAtendedores B
        label_atendPerfB = tk.Label(self, text="Nº Atendedores Perfuração B: ")
        perf_atendB = tk.Entry(self, validate="key")
        label_atendPerfB.pack()
        perf_atendB.pack()
        perf_atendB.focus_set()

        #Desvio Padrão B
        label_desvioPerfB = tk.Label(self, text="Desvio padrão Perfuração B:")
        perf_desvioB = tk.Entry(self, validate="key")
        label_desvioPerfB.pack()
        perf_desvioB.pack()
        perf_desvioB.focus_set()

        #Media serviço B
        label_mediaPerfB = tk.Label(self, text="Media de serviço Perfuração B: ")
        perf_mediaB = tk.Entry(self, validate="key")
        label_mediaPerfB.pack()
        perf_mediaB.pack()
        perf_mediaB.focus_set()

        #Polimento
        #NºAtendores A
        label_atendPolA = tk.Label(self, text ="Nº Atendedores Polimento A: ")
        pol_attendA = tk.Entry(self, validate="key")
        label_atendPolA.pack()
        pol_attendA.pack()
        pol_attendA.focus_set()

        #Desvio Padrão A
        label_desvioPolA = tk.Label(self, text="Desvio padrão Polimento A:")
        pol_desvioA = tk.Entry(self, validate="key")
        label_desvioPolA.pack()
        pol_desvioA.pack()
        pol_desvioA.focus_set()

        #Media serviço A
        label_mediaPolA = tk.Label(self, text="Media de serviço Polimento A: ")
        pol_mediaA = tk.Entry(self, validate="key")
        label_mediaPolA.pack()
        pol_mediaA.pack()
        pol_mediaA.focus_set()

        #NºAtendores B
        label_mediaPolB = tk.Label(self, text="Nº atendedores Polimento B: ")
        pol_attendB = tk.Entry(self, validate="key")
        label_mediaPolB.pack()
        pol_attendB.pack()
        pol_attendB.focus_set()

        #Desvio Padrão B
        label_desvioPolB = tk.Label(self, text="Desvio padrão Polimento B:")
        pol_desvioB = tk.Entry(self, validate="key")
        label_desvioPolB.pack()
        pol_desvioB.pack()
        pol_desvioB.focus_set()

        #Media serviço B
        label_mediaPolB = tk.Label(self, text="Media de serviço Polimento B: ")
        pol_mediaB = tk.Entry(self, validate="key")
        label_mediaPolB.pack()
        pol_mediaB.pack()
        pol_mediaB.focus_set()

        #Envernizamento
        #NºAtendedores
        label_attendEnv = tk.Label(self, text = "Nº Atendores Envernizamento: ")
        env_atend = tk.Entry(self, validate = "key")
        label_attendEnv.pack()
        env_atend.pack()
        env_atend.focus_set()

        #Desvio Padrão
        label_desvioEnv = tk.Label(self, text="Desvio padrão Envernizamento: ")
        env_desvio = tk.Entry(self, validate="key")
        label_desvioEnv.pack()
        env_desvio.pack()
        env_desvio.focus_set()

        #Media Serviço
        label_mediaEnv = tk.Label(self, text="Média de serviço Envernizamento: ")
        env_media = tk.Entry(self, validate="key")
        label_mediaEnv.pack()
        env_media.pack()
        env_media.focus_set()

        button1 = tk.Button(self, text="SIMULAR", command= lambda:callback(), width = 10)
        button1.pack()

        button2 = tk.Button(self, text="MENU INICIAL", command=lambda: controller.show_frame(MenuStart), width = 10)
        button2.pack()

        def callback():
            s = simulador.Simulador()
            if env_media.get() != '' and env_desvio.get() != '' and env_atend.get() != '' and pol_mediaB.get() != '' and pol_desvioB.get() != '' and pol_attendA.get() != '' and pol_mediaA.get() != '' and pol_attendB.get() != '' and pol_mediaB.get() != '' and perf_atendA.get() != '' and perf_mediaA.get() != '' and perf_desvioA.get() != '' and perf_atendB.get() != '' and perf_mediaB.get() != '' and perf_desvioB.get() != '' and temp_sim.get() != '' and chegA.get() != '' and chegB.get() != '':
                s.client_queue_envernizamento = servico.Servico(s, 2, float(env_media.get()), float(env_desvio.get()), None, s.seed_envernizamento)
                s.client_queue_polimento_B = servico.Servico(s, 2, float(pol_mediaB.get()), float(pol_desvioB.get()), s.client_queue_envernizamento, s.seed_polimento_Bo)
                s.client_queue_perfuracao_B = servico.Servico(s, 2, float(perf_mediaB.get()), float(perf_desvioB.get()),s.client_queue_polimento_B, s.seed_perfuracao_B)
                s.client_queue_polimentoA = servico.Servico(s, 1, float(pol_mediaA.get()), float(pol_desvioA.get()), s.client_queue_envernizamento, s.seed_polimento_A)
                s.client_queue_perfuracaoA = servico.Servico(s, 1, float(perf_mediaA.get()), float(perf_desvioA.get()), s.client_queue_polimento_A, s.seed_perfuracao_A)
                s.execution_time = float(temp_sim.get())
                s.executa()
                self.destroy()

if __name__ == '__main__':
    app = Menu()
    app.mainloop()
