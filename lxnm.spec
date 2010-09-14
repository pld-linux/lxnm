Summary:	Lightweight stand-alone network manager
Name:		lxnm
Version:	0.2.2
Release:	1
License:	GPL v2
Group:		X11/Applications/Networking
Source0:	http://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.gz
# Source0-md5:	2ee64e5fad4a27a522f1eb2da08dd46a
URL:		http://wiki.lxde.org/en/LXNM
BuildRequires:	glib2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LXNetdaemon is a fast, lightweight, stand-alone network manager.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/{frp,ur_PK}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_sbindir}/lxnm
%attr(755,root,root) %{_datadir}/lxnm
%{_mandir}/man1/lxnm*
