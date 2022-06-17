"""
Module for counting files in directory

exports count_files_by_type
"""
import os
import rss_reader_package.utils.config as config


def count_files_by_type(dir_path: str, file_type: str or None) -> int:
    """
    Function that counts files by its type. If type is not provided, will count all files

    Args:
        dir_path:   path of directory where files should be counted
        file_type:  file extension that should be considered for counting

    Returns:
        int:        number of files after counting
    """

    files = []
    for (_, __, filenames) in os.walk(dir_path):
        if file_type is None:
            config.verbose_print("File type not specified. Counting all files", "warn")
            files.extend(filenames)
        else:
            for file in filenames:
                if file.endswith(file_type):
                    files.append(file)

    return len(files)
