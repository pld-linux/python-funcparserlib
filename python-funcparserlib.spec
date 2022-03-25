#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define 	module	funcparserlib
Summary:	Recursive descent parsing library based on functional combinators
Summary(pl.UTF-8):	Biblioteka analizy rekurencyjnej oparta na kombinatorach funkcyjnych
Name:		python-%{module}
Version:	0.3.6
Release:	4
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/funcparserlib/
Source0:	https://files.pythonhosted.org/packages/source/f/funcparserlib/%{module}-%{version}.tar.gz
# Source0-md5:	3aba546bdad5d0826596910551ce37c0
URL:		https://github.com/vlasovskikh/funcparserlib
%if %{with python2}
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-2to3 >= 1:3.2
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.5
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
Requires:	python3-modules >= 1:3.2

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
cd build-2/lib
%{__python} -m unittest discover
cd ../..
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
# run tests on 2to3'd sources
cd build-3/lib
%{__python3} -m unittest discover
cd ../..
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/%{module}/tests
%py_postclean
%endif

%if %{with python3}
%py3_install

%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/%{module}/tests
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGES LICENSE README doc/*.md
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc CHANGES LICENSE README doc/*.md
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif
