%define major 0
%define Werror_cflags %nil
%define snapshot 20170221

Summary:        A collection of core classes used throughout Liri
Name:           liri-workspace
Version:        0.9.0
%if "%{snapshot}" != ""
%define tarname %{name}-%{version}-%{snapshot}
Release:        1.%{snapshot}.1
Source0:        %{name}-%{version}-%{snapshot}.tar.xz
%else
Release:        1
Source0:        https://github.com/lirios/workspace/releases/download/v%{version}/%{name}-%{version}.tar.xz
%define tarname %{name}-%{version}
%endif
License:        LGPLv3
Url:            https://github.com/lirios

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  qt5-devel
BuildRequires:  cmake(Qt5QuickControls2)
BuildRequires:	cmake(Fluid)
BuildRequires:	cmake(Vibe)
BuildRequires:	cmake(LiriWayland)
BuildRequires:	cmake(Qt5GStreamer)
BuildRequires:	pkgconfig(libsystemd)
BuildRequires:	pkgconfig(wayland-egl)
BuildRequires:	pkgconfig(glib-2.0)

%description
A collection of core classes used throughout Liri

%prep
%setup -qn %{tarname}
%apply_patches

%build
%cmake_qt5
%make

%install
%makeinstall_std -C build
%find_lang -f liri-screenshot liri-screencast --with-qt

%files -f liri-screencast
%{_bindir}/liri-powermanager
%{_bindir}/liri-screencast
%{_bindir}/liri-screenshot
%{_libdir}/plugins/platformthemes/liriplatformtheme.so
%{_datadir}/applications/io.liri.Screenshot.desktop
%{_datadir}/desktop-directories/*.directory
%{_datadir}/glib-2.0/schemas/io.liri*.xml
%{_kde5_autostart}/liri-powermanager.desktop
%{_sysconfdir}/xdg/menus/liri-applications.menu
