# JsonUI
A JSON based web UI for desktop applications built in Python.

## Idea
### UI -> Server -> UI
- Represent entire app UI data as a single JSON + an optional JSON schema to denote preferred structure (like tabs, drop downs) aka GET API
- Whenever a variable is updated by user in front end, an update API is triggered with the variable's JSON path and value aka PUT API or PATCH API

### Server -> UI
### Option 1: Long Polling
- Use long polling with GET API for server to push updates to client (technically it is still UI -> Server -> UI)
- Share a CRC or equivalent ID representing entire JSON. When making a GET request, UI will send this CRC ID as argument and if there are any updates, the server immediately responds with an update. If there are no updates, the API waits for the timeout (say 20s) and responds with empty.
- UI immediately reinitiates another long poll GET request
- For initial call, the CRC ID will be empty for which server immediately responds with the entire JSON
- For subsequent updates, the server can send patch updates of JSON subsets, instead of resending entire JSON for each update.

### Option 2: Web Sockets
TBD

# Demo
Run the backend service:
```
cd backend
uv run fastapi dev main.py
```
Then open frontend/index.html in browser & you can interact with it.