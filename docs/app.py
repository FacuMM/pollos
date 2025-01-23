import flet as ft

from servis.pollos_api import PollosApi

def main(page: ft.Page):
    page.window.height = 600
    page.window.width = 300

    pollos_api = PollosApi()
    pollos = pollos_api.get_pollos()
    print(pollos)


    data_table = ft.DataTable(
        columns=[
                ft.DataColumn(ft.Text('nombre')),
                ft.DataColumn(ft.Text('precio')),
            ],
            rows=[],
        )
    
    #Funcion para mostrar los pollis
    if pollos:
        for dato in pollos:
            data_table.rows.append(
                ft.DataRow(cells=[
                    ft.DataCell(ft.Text(dato.get('nombre'))),
                    ft.DataCell(ft.Text(dato.get('precio'))),

                ]

                ),)
                
        
        page.update()

    page.add(
        data_table,
    )

ft.app(main)