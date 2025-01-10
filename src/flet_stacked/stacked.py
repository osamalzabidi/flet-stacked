#!/usr/bin/python3
# -*- coding: utf-8 -*-


import flet as ft


class Stacked(ft.AnimatedSwitcher):
    """
    a custom Flet control for managing multiple pages with smooth animations.

    Example:
    ```
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
                alignment=ft.MainAxisAlignment.CENTER
            ),
        )


    if __name__ == "__main__":
        ft.app(target=main)

    ```
    """

    def __init__(
        self, pages: dict[str, ft.Control], index: str | int = 0, **kwargs
    ) -> None:
        kwargs.pop("content", None)
        self._pages = pages
        self._index = self._parse_index(index, pages)

        # default animations
        kwargs.setdefault("transition", ft.AnimatedSwitcherTransition.FADE)
        kwargs.setdefault("duration", 150)
        kwargs.setdefault("reverse_duration", 50)
        kwargs.setdefault("switch_in_curve", ft.AnimationCurve.LINEAR)
        kwargs.setdefault("switch_out_curve", ft.AnimationCurve.EASE_IN_CUBIC)

        super().__init__(self._pages.get(self._index), **kwargs)

    def _parse_index(
        self, index: str | int, pages: dict[str, ft.Control] = None
    ) -> None:
        pages = self._pages or pages
        if isinstance(index, int):
            return tuple(pages.keys())[index]
        return index

    def switch(self, route: str | int = 0) -> None:
        route: str = self._parse_index(route)
        assert route in self._pages, KeyError(f"'{route}' is not exists.")
        self._index = route
        self.content = self._pages.get(route)
        self.update()

    def go(self, route: str | int = 0) -> None:
        return self.switch(route)

    def get(self, route: str | int) -> ft.Control:
        return self._pages.get(route)

    def cur_route(self) -> str:
        return self._index

    def cur_page(self) -> ft.Control:
        return self._pages.get(self._index)

    def go_next(self) -> None:
        cur_index: int = tuple(self._pages.keys()).index(self._index)
        pages_count: int = len(self._pages)
        if cur_index < pages_count - 1:
            self.switch(cur_index + 1)

    def go_prev(self) -> None:
        cur_index: int = tuple(self._pages.keys()).index(self._index)
        if cur_index > 0:
            self.switch(cur_index - 1)