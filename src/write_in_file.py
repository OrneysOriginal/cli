def write_in_file(file_name: str, endpoint_call_level: dict[str, dict]) -> None:
    endpoints = sorted(endpoint_call_level.keys())
    call_level_count = level_dict()
    with open(file_name, "w+") as f:
        f.write(f"Total requests: {calculate_count_call(endpoint_call_level)}\n\n")
        f.write(
            "{:<20} {:<20} {:<20} {:<20} {:<20} {:<20}\n".format(
                "HANDLER", "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"
            )
        )
        for endpoint in endpoints:
            log = get_serialize_log(endpoint, call_level_count, endpoint_call_level)
            f.write(log)
        f.write(
            "{:<20} {:<20} {:<20} {:<20} {:<20} {:<20}\n\n".format(
                "TOTAL", *call_level_count.values()
            )
        )


def calculate_count_call(endpoint_call_level: dict[str, dict]):
    cnt_call = 0
    for key in endpoint_call_level.keys():
        cnt_call += sum(endpoint_call_level[key].values())
    return cnt_call


def get_serialize_log(
    endpoint: str,
    call_level_count: dict[str, int],
    endpoint_call_level: dict[str, dict],
) -> str:
    call_level = endpoint_call_level[endpoint]
    debug, info, warning, error, critical = call_level.values()
    log = "{:<20} {:<20} {:<20} {:<20} {:<20} {:<20}\n".format(
        endpoint, *call_level.values()
    )
    call_level_count["debug"] += debug
    call_level_count["info"] += info
    call_level_count["warning"] += warning
    call_level_count["error"] += error
    call_level_count["critical"] += critical
    return log


def level_dict() -> dict[str, int]:
    return {
        "debug": 0,
        "info": 0,
        "warning": 0,
        "error": 0,
        "critical": 0,
    }
