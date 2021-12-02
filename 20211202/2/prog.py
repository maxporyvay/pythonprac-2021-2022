class C:
    field: int = 42
    def __init__(self, value: int) -> None:
        self.field = value

    def string(self, level: int = 1) -> str:
        return f'{"<"*level}{self.field}{">"*level}'
