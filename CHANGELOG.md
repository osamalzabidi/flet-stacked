# CHANGELOG

## v1.0.2

- Changed: the argument `pages` has been rename to `routes`
- Chnaged: `cur_page` method has been rename to `cur_control`

## v1.0.3

- Added: `on_route_change` argument.
- Updated: Bug Fix
- Updated: Code Improvment

## v1.0.4

- Added: `*args` and `**kwargs` to `switch` method to pass them into `on_route_change`.

## v1.1.0

- Added: `go_back` alias method
- Removed: built-in excption handler on call `on_route_change` callback method
- Fixed: `get` method
- Changed: `switch` method and ther instance methods return `Tuple[str, ft.Control]` insted `ft.Contorl`