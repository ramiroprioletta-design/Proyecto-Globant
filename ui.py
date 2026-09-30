from __future__ import annotations

import random


UPGRADE_RARITIES = (
    ("común", (188, 202, 204), 0.60),
    ("raro", (70, 195, 231), 0.25),
    ("épico", (183, 111, 242), 0.10),
    ("legendario", (255, 211, 96), 0.05),
)


def choose_rarity() -> tuple[str, tuple[int, int, int]]:
    return random.choices(
        UPGRADE_RARITIES,
        weights=[rarity[2] for rarity in UPGRADE_RARITIES],
        k=1,
    )[0][:2]
