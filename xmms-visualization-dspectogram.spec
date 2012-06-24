Summary:	Dual Spectogram
Summary(pl):	Podw�jny Spektogram
Name:		xmms-visualization-dspectogram
Version:	1.2
Release:	2
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://hem.passagen.se/joakime/dspectogram-%{version}.tar.gz
URL:		http://hem.passagen.se/joakime/linuxapp.html
Requires:	xmms
BuildRequires:	xmms-devel >= 1.2.3
BuildRequires:	glib-devel >= 1.2.2
BuildRequires:	gtk+-devel >= 1.2.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Dual Spectogram - Dual Spectral Histogram plugin for XMMS.

%description -l pl
Plugin Podw�jnej Analizy Spektralnej dla XMMS.

%prep
%setup -q -n dspectogram-%{version}

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
%doc Change* README
%attr(755,root,root) %{_libdir}/xmms/*/*.so
%{_datadir}/xmms/*
