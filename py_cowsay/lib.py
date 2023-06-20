import textwrap

from rich.console import Console
from rich.containers import Lines
from rich.text import Text

console = Console()

COW_TEXT = r"""
\
 \
   ^__^
   (oo)\_______
   (__)\       )\/\
       ||----w |
       ||     ||
""".strip()


def wrap_lines(lines: list[str], max_width=40) -> Lines:
    """
    Wrap lines using ``Text.wrap`` for each line and join them.
    """

    wrapped_lines = Lines()

    for line in lines:
        wrapped_lines.extend(
            Text(line).wrap(
                console,
                width=max_width,
            )
        )

    for line in wrapped_lines:
        line.rstrip()

    return wrapped_lines


def generate_bubble(message: str) -> str:
    lines = [line.strip() for line in message.strip().split("\n")]
    wrapped_lines = wrap_lines([line for line in lines if line])

    text_width = max(map(len, wrapped_lines))
    output = [
        "  " + "_" * text_width,
        " /" + " " * text_width + "\\",
    ]
    output.extend(
        f"| {line}" + " " * (text_width - len(line) + 1) + "|" for line in wrapped_lines
    )
    output.append(" \\" + "_" * text_width + "/")
    return "\n".join(output)


def say(message: str, *, bold: bool):
    bubble = generate_bubble(message)
    bubble_width = max(map(len, bubble.split("\n")))
    cow_text_shift = min(bubble_width // 2, 10)

    style = "bold" if bold else None
    console.print(bubble, style=style)
    console.print(textwrap.indent(COW_TEXT, " " * cow_text_shift))
