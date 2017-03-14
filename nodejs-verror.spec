%{?scl:%scl_package nodejs-%{srcname}}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}
%global srcname verror

Name:           %{?scl_prefix}nodejs-%{srcname}
Version:        1.8.1
Release:        2%{?dist}
Summary:        Richer JavaScript errors
License:        MIT
URL:            https://github.com/joyent/node-verror
Source0:        https://github.com/joyent/node-verror/archive/v%{version}.tar.gz#/%{pkg_name}-%{version}.tar.gz
# This is a testing tool we probably don't need in scl
Source1:        https://raw.githubusercontent.com/joyent/catest/ca138645cc9647d6976063c61fa9f28dd16c5023/catest

BuildArch:      noarch

ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  %{?scl_prefix}nodejs-devel

%description
%{summary}.

%prep
%setup -q -n node-verror-%{version}
%nodejs_fixdep extsprintf '1.x'
rm -rf node_modules
#install -m0755  %{SOURCE1} ./deps/catest

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{srcname}

cp -pr package.json lib/ \
    %{buildroot}%{nodejs_sitelib}/%{srcname}

%{nodejs_symlink_deps}

#%check
#%{nodejs_symlink_deps} --check
#%{?scl:scl enable %{scl} - << \EOF}
#make test
#%{?scl:EOF}


%files
%{!?_licensedir:%global license %doc}
%doc README.md examples/
%license LICENSE
%{nodejs_sitelib}/%{srcname}

%changelog
* Thu Sep 15 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.8.1-2
- Built for RHSCL
- turn off tests

* Sun Aug 28 2016 Piotr Popieluch <piotr1212@gmail.com> - - 1.8.1-1
- Update to 1.8.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 21 2016 Tom Hughes <tom@compton.nu> - 1.6.0-2
- Patch tests for changes in stack traces with nodejs 4

* Sun Dec 06 2015 Piotr Popieluch <piotr1212@gmail.com> - 1.6.0-1
- Initial package
