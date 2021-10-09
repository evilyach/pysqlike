import sys


class InputBuffer:
    def __init__(self):
        self.buffer: str = None

    def read(self) -> None:
        try:
            self.buffer = input(self._print_prompt())
        except KeyboardInterrupt:
            sys.exit(0)
        except EOFError:
            print("\nExiting with Ctrl+D", file=sys.stderr)
            sys.exit(1)

    def close(self) -> None:
        pass

    def _print_prompt(self) -> str:
        return "db > "
