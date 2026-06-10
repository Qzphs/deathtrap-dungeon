import json


class Path:
    """Represent a path on a page."""

    def __init__(self, label: str, destination: int):
        """
        Initialise self with label and destination.

        `label` is the path text that is displayed to users.
        `destination` is the page number that the path leads to.
        """
        self.label = label
        self.destination = destination


PageJSON = dict[str, str | list[dict[str, str | int]]]


class Page:
    """Represent a page."""

    def __init__(self, top: str, bottom: str, paths: list[Path]):
        self.top = top
        self.bottom = bottom
        self.paths = paths

    @classmethod
    def from_json(cls, data: PageJSON):
        """
        Parse page from JSON data.

        `data` should be structured as follows:
        ```
        {
            "top": ...
            "bottom": ...
            "paths": [
                {
                    "label": ...
                    "destination": ...
                },
                ...
            ]
        }
        ```
        """
        top = data["top"].replace("\\n", "\n")
        bottom = data["bottom"].replace("\\n", "\n")
        paths = [Path(path["label"], path["destination"]) for path in data["paths"]]
        return Page(top, bottom, paths)

    def json(self):
        """Convert this page to JSON."""
        return {
            "top": self.top,
            "bottom": self.bottom,
            "paths": [
                {"label": path.label, "destination": path.destination}
                for path in self.paths
            ],
        }


def parse_pages():
    with open("pages.json") as file:
        data = json.load(file)
        pages = [Page.from_json(page) for page in data]
    return pages


PAGES = parse_pages()
