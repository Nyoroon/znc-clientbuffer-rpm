%global commit 7ae14f82f74eee552d0bfdd9e6c6e96a2b31608d
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global modname clientbuffer

%global znc_version %((znc -v 2>/dev/null || echo 'a 0') | head -1 | awk '{print $2}')

Name:           znc-%{modname}
Version:        0
Release:        37.1git%{shortcommit}%{?dist}
Summary:        ZNC module for client specific buffers

License:        ASL 2.0
URL:            https://github.com/CyberShadow/znc-clientbuffer
Source0:        %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  znc-devel
Requires:       znc%{?_isa} = %znc_version

%description
The client buffer module maintains client specific buffers for identified
clients.

%prep
%autosetup -n %{name}-%{commit}

%build
CXXFLAGS="%{optflags}" LDFLAGS="%{__global_ldflags}" znc-buildmod %{modname}.cpp

%install
install -Dpm0755 %{modname}.so %{buildroot}%{_libdir}/znc/%{modname}.so

%files
%{_libdir}/znc/%{modname}.so
