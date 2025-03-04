from functools import singledispatch, singledispatchmethod

@singledispatch
def log_event(event):
    raise NotImplementedError(f"Brak implementacji dla typu: {type(event)}")

@log_event.register
def _(event: str):
    print(f"[log_event] Obsługa zdarzenia str: {event}")

@log_event.register
def _(event: int):
    print(f"[log_event] Obsługa zdarzenia int: {event}")

# Obsługa zdarzeń typu dict
@log_event.register
def _(event: dict):
    print(f"[log_event] Obsługa zdarzenia dict: {event}")


class EventHandler:
    def __init__(self):
        self.event_count = 0
    @singledispatchmethod
    def handle_event(self, event):
        """Domyślna obsługa zdarzeń"""
        raise NotImplementedError(f"Nieobsługiwany typ zdarzenia: {type(event)}")

    @handle_event.register
    def _(self, event: str):
        self.event_count += 1
        print(f"[EventHandler] Obsługa zdarzenia str: {event}")

    @handle_event.register
    def _(self, event: int):
        self.event_count += 1
        print(f"[EventHandler] Obsługa zdarzenia int: {event}")

    @handle_event.register
    def _(self, event: list):
        self.event_count += 1
        print(f"[EventHandler] Obsługa zdarzenia list: {event}")


class DerivedHandler(EventHandler):

    @EventHandler.handle_event.register
    def _(self, event: int):
        self.event_count += 1
        print(f"[DerivedHandler] Obsługa zdarzenia int: {event}")

    @EventHandler.handle_event.register
    def _(self, event: float):
        self.event_count += 1
        print(f"[DerivedHandler] Obsługa zdarzenia float: {event}")


# Demonstracja użycia
if __name__ == "__main__":
    # Globalna funkcja logowania zdarzeń
    print("=== Globalne logowanie zdarzeń ===")
    log_event("Uruchomienie systemu")
    log_event(404)
    log_event({"typ": "error", "opis": "Nieznany błąd"})

    # Klasa obsługująca zdarzenia
    print("\n=== Klasa EventHandler ===")
    handler = EventHandler()
    handler.handle_event("Zdarzenie logowania")
    handler.handle_event(123)
    handler.handle_event(["zdarzenie1", "zdarzenie2", "zdarzenie3"])

    # Obsługa nieobsługiwanego typu
    print("\n=== Obsługa nieobsługiwanego typu ===")
    try:
        log_event(3.14)  # Nieobsługiwany typ w log_event
    except NotImplementedError as e:
        print(e)

    try:
        handler.handle_event(set([1, 2, 3]))  # Nieobsługiwany typ w handle_event
    except NotImplementedError as e:
        print(e)

    # Klasa DerivedHandler
    print("\n=== Klasa DerivedHandler ===")
    derived_handler = DerivedHandler()
    derived_handler.handle_event("Inne zdarzenie tekstowe")
    derived_handler.handle_event(789)  # Obsługa zmieniona dla int
    derived_handler.handle_event(3.14)  # Obsługa float zarejestrowana w DerivedHandler

    # Niespodzianka: prosze sprawdzic co zobaczymy?
    handler.handle_event(12356789)
