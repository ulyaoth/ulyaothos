lang en_US.UTF-8
#keyboard us
auth --useshadow --passalgo=sha512
selinux --enforcing
firewall --enabled --service=mdns,ssh

repo --name=ulyaoth --baseurl=https://repos.ulyaoth.net/ulyaothos/x86_64/os/

%packages
@core --nodefaults
@anaconda-tools

## Add Generic packages and remove fedora packages. 
generic-logos
ulyaoth-release
ulyaoth-release-notes
-generic-release
-generic-release-notes
-fedora-logos
-fedora-release
-fedora-release-notes
#####
%end
