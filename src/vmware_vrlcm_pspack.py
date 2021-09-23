#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2019 VMware, Inc.  All rights reserved. -- VMware Confidential

"""
Gobuild components for vRealize LCM pspack
"""

# vrlcm_services
VRLCM_SERVICES_ALIAS = 'vrlcm_services'
VRLCM_SERVICES_BRANCH = 'vrlcm-84-GA-patch1'
VRLCM_SERVICES_CLN = 'acd146c269660f48b195eec41b259908c24dc3c9'
VRLCM_SERVICES_BUILDTYPE = 'release'
VRLCM_SERVICES_FILES = {'linux64-vm': [r'publish/']}

# blackstone
VREALIZE_BLACKSTONE_BRANCH = 'mana-rel'
VREALIZE_BLACKSTONE_CLN = 'e4a6b2e9db9be2749fc186fc2ce16e293bf2d34e'
VREALIZE_BLACKSTONE_BUILDTYPE = 'release'
VREALIZE_BLACKSTONE_DELIVERABLE = {
    'linux64-vm': [ r'publish/blackstone.zip'],
    'linux64': [ r'publish/blackstone.zip']
}

# apuat-paks 8.5.0
VROPS_APUAT850_BRANCH = 'v8.5.0'
VROPS_APUAT850_BUILDTYPE = 'release'
VROPS_APUAT850_CLN = '1703021'
VROPS_APUAT850_FILES = \
    {'linux64-vm': [r'publish/.*.pak']}

# photon iso
CSC_PHOTON_BRANCH = 'photon3-vmw-updates'
CSC_PHOTON_CLN = 9176122
CSC_PHOTON_BUILDTYPE = 'release'
CSC_PHOTON_FILES = {'linux64-vm': [r'publish/csc-photon-3.0.0-x86_64.iso']}

# vmware_vrlcm iso
VMWARE_VRLCM_BRANCH = 'vrlcm-84-GA-patch1'
VMWARE_VRLCM_CLN = 'f454f2fd918a67f5a3c237311df42f98df430800'
VMWARE_VRLCM_BUILDTYPE = 'release'
VMWARE_VRLCM_FILES = {'linux64-vm': [r'publish/exports/iso/.*.iso']}
