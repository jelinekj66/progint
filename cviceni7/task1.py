def text_stats(path):
    stats = {
        "all_lines": 0,
        "none_lines": 0,
        "words": 0,
        "chars": 0,
        "longest_line": 0
    }
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            stats["all_lines"] +=1
            stripped_line = line.strip("\r\n")
            if stripped_line.strip():
                stats["none_lines"] +=1
            words_count = len(stripped_line.split())
            stats["words"] +=1
            line_len = len(stripped_line)
            stats["chars"] += line_len
            if line_len > stats["longest_line"]:
                stats["longest_line"] = line_len
    return stats
if __name__ == "__main__":
    file_path = input("Zadejte cestu k textovému souboru: ")
    
    try:
        vysledky = text_stats(file_path)
        
        print("\n--- Statistiky textu ---")
        print(f"Celkový počet řádků:          {vysledky['all_lines']}")
        print(f"Počet neprázdných řádků:      {vysledky['none_lines']}")
        print(f"Celkový počet slov:           {vysledky['words']}")
        print(f"Celkový počet znaků (bez \\n): {vysledky['chars']}")
        print(f"Délka nejdelšího řádku:       {vysledky['longest_line']}")
        
    except FileNotFoundError:
        print(f"\nChyba: Soubor na zadané cestě '{file_path}' nebyl nalezen. Zkontrolujte prosím překlepy.")
    except PermissionError:
        print(f"\nChyba: Nemáte oprávnění ke čtení souboru '{file_path}'.")
    except Exception as e:
        print(f"\nDošlo k neočekávané chybě: {e}")