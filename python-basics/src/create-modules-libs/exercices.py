def isPalindromo(message: str) -> bool:
    # Ele comeca  do ultimo ate o primeiro
    return message == message[::-1]
