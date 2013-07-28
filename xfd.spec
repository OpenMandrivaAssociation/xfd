Name:		xfd
Version:	1.1.2
Release:	1
Summary:	Display all the characters in an X font
Group:		Development/X11
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License:	MIT

BuildRequires: pkgconfig(fontconfig) >= 2.3.93
BuildRequires: pkgconfig(freetype2) >= 2.1.10
BuildRequires: pkgconfig(xft) >= 2.1.8.2
BuildRequires: pkgconfig(xt)
BuildRequires: xaw-devel >= 1.0.1
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
%makeinstall_std

%files
%{_bindir}/xfd
%{_datadir}/X11/app-defaults/Xfd
%{_mandir}/man1/xfd.1*


%changelog
* Mon Feb 27 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.1.1-1
+ Revision: 781014
- version update 1.1.1

* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1.0-2
+ Revision: 671308
- mass rebuild

* Thu Oct 21 2010 Thierry Vignaud <tv@mandriva.org> 1.1.0-1mdv2011.0
+ Revision: 587076
- new release

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-10mdv2010.1
+ Revision: 524440
- rebuilt for 2010.1

* Mon Apr 13 2009 Funda Wang <fwang@mandriva.org> 1.0.1-9mdv2009.1
+ Revision: 366633
- no more autoconf needed

  + Antoine Ginies <aginies@mandriva.com>
    - rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.0.1-8mdv2009.0
+ Revision: 226035
- rebuild

  + Paulo Andrade <pcpa@mandriva.com.br>
    - Revert to use upstream tarball, build requires and remove non mandatory local patches.

* Fri Jan 18 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.1-7mdv2008.1
+ Revision: 154753
- Updated BuildRequires and resubmit package.
- Choose default Xaw from xaw.m4 unless configure explicitly told otherwise.

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Aug 31 2007 Adam Williamson <awilliamson@mandriva.org> 1.0.1-6mdv2008.0
+ Revision: 76524
- rebuild for 2008
- wrap description
- slight spec clean

  + Thierry Vignaud <tv@mandriva.org>
    - do not hardcode lzma extension!!!

* Fri Sep 01 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-09-01 21:18:27 (59537)
- rebuild to fix libXaw.so.8 dependency

* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Tue May 30 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-30 20:41:44 (31752)
- rebuild against new libXaw package

* Tue May 30 2006 Thierry Vignaud <tvignaud@mandriva.com>
+ 2006-05-30 16:15:56 (31710)
- fill in a few more missing descriptions

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository

