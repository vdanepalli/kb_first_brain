# /// script
# requires-python = ">=3.12"
# ///
import sys
import urllib.parse


def make_badge(label, message, color="blue", link="", logo=""):
    # 1. Escape the core syntax (Dash -> Double Dash, Underscore -> Double Underscore)
    def escape_part(text):
        return text.replace("-", "--").replace("_", "__")

    label_safe = escape_part(label)
    message_safe = escape_part(message)

    # 2. Handle the "Space to Underscore" rule for Shields.io
    label_safe = label_safe.replace(" ", "_")
    message_safe = message_safe.replace(" ", "_")

    # 3. URL Encode special chars (commas, etc.) using Python's built-in library
    # We only encode the message part mostly, as labels are usually simple
    message_safe = urllib.parse.quote(message_safe)

    # 4. Construct URL
    url = f"https://img.shields.io/badge/{label_safe}-{message_safe}-{color}?style=flat-square"
    if logo:
        url += f"&logo={logo}&logoColor=white"

    # 5. Construct Markdown
    md = f"[![{label}]({url})]({link})"
    print(md)


if __name__ == "__main__":
    # Usage: uv run badge.py "Status" "Done, verified" "green"
    if len(sys.argv) < 3:
        print("Usage: badge.py <LABEL> <MESSAGE> [COLOR]")
        sys.exit(1)

    make_badge(
        label=sys.argv[1],
        message=sys.argv[2],
        color=sys.argv[3] if len(sys.argv) > 3 else "blue",
    )
