# === Stage 1: Каркас модуля ===
# Project: AllowanceJar
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Child:
    name: str
    age: int
    allowance_per_week: float
    goal: Optional[str] = None


def make_demo_children() -> List[Child]:
    return [
        Child(name="Аня", age=8, allowance_per_week=300.0, goal="Плюшевый мишка"),
        Child(name="Боря", age=10, allowance_per_week=400.0, goal="Велосипед"),
        Child(name="Вика", age=7, allowance_per_week=250.0, goal=None),
    ]


def main() -> None:
    children = make_demo_children()
    for child in children:
        goal_text = child.goal if child.goal else "нет цели"
        print(f"{child.name}, {child.age} лет, "
              f"{child.allowance_per_week} руб./нед, цель: {goal_text}")


if __name__ == "__main__":
    main()
