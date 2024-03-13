# -*- coding: utf-8 -*-

import chardet
import yaml


def parse_yaml(yaml_file_path: str) -> dict:
    # Check Encoding
    with open(yaml_file_path, "rb") as f:
        raw_data = f.read()
        result_encoding = chardet.detect(raw_data)
        encoding = result_encoding["encoding"]

        if encoding is None:
            encoding = "utf-8"

    file_content = raw_data.decode(encoding).strip()

    if len(file_content) == 0:
        return {}

    yaml_data = yaml.safe_load(file_content)

    return yaml_data


if __name__ == "__main__":
    result = parse_yaml("../config/config.yaml")
    print(result)
