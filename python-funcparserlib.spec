#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define 	module	funcparserlib
Summary:	-
Name:		python-%module
Version:	0.3.5
Release:	0.1
License:	MIT
Group:		Development/Languages
URL:		http://code.google.com/p/%{module}/
Source0:	http://pypi.python.org/packages/source/f/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	52dfec49f2d2c4d816fe8d8c90f7dcf1
#BuildRequires:	python-coverage
#BuildRequires:	python-devel
#BuildRequires:	python-django
#BuildRequires:	python-nose
#BuildRequires:	python-pyflakes
#BuildRequires:	python-setuptools
#BuildRequires:	python-sqlite
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	sed >= 4.0
Requires:	python-django
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
<empty>

%prep
%setup -q -n %{module}-%{version}
%{__sed} -i -e 's/^from ez_setup/#from ez_setup/' setup.py
%{__sed} -i -e 's/^use_setuptools()/#use_setuptools()/' setup.py

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--optimize=2 \
	--skip-build \
	--root $RPM_BUILD_ROOT

%py_postclean

rm -rf $RPM_BUILD_ROOT%{py_sitescriptdir}/%{module}/tests
rm -rf $RPM_BUILD_ROOT%{py_sitescriptdir}/tests

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{py_sitescriptdir}/%{module}
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/%{module}-%{version}-*.egg-info/
%endif
