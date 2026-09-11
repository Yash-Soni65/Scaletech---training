

import logging


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


def calculate_total(price, quantity):
    logger.debug("calculate_total() called")

    logger.debug(
        "Price=%s, Quantity=%s",
        price,
        quantity
    )

    total = price * quantity

    logger.info("Total calculated: %s", total)

    return total


logger.info("Application started")

result = calculate_total(100, 5)

logger.info("Final result: %s", result)