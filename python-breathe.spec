Summary:	Extension to reStructuredText and Sphinx for working with Doxygen xml output
Name:		python-breathe
Version:	4.36.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/b/breathe/breathe-%{version}.tar.gz
License:	MIT
Group:		Development/Python
Url:		https://pypi.org/project/breathe/
BuildArch:	noarch
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(sphinx)
BuildRequires:	python%{pyver}dist(pip)

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
