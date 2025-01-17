#!/usr/bin/python3
# -*- coding: utf-8 -*-


from typing import Callable, Dict, Optional, Union

import flet as ft


class Stacked(ft.AnimatedSwitcher):
    """
    a custom Flet control for managing multiple routes with smooth animations.

    Example:
    ```
    import flet as ft
    from flet_stacked import Stacked


    def main(page: ft.Page):
        page.title = "Flet Stacked Example 1"
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        page.window.width = page.window.height = 600

        routes = {
            "home": ft.Text("Home Page", size=30),
            "about": ft.Text("About Page", size=30),
            "contact": ft.Text("Contact Page", size=30),
        }

        stacked = Stacked(routes, index="home")

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
        self,
        routes: Dict[str, ft.Control],
        index: Union[str, int] = 0,
        on_route_change: Optional[Callable[[str], None]] = None,
        **kwargs,
    ) -> None:

        self._routes = routes
        self._index = self._parse_route(index, routes)
        self._on_route_change = on_route_change

        # default animations
        kwargs.setdefault("transition", ft.AnimatedSwitcherTransition.FADE)
        kwargs.setdefault("duration", 150)
        kwargs.setdefault("reverse_duration", 50)
        kwargs.setdefault("switch_in_curve", ft.AnimationCurve.LINEAR)
        kwargs.setdefault("switch_out_curve", ft.AnimationCurve.EASE_IN_CUBIC)

        kwargs.pop("content", None)
        super().__init__(self._routes.get(self._index), **kwargs)

    def _parse_route(
        self, index: Union[str, int], routes: Dict[str, ft.Control] = None
    ) -> str:
        routes = self._routes or routes
        if isinstance(index, int):
            return tuple(routes.keys())[index]
        return index

    def switch(self, route: Union[str, int] = 0) -> ft.Control:
        route: str = self._parse_route(route)
        assert route in self._routes, KeyError(f"'{route}' is not exists.")
        self._index = route
        self.content = self._routes.get(route)
        self.update()

        if self._on_route_change is not None:
            try:
                self._on_route_change(route)
            except Exception as e:
                print(e)

        return self.content

    def get(self, route: Union[str, int]) -> ft.Control:
        return self._routes.get(route)

    def cur_route(self) -> str:
        return self._index

    def cur_control(self) -> ft.Control:
        return self._routes.get(self._index)

    def cur_page(self) -> ft.Control:
        return self.cur_control()

    def go(self, route: Union[str, int] = 0) -> ft.Control:
        return self.switch(route)

    def go_next(self) -> ft.Control:
        cur_index: int = tuple(self._routes.keys()).index(self._index)
        routes_count: int = len(self._routes)
        if cur_index < routes_count - 1:
            return self.switch(cur_index + 1)

    def go_prev(self) -> ft.Control:
        cur_index: int = tuple(self._routes.keys()).index(self._index)
        if cur_index > 0:
            return self.switch(cur_index - 1)
