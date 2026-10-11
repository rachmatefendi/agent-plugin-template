# Upload to GitHub

Suggested repository name: agent-plugin-template. Select the repository owner and visibility when creating it. Create an empty repository without a generated README, license, or gitignore so the prepared source can be pushed without an unrelated initial commit.

## From the extracted source package

The source archive contains tracked files and excludes local Git history, caches, generated distribution archives, and evaluation results. Extract it, enter the agent-plugin-template directory, and run:

```bash
python scripts/validate.py
python -m unittest discover -s tests -v
git init -b main
git add .
git commit -m "Add governed skills plugin template"
git remote add origin https://github.com/rachmatefendi/agent-plugin-template.git
git push -u origin main
```

Use the actual repository URL if a different name or owner is selected. GitHub authentication must be configured in the user's Git client. Do not force-push over an existing repository.

## Generate the installable plugin archive

```bash
python scripts/package.py
```

The dist archive is for the plugin host. The complete source repository also includes developer documentation, evaluation fixtures, and utilities.

## After upload

Confirm that README renders, the copyright attribution is visible, internal links resolve, and all intended source files are present. Enable the repository's template setting if reuse through GitHub's template workflow is desired. Keep all behavioral cases not_executed until their actual execution evidence exists.
