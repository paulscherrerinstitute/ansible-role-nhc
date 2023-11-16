import pytest
import os
## Confirm that specific packages and versions are installed
#@pytest.mark.parametrize("name,version", [
#    ("epel-release", "8"),
#    ("htop", "3.0"),
#    ("nginx", "1.14"),
#    ("git", "2.31"),
#])
#def test_packages(host, name, version):
#    pkg = host.package(name)
#    assert pkg.is_installed
#    assert pkg.version.startswith(version)

def test_nhc_conf_exists(host):
	assert os.path.exists("/etc/nhc/nhc.conf") == True
