Name:           puppet-vlan
Version:        XXX
Release:        XXX
Summary:        Vlan Puppet Module
License:        Apache-2.0

URL:            https://github.com/derekhiggins/puppet-vlan

Source0:        http://github.com/derekhiggins/puppet-nssdb/archive/%{version}.tar.gz

BuildArch:      noarch

Requires:       puppet >= 2.7.0

%description
Very simple puppet module to install a vlan.

%prep
%setup -q -n %{name}-%{version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/vlan/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/vlan/



%files
%{_datadir}/openstack-puppet/modules/vlan/


%changelog

