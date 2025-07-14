Summary:	Tools to manage the Linux NetLabel subsystem
Summary(pl.UTF-8):	Narzędzia do zarządzania linuksowym podsystemem NetLabel
Name:		netlabel_tools
Version:	0.19
Release:	3
License:	GPL
Group:		Daemons
Source0:	http://dl.sourceforge.net/netlabel/%{name}-%{version}.tar.gz
# Source0-md5:	f7a9f397e5bf2364676e2beba1a61beb
Source1:	%{name}.init
Source2:	%{name}.rules
Patch1:		%{name}-new-hdrs.patch
URL:		http://netlabel.sourceforge.net/
BuildRequires:	libnl-devel >= 1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NetLabel is a kernel subsystem which implements explicit packet
labeling protocols such as CIPSO and RIPSO for Linux. Packet labeling
is used in secure networks to mark packets with the security
attributes of the data they contain. This package provides the
necessary user space tools to query and configure the kernel
subsystem.

%description -l pl.UTF-8
NetLabel to podsystem jądra implementujący pod Linuksem protokoły ze
znakowaniem pakietów wprost, takie jak CIPSO czy RIPSO. Znakowanie
pakietów jest używane w bezpiecznych sieciach do oznaczania pakietów
atrybutami bezpieczeństwa określającymi dane, które zawierają. Ten
pakiet udostępnia narzędzie przestrzeni użytkownika potrzebne do
odpytywania i konfigurowania podsystemu jądra.

%prep
%setup -q
%patch -P1 -p1

%build
%{__make} -j1 \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	INSTALL_PREFIX=$RPM_BUILD_ROOT \
	INSTALL_MAN_DIR=$RPM_BUILD_ROOT%{_mandir}

install -D %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/netlabel
install %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/netlabel.rules

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/*.txt
%attr(755,root,root) /sbin/*
%attr(754,root,root) /etc/rc.d/init.d/netlabel
%config(noreplace) %verify(not md5 mtime size) %attr(640,root,root) %{_sysconfdir}/netlabel.rules
%{_mandir}/man?/*
