# FastAPI GitHub Workflow Practice

This repository is created to practice real-world Git and GitHub workflows using a FastAPI backend.

The main focus is not building a complex application, but learning:
- Branching strategy
- Pull Requests
- Code reviews
- Merge conflict resolution
- Team collaboration workflow

---

## Tech Stack

- Python
- FastAPI
- Uvicorn

---

## Project Setup

### 1. Clone the repository

```bash
git clone <repo-url>
cd fastapi-github-workflow-practice
```

---

### 2. Create virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows**
```bash
venv\Scripts\activate
```

**Linux/macOS**
```bash
source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Run the server

```bash
uvicorn app.main:app --reload
```

Visit:
- http://127.0.0.1:8000
- http://127.0.0.1:8000/docs

---

## Requirements File Rule

This project follows a **manual dependency management approach**.

### Important Rules:

- ❌ Do NOT use `pip freeze > requirements.txt`
- ❌ Do NOT add transitive dependencies (auto-installed packages)
- ✅ Only add **direct dependencies used in code**
- ✅ Keep `requirements.txt` clean and minimal

### Example `requirements.txt`

```txt
fastapi
uvicorn[standard]
```

As the project grows, you may add only the libraries you directly use:

```txt
fastapi
uvicorn[standard]
sqlalchemy
alembic
python-dotenv
```

Each new dependency must be added in the same Pull Request where it is used.

---

## Git Workflow Rules

### Branching Strategy

- `main` → stable code (protected branch)
- `feature/<name>` → new features
- `fix/<name>` → bug fixes
- `docs/<name>` → documentation updates

---

### Standard Workflow

```bash
git checkout main
git pull origin main

git checkout -b feature/<feature-name>
```

Make changes → commit → push:

```bash
git add .
git commit -m "feat: add user API"
git push origin feature/<feature-name>
```

Then open a Pull Request.

---

## Pull Request Rules

- One feature per PR
- Small and readable commits
- Must pass review before merging
- Resolve merge conflicts if any
- Always rebase before merging if needed

---

## Commit Convention

- feat: new feature
- fix: bug fix
- docs: documentation changes
- refactor: code improvements
- test: adding tests

Example:
```
feat: add task CRUD API
fix: resolve authentication bug
docs: update setup instructions
```

---

## Project Structure

```
app/
│
├── main.py
├── database.py
├── models.py
├── schemas.py
├── routers/
│   ├── users.py
│   ├── tasks.py
│   └── auth.py
└── services/
```

---

## Goal of This Practice

By the end of this exercise, the team should be comfortable with:

- Working in branches
- Handling merge conflicts
- Reviewing code via PRs
- Following structured backend development workflow
- Collaborating like a real software team

---

Happy Coding 🚀