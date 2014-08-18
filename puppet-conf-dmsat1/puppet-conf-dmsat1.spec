Name:         puppet-conf-dmsat1
Version:      0.1.1
Release:      2
Summary:      Puppet configuration of depzone dmsat1
Group:        Applications/System
License:      GPL
Vendor:       MSAT
Source:       %{name}.tar.gz
BuildRoot:    %{_tmppath}/%{name}-root
Requires:     puppet-structure
Requires:     puppet-baseinfra

%description
This RPM provides the parameters for the dmsat1 Deployment
zone.

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
%dir    /var/lib/hiera/depzones/dmsat1
%config /var/lib/hiera/depzones/dmsat1.yaml
%config /var/lib/hiera/depzones/dmsat1/hosts
%config /var/lib/hiera/depzones/dmsat1/platforms
%config /var/lib/hiera/depzones/dmsat1/subzones

%changelog
* Sat Aug 16 2014 Allard Berends <allard.berends@example.com> - 0.1.1-2
- changed from puppet-dmsat1 to puppet-conf-dmsat1
* Sun Jul 6 2014 Allard Berends <allard.berends@example.com> - 0.1.1-1
- Initial creation of the RPM
