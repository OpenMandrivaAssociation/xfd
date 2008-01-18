Name:		xfd
Version:	1.0.1
Release:	%mkrel 7
Summary:	Display all the characters in an X font
Group:		Development/X11
Source:		http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License:	MIT
BuildRoot:	%{_tmppath}/%{name}-root

BuildRequires:	x11-util-macros		>= 1.1.5
BuildRequires:	libxaw-devel		>= 1.0.4
BuildRequires:	libfontconfig-devel	>= 2.5.0
BuildRequires:	freetype2-devel		>= 2.3.5
BuildRequires:	xft2-devel		>= 2.1.12

%description
The xfd utility creates a window containing the name of the font being
displayed, a row of command buttons, several lines of text for 
displaying character metrics, and a grid containing one glyph per cell.
The characters are shown in increasing order from left to right, top
to bottom.

%prep
%setup -q -n %{name}-%{version}

%build
autoreconf -ifs
%configure	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

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
