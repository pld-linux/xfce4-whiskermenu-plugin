Summary:	Alternate application launcher for Xfce
Name:		xfce4-whiskermenu-plugin
Version:	2.9.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	https://archive.xfce.org/src/panel-plugins/xfce4-whiskermenu-plugin/2.9/%{name}-%{version}.tar.bz2
# Source0-md5:	2283dff5fd4cf6b10aecc4abf5847d40
URL:		https://git.xfce.org/panel-plugins/xfce4-whiskermenu-plugin/
BuildRequires:	accountsservice-devel >= 0.6.45
BuildRequires:	cmake
BuildRequires:	exo-devel >= 4.16.0
BuildRequires:	garcon-devel >= 0.6.4
BuildRequires:	glib2-devel >= 1:2.50.2
BuildRequires:	gtk+3-devel >= 3.22
BuildRequires:	gtk-layer-shell-devel >= 0.7
BuildRequires:	libxfce4ui-devel >= 4.16.0
BuildRequires:	libxfce4util-devel >= 4.16.0
BuildRequires:	rpmbuild(macros) >= 1.601
BuildRequires:	xfce4-dev-tools >= 4.16.0
BuildRequires:	xfce4-panel-devel >= 4.16.0
BuildRequires:	xfconf-devel >= 4.16.0
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme
Requires:	xfce4-panel >= 4.16.0
Suggests:	mugshot
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Whisker Menu is an alternate application launcher for Xfce. When you
open it you are shown a list of applications you have marked as
favorites. You can browse through all of your installed applications
by clicking on the category buttons on the side. Top level categories
make browsing fast, and simple to switch between. Additionally,
Whisker Menu keeps a list of the last ten applications that you've
launched from it.

%prep
%setup -q

%build
mkdir -p build
cd build
%{cmake} \
	..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/ie

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/xfce4-popup-whiskermenu
%attr(755,root,root) %{_libdir}/xfce4/panel/plugins/libwhiskermenu.so
%{_datadir}/xfce4/panel/plugins/whiskermenu.desktop
%{_iconsdir}/hicolor/*/apps/org.xfce.panel.whiskermenu.*
%{_mandir}/man1/xfce4-popup-whiskermenu.1*
