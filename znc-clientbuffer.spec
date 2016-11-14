%global commit fe0f368e1fcab2b89d5c94209822d9b616cea840
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global modname clientbuffer

Name:           znc-%{modname}
Version:        0
Release:        0.1git%{shortcommit}%{?dist}
Summary:        ZNC module for client specific buffers

License:        ASL 2.0
URL:            https://github.com/jpnurmi/znc-clientbuffer
Source0:        %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  znc-devel
Requires:       znc%{?_isa}

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

%changelog
* Wed Aug 17 2016 Igor Gnatenko <ignatenko@redhat.com> - 0-0.1gitfe0f368
- Initial package
