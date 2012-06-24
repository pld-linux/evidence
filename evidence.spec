#
# Conditional build:
%bcond_without	kio	# disable kio backend
#
Summary:	Evidence - an eye-candy GTK+2/evas file manager
Summary(pl):	Evidence - przyci�gaj�cy oczy zarz�dca plik�w oparty na GTK+2/evas
Name:		evidence
Version:	0.9.8
%define	_snap	20050701
Release:	0.%{_snap}.0.1
License:	GPL v2
Group:		X11/Applications
Source0:	ftp://sparky.homelinux.org/snaps/evidence/%{name}-%{_snap}.tar.gz
# Source0-md5:	57077b7549fd8aeacad8670ed5dc30e7
#http://dl.sourceforge.net/evidence/%{name}-%{version}-%{_snap}.tar.gz
Source1:	%{name}.desktop
URL:		http://evidence.sourceforge.net/
BuildRequires:	XFree86-devel
BuildRequires:	acl-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	avifile-devel
BuildRequires:	curl-devel
BuildRequires:	edje-devel
BuildRequires:	evas-devel
BuildRequires:	fam-devel
#BuildRequires:	gnome-vfs2-devel #want's build
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	id3lib-devel
%if %{with kio}
BuildRequires:	kdelibs-devel
%endif
BuildRequires:	libextractor-devel
BuildRequires:	libmagic-devel
BuildRequires:	libmpeg3-devel
BuildRequires:	libtool
BuildRequires:	libvorbis-devel
BuildRequires:	netpbm-progs
BuildRequires:	pcre-devel
BuildRequires:	pkgconfig
BuildRequires:	readline-devel
BuildRequires:	taglib-devel
BuildRequires:	xine-lib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Evidence is a file-manager with plugins for everything - from
ultra-fast JPEG previews to MP3/ID3 and Ogg tag editing. No bloat -
what you don't need, you don't load. Micro-shell, MP3 thumbnailing and
extensive theming opportunities complete this slightly different
browser.

%description -l pl
Evidence to zarz�dca plik�w z wtyczkami do wszystkiego - od bardzo
szybkiego podgl�du JPEG-�w do modyfikowania znacznik�w MP3/ID3 i Ogg.
Bez �adnego narzutu - tego, czego nie potrzeba, nie wczytuje si�.
Mikro-pow�oka, miniaturki MP3 i rozleg�e mo�liwo�ci zmiany motywu
dope�niaj� t� nieco odmienn� przegl�dark�.

%package backend-kio
Summary:	kio backend
Summary(pl):	Backend kio
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}

%description backend-kio
kio backend.

%description backend-kio -l pl
Backend kio.

%package metadata-extractor
Summary:	Library for extracting information from any file
Summary(pl):	Biblioteka do wyci�gania informacji z dowolnego pliku
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}

%description metadata-extractor
Library for extracting information from any file.

%description metadata-extractor -l pl
Biblioteka do wyci�gania informacji z dowolnego pliku.

%package metadata-mp3
Summary:	Library for extracting information from MP3 files using libid3
Summary(pl):	Biblioteka do wyci�gania informacji z plik�w MP3 przy u�yciu libid3
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}

%description metadata-mp3
Library for extracting information from MP3 files using libid3.

%description metadata-mp3 -l pl
Biblioteka do wyci�gania informacji z plik�w MP3 przy u�yciu libid3.

%package metadata-taglib
Summary:	Library for extracting information from MP3 files using libtag
Summary(pl):	Biblioteka do wyci�gania informacji z plik�w MP3 przy u�yciu libtag
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}

%description metadata-taglib
Library for extracting information from MP3 files using libtag.

%description metadata-taglib -l pl
Biblioteka do wyci�gania informacji z plik�w MP3 przy u�yciu libtag.

%package metadata-vorbis
Summary:	Library for extracting information from Ogg/Vorbis files
Summary(pl):	Biblioteka do wyci�gania informacji z plik�w Ogg/Vorbis
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}

%description metadata-vorbis
Library for extracting information from Ogg/Vorbis files.

%description metadata-vorbis -l pl
Biblioteka do wyci�gania informacji z plik�w Ogg/Vorbis.

%package thumbnailer-avifile
Summary:	Thumbnailer for video files using avifile
Summary(pl):	Generator miniaturek dla plik�w z filmami przy u�yciu avifile
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}

%description thumbnailer-avifile
Thumbnailer for video files using avifile.

%description thumbnailer-avifile -l pl
Generator miniaturek dla plik�w z filmami przy u�yciu avifile.

%package thumbnailer-id3
Summary:	Thumbnailer for files having ID3 tag
Summary(pl):	Generator miniaturek dla plik�w ze znacznikami ID3
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}

