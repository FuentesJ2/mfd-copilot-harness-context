# jira-context Portable Runtime

This folder is the portable runtime bundle for the Jira context CLI.

The preferred deployed shape is a compiled `jira-context.exe` plus this folder's support files.

## Runtime contract

- Run `jira-context.exe` from this folder.
- Configuration is stored in `.env` in this folder.
- Saved JSON files, including normalized fetches and optional raw payload captures, go in `jira-output/` in this folder.
- Check runtime identity with `jira-context.exe version --format json`.
- If command execution is unavailable, inspect `VERSION.json` in this folder.
