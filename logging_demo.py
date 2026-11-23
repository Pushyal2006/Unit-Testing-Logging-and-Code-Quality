import logging

logging.basicConfig(
    filename="application.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def process_order(price, discount, gst_rate):
    logging.debug("Starting order processing")

    if price < 0:
        logging.error("Invalid price: price cannot be negative")
        raise ValueError("Price cannot be negative")

    logging.info("Calculating discount")
    discount_amount = price * discount / 100

    discounted_price = price - discount_amount

    logging.info("Calculating GST")
    gst_amount = discounted_price * gst_rate / 100

    total = discounted_price + gst_amount

    if discount > 50:
        logging.warning("High discount applied")

    logging.info("Order processed successfully")
    logging.debug("Final order total: %s", total)

    return total


if __name__ == "__main__":
    print("Order Total:", process_order(1000, 10, 18))

    try:
        process_order(-100, 10, 18)
    except ValueError:
        print("Error handled successfully")