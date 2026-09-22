import asyncio
import flet
from flet import ThemeMode, View, Colors, Button, FloatingActionButton, Icons, TextField, ListView, Icon, Text, Column, \
    Pagelet, NavigationBar, NavigationBarDestination, ScrollMode, FontWeight, TextOverflow, Card, \
    Container, Row, ListTile, PopupMenuButton, PopupMenuItem, CrossAxisAlignment
from src.api_endpoints import get_itens, get_meus_itens, get_notificacao


def cadastrarse(nome, telefone, serie, senha):
    pass


def main(page: flet.Page):
    # CONFIGURAÇÕES
    page.title = "Exemplo Cafeteira"
    page.theme_mode = ThemeMode.DARK
    page.window.width = 400
    page.window.height = 700

    lista_dados = []

    # FUNÇÕES
    # navegar
    def navegar(route):
        asyncio.create_task(
            page.push_route(route)
        )

    def ver_detalhes(cadastrarse):
        text_nome.value = cadastrarse.nome
        text_telefone.value = cadastrarse.telefone
        text_serie.value = cadastrarse.serie
        text_senha.value = cadastrarse.senha

        navegar("/detalhes")

    def salvar_dados():
        nome = input_nome.value
        telefone = input_telefone.value
        serie = input_serie.value
        senha = input_senha.value

        tem_erro = False
        if nome:
            input_nome.error = None
        else:
            input_nome.error = "Campo Obrigatório"
            tem_erro = True

        if telefone:
            input_telefone.error = None
        else:
            input_telefone.error = "Campo Obrigatório"
            tem_erro = True

        if serie:
            input_serie.error = None
        else:
            input_serie.error = "Campo Obrigatório"
            tem_erro = True

        if senha:
            input_senha.error = None
        else:
            input_senha.error = "Campo Obrigatório"
            tem_erro = True

        if not tem_erro:
            p1 = cadastrarse(nome=nome.strip(), telefone=telefone.strip(), serie=serie.strip(), senha=senha.strip())
            lista_dados.append(p1)
        navegar("/lista_padrao")

    def montar_lista_cadastro():
        print("Cadastro")
        list_view = ListView()
        for item in lista_dados:
            list_view.controls.append(
            Card(
                height=50,
                content=Row([
                    Text(item["nome"], weight=FontWeight.BOLD, color=Colors.BLUE_900),
                    Text(item["telefone"], max_lines=4, overflow=TextOverflow.ELLIPSIS, color=Colors.GREY),
                    Text(item["serie"], max_lines=4, overflow=TextOverflow.ELLIPSIS, color=Colors.GREY),
                    Text(item["senha"], max_lines=4, overflow=TextOverflow.ELLIPSIS, color=Colors.GREY),
                ]),
                margin=8
            )
            )

    # gerenciar telas(routes)
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
                    list_view

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
                            title="Cadastro",
                            bgcolor=Colors.RED_800

                        ),
                        input_nome,
                        input_telefone,
                        input_serie,
                        input_senha,
                        btn_cadastrarse,

                    ]
                )
            )



        elif page.route == "/detalhes":
            page.views.append(
                View(
                    route="/detalhes",
                    controls=[
                        flet.AppBar(
                            title="TRUETRADE",
                            bgcolor=Colors.RED_800

                        ),

                    ]
                )
            )

    # voltar
    async def view_pop(e):
        if e.view is not None:
            page.views.remove(e.view)
            top_view = page.views[-1]
            await page.push_route(top_view.route)

    # COMPONENTES

    text_nome = Text()
    text_telefone = Text()
    text_serie = Text()
    text_senha = Text()

    input_nome = TextField(label="Digite seu nome")
    input_telefone = TextField(label="Digite seu telefone")
    input_serie = TextField(label="Digite a sua serie")
    input_senha = TextField(label="Digite a sua senha")
    btn_cadastrarse = Button("Cadastrar-se", width=400, on_click=lambda: salvar_dados(), color=Colors.RED_800)
    list_view = ListView(height=500)



    # EVENTOS
    page.on_route_change = route_change
    page.on_view_pop = view_pop


    #  eventos
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change()


flet.run(main)
