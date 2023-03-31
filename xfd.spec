Name:		xfd
Version:	1.1.4
Release:	2
Summary:	Display all the characters in an X font
Group:		Development/X11
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.xz
License:	MIT
BuildRequires:	pkgconfig(fontconfig) >= 2.3.93
BuildRequires:	pkgconfig(freetype2) >= 2.1.10
BuildRequires:	pkgconfig(xft) >= 2.1.8.2
BuildRequires:	pkgconfig(xt)
BuildRequires:	pkgconfig(xrender)
BuildRequires:	pkgconfig(xmu)
BuildRequires:	pkgconfig(xkbfile)
BuildRequires:	xaw-devel >= 1.0.1
BuildRequires:	pkgconfig(xorg-macros)

%description
The xfd utility creates a window containing the name of the font being
displayed, a row of command buttons, several lines of text for 
displaying character metrics, and a grid containing one glyph per cell.
The characters are shown in increasing order from left to right, top
to bottom.

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install

%files
%{_bindir}/xfd
%{_datadir}/X11/app-defaults/Xfd
%doc %{_mandir}/man1/xfd.1*
