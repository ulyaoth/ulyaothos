useradd ulyaoth
su ulyaoth -c "rpmdev-setuptree"
cd /home/ulyaoth/rpmbuild/SPECS/

su ulyaoth -c "wget https://raw.githubusercontent.com/ulyaoth/ulyaothos/master/Packages/u/ulyaoth-repo/SPEC/ulyaoth-repos.spec -O /home/ulyaoth/rpmbuild/SPECS/ulyaoth-repo.spec"

su ulyaoth -c "spectool /home/ulyaoth/rpmbuild/SPECS/ulyaoth-repo.spec -g -R"
su ulyaoth -c "rpmbuild -ba /home/ulyaoth/rpmbuild/SPECS/ulyaoth-repo.spec"

cp /home/ulyaoth/rpmbuild/SRPMS/* /root/
cp /home/ulyaoth/rpmbuild/RPMS/x86_64/* /root/
cp /home/ulyaoth/rpmbuild/RPMS/i686/* /root/
cp /home/ulyaoth/rpmbuild/RPMS/i386/* /root/
cp /home/ulyaoth/rpmbuild/RPMS/noarch/* /root/

rm -rf /root/build-ulyaoth-*
rm -rf /home/ulyaoth/rpmbuild