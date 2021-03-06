%define module breathe

Summary:	Extension to reStructuredText and Sphinx for working with Doxygen xml output
Name:		python-%{module}
Version:	4.33.1
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/b/breathe/breathe-%{version}.tar.gz
Patch0:   breathe-4.33.1-fix-required-sphinx-version.patch
License:	MIT
Group:		Development/Python
Url:		https://pypi.org/project/breathe/
BuildArch:	noarch
BuildRequires:	pkgconfig(python)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)

%description
Breathe is an extension to reStructuredText and Sphinx to be able to read and
render Doxygen xml output.

%prep
%autosetup -p1 -n %{module}-%{version}

%build
%py_build

%install
%py_install

%files
%{_bindir}/breathe-apidoc
%{python_sitelib}/breathe-%{version}-py*.*.egg-info
%{python_sitelib}/breathe/
