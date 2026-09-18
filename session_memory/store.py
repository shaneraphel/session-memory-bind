"""Persistent memory keyed by session."""

from __future__ import annotations

import time

MEMORY: dict[str, list] = {}


def remember(text: str, session_id: str | None = None) -> None:
    if not session_id:
        raise ValueError("memory write requires a session id")
    MEMORY.setdefault(session_id, []).append({"text": text, "ts": time.time()})
