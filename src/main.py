import flet as ft

from pages import restaurants
from pages import order_history

def page(page: ft.Page):
	page.title = "Browse Restaurants!"

	pages = [
		restaurants.new(),
		order_history.new(),
		
	]
 
	index = 0

	pageArea = ft.Column(
		alignment=ft.MainAxisAlignment.START,
		controls=[pages[index]],
		expand=True
	)
 

	def rail_changed(e):
		index = e.control.selected_index
		pageArea.controls = [pages[index]]
		pageArea.update()

	

	page.add(
		ft.Row(
			[
				ft.NavigationRail(
					min_width=100,
					selected_index=index,
					
					destinations=[
						ft.NavigationRailDestination(
							icon=ft.Icons.RESTAURANT_OUTLINED,
							selected_icon=ft.Icons.RESTAURANT,
							label="Restaurants"
						),
						ft.NavigationRailDestination(
							icon=ft.Icons.HISTORY_OUTLINED,
							selected_icon=ft.Icons.HISTORY,
							label="Order History"
						),
					],
     
					on_change=rail_changed,
				),
    
				ft.VerticalDivider(width=1),
				pageArea,
			],
			expand=True,
		)
	)


ft.run(page)