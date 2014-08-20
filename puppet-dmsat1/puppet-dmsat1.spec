Name:         puppet-dmsat1
Version:      0.1.1
Release:      1
Summary:      Puppet configuration of depzone dmsat1
Group:        Applications/System
License:      GPL
Vendor:       MSAT
BuildRoot:    %{_tmppath}/%{name}-root
Requires:     puppet-baseinfra
Requires:     puppet-int-baseinfra
Requires:     puppet-conf-dmsat1

%description
Meta RPM of depzone dmsat1 to pull in:
* puppet-construction
  * puppet-baseinfra
* puppet-integration
  * puppet-int-baseinfra
* puppet-configuration
  * puppet-conf-dmsat1

%prep
# Empty.

%build
# Empty.

%install
# Empty.

%clean
# Empty.

%pre
# Empty.

%post
# Empty.

%preun
# Empty.

%postun
# Empty.

%files
# Empty.

%changelog
* Tue Aug 19 2014 Allard Berends <allard.berends@example.com> - 0.1.1-1
- Initial creation of the RPM
