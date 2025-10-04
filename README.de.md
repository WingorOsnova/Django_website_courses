Kurs-Shop (Django)

Admin name: guest
password: g123456g

Überblick
- Ein einfacher Kurskatalog/-shop mit Django und Bootstrap.
- REST-ähnliche API über django-tastypie.
- Lesen ist öffentlich; Schreibzugriffe erfordern einen API-Schlüssel.
- Admin mit Inline-Bearbeitung und optionalem django-jet Theme.

Hauptfunktionen
- Datenmodell: `Category` und `Course` (ForeignKey von Course zu Category).
- Web-UI: Liste aller Kurse und Kursdetailseite.
- Admin: Listenansichten, Inline-Kurse unter Kategorien, grundlegendes Branding.
- API: `GET` frei zugänglich; `POST/PUT/DELETE` per API-Schlüssel geschützt.
- API hydrate/dehydrate für saubere Nutzung von `category_id`.

Technologien
- Python 3.10+
- Django 4.0.8
- django-tastypie 0.15.1
- Bootstrap 5.3 (CDN)
- SQLite (Standard)
- Optional: django-jet (Admin-Theme)

Projektstruktur
- `base/` – Einstellungen, URLs, WSGI/ASGI.
- `shop/` – Domänen-App: Models, Views, URLs, Admin, Migrationen.
- `api/` – Tastypie Resources, Authentifizierung, URLs.
- `templates/` – Basislayout und Shop-Templates.
- `manage.py`, `requirements.txt`, `db.sqlite3`.

Lokal ausführen
1) Virtuelle Umgebung erstellen und aktivieren
   - `python -m venv .venv`
   - macOS/Linux: `source .venv/bin/activate`
   - Windows (PowerShell): `.venv\Scripts\Activate.ps1`

2) Abhängigkeiten installieren
   - `pip install -r requirements.txt`
   - Optional (Admin-Theme): `pip install django-jet`

3) Migrationen anwenden
   - `python manage.py migrate`

4) Superuser erstellen
   - `python manage.py createsuperuser`

5) Entwicklungsserver starten
   - `python manage.py runserver`
   - Web-UI: http://127.0.0.1:8000/
   - Admin: http://127.0.0.1:8000/admin/
   - API Root: http://127.0.0.1:8000/api/v1/

Web-UI
- Kursliste: `/` (Titel anklicken für Details)
- Kursdetails: `/<course_id>`

Admin
- Individuelle Titel und Inline-Bearbeitung von Kursen innerhalb von Kategorien.
- Falls `django-jet` nicht installiert ist, entfernen Sie `jet` und `jet.dashboard` aus `INSTALLED_APPS` in `base/settings.py` oder installieren Sie das Paket.

API (Tastypie)
- Root: `/api/v1/`
- Ressourcen:
  - `GET /api/v1/categories/`
  - `GET /api/v1/courses/`
  - `POST /api/v1/courses/` (API-Schlüssel erforderlich)
  - `PUT /api/v1/courses/<id>/` (API-Schlüssel erforderlich)
  - `DELETE /api/v1/courses/<id>/` (API-Schlüssel erforderlich)

Authentifizierung
- Lesen (`GET`) ist öffentlich.
- Schreiben (`POST/PUT/DELETE`) erfordert einen Tastypie API-Schlüssel.
- `username` und `api_key` als Query-Parameter oder per `Authorization`-Header übergeben (gemäß ApiKeyAuthentication von Tastypie).
- API-Schlüssel sind Django-Benutzern zugeordnet. Falls kein Schlüssel existiert, öffnen Sie den Benutzer im Admin und speichern Sie – der Schlüssel wird per Tastypie-Signal erzeugt (oder nutzen Sie ggf. einen verfügbaren Management-Befehl).

Kursfelder (API)
- Erforderlich bei Anlage/Änderung: `title` (str), `price` (float), `students_qty` (int), `reviews_qty` (int), `category_id` (int)
- In der Antwort ausgeschlossen: `created_at`, `reviews_qty`
- Besonderheiten:
  - hydrate: setzt `category_id` am `Course` Objekt
  - dehydrate: liefert `category_id` und eine einfache `category` Darstellung

Beispiele
- Kurse auflisten (öffentlich):
  - `curl http://127.0.0.1:8000/api/v1/courses/?format=json`

- Kurs anlegen (API-Schlüssel erforderlich):
  - `curl -X POST \
    -H "Content-Type: application/json" \
    -d '{"title":"Django Basics","price":49.0,"students_qty":100,"reviews_qty":10,"category_id":1}' \
    'http://127.0.0.1:8000/api/v1/courses/?username=<USER>&api_key=<API_KEY>&format=json'`

Schwerpunkte des Projekts
- Klare Trennung von Web-Views und API-Ressourcen.
- Einfaches, ausdrucksstarkes Datenmodell und Admin-UX (Inlines, Listendarstellung).
- Beispiel für Tastypie mit benutzerdefinierter Authentifizierung: offene Lesezugriffe, geschützte Schreibzugriffe.
- Saubere Template-Struktur mit Bootstrap und Navigation.

Hinweise
- Bei anderer Datenbank `DATABASES` in `base/settings.py` anpassen.
- In `requirements.txt` ist Django 4.0.8 angegeben; stellen Sie sicher, dass Ihre Python-Version kompatibel ist.

