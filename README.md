
# Task Manager

Ein einfaches Python-Programm zur Verwaltung von Aufgaben, das Aufgaben hinzufügen, aktualisieren, löschen und filtern kann. Die Aufgaben werden in einer JSON-Datei (`tasks-database.json`) gespeichert und können über verschiedene Befehle bearbeitet werden.

## Funktionen

- **`add`**: Fügt eine neue Aufgabe hinzu
- **`test`**: Fügt eine Testaufgabe hinzu
- **`update`**: Aktualisiert eine bestehende Aufgabe
- **`delete`**: Löscht eine spezifische Aufgabe
- **`deleteall`**: Löscht alle Aufgaben
- **`list`**: Listet alle Aufgaben auf
- **`show`**: Zeigt Details einer bestimmten Aufgabe an
- **`filter`**: Filtert Aufgaben nach Status

## Installation

1. **Klonen oder Herunterladen des Projekts:**
   ```bash
   git clone https://github.com/username/task-manager.git
   cd task-manager
   ```

2. **Python-Umgebung vorbereiten:**
   Stelle sicher, dass Python installiert ist (mindestens Version 3.6).

3. **Benötigte Bibliotheken:**  
   Dieses Programm benötigt keine zusätzlichen Bibliotheken; alle Module sind in Python enthalten.

## Verwendung

Führe das Skript über die Kommandozeile aus und gib den gewünschten Befehl als Argument an:

```bash
python task_manager.py [command]
```

### Verfügbare Befehle

- **add**  
  Fügt eine neue Aufgabe hinzu. Nach dem Aufruf wird der Benutzer zur Eingabe einer Aufgabenbeschreibung aufgefordert.

  ```bash
  python task_manager.py add
  ```

- **test**  
  Fügt eine Testaufgabe hinzu, die als Beispiel dient.  

  ```bash
  python task_manager.py test
  ```

- **update**  
  Aktualisiert eine bestehende Aufgabe. Nach dem Aufruf wird der Benutzer aufgefordert, eine Aufgaben-ID, neue Beschreibung und neuen Status einzugeben.

  ```bash
  python task_manager.py update
  ```

- **delete**  
  Löscht eine Aufgabe anhand ihrer ID.

  ```bash
  python task_manager.py delete
  ```

- **deleteall**  
  Löscht alle Aufgaben.

  ```bash
  python task_manager.py deleteall
  ```

- **list**  
  Listet alle Aufgaben auf.

  ```bash
  python task_manager.py list
  ```

- **show**  
  Zeigt Details zu einer bestimmten Aufgabe an, basierend auf der ID.

  ```bash
  python task_manager.py show
  ```

- **filter**  
  Filtert Aufgaben nach Status. Der Benutzer wird aufgefordert, den gewünschten Status (z. B. `open`, `in-progress`, `done`) einzugeben.

  ```bash
  python task_manager.py filter
  ```

## Datenstruktur

Die Aufgaben werden in einer JSON-Datei (`tasks-database.json`) gespeichert. Die Struktur ist wie folgt:

```json
{
  "tasks": {
    "1": {
      "description": "Example task",
      "status": "open",
      "created_at": "2024-11-02 12:00:00",
      "updated_at": "2024-11-02 12:00:00"
    },
    "2": {
      "description": "Another task",
      "status": "in-progress",
      "created_at": "2024-11-03 08:30:00",
      "updated_at": "2024-11-03 09:00:00"
    }
  }
}
```

## Fehlerbehandlung

Das Programm behandelt die folgenden Fehler:

- **Dateifehler**: Falls die Datei `tasks-database.json` nicht existiert, wird sie automatisch erstellt.
- **Ungültige Eingaben**: Falls eine ungültige Aufgaben-ID oder ein ungültiger Status eingegeben wird, informiert das Programm den Benutzer entsprechend.

## Beispiel

Ein Beispielablauf für das Hinzufügen, Aktualisieren und Löschen einer Aufgabe könnte wie folgt aussehen:

1. **Eine Aufgabe hinzufügen**:  
   ```bash
   python task_manager.py add
   ```
   Eingabeaufforderung: `What task would you like to add?`

2. **Die Aufgabe aktualisieren**:  
   ```bash
   python task_manager.py update
   ```
   Eingabeaufforderungen:
   - `What task would you like to update?`
   - `What is the new task description?`
   - `What is the new status?`

3. **Die Aufgabe anzeigen**:  
   ```bash
   python task_manager.py show
   ```

4. **Die Aufgabe löschen**:  
   ```bash
   python task_manager.py delete
   ```

## Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert.

---

Dieses Skript eignet sich ideal für einfache Aufgabenverwaltung und eignet sich für Benutzer, die eine schnelle Möglichkeit zur Verwaltung und Protokollierung von Aufgaben benötigen.
