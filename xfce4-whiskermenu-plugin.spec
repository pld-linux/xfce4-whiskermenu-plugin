Summary:	Alternate application launcher for Xfce
Name:		xfce4-whiskermenu-plugin
Version:	1.5.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-whiskermenu-plugin/1.5/%{name}-%{version}.tar.bz2
# Source0-md5:	32fcbf16931038c10b1b7a7ccc392132
URL:		http://git.xfce.org/panel-plugins/xfce4-whiskermenu-plugin/
BuildRequires:	cmake
BuildRequires:	exo-devel >= 0.6.0
BuildRequires:	garcon-devel
BuildRequires:	glib2-devel >= 1:2.30.2
BuildRequires:	gtk+2-devel
BuildRequires:	libxfce4ui-devel >= 4.12.0
BuildRequires:	libxfce4util-devel >= 4.12.0
BuildRequires:	rpmbuild(macros) >= 1.601
BuildRequires:	xfce4-dev-tools >= 4.12.0
BuildRequires:	xfce4-panel-devel >= 4.12.0
BuildRequires:	xfconf-devel >= 4.12.0
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme
Requires:	xfce4-panel >= 4.12.0
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

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
#%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/xfce4-popup-whiskermenu
%attr(755,root,root) %{_libdir}/xfce4/panel/plugins/libwhiskermenu.so
%{_datadir}/xfce4/panel/plugins/whiskermenu.desktop
%{_iconsdir}/hicolor/*/apps/xfce4-whiskermenu*
%{_mandir}/man1/xfce4-popup-whiskermenu.1*
