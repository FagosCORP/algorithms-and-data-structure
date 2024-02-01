def isPalindromo(message: str) -> bool:
    # Ele comeca  do ultimo ate o primeiro
    # 0::3
    # -1 do final ate o inicio
    # 4::-1
    # do final ate a 4
    return message == message[::-1]
