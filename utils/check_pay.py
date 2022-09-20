from pyqiwip2p.p2p_types.errors import QiwiError
from loader import p2p


async def check_pay(bill_id: int):
    """Проверка платежа
    Если платеж с переданным номером существует, то возвращается его статус, иначе None"""
    try:
        check = await p2p.check(bill_id=bill_id)
    except QiwiError:
        pass
    else:
        return check.status
