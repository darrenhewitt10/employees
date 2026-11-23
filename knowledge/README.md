# Knowledge folders

One folder per agent (`knowledge/<agent-name>/`). Each agent reads its own folder before every answer, so this is where you give an expert extra material: your preferences, past decisions, notes from your CPA or lawyer, papers, vendor terms.

- **Shared research for the whole team** belongs in `docs/`, not here.
- **Never** put secrets, account numbers or licensed vendor data in these folders: the repo is pushed to GitHub.
- **Personal details** (finances, tax situation) are visible to anyone who can see the GitHub repo. Keep the repo private if you add them, and keep them to summaries.
- Each folder's `README.md` lists what belongs there.
- New agents get a folder too (the meta-agent creates it; the validator checks it exists).
