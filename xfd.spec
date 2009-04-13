Name:		xfd
Version:	1.0.1
Release:	%mkrel 9
Summary:	Display all the characters in an X font
Group:		Development/X11
Source:		http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License:	MIT
BuildRoot:	%{_tmppath}/%{name}-root

BuildRequires: libfontconfig-devel >= 2.3.93
BuildRequires: freetype2-devel >= 2.1.10
BuildRequires: xft2-devel >= 2.1.8.2
BuildRequires: libxt-devel >= 1.0.0
BuildRequires: libxaw-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1

%description
The xfd utility creates a window containing the name of the font being
displayed, a row of command buttons, several lines of text for 
displaying character metrics, and a grid containing one glyph per cell.
The characters are shown in increasing order from left to right, top
to bottom.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/xfd
%{_datadir}/X11/app-defaults/Xfd
%{_mandir}/man1/xfd.1*
