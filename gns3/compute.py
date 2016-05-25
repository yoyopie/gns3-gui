#!/usr/bin/env python
#
# Copyright (C) 2016 GNS3 Technologies Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


class Compute:
    """
    A compute node on the remote server
    """
    def __init__(self, compute_id):
        self._compute_id = compute_id
        self._name = compute_id
        self._connected = False
        self._protocol = None
        self._host = None
        self._port = None
        self._user = None

    def id(self):
        return self._compute_id

    def name(self):
        return self._name

    def setName(self, name):
        self._name = name

    def connected(self):
        return self._connected

    def setConnected(self, value):
        self._connected = value

    def port(self):
        return self._port

    def setPort(self, port):
        self._port = port

    def user(self):
        return self._user

    def setUser(self, user):
        self._user = user

    def protocol(self):
        return self._protocol

    def setProtocol(self, protocol):
        self._protocol = protocol

    def host(self):
        return self._host

    def setHost(self, host):
        self._host = host

    def __str__(self):
        return self._compute_id

