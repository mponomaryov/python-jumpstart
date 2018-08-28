import journal

def main():
    print_header()
    run_event_loop()

def print_header():
    print('-------------------')
    print('    JOURNAL APP')
    print('-------------------')
    print()

def run_event_loop():
    journal_name = 'default'
    journal_data = journal.load(journal_name)

    while True:
        cmd = input('What do you want to do? [L]ist, [A]dd, E[x]it: ')
        cmd = cmd.strip().lower()

        if cmd == 'l':
            print('Your {} journal entries'.format(len(journal_data)))
            for idx, entry in enumerate(reversed(journal_data), 1):
                print('{}. {}'.format(idx, entry))
        elif cmd == 'a':
            new_entry = input('Enter your journal entry:\n')
            journal.add_entry(new_entry, journal_data)
        elif not cmd or cmd == 'x':
            break
        else:
            print('Unknown command "{}"'.format(cmd))

    journal.save(journal_name, journal_data)
    print('Done, goodbye.')

if __name__ == '__main__':
    main()
