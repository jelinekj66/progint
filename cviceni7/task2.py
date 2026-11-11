import sys
import os
from datetime import datetime

FILENAME = "journal.txt"

def add_entry():
    """Načte poznámku z příkazové řádky a přidá ji do souboru."""
    if len(sys.argv) < 3:
        print("Chyba: Zadejte text poznámky. Použití: python journal.py add \"Text poznámky\"")
        return
    
    # Spojí případné další argumenty do jednoho textu
    text = " ".join(sys.argv[2:])
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    line = f"{timestamp} | {text}\n"
    
    # Režim přidávání 'a' (append) vytvoří soubor, pokud neexistuje
    with open(FILENAME, "a", encoding="utf-8") as file:
        file.write(line)
    print("Poznámka byla úspěšně uložena.")

def list_entries():
    """Vypíše všechny záznamy očíslované od 1. Funguje i když soubor neexistuje."""
    if not os.path.exists(FILENAME):
        print("Deník je zatím prázdný (soubor neexistuje).")
        return
        
    with open(FILENAME, "r", encoding="utf-8") as file:
        lines = file.readlines()
        
    if not lines:
        print("Deník je prázdný.")
        return
        
    for index, line in enumerate(lines, start=1):
        print(f"{index}. {line.strip()}")

def search_entries():
    """Vypíše záznamy obsahující hledaný text."""
    if len(sys.argv) < 3:
        print("Chyba: Zadejte hledaný text. Použití: python journal.py search \"hledaný výraz\"")
        return
        
    query = " ".join(sys.argv[2:]).lower()
    
    if not os.path.exists(FILENAME):
        print("Deník je prázdný, nelze vyhledávat.")
        return
        
    found = False
    with open(FILENAME, "r", encoding="utf-8") as file:
        for index, line in enumerate(file, start=1):
            if query in line.lower():
                print(f"{index}. {line.strip()}")
                found = True
                
    if not found:
        print(f"Žádný záznam neobsahuje text: '{query}'")

def main():
    if len(sys.argv) < 2:
        print("Použití: python journal.py [add|list|search] [text]")
        return
        
    command = sys.argv[1].lower()
    
    if command == "add":
        add_entry()
    elif command == "list":
        list_entries()
    elif command == "search":
        search_entries()
    else:
        print(f"Neznámý příkaz: '{command}'. Použijte add, list nebo search.")

if __name__ == "__main__":
    main()
