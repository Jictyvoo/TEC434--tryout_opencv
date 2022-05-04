import hashlib


def output_filename(input_name: str) -> str:
    hash_filename = hashlib.md5(input_name.encode("utf-8")).hexdigest()
    index = input_name.rindex("/")
    filename = input_name[index + 1 :].replace(".", "")

    return filename + "_" + hash_filename[: int(len(hash_filename) / 2)]
