import argparse

from src.read_file import parallel_count_lines
from src.write_in_file import write_in_file


PROCESS_COUNT = 1


def main():
    pars = argparse.ArgumentParser()
    pars.add_argument("path", nargs="*")
    pars.add_argument("--report")

    args = pars.parse_args()
    if args.report is None or args.report != "handlers":
        print("Неверное имя отчёта")
        return

    endpoint_call_level = parallel_count_lines(args.path, processes=PROCESS_COUNT)
    write_in_file(args.report, endpoint_call_level)


if __name__ == "__main__":
    main()
