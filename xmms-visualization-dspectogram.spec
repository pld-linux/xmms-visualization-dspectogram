Summary:	Dual Spectogram
Summary(pl):	Podwójny Spektogram
Name:		xmms-visualization-dspectogram
Version:	1.2.1
Release:	2
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://www.shell.linux.se/bm/f/dspectogram-v%{version}.tar.gz
# Source0-md5:	8b09934edac2bc865617b7a08cf3f48d
URL:		http://www.shell.linux.se/bm/index.php
BuildRequires:	xmms-devel >= 1.2.3
Requires:	xmms
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _xmms_plugin_dir        %(xmms-config --visualization-plugin-dir)
%define		_xmms_data_dir		%(xmms-config --data-dir)

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
install -d $RPM_BUILD_ROOT{%{_xmms_plugin_dir},%{_xmms_data_dir}}

%{__make} install \
	INSTALL-DIR=$RPM_BUILD_ROOT%{_xmms_plugin_dir} \
	XMMS_DATADIR=$RPM_BUILD_ROOT%{_xmms_data_dir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change* README UPGRADE
%attr(755,root,root) %{_xmms_plugin_dir}/*.so
%{_xmms_data_dir}/*
