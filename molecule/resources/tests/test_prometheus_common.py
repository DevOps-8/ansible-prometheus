import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_prometheus_config(host):

    d = host.file('/etc/prometheus/')
    assert d.exists
    assert d.user == 'prometheus'
    assert d.group == 'prometheus'
    assert d.mode == 0o755

    f = host.file('/etc/prometheus/prometheus.yml')
    assert f.exists
    assert f.user == 'prometheus'
    assert f.group == 'prometheus'
    assert f.mode == 0o640


def test_prometheus_tsdb(host):

    d = host.file('/var/lib/prometheus/')
    assert d.exists
    assert d.user == 'prometheus'
    assert d.group == 'prometheus'
    assert d.mode == 0o755


def test_prometheus_service(host):

    s = host.service('prometheus')
    assert s.is_running
    assert s.is_enabled


def test_prometheus_webserver(host):

    host.socket("tcp://127.0.0.1:9090").is_listening
