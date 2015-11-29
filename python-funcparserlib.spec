%define 	module	funcparserlib
Summary:	Recursive descent parsing library based on functional combinators
Name:		python-%{module}
Version:	0.3.5
Release:	2
License:	MIT
Group:		Development/Languages
URL:		http://code.google.com/p/funcparserlib/
Source0:	http://pypi.python.org/packages/source/f/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	52dfec49f2d2c4d816fe8d8c90f7dcf1
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRequires:	sed >= 4.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Parser combinators are just higher-order functions that take parsers
and thier arguments and return them as result values.

%prep
%setup -q -n %{module}-%{version}
%{__sed} -i -e 's/^from ez_setup/#from ez_setup/' setup.py
%{__sed} -i -e 's/^use_setuptools()/#use_setuptools()/' setup.py

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install \
	--root $RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%dir %{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}/*.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/%{module}-%{version}-*.egg-info
%endif
