Summary:	Parallel implementation of bzip2
Name:		pbzip2
Version:	0.9.6
Release:	%mkrel 2
URL:		http://www.compression.ca/pbzip2/
License:	BSD
Group:		Archiving/Compression
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:	tar, gzip, make, gcc-c++, bzip2-devel
Source0:	http://www.compression.ca/pbzip2/%{name}-%{version}.tar.bz2

%description
PBZIP2 is a parallel implementation of the bzip2 block-sorting file
compressor that uses pthreads and achieves near-linear speedup on SMP
machines.

%prep
%setup -q

%build
g++ %optflags -D_LARGEFILE64_SOURCE -D_FILE_OFFSET_BITS=64 -o pbzip2 pbzip2.cpp -pthread -lpthread -lbz2

%install
install -D -m755 %{name} %{buildroot}%{_bindir}/%{name}

%clean
[ "%{buildroot}" != "/" ] && [ -d %{buildroot} ] && rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc README ChangeLog AUTHORS
%attr(0755,root,root) %{_bindir}/%{name}

