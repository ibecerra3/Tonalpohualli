# tonalpohualli/icons.py

from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
import re
from typing import Optional


@dataclass(frozen=True)
class IconPaths:
    day_signs_dir: Path
    numerals_dir: Path


def _project_root() -> Path:
    """
    Returns repo/project root assuming this file lives in:
      Tonalpohualli/tonalpohualli/icons.py
    and assets lives in:
      Tonalpohualli/assets/
    """
    return Path(__file__).resolve().parents[1]


def get_icon_paths() -> IconPaths:
    root = _project_root()
    return IconPaths(
        day_signs_dir=root / "assets" / "day_signs",
        numerals_dir=root / "assets" / "numerals",
    )


def slugify_day_sign(name: str) -> str:
    """
    'Cozcacuauhtli' -> 'cozcacuauhtli'
    'Quiahuitl' -> 'quiahuitl'
    Keeps letters/numbers, converts spaces to underscore.
    """
    s = name.strip().lower()
    s = s.replace(" ", "_")
    s = re.sub(r"[^a-z0-9_]+", "", s)
    return s


def find_day_sign_icon(day_sign: Optional[str]) -> Optional[Path]:
    if not day_sign:
        return None

    paths = get_icon_paths()
    filename = f"{slugify_day_sign(day_sign)}.png"
    p = paths.day_signs_dir / filename
    if p.exists():
        return p

    # Optional: allow SVG if you later switch to it
    svg = paths.day_signs_dir / f"{slugify_day_sign(day_sign)}.svg"
    if svg.exists():
        return svg

    return None


def find_numeral_icon(n: Optional[int]) -> Optional[Path]:
    if not n:
        return None
    paths = get_icon_paths()
    p = paths.numerals_dir / f"{int(n)}.png"
    if p.exists():
        return p
    svg = paths.numerals_dir / f"{int(n)}.svg"
    if svg.exists():
        return svg
    return None


def parse_year_bearer(year_bearer: Optional[str]) -> tuple[Optional[int], Optional[str]]:
    """
    Typical '4 Tochtli' -> (4, 'Tochtli')
    If parse fails, returns (None, None)
    """
    if not year_bearer:
        return None, None

    m = re.match(r"^\s*(\d+)\s+([A-Za-z]+)\s*$", year_bearer)
    if not m:
        return None, None

    return int(m.group(1)), m.group(2)