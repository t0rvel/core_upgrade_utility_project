import difflib
import os


def assert_content_equal(file1, file2, search_key):

    with open(file1, 'r') as f1:
        with open(file2, 'r') as f2:
            diff = difflib.ndiff(f1.readlines(), f2.readlines())

            delta = ''.join(x[2:] for x in diff if x.startswith(search_key))

            if delta:
                # update this to return not print.
                print(' ')
                print( f"delta is: {delta}\n " \
                       f"when comparing {file2}\n" \
                      f"with {file1}")


def search_directory(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)