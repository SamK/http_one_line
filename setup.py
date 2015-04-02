from setuptools import setup

# read metadata

program_name = 'http_one_line'

def get_metadata(program_name):
    metadata = {}
    with file(program_name) as f:
        for line in f:
            if line.startswith('__'):
                els = line.split('=')
                metadata[els[0].strip().strip('_')] = els[1].strip().strip('"\'')
    return metadata

metadata = get_metadata(program_name)

setup(
    name = program_name,
    version = metadata['version'],
    author = metadata['author'],
    author_email = metadata['author_email'],
    description = ("HTTP server designed to serve one single page"),
    license = metadata['license'],
    url = 'https://github.com/SamK/{}'.format(program_name),
    scripts = [program_name],
)

