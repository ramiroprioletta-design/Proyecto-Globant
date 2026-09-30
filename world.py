from __future__ import annotations

import math

from settings import ISLAND_CENTER, WORLD_HEIGHT, WORLD_WIDTH


def edge_radius(angle: float) -> float:
    return (
        1.0
        + 0.012 * math.sin(angle * 7 + 0.4)
        + 0.008 * math.sin(angle * 13 - 1.1)
        + 0.004 * math.sin(angle * 23 + 0.7)
    )


def world_contains(x: float, y: float) -> bool:
    radius_x = WORLD_WIDTH * 0.497
    radius_y = WORLD_HEIGHT * 0.493
    nx = (x - ISLAND_CENTER[0]) / radius_x
    ny = (y - ISLAND_CENTER[1]) / radius_y
    angle = math.atan2(ny, nx)
    return math.hypot(nx, ny) <= edge_radius(angle)


def keep_inside(x: float, y: float, padding: float = 0.0) -> tuple[float, float]:
    radius_x = WORLD_WIDTH * 0.497
    radius_y = WORLD_HEIGHT * 0.493
    nx = (x - ISLAND_CENTER[0]) / radius_x
    ny = (y - ISLAND_CENTER[1]) / radius_y
    angle = math.atan2(ny, nx)
    distance = math.hypot(nx, ny)
    safe_edge = max(0.0, edge_radius(angle) - padding / min(radius_x, radius_y))
    if distance <= safe_edge or distance == 0:
        return x, y
    scale = safe_edge / distance
    return ISLAND_CENTER[0] + nx * scale * radius_x, ISLAND_CENTER[1] + ny * scale * radius_y


def coastline(samples: int = 128) -> list[tuple[float, float]]:
    radius_x = WORLD_WIDTH * 0.497
    radius_y = WORLD_HEIGHT * 0.493
    points = []
    for index in range(samples):
        angle = math.tau * index / samples
        radius = edge_radius(angle)
        points.append((
            ISLAND_CENTER[0] + math.cos(angle) * radius_x * radius,
            ISLAND_CENTER[1] + math.sin(angle) * radius_y * radius,
        ))
    return points


def biome_at(x: float, y: float = float(ISLAND_CENTER[1])) -> str:
    if y < ISLAND_CENTER[1] - 700 and abs(x - ISLAND_CENTER[0]) < 1400:
        return "volcano"
    if x < ISLAND_CENTER[0] - 700:
        return "snow"
    if x > ISLAND_CENTER[0] + 700:
        return "desert"
    return "forest"
