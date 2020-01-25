%define		_status		beta
%define		_pearname	Services_SharedBook
Summary:	%{_pearname} - PHP wrapper for SharedBook Open API
Summary(pl.UTF-8):	%{_pearname} - wrapper PHP dla otwartego API SharedBook
Name:		php-pear-%{_pearname}
Version:	0.2.6
Release:	3
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	013c50484ba39c83c1b45c18df5b410a
URL:		http://pear.php.net/package/Services_SharedBook/
BuildRequires:	php-pear-PEAR >= 1:1.4.0
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-HTTP_Client >= 1.1.1
Requires:	php-pear-PEAR-core >= 1:1.4.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SharedBook has developed a unique, on demand reverse publishing
platform to help businesses and consumers extract, manipulate and
publish the Internet content. SharedBook now has an Open API
(Application Programming Interface). Now anyone can write a program
that will transfer data to the SharedBook platform and utilize our
full functionality to create revenue-producing books, both online and
off. This package is a wrapper for Open API calls, handles XML
responses, file uploads.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
SharedBook opracował unikalną, uruchamianą na żądanie platformę
ułatwiającą odbieranie, obróbkę oraz publikowanie treści w Internecie.
SharedBook obecnie posiada także ogólnodostępne Open API (Application
Programming Interface) - każdy może napisać program przesyłający dane
do platformy SharedBook i korzystający z jej funkcjonalności do
stworzenia przynoszących zyski książek, zarówno w wersji online jak i
offline. Ten pakiet jest wrapperem dla wywołań Open API, zajmuje się
obsługą odpowiedzi XML jak również wysyłką plików.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log docs/Services_SharedBook
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Services/SharedBook
%{php_pear_dir}/Services/SharedBook.php
