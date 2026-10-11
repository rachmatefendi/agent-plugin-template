"""Customize identity; preserve behavioral instructions."""
import argparse
import json
from pathlib import Path
from validate import NAME, ROOT

def customize(root, name, display_name, author):
    if not NAME.fullmatch(name) or len(name) > 64:
        raise ValueError('Name must be lowercase kebab-case, at most 64 characters')
    if not display_name.strip() or not author.strip():
        raise ValueError('Display name and author must be non-empty')
    path = Path(root) / 'plugin/plugin.json'
    data = json.loads(path.read_text())
    data['name'] = name
    data['author']['name'] = author
    ui = data['extensions']['com.openai']['interface']
    ui['displayName'] = display_name
    ui['developerName'] = author
    path.write_text(json.dumps(data, indent=2) + '\n')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--name', required=True)
    parser.add_argument('--display-name', required=True)
    parser.add_argument('--author', required=True)
    args = parser.parse_args()
    customize(ROOT, args.name, args.display_name, args.author)
    print('Manifest updated. Adapt descriptions, skills, and acceptance criteria before release.')
