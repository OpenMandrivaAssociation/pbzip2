Name:		pbzip2
Version:	1.1.8
Release:	%mkrel 1
Summary:	Parallel implementation of bzip2
URL:		http://www.compression.ca/pbzip2/
License:	BSD
Group:		Archiving/Other
BuildRequires:	bzip2-devel
Source0:	http://www.compression.ca/pbzip2/%{name}-%{version}.tar.gz

%description
PBZIP2 is a parallel implementation of the bzip2 block-sorting file
compressor that uses pthreads and achieves near-linear speedup on SMP
machines.  The output of this version is fully compatible with bzip2
v1.0.2 or newer (ie: anything compressed with pbzip2 can be 
decompressed with bzip2).


%prep
%setup -q
sed -i -e 's/ -O2/ %{optflags} /' Makefile

%build
make

%install
install -D -m755 %{name} %{buildroot}%{_bindir}/%{name}
install -D -m644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1
ln -sf ./%{name} %{buildroot}%{_bindir}/pbunzip2
ln -sf ./%{name} %{buildroot}%{_bindir}/pbzcat

%files
%doc AUTHORS ChangeLog COPYING README
%{_bindir}/%{name}
%{_bindir}/pbunzip2
%{_bindir}/pbzcat
%{_mandir}/man1/*


%changelog
* Wed Aug 15 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.1.8-1mdv2012.0
+ Revision: 814886
- version update 1.1.8

* Fri Nov 11 2011 Alexander Khrukin <akhrukin@mandriva.org> 1.1.6-2
+ Revision: 730027
- spec file cleaned

* Wed Nov 02 2011 Alexander Khrukin <akhrukin@mandriva.org> 1.1.6-1
+ Revision: 712981
- version update

* Fri Sep 23 2011 Alexander Barakin <abarakin@mandriva.org> 1.1.5-1
+ Revision: 701088
- imported package pbzip2

  + Oden Eriksson <oeriksson@mandriva.com>
    - the mass rebuild of 2010.0 packages

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 1.0.5-2mdv2010.0
+ Revision: 440499
- rebuild

* Mon Feb 23 2009 Olivier Thauvin <nanardon@mandriva.org> 1.0.5-1mdv2009.1
+ Revision: 344131
- 1.0.5

* Thu Dec 25 2008 Olivier Thauvin <nanardon@mandriva.org> 1.0.4-1mdv2009.1
+ Revision: 318579
- 1.0.4

* Fri Oct 31 2008 Olivier Thauvin <nanardon@mandriva.org> 1.0.3-1mdv2009.1
+ Revision: 299089
- 1.0.3

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.0.2-3mdv2009.0
+ Revision: 241137
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Thu Jul 26 2007 Olivier Thauvin <nanardon@mandriva.org> 1.0.2-1mdv2008.0
+ Revision: 55797
- 1.0.2

* Mon Apr 30 2007 Olivier Thauvin <nanardon@mandriva.org> 1.0.1-1mdv2008.0
+ Revision: 19664
- 1.0.1

