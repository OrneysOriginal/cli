from parameterized import parameterized

from src.read_file import parallel_count_lines, serialize_endpoints, parse_logs_files


@parameterized.expand(
    [
        (['test/test.log'], ),
    ]
)
def test_read(path: list[str]):
    data = parallel_count_lines(path, processes=1)
    assert data == {'/admin/dashboard/': {'debug': 0, 'info': 3, 'warning': 0, 'error': 1, 'critical': 0}, '/api/v1/users/': {'debug': 0, 'info': 1, 'warning': 0, 'error': 0, 'critical': 0}}


@parameterized.expand(
    [
        ([{'/admin/dashboard/': {'debug': 0, 'info': 3, 'warning': 0, 'error': 1, 'critical': 0}, '/api/v1/users/': {'debug': 0, 'info': 1, 'warning': 0, 'error': 0, 'critical': 0}}], ),
    ]
)
def test_serialize_endpoints(endpoints: list[dict]):
    data = serialize_endpoints(endpoints)
    assert data == {'/admin/dashboard/': {'debug': 0, 'info': 3, 'warning': 0, 'error': 1, 'critical': 0}, '/api/v1/users/': {'debug': 0, 'info': 1, 'warning': 0, 'error': 0, 'critical': 0}}


@parameterized.expand(
    [
        ('test/test.log', ),
    ]
)
def test_parse_logs_files(path: str):
    data = parse_logs_files(path)
    assert data == {'/admin/dashboard/': {'debug': 0, 'info': 3, 'warning': 0, 'error': 1, 'critical': 0}, '/api/v1/users/': {'debug': 0, 'info': 1, 'warning': 0, 'error': 0, 'critical': 0}}