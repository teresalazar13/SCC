import tkinter as tk
import simulador
import servico


FONT = ("Verdana", 7)


class Menu(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        wdw = tk.Frame(self)

        wdw.pack(side="top", fill="both", expand=True)

        wdw.grid_rowconfigure(0, weight=3)
        wdw.grid_columnconfigure(0, weight=3)

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
        tk.Frame.__init__(self, parent, width=200, height=100, background="bisque")
        label = tk.Label(self, text="Simulador SCC - Fábrica", font=FONT)
        label.pack(pady=10, padx=10)

        button = tk.Button(self, text="START",command=lambda: controller.show_frame(MenuSimulator), font=FONT, width=20)
        button.pack()

        button2 = tk.Button(self, text="SAIR", command=lambda: quit(), font=FONT, width=20)
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

        # Tempo de simulação
        label_sim = tk.Label(self, text="Tempo de simulação: ", font=FONT)
        temp_sim = tk.Entry(self, validate="key", validatecommand=vcmd)
        label_sim.pack()
        temp_sim.pack()
        temp_sim.focus_set()

        # Número de maquinas
        label_temp = tk.Label(self, text="Número de máquinas: ", font=FONT)
        labem_temp = tk.Entry(self, validate="key", validatecommand=vcmd)

        # Média de Chegadas A
        label_chegA = tk.Label(self, text = "Média de chegadas A: ", font=FONT)
        chegA = tk.Entry(self, validate="key",validatecommand=vcmd)
        label_chegA.pack()
        chegA.pack()
        chegA.focus_set()

        # Média de Chegadas B
        label_chegB = tk.Label(self, text="Média de chegadas B: ", font=FONT)
        chegB = tk.Entry(self, validate="key", validatecommand=vcmd)
        label_chegB.pack()
        chegB.pack()
        chegB.focus_set()

        # Perfuração
        # Nº Atendedores A
        label_atendPerfA = tk.Label(self, text = "Nº Atendedores Perfuração A: ", font=FONT)
        perf_atendA = tk.Entry(self, validate="key", validatecommand=vcmd)
        label_atendPerfA.pack()
        perf_atendA.pack()
        perf_atendA.focus_set()

        # Desvio Padrão A
        label_desvioPerfA = tk.Label(self, text="Desvio padrão Perfuração A:", font=FONT)
        perf_desvioA = tk.Entry(self, validate="key", validatecommand=vcmd)
        label_desvioPerfA.pack()
        perf_desvioA.pack()
        perf_desvioA.focus_set()

        # Media serviço A
        label_mediaPerfA = tk.Label(self, text="Media de serviço Perfuração A: ", font=FONT)
        perf_mediaA = tk.Entry(self, validate="key", validatecommand=vcmd)
        label_mediaPerfA.pack()
        perf_mediaA.pack()
        perf_mediaA.focus_set()

        # NºAtendedores B
        label_atendPerfB = tk.Label(self, text="Nº Atendedores Perfuração B: ", font=FONT)
        perf_atendB = tk.Entry(self, validate="key", validatecommand=vcmd)
        label_atendPerfB.pack()
        perf_atendB.pack()
        perf_atendB.focus_set()

        # Desvio Padrão B
        label_desvioPerfB = tk.Label(self, text="Desvio padrão Perfuração B:", font=FONT)
        perf_desvioB = tk.Entry(self, validate="key", validatecommand=vcmd)
        label_desvioPerfB.pack()
        perf_desvioB.pack()
        perf_desvioB.focus_set()

        # Media serviço B
        label_mediaPerfB = tk.Label(self, text="Media de serviço Perfuração B: ", font=FONT)
        perf_mediaB = tk.Entry(self, validate="key", validatecommand=vcmd)
        label_mediaPerfB.pack()
        perf_mediaB.pack()
        perf_mediaB.focus_set()

        # Polimento
        # Nº Atendores A
        label_atendPolA = tk.Label(self, text ="Nº Atendedores Polimento A: ", font=FONT)
        pol_attendA = tk.Entry(self, validate="key", validatecommand=vcmd)
        label_atendPolA.pack()
        pol_attendA.pack()
        pol_attendA.focus_set()

        # Desvio Padrão A
        label_desvioPolA = tk.Label(self, text="Desvio padrão Polimento A:", font=FONT)
        pol_desvioA = tk.Entry(self, validate="key", validatecommand=vcmd)
        label_desvioPolA.pack()
        pol_desvioA.pack()
        pol_desvioA.focus_set()

        # Media serviço A
        label_mediaPolA = tk.Label(self, text="Media de serviço Polimento A: ", font=FONT)
        pol_mediaA = tk.Entry(self, validate="key", validatecommand=vcmd)
        label_mediaPolA.pack()
        pol_mediaA.pack()
        pol_mediaA.focus_set()

        # Nº Atendores B
        label_mediaPolB = tk.Label(self, text="Nº atendedores Polimento B: ", font=FONT)
        pol_attendB = tk.Entry(self, validate="key", validatecommand=vcmd)
        label_mediaPolB.pack()
        pol_attendB.pack()
        pol_attendB.focus_set()

        # Desvio Padrão B
        label_desvioPolB = tk.Label(self, text="Desvio padrão Polimento B:", font=FONT)
        pol_desvioB = tk.Entry(self, validate="key", validatecommand=vcmd)
        label_desvioPolB.pack()
        pol_desvioB.pack()
        pol_desvioB.focus_set()

        # Media serviço B
        label_mediaPolB = tk.Label(self, text="Media de serviço Polimento B: ", font=FONT)
        pol_mediaB = tk.Entry(self, validate="key", validatecommand=vcmd)
        label_mediaPolB.pack()
        pol_mediaB.pack()
        pol_mediaB.focus_set()

        # Envernizamento
        # Nº Atendedores
        label_attendEnv = tk.Label(self, text="Nº Atendores Envernizamento: ", font=FONT)
        env_atend = tk.Entry(self, validate="key", validatecommand=vcmd)
        label_attendEnv.pack()
        env_atend.pack()
        env_atend.focus_set()

        # Desvio Padrão
        label_desvioEnv = tk.Label(self, text="Desvio padrão Envernizamento: ", font=FONT)
        env_desvio = tk.Entry(self, validate="key", validatecommand=vcmd)
        label_desvioEnv.pack()
        env_desvio.pack()
        env_desvio.focus_set()

        # Media Serviço
        label_mediaEnv = tk.Label(self, text="Média de serviço Envernizamento: ", font=FONT)
        env_media = tk.Entry(self, validate="key", validatecommand=vcmd)
        label_mediaEnv.pack()
        env_media.pack()
        env_media.focus_set()

        button1 = tk.Button(self, text="SIMULAR", command=lambda:ResultWindow(), width=10)
        button1.pack()

        button2 = tk.Button(self, text="MENU INICIAL", command=lambda: controller.show_frame(MenuStart), width = 10)
        button2.pack()
        def ResultWindow():
            wd = tk.Tk()
            if env_media.get() != '' and env_desvio.get() != '' and env_atend.get() != '' and pol_mediaB.get() != '' and pol_desvioB.get() != '' and pol_attendA.get() != '' and pol_mediaA.get() != '' and pol_attendB.get() != '' and pol_mediaB.get() != '' and perf_atendA.get() != '' and perf_mediaA.get() != '' and perf_desvioA.get() != '' and perf_atendB.get() != '' and perf_mediaB.get() != '' and perf_desvioB.get() != '' and temp_sim.get() != '' and chegA.get() != '' and chegB.get() != '':
                s = simulador.Simulador(int(temp_sim.get()), float(chegA.get()), float(chegB.get()), float(env_media.get()), float(env_desvio.get()),
                        int(env_atend.get()), float(pol_mediaB.get()), float(pol_desvioB.get()), int(pol_attendB.get()), float(perf_mediaB.get()),
                        float(perf_desvioB.get()), int(perf_atendB.get()), float(pol_mediaA.get()), float(pol_desvioA.get()), int(pol_attendA.get()),
                        float(perf_mediaA.get()), float(perf_desvioA.get()), int(perf_atendA.get()))
                s.executa()
                #serv.relat(serv, app)
                # Apresenta resultados
                # print("Tempo medio de espera", temp_med_fila)
                # print("Comp. medio da fila", serv.comp_med_fila)
                # print("Utilizacao do servico", serv.utilizacao_serv)
                # print("Tempo de simulacao", serv.simulator.instant)
                # print("Numero de clientes atendidos", serv.atendidos)
                # print("Numero de clientes na fila", len(serv.fila))

            else:
                button = tk.Button(wd, text="Close", command = lambda:wd.destroy(), width = 10)
                label.pack()
                button.pack()


if __name__ == '__main__':
    app = Menu()
    app.mainloop()
