Name:		pbzip2
Version:	1.1.13
Release:	1
Summary:	Parallel implementation of bzip2
URL:		http://www.compression.ca/pbzip2/
License:	BSD
Group:		Archiving/Other
BuildRequires:	pkgconfig(bzip2)
Source0:	https://launchpad.net/pbzip2/1.1/%{version}/+download/%{name}-%{version}.tar.gz

%description
PBZIP2 is a parallel implementation of the bzip2 block-sorting file
compressor that uses pthreads and achieves near-linear speedup on SMP
machines.  The output of this version is fully compatible with bzip2
v1.0.2 or newer (ie: anything compressed with pbzip2 can be 
decompressed with bzip2).


%prep
%setup -q
%global optflags %{optflags} -Ofast
sed -i -e 's/ -O2/ %{optflags} /' Makefile
sed -i -e 's/LDFLAGS.*/LDFLAGS = %{ldflags} /' Makefile

%build
%setup_compile_flags
%make

%install
%makeinstall_std

%files
%doc AUTHORS ChangeLog COPYING README
%{_bindir}/%{name}
%{_bindir}/pbunzip2
%{_bindir}/pbzcat
%{_mandir}/man1/*
