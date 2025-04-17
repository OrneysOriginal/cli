import os

from parameterized import parameterized

from src.write_in_file import write_in_file


@parameterized.expand(
    [
        ('test/test1.log',
         {'/admin/dashboard/': {'debug': 0, 'info': 1000, 'warning': 0, 'error': 1, 'critical': 0}, '/api/v1/users/': {'debug': 0, 'info': 1, 'warning': 0, 'error': 0, 'critical': 0}},
         1002
         ),
    ]
)
def test_write_in_file(path: str, endpoint_call_level: dict[str, dict], cnt_call: int):
    write_in_file(path, endpoint_call_level)
    with open(path, 'r') as f:
        line = f.readline().split()
        assert int(line[2]) == cnt_call
    os.remove(path)
