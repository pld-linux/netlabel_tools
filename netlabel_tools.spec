Summary:	Tools to manage the Linux NetLabel subsystem
Name:		netlabel_tools
Version:	0.17
Release:	5%{?dist}
License:	GPL
Group:		Daemons
URL:		http://netlabel.sourceforge.net/
Source0:	http://dl.sourceforge.net/netlabel/%{name}-%{version}.tar.gz
# Source0-md5:	905ffd48714f48aaa34ecdc3c51d3dcb
Source1:	%{name}.init
Source2:	%{name}.rules
Patch1:		%{name}-new-hdrs.patch
Patch2:		%{name}.patch
BuildRequires:	libnl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NetLabel is a kernel subsystem which implements explicit packet
labeling protocols such as CIPSO and RIPSO for Linux. Packet labeling
is used in secure networks to mark packets with the security
attributes of the data they contain. This package provides the
necessary user space tools to query and configure the kernel
subsystem.

%prep
%setup -q
%patch1 -p1
%patch2 -p0

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	INSTALL_PREFIX=${RPM_BUILD_ROOT} \
	INSTALL_MAN_DIR=${RPM_BUILD_ROOT}%{_mandir}

install -d $RPM_BUILD_ROOT/etc/rc.d/init.d/
install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/netlabel
install %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/*.txt
%attr(755,root,root) /sbin/*
%attr(754,root,root) /etc/rc.d/init.d/netlabel
%config(noreplace) %attr(640,root,root) %{_sysconfdir}/netlabel.rules
%{_mandir}/man?/*
