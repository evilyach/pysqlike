import sys

from input_buffer import InputBuffer


class App:
    def __init__(self):
        pass

    def loop(self) -> None:
        input_buffer: InputBuffer = InputBuffer()

        while True:
            input_buffer.read()

            if input_buffer.buffer == ".exit":
                input_buffer.close()
                sys.exit(0)
            else:
                print(f"Unrecognized command '{input_buffer.buffer}'", file=sys.stderr)


def main():
    app = App()
    app.loop()


if __name__ == "__main__":
    main()