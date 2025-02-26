#!/bin/bash

set -e

source ./scripts/spec-file.sh
source ./scripts/bash-color.sh
bash ./scripts/checkout-deps.sh --apply-patches

echo_color "\n=== RPM build ==="

rm -rf ./rpmbuild
mkdir -p ./rpmbuild/SOURCES
set +e
cp *.patch ./rpmbuild/SOURCES
set -e

echo_color "\nRPM Lint"
rpmlint ./$spec_file

echo_color "\nRPM Build"
echo_debug rpmbuild --define "_topdir $PWD/rpmbuild" -ba --noclean ./$spec_file

echo_color "\n=== RPM Contents ==="

# One-by-one for some separation
for file in ./rpmbuild/RPMS/**/*.rpm; do
  echo_color "\nRPM <$file>:"

  echo_color "\nFiles:"
  rpm -qvlp $file

  echo_color "\nScripts:"
  rpm -qp --scripts $file
done
