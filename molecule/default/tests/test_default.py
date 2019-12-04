import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('instance')


FCGI_CMD = "/usr/bin/cgi-fcgi"
PHP_FPM_SOCKET = "/var/run/php/php7.1-nextcloud-fpm.sock"


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_php_fpm_ping(host):
    env = {}
    env["SCRIPT_NAME"] = "/ping"
    env["SCRIPT_FILENAME"] = "/ping"
    env["REQUEST_METHOD"] = "GET"

    env = ['%s=%s' % (k, v) for k, v in env.items()]
    env = ' '.join(env)

    cmd = host.run("%s %s -bind -connect %s" % (
        env,
        FCGI_CMD,
        PHP_FPM_SOCKET
    ))
    assert cmd.rc == 0
    assert cmd.stdout.split('\r\n')[-1] == 'pong'


def test_nextcloud(host):
    env = {}
    env["SCRIPT_NAME"] = "/"
    env["SCRIPT_FILENAME"] = "/srv/nextcloud/nextcloud/index.php"
    env["REQUEST_METHOD"] = "GET"

    env = ['%s=%s' % (k, v) for k, v in env.items()]
    env = ' '.join(env)

    cmd = host.run("%s %s -bind -connect %s" % (
        env,
        FCGI_CMD,
        PHP_FPM_SOCKET
    ))
    assert cmd.rc == 0
    lines = cmd.stdout.split('\r\n')
    assert "Status: 302 Found" in lines
    assert "Location: http://localhost/index.php/login" in lines
