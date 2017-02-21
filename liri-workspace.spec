%define major 0
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
BuildRequires:  qt5-devel
BuildRequires:  cmake(Qt5QuickControls2)
BuildRequires:	cmake(Fluid)
BuildRequires:	cmake(Vibe)
BuildRequires:	cmake(LiriWayland)
BuildRequires:	cmake(Qt5GStreamer)

%description
A collection of core classes used throughout Liri

%prep
%setup -qn %{tarname}
%apply_patches

%build
%cmake_qt5
%make

%install
%makeinstall_std INSTALL_ROOT="%{buildroot}"

%files
%{_bindir}/%{name}
