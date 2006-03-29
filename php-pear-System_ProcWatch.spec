%include	/usr/lib/rpm/macros.php
%define		_class		System
%define		_subclass	ProcWatch
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - monitor processes
Summary(pl):	%{_pearname} - monitorowanie procesów
Name:		php-pear-%{_pearname}
Version:	0.4.2
Release:	4
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	35d4471a5f044569ccb34a72d8d1c72b
URL:		http://pear.php.net/package/System_ProcWatch/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-common >= 3:4.0.2
Requires:	php-pcre
Requires:	php-pear
Requires:	php-pear-PEAR-core
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	'pear(XML/Parser.*)' 'pear(XML/DTD.*)' 'pear(Console/Getopt.*)' 'pear(.*)'

%description
With this package you can monitor running processes based upon an XML
configuration file, XML string, INI file or an array where you define
patterns, conditions and actions.

In PEAR status of this package is: %{_status}.

%description -l pl
Za pomoc± tej klasy mo¿liwe jest monitorowanie procesów na podstawie
pliku konfiguracyjnego w formacie XML, ci±gu znaków XML, pliku INI
b±d¼ tablicy w której zdefiniowane s± wzorce, warunki oraz akcje.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_pear_dir},%{_bindir}}
%pear_package_install
cp -a ./%{_bindir}/* $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f %{_docdir}/%{name}-%{version}/optional-packages.txt ]; then
	cat %{_docdir}/%{name}-%{version}/optional-packages.txt
fi

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
%attr(755,root,root) %{_bindir}/procwatch
%attr(755,root,root) %{_bindir}/procwatch-lint

%{php_pear_dir}/data/%{_pearname}
