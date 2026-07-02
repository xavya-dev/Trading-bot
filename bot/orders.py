from bot.client import client
from bot.logging_config import logger


def place_market_order(symbol, side, quantity):
    try:
        logger.info(f"Market Order Request: {symbol} {side} {quantity}")

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )

        logger.info(f"Market Order Success: {order}")

        return order

    except Exception as e:
        logger.error(f"Market Order Error: {str(e)}")
        raise


def place_limit_order(symbol, side, quantity, price):
    try:
        logger.info(f"Limit Order Request: {symbol} {side} {quantity} {price}")

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )

        logger.info(f"Limit Order Success: {order}")

        return order

    except Exception as e:
        logger.error(f"Limit Order Error: {str(e)}")
        raise