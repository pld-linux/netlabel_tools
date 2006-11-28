Summary:	Tools to manage the Linux NetLabel subsystem
Summary(pl):	Narzêdzia do zarz±dzania linuksowym podsystemem NetLabel
Name:		netlabel_tools
Version:	0.17
Release:	0.1
License:	GPL
Group:		Daemons
Source0:	http://dl.sourceforge.net/netlabel/%{name}-%{version}.tar.gz
# Source0-md5:	905ffd48714f48aaa34ecdc3c51d3dcb
Source1:	%{name}.init
Source2:	%{name}.rules
Patch1:		%{name}-new-hdrs.patch
Patch2:		%{name}.patch
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

%description -l pl
NetLabel to podsystem j±dra implementuj±cy pod Linuksem protoko³y ze
znakowaniem pakietów wprost, takie jak CIPSO czy RIPSO. Znakowanie
pakietów jest u¿ywane w bezpiecznych sieciach do oznaczania pakietów
atrybutami bezpieczeñstwa okre¶laj±cymi dane, które zawieraj±. Ten
pakiet udostêpnia narzêdzie przestrzeni u¿ytkownika potrzebne do
odpytywania i konfigurowania podsystemu j±dra.

%prep
%setup -q
%patch1 -p1
%patch2 -p0

%build
%{__make}

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
