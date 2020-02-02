from pathlib import Path, PurePath
from util_main_dir.generic_helpers import assert_content_equal, search_directory


class Analyzer:

    def __init__(self, core_directory, *client_directories, schema='API', platform='OneShield'):
        self.schema = schema
        self.core_directory = Path(core_directory)
        # why does map lost data once we iterate over it?? list(map) seems to solve..
        self.client_directories = list(map(Path, client_directories))
        self.platform = platform

    def rename_client_files(self):

        if self.platform == 'OneShield':

            for client_dir in self.client_directories:
                for client_file in client_dir.iterdir():
                    target_file_parts = ["CORE_API" if i == 0 else part
                                         for i, part in enumerate(client_file.name.split("."))]

                    # rejoin the filename to it's directory
                    target = PurePath(client_dir).joinpath('.'.join(target_file_parts))
                    print(f"renaming {client_file} to {target}")
                    client_file.rename(target)

    def compare_dir_files(self, search_key='-'):

        for client_directory in self.client_directories:
            for client_file in client_directory.iterdir():

                core_file_result = search_directory(client_file.parts[-1], self.core_directory)

                assert_content_equal(core_file_result, client_file, search_key)


if __name__ == "__main__":
    directory_analysis = Analyzer(r"V:\test_junk\core_directory", r"V:\test_junk\selective_directory", r"V:\test_junk\cap_directory")
    directory_analysis.rename_client_files()
    directory_analysis.compare_dir_files('+')
