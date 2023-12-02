import PySimpleGUI as sg


def make_window() -> sg.Window:
    sg.theme("DefaultNoMoreNagging")

    pf_layout = [
        # [sg.Menu(menu_def, key='-MENU-')],
        [sg.Text("Selecione o tipo de pessoa física:")],
        [
            sg.OptionMenu(values=("Aluno", "Motorista"), k="-OPTION MENU-"),
            sg.Button("Selecionar"),
        ],
        # [sg.Checkbox("Checkbox", default=True, k="-CB-")],
        # [
        #     sg.Radio("Radio1", "RadioDemo", default=True, size=(10, 1), k="-R1-"),
        #     sg.Radio("Radio2", "RadioDemo", default=True, size=(10, 1), k="-R2-"),
        # ],
        # [
        #     sg.Spin([i for i in range(1, 11)], initial_value=10, k="-SPIN-"),
        #     sg.Text("Spin"),
        # ],
        # [
        #     sg.Multiline(
        #         "Demo of a Multi-Line Text Element!\nLine 2\nLine 3\nLine 4\nLine 5\nLine 6\nLine 7\nYou get the point.",
        #         size=(45, 5),
        #         expand_x=True,
        #         expand_y=True,
        #         k="-MLINE-",
        #     )
        # ],
        # [
        #     sg.Button("Button"),
        #     sg.Button("Popup"),
        #     sg.Button(image_data=sg.DEFAULT_BASE64_ICON, key="-LOGO-"),
        # ],
    ]

    pj_layout = [
        # [sg.Menu(menu_def, key='-MENU-')],
        [sg.Text("Selecione o tipo de pessoa jurídica:")],
        [
            sg.OptionMenu(
                values=("Funcionário", "Escola", "Veículo", "Contrato"),
                k="-OPTION MENU-",
            ),
        ],
        # [sg.Input(key="-INPUT-")],
        [sg.Checkbox("Checkbox", default=True, k="-CB-")],
        [
            sg.Radio("Radio1", "RadioDemo", default=True, size=(10, 1), k="-R1-"),
            sg.Radio("Radio2", "RadioDemo", default=True, size=(10, 1), k="-R2-"),
        ],
        [
            sg.Spin([i for i in range(1, 11)], initial_value=10, k="-SPIN-"),
            sg.Text("Spin"),
        ],
        [
            sg.Multiline(
                "Demo of a Multi-Line Text Element!\nLine 2\nLine 3\nLine 4\nLine 5\nLine 6\nLine 7\nYou get the point.",
                size=(45, 5),
                expand_x=True,
                expand_y=True,
                k="-MLINE-",
            )
        ],
        [
            sg.Button("Button"),
            sg.Button("Popup"),
            sg.Button(image_data=sg.DEFAULT_BASE64_ICON, key="-LOGO-"),
        ],
    ]

    # Título do app
    layout = [
        # [sg.MenubarCustom(menu_def, key="-MENU-", font="Courier 15", tearoff=True)],
        [
            sg.Text(
                "SchoolBus App",
                size=(38, 1),
                justification="center",
                font=("Helvetica", 16),
                relief=sg.RELIEF_RIDGE,
                k="-TEXT HEADING-",
                enable_events=True,
            )
        ],
    ]

    # Abas superiores
    layout += [
        [
            sg.TabGroup(
                [
                    [
                        sg.Tab("Criar PF", pf_layout),
                        sg.Tab("Criar PJ", pj_layout),
                        # sg.Tab("Asthetic Elements", asthetic_layout),
                        # sg.Tab("Graphing", graphing_layout),
                        # sg.Tab("Popups", popup_layout),
                        # sg.Tab("Theming", theme_layout),
                        # sg.Tab("Output", logging_layout),
                    ]
                ],
                key="-TAB GROUP-",
                expand_x=True,
                expand_y=True,
            ),
        ],
        [sg.Sizegrip()],
    ]

    window = sg.Window(
        "SchoolBus",
        layout,
        grab_anywhere=False,
        resizable=True,
        margins=(0, 0),
        use_custom_titlebar=True,
        finalize=True,
        keep_on_top=True,
    )

    window.set_min_size(window.size)
    # layout = [
    #     [sg.Text("O que deseja realizar?", size=50)],
    #     [sg.Button("Criar classe")],
    #     [sg.Button("Criar rota")],
    #     [sg.Button("Calcular demanda de rota")],
    #     [sg.Button("Exibir número de rotas criadas")],
    #     [sg.Button("Exibir número de pontos de parada")],
    #     [sg.Button("Sair")],
    # ]

    return window
