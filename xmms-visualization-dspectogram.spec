Summary:	Dual Spectogram
Summary(pl):	Podwójny Spektogram
Name:		xmms-visualization-dspectogram
Version:	1.2.1
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://www.shell.linux.se/bm/f/dspectogram-v%{version}.tar.gz
URL:		http://www.shell.linux.se/bm/index.php
Requires:	xmms
BuildRequires:	xmms-devel >= 1.2.3
BuildRequires:	glib-devel >= 1.2.2
BuildRequires:	gtk+-devel >= 1.2.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Dual Spectogram - Dual Spectral Histogram plugin for XMMS.

%description -l pl
Plugin Podwójnej Analizy Spektralnej dla XMMS.

%prep
%setup -q -n dspectogram-v%{version}

%build
%{__make} OPT="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/`%{_bindir}/xmms-config --visualization-plugin-dir`/ \
	$RPM_BUILD_ROOT/`%{_bindir}/xmms-config --data-dir`/

%{__make} install \
	INSTALL-DIR=$RPM_BUILD_ROOT/`%{_bindir}/xmms-config --visualization-plugin-dir`/ \
	XMMS_DATADIR=$RPM_BUILD_ROOT/`%{_bindir}/xmms-config --data-dir`/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change* README UPGRADE
%attr(755,root,root) %{_libdir}/xmms/*/*.so
%{_datadir}/xmms/*
