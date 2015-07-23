%global scl lsst-stack1

%{?scl:%global _scl_prefix /opt/lsst}
%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-1.1.2
%global pypi_name pykg-config

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        1.3.0
Release:        2%{?dist}
Summary:        pkg-config replacement

License:        BSD
URL:            http://github.com/gbiggs/pykg-config
Source0:        https://pypi.python.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl:scl_prefix_python}python2-devel
%{?scl:BuildRequires: %{scl_prefix}build %{scl_prefix}runtime}
%{?scl:Requires: %{scl_prefix}runtime}


%description
pykg-config
==============================================================================
A pkg-config replacement.

pykg-config is an input- and output-compatible
implementation of pkg-config
written in Python for greater ease of portability.
It is designed to be a
drop-in replacement: command lines that work for pkg-
config should produce
identical output from ...

%prep
%setup -q -n %{pypi_name}-%{version}

%build
%{?scl:scl enable %{scl} - << \EOF}
%{__python2} setup.py build
%{?scl:EOF}

%install
%{?scl:scl enable %{scl} - << \EOF}
%{__python2} setup.py install --skip-build --root %{buildroot}
%{?scl:EOF}

%files
%doc README.txt LICENSE.txt
%{_bindir}/pykg-config.py
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/pykg_config-%{version}-py?.?.egg-info

%changelog
* Thu Jul 23 2015 Joshua Hoblitt <josh@hoblitt.com> 1.3.0-2
- new package built with tito

* Thu Jul 23 2015 jhoblitt - 1.3.0-1
- Initial package.
