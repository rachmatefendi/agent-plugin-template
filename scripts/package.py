"""Create a reproducible plugin archive containing only installable source."""
import gzip
import io
import json
import tarfile
import tempfile
from pathlib import Path
from validate import ROOT, validate, validate_plugin_links

def package(root=ROOT):
    root = Path(root).resolve()
    problems = validate(root)
    if problems:
        raise ValueError('\n'.join(problems))
    source = root / 'plugin'
    manifest = json.loads((source / 'plugin.json').read_text())
    name, version = manifest['name'], manifest['version']
    files = sorted(source.rglob('*'))
    for path in files:
        if path.is_symlink():
            raise ValueError('Symlinks are not allowed')
        if any(part in ('.env', '.git', '__pycache__', 'node_modules', '.venv') for part in path.relative_to(source).parts):
            raise ValueError('Excluded content in plugin source: ' + str(path))
        if path.name.startswith('.env.') or path.suffix in ('.pyc', '.pem', '.key'):
            raise ValueError('Secret/dependency file rejected: ' + str(path))
    output = root / 'dist' / f'{name}-{version}.tar.gz'
    output.parent.mkdir(exist_ok=True)
    with output.open('wb') as raw:
        with gzip.GzipFile(filename='', mode='wb', fileobj=raw, mtime=0) as gz:
            with tarfile.open(fileobj=gz, mode='w') as archive:
                for path in files:
                    if not path.is_file():
                        continue
                    data = path.read_bytes()
                    info = tarfile.TarInfo(f'{name}/{path.relative_to(source).as_posix()}')
                    info.size = len(data)
                    info.mode = 0o644
                    info.mtime = 0
                    archive.addfile(info, io.BytesIO(data))
    with tempfile.TemporaryDirectory() as staging:
        extracted = Path(staging)
        with tarfile.open(output) as archive:
            for item in archive.getmembers():
                if not (extracted / item.name).resolve().is_relative_to(extracted) or not item.isfile():
                    raise ValueError('Unexpected archive entry')
            for item in archive.getmembers():
                target = extracted / item.name
                target.parent.mkdir(parents=True, exist_ok=True)
                with archive.extractfile(item) as stream:
                    target.write_bytes(stream.read())
        unpacked = extracted / name
        errors = validate_plugin_links(unpacked)
        for filename in ('plugin.json', 'COPYRIGHT.md'):
            if not (unpacked / filename).is_file() or (unpacked / filename).read_bytes() != (source / filename).read_bytes():
                errors.append('Archive/source mismatch: ' + filename)
        if errors:
            output.unlink()
            raise ValueError('\n'.join(errors))
    return output

if __name__ == '__main__':
    print(package())
