Name:         puppet-structure
Version:      0.1.1
Release:      5
Summary:      Puppet structure
Group:        Applications/System
License:      GPL
Vendor:       MSAT
Source:       %{name}.tar.gz
BuildRoot:    %{_tmppath}/%{name}-root
Requires:     puppet

%description
This RPM provides the basic structure of the Puppet
configuration and Hiera/YAML key lookup.

Other RPM's can add YAML files to this structure and must
require this RPM to be present.

%prep
%setup -q -n %{name}

%build
# Empty.

%install
rm -rf $RPM_BUILD_ROOT
mkdir $RPM_BUILD_ROOT
cp -R etc var $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/share/doc/%{name}
install README $RPM_BUILD_ROOT/usr/share/doc/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%pre

%post

# AB: we need to overwrite the default /etc/hiera.yaml,
# which belongs to the puppet rpm. Note that we need to
# escape the percent characters with double percents!
/bin/mv /etc/hiera.yaml /etc/hiera.yaml.rpmsave
/bin/cat << EOF > /etc/hiera.yaml
---
:backends:
  - yaml
:hierarchy:
  - depzones/%%{depzone}/hosts/%%{fqdn}
  - depzones/%%{depzone}/subzones/%%{subzone}
  - depzones/%%{depzone}
  - base

:yaml:
# datadir is empty here, so hiera uses its defaults:
# - /var/lib/hiera on *nix
# - %%CommonAppData%%\PuppetLabs\hiera\var on Windows
# When specifying a datadir, make sure the directory exists.
  :datadir: /var/lib/hiera
EOF

# AB: we need to overwrite the default
# /etc/puppet/puppet.conf, which belongs to the puppet rpm.
/bin/mv /etc/puppet/puppet.conf /etc/puppet/puppet.conf.rpmsave
/bin/cat << 'EOF' > /etc/puppet/puppet.conf
[main]
    # AB: We use an each loop. Hence we need the future
    # option.
    parser = future
    # The Puppet log directory.
    # The default value is '$vardir/log'.
    logdir = /var/log/puppet

    # Where Puppet PID files are kept.
    # The default value is '$vardir/run'.
    rundir = /var/run/puppet

    # Where SSL certificates are kept.
    # The default value is '$confdir/ssl'.
    ssldir = $vardir/ssl

[agent]
    # The file in which puppetd stores a list of the classes
    # associated with the retrieved configuratiion.  Can be loaded in
    # the separate ``puppet`` executable using the ``--loadclasses``
    # option.
    # The default value is '$confdir/classes.txt'.
    classfile = $vardir/classes.txt

    # Where puppetd caches the local configuration.  An
    # extension indicating the cache format is added automatically.
    # The default value is '$confdir/localconfig'.
    localconfig = $vardir/localconfig
EOF

# AB: make sure to set the first_puppet service to on. After
# the reboot, this service will disable itself.
/sbin/chkconfig first_puppet on

%preun
# Empty.

%postun
# Empty.

%files
%defattr(0644,root,root)
%config /etc/puppet/hiera.yaml
%dir /etc/puppet/manifests
/etc/puppet/manifests/site.pp
%attr(0755,root,root) %config /etc/rc.d/init.d/first_puppet
%doc /usr/share/doc/%{name}/README
%dir /var/lib/hiera
%dir /var/lib/hiera/depzones
%dir /var/lib/hiera/platforms

%changelog
* Mon Jul 14 2014 Allard Berends <allard.berends@example.com> - 0.1.1-5
- Restructured. All platform layers remove from hiera.yaml
* Sun Jul 6 2014 Allard Berends <allard.berends@example.com> - 0.1.1-4
- Restructured. All node YAML files removed.
* Sun Jun 29 2014 Allard Berends <allard.berends@example.com> - 0.1.1-3
- Added lvs nodes
* Sat Jun 21 2014 Allard Berends <allard.berends@example.com> - 0.1.1-2
- Added ds3
* Sat Jun 21 2014 Allard Berends <allard.berends@example.com> - 0.1.1-1
- Initial creation of the RPM
