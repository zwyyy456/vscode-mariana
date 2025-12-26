"""Copyright © 2022 mightbesimon.com
All rights reserved.

Material belonging to others may have been
used under Creative Commons Licence or with
explicit or implicit permission.
"""

class ThemeColors:
    def __init__(self, file_in: str) -> None:
        self.colors = {
            "BLACK": "#000000",
            "BLUE": "#6699cc",
            "CORAL": "#f97b58",
            "DARK_0": "#181c20",
            "DARK_1": "#1c2126",
            "DARK_2": "#293038",
            "DARK_3": "#1e1e1e",
            "LIGHT_0": "#a6adb9",
            "LIGHT_1": "#d8dee9",
            "MARIANA": "#303841",
            "MEDIUM_0": "#303841",
            "MEDIUM_1": "#576675bf",
            "MEDIUM_2": "#627384",
            "MINT": "#99c794",
            "MINT_1": "#99c79433",
            "CORAL_1": "#f97b5833",
            "ORANGE": "#f9ae58",
            "PURPLE": "#c695c6",
            "RED": "#ec5f66",
            "SHADOW": "#00000080",
            "TEAL": "#5fb4b4",
            "TRANSPARENT": "#00000000",
            "WHITE": "#ffffff",
            "YELLOW": "#fac761",
        }
        self.file_in = file_in

    def export_theme(self, file_out: str):
        with open(self.file_in, "r") as f:
            content = f.read()
            content = content.replace(": ", ":").replace("\t", "").replace("\n", "")

        # Replace longer keys first to avoid partial replacements (e.g. MINT vs MINT_1).
        for name in sorted(self.colors, key=len, reverse=True):
            content = content.replace(name, self.colors[name])
        with open(file_out, "w") as f:
            f.write(content)


################################################################
#######                 MAIN STARTS HERE                 #######
################################################################
if __name__ == "__main__":
    (
        ThemeColors(file_in="themes/mariana-reference.json").export_theme(
            file_out="themes/mariana-color-theme.json"
        )
    )
