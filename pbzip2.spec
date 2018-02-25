Name:		pbzip2
Version:	1.1.13
Release:	2
Summary:	Parallel implementation of bzip2
URL:		http://www.compression.ca/pbzip2/
Source0:	https://launchpad.net/pbzip2/1.1/%{version}/+download/%{name}-%{version}.tar.gz
License:	BSD
Group:		Archiving/Other
Patch0:		pbzip2-1.1.13-invalid-suffix-on-literal-C11-requires-a-space.patch
BuildRequires:	pkgconfig(bzip2)
Conflicts:	bzip2 < 1.0.6-28

%description
PBZIP2 is a parallel implementation of the bzip2 block-sorting file
compressor that uses pthreads and achieves near-linear speedup on SMP
machines.  The output of this version is fully compatible with bzip2
v1.0.2 or newer (ie: anything compressed with pbzip2 can be 
decompressed with bzip2).


%prep
%setup -q
%apply_patches

%build
%global optflags %{optflags} -Ofast
%setup_compile_flags

sed -i -e 's/ -O2/ %{optflags} /' Makefile
sed -i -e 's/LDFLAGS =.*/LDFLAGS = %{ldflags} /' Makefile

%make

%install
%makeinstall_std

# (tpg) provide compat symlinks to use pbzip2 system-wide
ln -sf %{_bindir}/%{name} %{buildroot}%{_bindir}/bzip2
ln -sf %{_bindir}/pbunzip2 %{buildroot}%{_bindir}/bunzip2
ln -sf %{_bindir}/pbzcat %{buildroot}%{_bindir}/bzcat

%files
%doc AUTHORS ChangeLog COPYING README
%{_bindir}/%{name}
%{_bindir}/pbunzip2
%{_bindir}/pbzcat
%{_bindir}/bzip2
%{_bindir}/bunzip2
%{_bindir}/bzcat
%{_mandir}/man1/*
