"""Parser fixture module with diverse Python syntax constructs."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Iterable


class Status(Enum):
    NEW = "new"
    ACTIVE = "active"
    CLOSED = "closed"


@dataclass(slots=True)
class Record:
    id: int
    name: str
    status: Status = Status.NEW

    def label(self) -> str:
        return f"{self.id}:{self.name}:{self.status.value}"


def normalize(text: str) -> str:
    parts = [chunk.strip().lower() for chunk in text.split(",") if chunk.strip()]
    return "|".join(parts)


def summarize(records: Iterable[Record]) -> dict[str, int]:
    summary: dict[str, int] = {member.value: 0 for member in Status}
    for record in records:
        match record.status:
            case Status.NEW:
                summary["new"] += 1
            case Status.ACTIVE:
                summary["active"] += 1
            case Status.CLOSED:
                summary["closed"] += 1
    return summary


async def fetch_record_name(record_id: int) -> str:
    return f"record-{record_id}"


def main() -> None:
    records = [
        Record(1, normalize("Alpha, Beta"), Status.ACTIVE),
        Record(2, normalize("Gamma"), Status.NEW),
        Record(3, normalize("Delta"), Status.CLOSED),
    ]

    for entry in records:
        print(entry.label())

    print(summarize(records))


if __name__ == "__main__":
    main()