%description thumbnailer-id3
Thumbnailer for files having ID3 tag.

%description thumbnailer-id3 -l pl
Generator miniaturek dla plik�w ze znacznikami ID3.

%package thumbnailer-mpeg3
Summary:	Thumbnailer for MP3 files
Summary(pl):	Generator miniaturek dla plik�w MP3
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}

%description thumbnailer-mpeg3
Thumbnailer for MP3 files.

%description thumbnailer-mpeg3 -l pl
Generator miniaturek dla plik�w MP3.

%package thumbnailer-xine
Summary:	Thumbnailer for video files using xine
Summary(pl):	Generator miniaturek dla plik�w z filmami przy u�yciu xine
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}

%description thumbnailer-xine
Thumbnailer for video files using xine.

%description thumbnailer-xine -l pl
Generator miniaturek dla plik�w z filmami przy u�yciu xine.

%prep
%setup -q -n %{name}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure	\
	--enable-largefile		\
	--enable-glib			\
	--disable-btrace		\
	--disable-doodle %{?0:not packaged yet}	\
	--disable-dbus %{?0:experimental}	\
	--disable-dcop			\
	--enable-ecore-ipc		\
	--enable-ecore			\
	--enable-canvas-evas2		\
	--enable-edje			\
	--disable-canvas-gnomecanvas	\
	--disable-extra-themes		\
	--enable-extra-iconsets		\
	--enable-tree-view		\
	--enable-icon-view		\
	--enable-browser-view		\
	--enable-xds			\
	--enable-x			\
	--disable-backend-gnomevfs2 %{?0:want's build}	\
%if !%{with kio}
	--disable-backend-kio		\
%else
	--enable-backend-kio		\
%endif
	--enable-attrs			\
	--enable-acls			\
	--enable-libmagic		\
	--enable-sharedmime		\
	--enable-plugin-extractor	\
	--enable-plugin-taglib		\
	--enable-plugin-vorbis		\
	--enable-plugin-id3		\
	--enable-thumbnailer-xine	\
	--enable-thumbnailer-avi	\
	--enable-thumbnailer-mpeg3	\
	--enable-plugin-ttf		\
	--disable-debug

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# rubbish
find $RPM_BUILD_ROOT%{_datadir}/%{name} -name CVS -or -name .cvsignore | xargs rm -rf
rm -r $RPM_BUILD_ROOT%{_datadir}/%{name}/icons/efm/.icons
rm $RPM_BUILD_ROOT%{_datadir}/%{name}/icons/*.tar.gz
rm $RPM_BUILD_ROOT%{_datadir}/%{name}/icons/Makefile

# clean, so no not packaged files message will appear
find $RPM_BUILD_ROOT%{_libdir} -name "*.a" -or -name "*.la" | xargs rm

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{name}.xpm $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs AUTHORS COPYING.epeg README NEWS ChangeLog DEPENDENCIES HELP_DEVELOP
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/*
%attr(755,root,root) %{_libdir}/%{name}/action/*.so
%attr(755,root,root) %{_libdir}/%{name}/backend/[!k]*.so
%attr(755,root,root) %{_libdir}/%{name}/ipc/*.so
%attr(755,root,root) %{_libdir}/%{name}/metadata/ape.so
%attr(755,root,root) %{_libdir}/%{name}/metadata/exif.so
%attr(755,root,root) %{_libdir}/%{name}/metadata/folder.so
%attr(755,root,root) %{_libdir}/%{name}/metadata/image.so
%attr(755,root,root) %{_libdir}/%{name}/metadata/ttf.so
%attr(755,root,root) %{_libdir}/%{name}/thumbnailer/epeg.so
%attr(755,root,root) %{_libdir}/%{name}/thumbnailer/imlib.so
%attr(755,root,root) %{_libdir}/%{name}/thumbnailer/ttf.so
%dir %{_libdir}/%{name}/gui/efl
%dir %{_libdir}/%{name}/gui/efl/engines
%attr(755,root,root) %{_libdir}/%{name}/gui/efl/engines/*.so
%{_mandir}/man1/%{name}.1*
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.xpm

%if %{with kio}
%files backend-kio
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/backend/kio.so
%endif

%files metadata-extractor
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/metadata/extractor.so

%files metadata-mp3
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/metadata/mp3.so

%files metadata-taglib
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/metadata/taglib.so

%files metadata-vorbis
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/metadata/vorbis.so

%files thumbnailer-avifile
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/thumbnailer/avifile.so

%files thumbnailer-id3
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/thumbnailer/id3.so

%files thumbnailer-mpeg3
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/thumbnailer/mpeg3.so

%files thumbnailer-xine
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/thumbnailer/xine.so
