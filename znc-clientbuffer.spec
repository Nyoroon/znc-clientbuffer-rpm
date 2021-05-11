%global modname clientbuffer

%global znc_version %((znc -v 2>/dev/null || echo 'a 0') | head -1 | awk '{print $2}')

Name:           znc-%{modname}
Version:        1.0.48
Release:        1%{?dist}
Summary:        ZNC module for client specific buffers

License:        ASL 2.0
URL:            https://github.com/CyberShadow/%{name}
Source0:        %{url}/archive/v%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  zlib-devel
BuildRequires:  znc-devel
Requires:       znc%{?_isa} = %znc_version

%description
The client buffer module maintains client specific buffers for identified
clients.

%prep
%autosetup

%build
CXXFLAGS="%{optflags}" LDFLAGS="%{__global_ldflags}" znc-buildmod %{modname}.cpp

%install
install -Dpm0755 %{modname}.so %{buildroot}%{_libdir}/znc/%{modname}.so

%files
%{_libdir}/znc/%{modname}.so
