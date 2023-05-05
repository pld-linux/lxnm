Summary:	Lightweight stand-alone network manager
Summary(pl.UTF-8):	Lekki, samodzielny zarządca sieci
Name:		lxnm
Version:	0.2.2
Release:	2
License:	GPL v2+
Group:		X11/Applications/Networking
Source0:	https://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.gz
# Source0-md5:	2ee64e5fad4a27a522f1eb2da08dd46a
URL:		http://www.lxde.org/
BuildRequires:	glib2-devel >= 1:2.6.0
BuildRequires:	pkgconfig
Requires:	glib2 >= 1:2.6.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%undefine	__cxx

%description
LXNetdaemon is a fast, lightweight, stand-alone network manager.

%description -l pl.UTF-8
LXNetdaemon to szybki, lekki, samodzielny zarządca sieci.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_sbindir}/lxnm
%attr(755,root,root) %{_datadir}/lxnm
%{_mandir}/man1/lxnm.1*
