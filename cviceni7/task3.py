def load_measurements(path):
    """
    Načte měření ze souboru.
    Vrací dvojici: (seznam_mereni, seznam_chybnych_radku)
    kde seznam_mereni obsahuje n-tice (time, temperature).
    """
    measurements = []
    errors = []
    
    with open(path, 'r', encoding='utf-8') as file:
        for idx, line in enumerate(file, start=1):
            line = line.strip()
            
            # Přeskočení prázdných řádků (ale zaznamenáme číslo řádku)
            if not line:
                errors.append(idx)
                continue
                
            # Kontrola správného formátu (přítomnost středníku)
            if ';' not in line:
                errors.append(idx)
                continue
                
            time, temp_str = line.split(';', 1)
            
            try:
                # Pokus o převod teploty na desetinné číslo
                temperature = float(temp_str.strip())
                measurements.append((time.strip(), temperature))
            except ValueError:
                # Pokud převod selže (např. text "chyba"), řádek je chybný
                errors.append(idx)
                
    return measurements, errors


def summarize(measurements):
    """
    Vypočítá statistiky z platných měření.
    Vrací n-tici (minimum, maximum, průměr).
     Pokud je seznam prázdný, vrátí (None, None, None).
    """
    if not measurements:
        return None, None, None
        
    # Vytáhneme pouze teploty ze seznamu dvojic (čas, teplota)
    temperatures = [temp for _, temp in measurements]
    
    minimum = min(temperatures)
    maximum = max(temperatures)
    average = sum(temperatures) / len(temperatures)
    
    return minimum, maximum, average


def write_report(path, measurements, summary, errors):
    """
    Zapíše textový report do souboru, včetně statistik a chybných řádků.
    """
    minimum, maximum, average = summary
    
    with open(path, 'w', encoding='utf-8') as file:
        file.write("=== REPORT MĚŘENÍ TEPLOTY ===\n\n")
        
        file.write("Platná měření:\n")
        if measurements:
            for time, temp in measurements:
                file.write(f"  {time} -> {temp} °C\n")
        else:
            file.write("  Žádná platná měření.\n")
            
        file.write("\nStatistika:\n")
        if minimum is not None:
            file.write(f"  Minimální teplota: {minimum:.1f} °C\n")
            file.write(f"  Maximální teplota: {maximum:.1f} °C\n")
            file.write(f"  Průměrná teplota:  {average:.2f} °C\n")
        else:
            file.write("  Statistiky nelze spočítat (chybí data).\n")
            
        file.write("\nChybné a prázdné řádky:\n")
        if errors:
            file.write(f"  Čísla řádků s chybou: {', '.join(map(str, errors))}\n")
        else:
            file.write("  Žádné chybné řádky.\n")
