import os

def get_full_path(name):
    return os.path.abspath(os.path.join('.', name + '.jrl'))

def load(name):
    """
    This method creates and loads a new journal.

    :param name: This base name of the journal to load.
    :return: A new journal data structure populated with the file data.
    """
    data = []
    fname = get_full_path(name)
    if os.path.exists(fname):
        with open(fname) as fin:
            for line in fin:
                data.append(line.rstrip())
    return data

def save(name, data):
    fname = get_full_path(name)
    print("... saving to: {}".format(fname))
    with open(fname, 'w') as fout:
        fout.write('\n'.join(data))

def add_entry(entry, data):
    data.append(entry)
