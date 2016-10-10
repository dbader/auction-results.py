import pytest

from configparsing import load_config, InvalidConfig


def test_missing_config():
    with pytest.raises(InvalidConfig):
        load_config('does-not-exist.yaml')


def test_invalid_config(tmpdir):
    yaml_contents = (
        '%%%%%%%%\n'
    )

    tmp_config = tmpdir.join('temp-config.yaml')
    tmp_config.write_text(yaml_contents, encoding='utf-8')

    with pytest.raises(InvalidConfig):
        load_config(tmp_config.strpath)


def test_valid_config(tmpdir):
    yaml_contents = (
        'hello: yes\n'
        'a_number: 42\n'
    )

    tmp_config = tmpdir.join('temp-config.yaml')
    tmp_config.write_text(yaml_contents, encoding='utf-8')

    parsed_config = load_config(tmp_config.strpath)

    assert parsed_config['hello'] is True
    assert parsed_config['a_number'] == 42
