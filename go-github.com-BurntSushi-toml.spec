#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : go-github.com-BurntSushi-toml
Version  : v0.3.1
Release  : 1
URL      : https://proxy.golang.org/github.com/!burnt!sushi/toml/@v/list
Source0  : https://proxy.golang.org/github.com/!burnt!sushi/toml/@v/list
Source1  : https://proxy.golang.org/github.com/!burnt!sushi/toml/@v/v0.3.1.info
Source2  : https://proxy.golang.org/github.com/!burnt!sushi/toml/@v/v0.3.1.mod
Source3  : https://proxy.golang.org/github.com/!burnt!sushi/toml/@v/v0.3.1.zip
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: go-github.com-BurntSushi-toml-data = %{version}-%{release}
BuildRequires : buildreq-golang

%description
## TOML parser and encoder for Go with reflection
TOML stands for Tom's Obvious, Minimal Language. This Go package provides a
reflection interface similar to Go's standard library `json` and `xml`
packages. This package also supports the `encoding.TextUnmarshaler` and
`encoding.TextMarshaler` interfaces so that you can define custom data
representations. (There is an example of this below.)

%package data
Summary: data components for the go-github.com-BurntSushi-toml package.
Group: Data

%description data
data components for the go-github.com-BurntSushi-toml package.


%prep

%install
rm -fr %{buildroot}
mkdir -p %{buildroot}/usr/share/goproxy/github.com/!burnt!sushi/toml/@v
install -m 0644 %{SOURCE0} %{buildroot}/usr/share/goproxy/github.com/!burnt!sushi/toml/@v/list
install -m 0644 %{SOURCE1} %{buildroot}/usr/share/goproxy/github.com/!burnt!sushi/toml/@v/v0.3.1.info
install -m 0644 %{SOURCE2} %{buildroot}/usr/share/goproxy/github.com/!burnt!sushi/toml/@v/v0.3.1.mod
install -m 0644 %{SOURCE3} %{buildroot}/usr/share/goproxy/github.com/!burnt!sushi/toml/@v/v0.3.1.zip


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/goproxy/github.com/!burnt!sushi/toml/@v/list
/usr/share/goproxy/github.com/!burnt!sushi/toml/@v/v0.3.1.info
/usr/share/goproxy/github.com/!burnt!sushi/toml/@v/v0.3.1.mod
/usr/share/goproxy/github.com/!burnt!sushi/toml/@v/v0.3.1.zip
