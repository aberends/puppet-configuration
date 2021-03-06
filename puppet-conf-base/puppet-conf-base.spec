Name:         puppet-conf-base
Version:      0.1.1
Release:      1
Summary:      Puppet configuration base
Group:        Applications/System
License:      GPL
Vendor:       MSAT
Source:       %{name}.tar.gz
BuildRoot:    %{_tmppath}/%{name}-root
Requires:     puppet-structure

%description
This RPM provides the base YAML parameters. These are
independent on the deployment zone.

%prep
%setup -q -n %{name}

%build
# Empty.

%install
rm -rf $RPM_BUILD_ROOT
mkdir $RPM_BUILD_ROOT
cp -R var $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%pre
# Empty.

%post
# Empty.

%preun
# Empty.

%postun
# Empty.

%files
%defattr(0644,root,root)
%config /var/lib/hiera/base.yaml
%attr(0755,root,root) /var/lib/hiera/depzone_platform_instance.sh
/var/lib/hiera/platforms
%attr(0755,root,root) /var/lib/hiera/puppet_dev_copy.sh

%changelog
* Tue Aug 19 2014 Allard Berends <allard.berends@example.com> - 0.1.1-1
- Initial creation of the RPM
