#!/bin/bash
#
# SCRIPT
#   depzone_platform_instance.sh
# DESCRIPTION
#   The configuration on a node, provisioned with Puppet, is
#   determined by the set of YAML files being consulted. So,
#   which set is consulted? This script helps to provide the
#   answer. The higher level files overwrite the parameters
#   of lower level files.
#
#   An example illustrates this:
#   ./depzone_platform_instance.sh -d dmsat1 -i ldap2 \
#       -n ds3.dmz.dmsat1.org -p ldap -s dmz
#   depzones/dmsat1/hosts/ds3.dmz.dmsat1.org.yaml
#   depzones/dmsat1/platforms/ldap/ldap2.yaml
#   depzones/dmsat1/platforms/ldap.yaml
#   depzones/dmsat1/subzones/dmz.yaml
#   depzones/dmsat1.yaml
#   platforms/ldap/ldap2.yaml
#   platforms/ldap.yaml
#   base.yaml
# ARGUMENTS
#   None.
# RETURN
#   0: success.
# DEPENDENCIES
# FAILURE
# AUTHORS
#   Date strings made with 'date +"\%Y-\%m-\%d \%H:\%M"'.
#   Allard Berends (AB), 2014-08-16 12:40
# HISTORY
# LICENSE
#   Copyright (C) 2014 Allard Berends
# 
#   depzone_platform_instance.sh is free software; you can
#   redistribute it and/or modify it under the terms of the
#   GNU General Public License as published by the Free
#   Software Foundation; either version 3 of the License, or
#   (at your option) any later version.
#
#   depzone_platform_instance.sh is distributed in the hope
#   that it will be useful, but WITHOUT ANY WARRANTY;
#   without even the implied warranty of MERCHANTABILITY or
#   FITNESS FOR A PARTICULAR PURPOSE. See the GNU General
#   Public License for more details.
#
#   You should have received a copy of the GNU General
#   Public License along with this program; if not, write to
#   the Free Software Foundation, Inc., 59 Temple Place -
#   Suite 330, Boston, MA 02111-1307, USA.
# DESIGN
#
PNAME=$(basename $0)

#
# FUNCTION
#   usage
# DESCRIPTION
#   This function explains how this script should be called
#   on the command line.
# RETURN CODE
#   Nothing
#
usage() {
  echo "Usage: $PNAME"
  echo " -d <depzone>:   For example: dmsat1"
  echo " -i <instances>: Comma separated list of instances"
  echo " -n <node>:      Node of which we want yaml conf"
  echo " -p <platforms>: Comma separated list of platforms"
  echo " -s <subzone>:   Configuration yaml's of subzone"
  echo " -h :            this help message"
  cat << EOS
This script provides the answer to the question: what YAML
files influence the configuration of my target node, if I
put specific platform functions on it?

In the first example, we have a node that is configured as a
dedicated single node ldap server in the DMZ subzone.

In the second exmaple, we add the NTP platform function to
it.

Example usage of DS (Directory Server) in DMZ:

$PNAME -d dmsat1 -i ldap2 -n ds3.dmz.dmsat1.org -p ldap -s dmz

If, on node YAML level, a node is configured to provide both
ldap and ntp functions, one can specify both ldap and ntp as
platform, with specific instances ldap2 and ntp1:

Example usage of DS (Directory Server) and NTP in DMZ:

$PNAME -d dmsat1 -i ldap2,ntp1 -n ds3.dmz.dmsat1.org -p ldap,ntp -s dmz

EOS
} # end usage

while getopts "d:hi:n:p:s:" Option
do
  case $Option in
    d) D_OPTION=$OPTARG ;;
    i) I_OPTION=$OPTARG ;;
    n) N_OPTION=$OPTARG ;;
    p) P_OPTION=$OPTARG ;;
    s) S_OPTION=$OPTARG ;;
    ?|h|-h|-help) usage
      exit 0 ;;
    *) usage
      exit 1 ;;
  esac 
done

DEPZONE=$D_OPTION
HOST=$N_OPTION
INSTANCES=$(echo $I_OPTION | tr ',' ' ')
PLATFORMS=$(echo $P_OPTION | tr ',' ' ')
SUBZONE=$S_OPTION

layer1="depzones/${DEPZONE}/hosts/${HOST}.yaml"
[ -r "$layer1" ] && echo $layer1
for p in $PLATFORMS
do
  for i in $INSTANCES
  do
    layer2="depzones/${DEPZONE}/platforms/${p}/${i}.yaml"
    [ -r "$layer2" ] && echo $layer2
  done
done
for p in $PLATFORMS
do
  layer3="depzones/${DEPZONE}/platforms/${p}.yaml"
  [ -r "$layer3" ] && echo $layer3
done
layer4="depzones/${DEPZONE}/subzones/${SUBZONE}.yaml"
[ -r "$layer4" ] && echo $layer4
layer5="depzones/${DEPZONE}.yaml"
[ -r "$layer5" ] && echo $layer5

for p in $PLATFORMS
do
  for i in $INSTANCES
  do
    layer6="platforms/${p}/${i}.yaml"
    [ -r "$layer6" ] && echo $layer6
  done
done
for p in $PLATFORMS
do
  layer7="platforms/${p}.yaml"
  [ -r "$layer7" ] && echo $layer7
done
layer8="base.yaml"
[ -r "$layer8" ] && echo $layer8
