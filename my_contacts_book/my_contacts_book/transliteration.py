import difflib

TRANS_CYRILLIC_TO_LATIN = {
    # Ваш словник перекладу тут
    'а': 'a', 'б': 'b', 'в': 'v', 'г': 'h', 'д': 'd', 'е': 'e', 'ё': 'yo', 'ж': 'zh',
    'з': 'z', 'и': 'i', 'й': 'j', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o',
    'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts',
    'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ы': 'y', 'э': 'e', 'ю': 'yu', 'я': 'ya',
    'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'H', 'Д': 'D', 'Е': 'E', 'Ё': 'YO', 'Ж': 'ZH',
    'З': 'Z', 'И': 'I', 'Й': 'J', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O',
    'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'KH', 'Ц': 'TS',
    'Ч': 'CH', 'Ш': 'SH', 'Щ': 'SHCH', 'Ы': 'Y', 'Э': 'E', 'Ю': 'YU', 'Я': 'YA'
}

def transliterate(text: str) -> str:
    """
    Transliterates Cyrillic text to Latin text.

    Args:
        text (str): The text to transliterate.

    Returns:
        str: The transliterated text.
    """
    return ''.join(TRANS_CYRILLIC_TO_LATIN.get(char, char) for char in text)

def suggest_command(user_input: str, commands: list[str]) -> str:
    """
    Suggests the closest matching command based on user input.

    Args:
        user_input (str): The user input text.
        commands (list[str]): The list of available commands.

    Returns:
        str: The suggested command or '' if no close match is found.
    """
    # Переведення введеного тексту у латиницю
    user_input_transliterated = transliterate(user_input)
    # Пошук найближчих команд
    closest_matches = difflib.get_close_matches(user_input_transliterated, commands, n=1, cutoff=0.1)
    
    # Відбір найближчої команди, якщо така є
    if closest_matches:
        return closest_matches[0]
    return ""