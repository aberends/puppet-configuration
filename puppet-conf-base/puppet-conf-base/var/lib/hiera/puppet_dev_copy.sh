#!/bin/bash
#
# SCRIPT
#   puppet_dev_copy.sh
# DESCRIPTION
#   A simple script to copy our development stuff to a
#   target node for testing.
#
#   Use ssh-copy-id to avoid having to type in the remote
#   root password all the time.
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
#   puppet_dev_copy.sh is free software; you can
#   redistribute it and/or modify it under the terms of the
#   GNU General Public License as published by the Free
#   Software Foundation; either version 3 of the License, or
#   (at your option) any later version.
#
#   puppet_dev_copy.sh is distributed in the hope that it
#   will be useful, but WITHOUT ANY WARRANTY; without even
#   the implied warranty of MERCHANTABILITY or FITNESS FOR A
#   PARTICULAR PURPOSE. See the GNU General Public License
#   for more details.
#
#   You should have received a copy of the GNU General
#   Public License along with this program; if not, write to
#   the Free Software Foundation, Inc., 59 Temple Place -
#   Suite 330, Boston, MA 02111-1307, USA.
# DESIGN
#

dest=$1

if [ -z "$dest" ]; then
  echo "ERROR, must specify destination host" >&2
  exit 1
fi

rsync -a /root/.bashrc root@${dest}:/root
rsync -a /etc/hiera.yaml root@${dest}:/etc
rsync -a /etc/puppet/modules root@${dest}:/etc/puppet
rsync -a /etc/puppet/manifests root@${dest}:/etc/puppet
rsync -a /etc/puppet/puppet.conf root@${dest}:/etc/puppet
rsync -a /var/lib/hiera root@${dest}:/var/lib
