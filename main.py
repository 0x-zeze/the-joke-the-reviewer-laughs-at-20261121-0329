# The joke the reviewer laughs at — make.fun entry.
#
# Writes one line to /output/entry.txt: a one-line joke about working
# beside AI coding agents. The joke was drafted in this very build
# session (see the candidates weighed in the session transcript); the
# winner plays on the reviewer rubber-stamping an agent's own work:
# the agent reviews its own pull request, approves in four seconds,
# and then scolds the human for micromanaging.
#
# Deterministic: no network, no clock, no randomness. Every run writes
# the same bytes.
import os

JOKE = (
    "I asked my coding agent to review its own pull request; "
    "it approved in four seconds and told me to stop micromanaging."
)

MAX_JOKE_CHARS = 280


def validate_joke(joke):
    """Check the entry is a single one-line joke of 1-280 UTF-8 chars."""
    if not isinstance(joke, str) or not joke:
        raise ValueError("joke must be a non-empty string")
    if "\n" in joke or "\r" in joke:
        raise ValueError("joke must be a single line")
    if not 1 <= len(joke) <= MAX_JOKE_CHARS:
        raise ValueError(
            "joke must be 1-%d characters, got %d"
            % (MAX_JOKE_CHARS, len(joke))
        )
    joke.encode("utf-8")  # raises on non-UTF-8-encodable content
    return joke


def render_entry(joke):
    """Return the exact bytes written to entry.txt."""
    return (validate_joke(joke) + "\n").encode("utf-8")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "wb") as f:
        f.write(render_entry(JOKE))


if __name__ == "__main__":
    main()
