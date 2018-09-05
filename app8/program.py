import os
import collections


SearchResult = collections.namedtuple('SearchResult', 'file line text')


def main():
    print_header()

    folder = get_folder_from_user()
    if not folder:
        print("Sorry we can't search that location.")
        return

    text = get_text_from_user()
    if not text:
        print("We can't search for nothing!")
        return

    print('\nSearching "{}" for "{}"\n'.format(folder, text))
    matches = 0
    for match in search_folders(folder, text):
        matches += 1
        print('--------- MATCH -------------')
        print('file: ' + match.file)
        print('line: {}'.format(match.line))
        print('match: ' + match.text.strip())
        print()
    print('{} total matches'.format(matches))
    print('End of search')


def print_header():
    print('-------------------')
    print('  FILE SEARCH APP')
    print('-------------------')
    print()


def get_folder_from_user():
    folder = input('What directory do you want to search:\n').strip()

    if not folder or not os.path.isdir(folder):
        return

    return os.path.abspath(folder)


def get_text_from_user():
    return input('What string you are looking for: ').lower()


def search_folders(path, search_text):
    for root, dirs, files in os.walk(path):
        for file in files:
            filename = os.path.join(root, file)
            yield from search_file(filename, search_text)


def search_file(filename, search_text):
    with open(filename, encoding='utf-8') as fin:
        for line, text in enumerate(fin, 1):
            if search_text in text.lower():
                yield SearchResult(file=filename, line=line, text=text)


if __name__ == '__main__':
    main()
