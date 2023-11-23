def test_nhc_pkg_installed(host):
    suse = host.package('warewulf-nhc')
    rhel8 = host.package('lbnl-nhc')
    assert suse.is_installed == True or rhel8.is_installed == True

def test_nhc_conf_exists(host):
    assert host.file('/etc/nhc/nhc.conf').exists == True
