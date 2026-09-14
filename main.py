"""Начальный сценарий системы управления заявками на закупку."""

from datetime import UTC, date, datetime


def calculate_total(price: float, quantity: int) -> float:
    return price * quantity


def get_approval_status(total: float, budget_limit: float) -> str:
    if total <= budget_limit:
        return "Заявка согласована"
    return "Заявка отклонена: превышен лимит бюджета"


def create_request_number(employee_id: str, request_date: date) -> str:
    return f"{employee_id}-{request_date:%Y%m%d}"


employee_name = "Анна Смирнова"
employee_id = "EMP-042"
product_name = "Ноутбук"
unit_price = 75000.0
quantity = int("2")
budget_limit = 160000.0
request_date = datetime.now(UTC).date()

total_cost = calculate_total(unit_price, quantity)
request_number = create_request_number(employee_id, request_date)
approval_status = get_approval_status(total_cost, budget_limit)

print(f"Заявка № {request_number}")
print(f"Сотрудник: {employee_name}")
print(f"Товар: {product_name}")
print(f"Количество: {quantity} шт.")
print(f"Общая стоимость: {total_cost:.2f} руб.")
print(f"Статус: {approval_status}")


if __name__ == "__main__":
    assert calculate_total(100.0, 2) == 200.0
    assert get_approval_status(200.0, 200.0) == "Заявка согласована"
