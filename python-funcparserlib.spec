#
# Conditional build:
%bcond_with	tests	# unit tests (not in sdist)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define 	module	funcparserlib
Summary:	Recursive descent parsing library based on functional combinators
Summary(pl.UTF-8):	Biblioteka analizy rekurencyjnej oparta na kombinatorach funkcyjnych
Name:		python-%{module}
Version:	1.0.0
Release:	3
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/funcparserlib/
Source0:	https://files.pythonhosted.org/packages/source/f/funcparserlib/%{module}-%{version}.tar.gz
# Source0-md5:	c62c820f171f66c317ea9daf02c7f28a
URL:		https://github.com/vlasovskikh/funcparserlib
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.7
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Recursive descent parsing library based on functional combinators.

%description -l pl.UTF-8
Biblioteka analizy rekurencyjnej oparta na kombinatorach funkcyjnych.

%package -n python3-%{module}
Summary:	Recursive descent parsing library based on functional combinators
Summary(pl.UTF-8):	Biblioteka analizy rekurencyjnej oparta na kombinatorach funkcyjnych
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.7

%description -n python3-%{module}
Recursive descent parsing library based on functional combinators.

%description -n python3-%{module} -l pl.UTF-8
Biblioteka analizy rekurencyjnej oparta na kombinatorach funkcyjnych.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
%{__python} -m unittest discover
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
%{__python3} -m unittest discover
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc LICENSE README.md
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif
