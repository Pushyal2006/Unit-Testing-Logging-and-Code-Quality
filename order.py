def calculate_discount(price, discount):
    if price < 0:
        raise ValueError("Price cannot be negative")

    if discount < 0 or discount > 100:
        raise ValueError("Discount must be between 0 and 100")

    return price * discount / 100


def calculate_gst(price, gst_rate):
    if price < 0:
        raise ValueError("Price cannot be negative")

    if gst_rate < 0:
        raise ValueError("GST rate cannot be negative")

    return price * gst_rate / 100


def calculate_order_total(price, discount, gst_rate):
    discount_amount = calculate_discount(price, discount)
    discounted_price = price - discount_amount
    gst_amount = calculate_gst(discounted_price, gst_rate)

    return discounted_price + gst_amount


if __name__ == "__main__":
    price = 1000
    discount = 10
    gst_rate = 18

    total = calculate_order_total(price, discount, gst_rate)

    print("Original Price:", price)
    print("Discount:", discount, "%")
    print("GST:", gst_rate, "%")
    print("Final Order Total:", total)