import itertools


class Page:
    """Represent text content on a page."""

    def __init__(self, top: str, bottom: str):
        self.top = top
        self.bottom = bottom


def init_pages():
    with open("Text.txt") as file:
        lines = file.read().splitlines()
    assert len(lines) == 802  # 0 - 400 inclusive, 2 lines per page
    pages = [
        Page(top.replace("\\n", "\n"), bottom.replace("\\n", "\n"))
        for top, bottom in itertools.batched(lines, 2)
    ]
    return pages


PAGES = init_pages()
