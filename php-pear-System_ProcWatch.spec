%include	/usr/lib/rpm/macros.php
%define		_class		System
%define		_subclass	ProcWatch
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - monitor processes
Summary(pl):	%{_pearname} - monitorowanie procesów
Name:		php-pear-%{_pearname}
Version:	0.4.2
Release:	1
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	35d4471a5f044569ccb34a72d8d1c72b
URL:		http://pear.php.net/package/System_ProcWatch/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
With this package you can monitor running processes based upon an XML
configuration file, XML string, INI file or an array where you define
patterns, conditions and actions.

In PEAR status of this package is: %{_status}.

%description -l pl
Za pomoc± tej klasy mo¿liwe jest monitorowanie procesów na podstawie
pliku konfiguracyjnego w formacie XML, ci±gu znaków XML, pliku INI b±d¼
tablicy w której zdefiniowane s± wzorce, warunki oraz akcje.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Config

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}
install %{_pearname}-%{version}/%{_subclass}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}
install %{_pearname}-%{version}/%{_subclass}/Config/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Config

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/{data,docs,scripts}
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
