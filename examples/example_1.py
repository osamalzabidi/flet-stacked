import flet as ft
from flet_stacked import Stacked


def main(page: ft.Page):
    page.title = "Flet Stacked Example 1"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.window.width = page.window.height = 600

    pages = {
        "home": ft.Text("Home Page", size=30),
        "about": ft.Text("About Page", size=30),
        "contact": ft.Text("Contact Page", size=30),
    }

    stacked = Stacked(pages, index="home")

    def go_to_about(e):
        stacked.switch("about")

    def next_page(e):
        stacked.go_next()

    def prev_page(e):
        stacked.go_prev()

    page.add(
        stacked,
        ft.Row(
            [
                ft.ElevatedButton("Go to About", on_click=go_to_about),
                ft.ElevatedButton("Next", on_click=next_page),
                ft.ElevatedButton("Previous", on_click=prev_page),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
    )


if __name__ == "__main__":
    ft.app(target=main)
