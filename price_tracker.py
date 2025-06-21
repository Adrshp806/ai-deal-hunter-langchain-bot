def check_price(current_price, target_price):
    discount = (target_price - current_price) / target_price
    return discount <= 0.20
