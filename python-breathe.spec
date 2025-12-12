Summary:	Extension to reStructuredText and Sphinx for working with Doxygen xml output
Name:		python-breathe
Version:	4.35.0
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/b/breathe/breathe-%{version}.tar.gz
License:	MIT
Group:		Development/Python
Url:		https://pypi.org/project/breathe/
BuildArch:	noarch
BuildRequires:	pkgconfig(python)
BuildRequires:	python3dist(setuptools)
BuildRequires:	python3dist(sphinx)
BuildRequires:	python3dist(pip)

%description
Breathe is an extension to reStructuredText and Sphinx to be able to read and
render Doxygen xml output.

%prep
%autosetup -p1 -n breathe-%{version}

%build
%py_build

%install
%py_install

%files
%doc README.rst
%license LICENSE
%{_bindir}/breathe-apidoc
%{python_sitelib}/*
