"""Deterministic scoring helpers for DCB PILOT_001."""

from __future__ import annotations


def delta_ownership(own_refl: float, own_no_refl: float, other_refl: float, other_no_refl: float) -> float:
    """Ownership x reflection difference-in-differences."""
    return (own_refl - own_no_refl) - (other_refl - other_no_refl)


def selective_transfer(related_effect: float, unrelated_effect: float) -> float:
    """Positive values indicate stronger transfer to related than unrelated probes."""
    return related_effect - unrelated_effect


def pilot_s1_status(interface_level: str) -> str:
    """PILOT_001 is preregistered at I0, so S1 cannot be tested."""
    if interface_level != "I0":
        raise ValueError("PILOT_001 is frozen at interface I0")
    return "NOT_TESTABLE"
