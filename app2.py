import asyncio

import flet

from flet import ThemeMode, View, AppBar, Colors, Button, FloatingActionButton, Icons, TextField, ListView, Text, Card, \
    Column, Row, Icon, ListTile, PopupMenuButton, PopupMenuItem, Dropdown, DropdownOption, FontWeight, Container, \
    CrossAxisAlignment


class Cadastro():
    def __init__(self, nome, telefone, serie, senha):
        self.nome = nome
        self.telefone = telefone
        self.serie = serie
        self.senha = senha


def main(page: flet.Page):
    # Configurações
    page.title = "Exemplos de listas"
    page.theme_mode = ThemeMode.DARK  # ou ThemeMode.DARK
    page.window.width = 400
    page.window.height = 700

    lista_dados = []

    # Funções
    # Função de navegar
    def navegar(route):
        asyncio.create_task(
            page.push_route(route)
        )

    def montar_lista_texto():
        list_view.controls.clear()

        for item in lista_dados:
            list_view.controls.append(
                Text(item)
            )

    def montar_lista_card():
        list_view.controls.clear()

        for item in lista_dados:
            list_view.controls.append(
                Card(
                    height=50,
                    content=Row([
                        Icon(Icons.PERSON),
                        Text(item)
                    ],
                        margin=8
                    ),

                )
            )

    def montar_lista_padrao():
        list_view.controls.clear()

        # Item é uma pessoa com nome, profissão e sexo
        for item in lista_dados:
            list_view.controls.append(
                ListTile(
                    leading=Icon(Icons.ACCOUNT_CIRCLE_SHARP),
                    title=(f"O nome do aluno é {item.nome}"),
                    subtitle=(f"Aluno está matriculado no {item.serie}"),
                    trailing=PopupMenuButton(
                        icon=Icons.MORE_VERT,
                        items=[
                            PopupMenuItem("Ver detalhes", icon=Icons.REMOVE_RED_EYE,
                                          on_click=lambda _, pessoa=item: ver_detalhes(pessoa)),
                            PopupMenuItem("Excluir", icon=Icons.DELETE, on_click=lambda: excluir(item)),
                        ]
                    ),
                )
            )

    def ver_detalhes(pessoa):
        text_nome.value = pessoa.nome
        text_telefone.value = pessoa.telefone
        text_serie.serie = pessoa.serie
        text_senha.value = pessoa.senha

        navegar("/detalhes")

    def excluir(item):
        lista_dados.remove(item)
        montar_lista_padrao()

    def salvar_dados():
        nome = input_nome.value.strip()
        telefone = input_telefone.value.strip()
        serie = input_serie.value.strip()
        senha = input_senha.value.strip()


        tem_erro = False
        if nome:
            input_nome.error = None
        else:
            input_nome.error = "Campo obrigatório"

        if telefone:
            input_telefone.error = None
        else:
            input_telefone.error = "Campo obrigatório"

        if serie:
            input_serie.error = None
        else:
            input_serie.error = "Campo obrigatório"

        if senha:
            input_senha.error = None
        else:
            input_senha.error = "Campo obrigatório"


        if not tem_erro:
            # Montar o objeto
            cadastro = Cadastro(
                nome=nome,
                telefone=telefone,
                serie=serie,
                senha=senha,
            )

            # add objeto na lista
            lista_dados.append(cadastro)

            input_nome.value = ""
            input_telefone.value = ""
            input_serie.value = ""
            input_senha.value = ""
            navegar("lista_padrao")

        montar_lista_padrao()

    # Função de gerenciar as telas (routes)
    def route_change():
        page.views.clear()
        page.views.append(
            View(
                route="/lista_padrao",
                controls=[
                    flet.AppBar(
                        title="TRUE TRADE",
                        bgcolor=Colors.RED_800
                    ),
                    list_view,
                ],
                floating_action_button=FloatingActionButton(
                    icon=Icons.ADD,
                    on_click=lambda: navegar("/form_cadastro"),
                )
            )
        )
        if page.route == "/form_cadastro":
            page.views.append(
                View(
                    route="/form_cadastro",
                    controls=[
                        flet.AppBar(
                            title="Cadastro do ALUNO",
                            bgcolor=Colors.RED_800
                        ),
                        input_nome,
                        input_telefone,
                        input_serie,
                        input_senha,
                        btn_salvar,
                    ]
                )
            )
        elif page.route == "/detalhes":
            page.views.append(
                View(
                    route="/detalhes",
                    controls=[
                        flet.AppBar(
                            title="Detalhes",
                        ),
                        Container(
                            Column([
                                text_nome,
                                Row([
                                    Icon(Icons.ACCOUNT_CIRCLE_SHARP, color=Colors.PRIMARY, size=20),
                                    text_nome
                                ]),
                                Row([
                                    Icon(Icons.ADD_IC_CALL, color=Colors.PRIMARY, size=20),
                                    text_telefone
                                ]),
                                Row([
                                    Icon(Icons.ASSIGNMENT_OUTLINED, color=Colors.PRIMARY, size=20),
                                    text_serie
                                ]),
                                Row([
                                    Icon(Icons.ATTACH_FILE, color=Colors.PRIMARY, size=20),
                                    text_senha
                                ]),
                            ],
                                horizontal_alignment=CrossAxisAlignment.CENTER
                            ),
                            bgcolor=Colors.RED_800,
                            padding=15,
                            border_radius=10,
                            width=400
                        )
                    ]
                )
            )

    # Função de voltar
    async def view_pop(e):
        if e.view is not None:
            page.views.remove(e.view)
            top_view = page.views[-1]
            await page.push_route(top_view.route)

    # Componentes
    input_nome = TextField(label="Nome", hint_text="Digite seu nome")
    input_telefone = TextField(label="Telefone", hint_text="Digite seu telefone")
    input_serie = TextField(label="Serie", hint_text="Digite sua serie")
    input_senha = TextField(label="senha", hint_text="Digite sua senha")
    btn_salvar = Button("Salvar", width=400, on_click=lambda: salvar_dados())
    text_nome = Text(weight=FontWeight.BOLD, size=24)
    text_telefone = Text()
    text_serie = Text()
    text_senha = Text()

    list_view = ListView(height=500)

    # Eventos
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    route_change()


flet.run(main)