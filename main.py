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


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
