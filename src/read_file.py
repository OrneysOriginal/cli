import os
from multiprocessing import Pool


def parallel_count_lines(file_paths: list[str], processes: int) -> dict[str, dict]:
    with Pool(processes=processes) as pool:
        endpoint_call_level = pool.map(parse_logs_files, file_paths)
    return serialize_endpoints(endpoint_call_level)


def serialize_endpoints(endpoint_call_level: list[dict]):
    dict_ = {}
    for i in range(len(endpoint_call_level)):
        dict_ = add_dict(dict_, endpoint_call_level[i])
    return dict_


def add_dict(d1: dict, d2: dict) -> dict:
    d = d1
    for key in d2.keys():
        if key in d1:
            for level in d1[key]:
                d1[key][level] += d2[key][level]
        else:
            d1[key] = d2[key]
    return d


def parse_logs_files(path: str) -> dict[str, dict]:
    endpoint_call_level = {}
    if os.path.exists(path):
        parse_file(path, endpoint_call_level)
    else:
        print(f'Файла {path} не существует')
    return endpoint_call_level


def parse_file(path: str, endpoint_call_level: dict[str, dict]) -> None:
    with open(path, "r") as f:
        for line in f:
            parse_log(line, endpoint_call_level)


def parse_log(log: str, endpoint_call_level: dict[str, dict]) -> None:
    log = log.split()
    if log[3] != "django.request:":
        return
    status = log[2]
    endpoint = get_endpoint_name(log)
    if endpoint not in endpoint_call_level:
        endpoint_call_level[endpoint] = level_dict()
    endpoint_call_level[endpoint][status.lower()] += 1


def get_endpoint_name(log: list) -> str:
    endpoint = log[5]
    if endpoint[0] != "/":
        for part in log:
            if part[0] == "/":
                return part
    return endpoint


def level_dict() -> dict[str, int]:
    return {
        "debug": 0,
        "info": 0,
        "warning": 0,
        "error": 0,
        "critical": 0,
    }
