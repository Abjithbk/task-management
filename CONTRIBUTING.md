# Contributing Guidelines

This document explains how to contribute to this repository using a proper Git + GitHub workflow.

The goal is to simulate real-world team development practices.

---

## 🚨 Golden Rules

- ❌ Never push directly to `main`
- ❌ Never work on `main`
- ❌ Do not commit unrelated changes
- ❌ Do not mix multiple features in one branch

- ✅ Always create a feature branch
- ✅ Always open a Pull Request
- ✅ Always get review before merging
- ✅ Keep commits small and meaningful

---

## 📌 Branching Strategy

Use this naming convention:

- `feature/<feature-name>` → new features  
- `fix/<bug-name>` → bug fixes  
- `docs/<docs-name>` → documentation updates  
- `refactor/<module-name>` → code improvements  

### Examples:

```bash
feature/user-api
feature/task-crud
fix/login-error
docs/readme-update
refactor/database-layer
```

---

## 🚀 Workflow

### 1. Start from updated main

```bash
git checkout main
git pull origin main
```

---

### 2. Create a new branch

```bash
git checkout -b feature/<feature-name>
```

---

### 3. Make changes

Write clean, modular code.

---

### 4. Commit changes

Use meaningful commit messages:

```bash
git add .
git commit -m "feat: add user creation API"
```

### Commit Types:

- `feat:` new feature
- `fix:` bug fix
- `docs:` documentation
- `refactor:` code improvements
- `test:` adding tests

---

### 5. Push branch

```bash
git push origin feature/<feature-name>
```

---

### 6. Open Pull Request (PR)

- Provide clear description
- Mention what you implemented
- Link related issue (if any)

---

### 7. Code Review Process

Before merging:

- At least 1 reviewer approval required
- Fix review comments if any
- Ensure code runs without errors

---

### 8. Sync with latest main (if needed)

If main updates while you are working:

```bash
git fetch origin
git rebase origin/main
```

Resolve conflicts manually if they occur.

---

## ⚔️ Merge Conflict Rule

If a conflict occurs:

- Do NOT panic
- Open the conflicting file
- Decide correct final version
- Remove conflict markers
- Test the code
- Commit resolved changes

---

## 🧠 Code Quality Expectations

- Keep functions small and clean
- Avoid duplicate logic
- Use proper naming conventions
- Follow FastAPI best practices
- Keep API responses consistent

---

## 📁 Example Workflow

```bash
git checkout main
git pull origin main

git checkout -b feature/task-api

# work on code

git add .
git commit -m "feat: implement task CRUD API"

git push origin feature/task-api
```

Then open PR → review → merge.

---

## 🎯 Goal

This repository is not just for coding.

It is to learn:

- Real team collaboration
- Git branching strategy
- Conflict resolution
- Code review culture
- Professional development workflow

---

## 💬 Reminder

Think before committing:
> “Would I understand this change in 3 months?”

If not, improve it before pushing.

---